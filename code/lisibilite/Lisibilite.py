import logging as LOG

from customexceptions.ReadabilityErrors import BadInputError
from models.CoreMetrics import CoreMetrics
from models.OutputDataModel import OutputDataModel
from models.ReadabilityMetrics import ReadabilityMetrics
from utils.io.FileReader import FileReader
from lexis import LexisCalculator
from lexis import ReadabilityCalculator


class Lisibilite:
    def __init__(self, filename: str = None, contents: str = None):
        """
        Init lisibilite. Either the filename or contents should be input
        :param filename: Optional | The name of the file to compute metrics for
        :param contents: Optional | The string for which the metrics should be computed
        """
        LOG.debug(f'{__name__} init')
        self.outputModel = OutputDataModel()

        if filename:
            self.outputModel = self.__computeMetricsFromFile(filename)
        elif contents:
            self.outputModel = self.__computeMetricsFromString(contents)
        else:
            LOG.error('Bad input. One of filename or contents should be set')
            raise BadInputError(
                'Bad input. One of filename or contents should be set')

    def getReadabilityMetrics(self) -> OutputDataModel:
        """
        The method to retrieve the Output Model
        :return: The output model
        """
        return self.outputModel

    def __computeMetricsFromFile(self, filename: str) -> CoreMetrics:
        """
        Private: Method to compute the metrics from the input file
        :param filename: The name of the file for which the metrics should be computed
        :return: Metrics object
        """
        LOG.debug("Computing metrics from file")
        reader = FileReader()
        try:
            contentsOfFile = reader.read(filename)
            return self.__computeMetricsFromString(contentsOfFile)
        except Exception as error:
            LOG.error(
                f'Error in getting the contents from the file. Error = {error}')
            raise Exception(
                f'Error in getting the contents from the file. Error = {error}')

    def __computeMetricsFromString(self, contents: str) -> CoreMetrics:
        """
        Private: Method to compute the metrics from an input string
        :param contents: The string for which the metrics should be computed
        :return: Metrics object
        """
        LOG.debug("Computing metrics from string")
        outputData = OutputDataModel()

        lexisMetrics = LexisCalculator(contents)
        coreMetrics = lexisMetrics.computeMetrics()

        readabilityMetrics = ReadabilityMetrics()
        readabilityCalculator = ReadabilityCalculator(coreMetrics)
        readabilityMetrics = readabilityCalculator.computeReadabilityMetrics()

        outputData.setCoreMetrics(coreMetrics)
        outputData.setReadabilityMetrics(readabilityMetrics)
        LOG.debug(outputData)
        return outputData
