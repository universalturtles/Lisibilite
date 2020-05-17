from unittest import TestCase

from utils.lexis.LexisCalculator import LexisCalculator


class TestLexisCalculator(TestCase):

    def test_compute_metrics(self):
        # Arrange
        with open("../../resources/sample_text.txt", "r", encoding='utf8') as fileObj:
            text = fileObj.read()
        lexis = LexisCalculator(text)
        expectedSentences = 11
        expectedWords = 54
        expectedHardWords = 51
        expectedEasyWords = 3
        expectedSyllables = 82
        expectedCharacters = 260

        # Act
        metrics = lexis.computeMetrics()

        # Assert
        self.assertEqual(
            expectedSentences,
            metrics.getTotalSentences(),
            "Unexpected number of sentences")
        self.assertEqual(
            expectedWords,
            metrics.getTotalWords(),
            "Unexpected number of words")
        self.assertEqual(
            expectedHardWords,
            metrics.getTotalComplexWords(),
            "Unexpected number of hard words")
        self.assertEqual(
            expectedEasyWords,
            metrics.getTotalEasyWords(),
            "Unexpected number of easy words")
        self.assertEqual(
            expectedSyllables,
            metrics.getTotalSyllables(),
            "Unexpected number of syllables")
        self.assertEqual(
            expectedCharacters,
            metrics.getTotalCharacters(),
            "Unexpected number of characters")

    def test_compute_metrics_empty_string(self):
        # Arrange
        lexis = LexisCalculator("")
        expectedSentences = 0
        expectedWords = 0
        expectedHardWords = 0
        expectedEasyWords = 0
        expectedSyllables = 0
        expectedCharacters = 0

        # Act
        metrics = lexis.computeMetrics()

        # Assert
        self.assertEqual(
            expectedSentences,
            metrics.getTotalSentences(),
            "Unexpected number of sentences")
        self.assertEqual(
            expectedWords,
            metrics.getTotalWords(),
            "Unexpected number of words")
        self.assertEqual(
            expectedHardWords,
            metrics.getTotalComplexWords(),
            "Unexpected number of hard words")
        self.assertEqual(
            expectedEasyWords,
            metrics.getTotalEasyWords(),
            "Unexpected number of easy words")
        self.assertEqual(
            expectedSyllables,
            metrics.getTotalSyllables(),
            "Unexpected number of syllables")
        self.assertEqual(
            expectedCharacters,
            metrics.getTotalCharacters(),
            "Unexpected number of characters")
