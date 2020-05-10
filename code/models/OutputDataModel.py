import logging as LOG
from models.CoreMetrics import CoreMetrics
from models.ReadabilityMetrics import ReadabilityMetrics


class OutputDataModel:
    def __init__(self):
        LOG.debug(f"{__name__} init")
        self.coreMetrics = CoreMetrics()
        self.readabilityMetrics = ReadabilityMetrics()
        self.category = ""
        self.description = ""

    def setCoreMetrics(self, coreMetrics: CoreMetrics) -> None:
        """
        Set the Core Metrics
        :param coreMetrics: The Core Metrics
        :return: None
        """
        LOG.debug(f'Setting Core Metrics')
        self.coreMetrics = coreMetrics

    def getCoreMetrics(self) -> CoreMetrics:
        """
        Get the Core Metrics
        :return: The Core Metrics
        """
        LOG.debug(f'Getting Core Metrics')
        return self.coreMetrics

    def setReadabilityMetrics(self, readabilityMetrics: ReadabilityMetrics) -> None:
        """
        Set the Readability Metrics
        :param coreMetrics: The Readability Metrics
        :return: None
        """
        LOG.debug(f'Setting Core Metrics')
        self.readabilityMetrics = readabilityMetrics

    def getReadabilityMetrics(self) -> ReadabilityMetrics:
        """
        Get the Readability Metrics
        :return: The Readability Metrics
        """
        LOG.debug(f'Getting Readability Metrics')
        return self.readabilityMetrics

    def setCategory(self, category: str) -> None:
        """
        Set the Category
        :param category: The Category of the text
        :return: None
        """
        LOG.debug(f'Setting category as {category}')
        self.category = category

    def getCategory(self) -> str:
        """
        Get the Category
        :return: The Category of the text
        """
        LOG.debug(f'Getting category. Category = {self.category}')
        return self.category

    def setDescription(self, description: str) -> None:
        """
        Set the Description
        :param description: The Description of the text
        :return: None
        """
        LOG.debug(f'Setting category as {description}')
        self.description = description

    def getDescription(self) -> str:
        """
        Get the Description
        :return: The Description of the text
        """
        LOG.debug(f'Getting description. Description = {self.description}')
        return self.description

    def __str__(self) -> str:
        returnText = f'*** Core Metrics\n{str(self.getCoreMetrics())}\n'
        returnText += f'*** Readability Metrics\n{str(self.getReadabilityMetrics())}\n'
        returnText += f'Category = {self.getCategory()}\n'
        returnText += f'Description = {self.getDescription()}'
        return  returnText

    def __eq__(self, other):
        if not isinstance(other, OutputDataModel):
            # don't attempt to compare against unrelated types
            return NotImplemented

        return self.coreMetrics == other.coreMetrics and \
               self.readabilityMetrics == other.readabilityMetrics and \
               self.category == other.category and \
               self.description == other.description