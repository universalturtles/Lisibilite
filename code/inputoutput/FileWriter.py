import logging as LOG
from typing import Dict

import pandas as pd
from common.Constants import META_HEADERS, METRICS_HEADERS
from customexceptions.ReadabilityErrors import IOError
from models.CoreMetrics import CoreMetrics
from models.OutputDataModel import OutputDataModel
from models.ReadabilityMetrics import ReadabilityMetrics

# Indices of the specific headers
# assigned to constants to prevent
# magic number access of the list
ALGORITHM_HEADER_INDEX = 0
SCORE_HEADER_INDEX = 1
DESCRIPTION_HEADER_INDEX = 2

CORE_METRICS_HEADER_INDEX = 0
TOTAL_COUNT_HEADER_INDEX = 1

class FileWriter:
    def __init__(self):
        """
        File Writer init
        """
        LOG.debug(f'{__name__} init')
        self.outputCoreMetricsDf = None
        self.outputReadabilityMetricsDf = None

    def __generateCoreMetricsDf(self, coreMetrics: CoreMetrics) -> pd.DataFrame :
        coreMetricsDict = coreMetrics.getMetricsDict()
        
        return pd.DataFrame({META_HEADERS[CORE_METRICS_HEADER_INDEX]: list(coreMetricsDict.keys()),
            META_HEADERS[TOTAL_COUNT_HEADER_INDEX]: list(coreMetricsDict.values())})

    def __generateReadabilityMetricsDf(self, readabilityMetrics: ReadabilityMetrics) -> pd.DataFrame :
        readabilityMetricsDict = readabilityMetrics.getReadabilityMetricsDict()
        roundedValues = []
        rounderLabels = []
        for score in readabilityMetricsDict.values():
            roundedValues.append(score.getRoundedValue())
            rounderLabels.append(score.getLabel())

        return pd.DataFrame({METRICS_HEADERS[ALGORITHM_HEADER_INDEX]: list(readabilityMetricsDict.keys()),
            METRICS_HEADERS[SCORE_HEADER_INDEX]: roundedValues,
            METRICS_HEADERS[DESCRIPTION_HEADER_INDEX]: rounderLabels})


    def __modelToDf(self, output: OutputDataModel) -> (pd.DataFrame, pd.DataFrame) :

        if self.outputCoreMetricsDf != None and self.outputReadabilityMetricsDf != None:
            return self.outputCoreMetricsDf, self.outputReadabilityMetricsDf

        self.outputCoreMetricsDf = self.__generateCoreMetricsDf(output.getCoreMetrics())
        self.outputReadabilityMetricsDf = self.__generateReadabilityMetricsDf(output.getReadabilityMetrics())

        return self.outputCoreMetricsDf, self.outputReadabilityMetricsDf

    def writeCsv(self, output: OutputDataModel, filename: str):
        """
        Write the OutputData to a CSV file
        :param output: The instance of OutputDataModel with the metrics to write
        :param filename: The name of the file to write to
        :return: true if write is successful. Else false
        """
        LOG.debug(f'Writing to {filename}')
        dfCoreMetrics, dfReadabilityMetrics = self.__modelToDf(output)

        try:
            with open(filename, mode='a', encoding='utf-8', newline='') as file:
                file.seek(0)
                file.truncate()
                dfCoreMetrics.to_csv(file, index=False)
                file.write("\n")
                dfReadabilityMetrics.to_csv(file, index=False)
        except FileNotFoundError as fnf_error:
            LOG.error(f'File {filename} not found. Error: {fnf_error}')
            raise IOError(f'File {filename} not found. Error: {fnf_error}')
        except Exception as error:
            LOG.error(f'Error in reading the file {filename}. Error: {error}')
            raise IOError(f'Error in reading the file {filename}. Error: {error}')
