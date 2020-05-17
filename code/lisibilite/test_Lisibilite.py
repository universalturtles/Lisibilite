from unittest import TestCase

from customexceptions.ReadabilityErrors import BadInputError, IOError
from lisibilite.Lisibilite import Lisibilite


class TestLisibilite(TestCase):
    def test_get_readability_bad_reqeust(self):
        with self.assertRaises(BadInputError) as context:
            lisibilite = Lisibilite()
            self.assertTrue(
                'Bad input. One of filename or contents should be set' in context.exception)

    def test_get_readability_metrics_inputFile(self):
        # Arrange
        filePath = "../resources/sample_text.txt"
        lisibilite = Lisibilite(filePath)
        # Act
        outputModel = lisibilite.getReadabilityMetrics()
        # Assert
        self.assertIsNotNone(outputModel)
        self.assertIsNotNone(outputModel.getReadabilityMetrics())
        self.assertIsNotNone(outputModel.getCoreMetrics())

    def test_get_readability_metrics_inputString(self):
        # Arrange
        filePath = "../resources/sample_text.txt"
        with open(filePath, 'r', encoding='utf8') as fileObject:
            text = fileObject.read()
        lisibilite = Lisibilite(contents=text)
        # Act
        outputModel = lisibilite.getReadabilityMetrics()
        # Assert
        self.assertIsNotNone(outputModel)
        self.assertIsNotNone(outputModel.getReadabilityMetrics())
        self.assertIsNotNone(outputModel.getCoreMetrics())
