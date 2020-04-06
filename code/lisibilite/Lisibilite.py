import logging as LOG

from utils.io.FileReader import FileReader
from models.CoreMetrics import CoreMetrics
from utils.helpers.metahelper import printLogo
from customexceptions.ReadabilityErrors import BadInputError, IOError


class Lisibilite:
    def __init__(self, filename: str = None, contents: str = None):
        """
        Init lisibilite. Either the filename or contents should be input
        :param filename: Optional | The name of the file to compute metrics for
        :param contents: Optional | The string for which the metrics should be computed
        """
        LOG.debug(f'{__name__} init')
        printLogo()
        self.computed = False

        try:
            if filename:
                self.metrics = self.__computeMetricsFromFile(filename)
                self.computed = True
            elif contents:
                self.metrics = self.__computeMetricsFromString(contents)
                self.computed = True
            else:
                LOG.error('Bad input. One of filename or contents should be set')
                raise BadInputError('Bad input. One of filename or contents should be set')
        except Exception as error:
            LOG.error(f'Error in computing the lisibilite errors. Error = {error}')
            raise IOError(f'Error in computing the lisibilite errors. Error = {error}')

    def __computeMetricsFromString(self, contents: str) -> CoreMetrics:
        """
        Private: Method to compute the metrics from an input string
        :param contents: The string for which the metrics should be computed
        :return: Metrics object
        """
        LOG.debug("Computing metrics from string")
        metrics = CoreMetrics()
        return metrics

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
            LOG.error(f'Error in getting the contents from the file. Error = {error}')
            raise Exception(f'Error in getting the contents from the file. Error = {error}')
