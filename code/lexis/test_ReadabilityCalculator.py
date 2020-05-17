from unittest import TestCase

from lexis.ReadabilityCalculator import ReadabilityCalculator
from models.CoreMetrics import CoreMetrics
from models.ReadabilityMetrics import ReadabilityMetrics


class TestReadabilityCalculator(TestCase):
    def setUp(self):
        coreMetrics = CoreMetrics()
        coreMetrics.setTotalSentences(11)
        coreMetrics.setTotalWords(54)
        coreMetrics.setTotalComplexWords(51)
        coreMetrics.setTotalEasyWords(3)
        coreMetrics.setTotalSyllables(82)
        coreMetrics.setTotalCharacters(260)
        self.readability = ReadabilityCalculator(coreMetrics)

    def test_compute_fres(self):
        expectedScore = 73.38560606060608
        actualScore = self.readability.computeFRES()
        self.assertEqual(expectedScore, actualScore)

    def test_compute_fkgl(self):
        expectedScore = 4.243063973063972
        actualScore = self.readability.computeFKGL()
        self.assertEqual(expectedScore, actualScore)

    def test_compute_gfi(self):
        expectedScore = 39.74141414141414
        actualScore = self.readability.computeGFI()
        self.assertEqual(expectedScore, actualScore)

    def test_compute_ari(self):
        expectedScore = 3.7023232323232307
        actualScore = self.readability.computeARI()
        self.assertEqual(expectedScore, actualScore)

    def test_compute_smog(self):
        expectedScore = 15.429909175157395
        actualScore = self.readability.computeSMOG()
        self.assertEqual(expectedScore, actualScore)

    def test_compute_cli(self):
        expectedScore = 6.481481481481481
        actualScore = self.readability.computeCLI()
        self.assertEqual(expectedScore, actualScore)

    def test_compute_lws(self):
        expectedScore = 6.09090909090909
        actualScore = self.readability.computeLWS()
        self.assertEqual(expectedScore, actualScore)

    def test_compute_fry(self):
        expectedScore = 0.0  # Since its not implemented
        actualScore = self.readability.computeFRY()
        self.assertEqual(expectedScore, actualScore)

    def test_compute_readability_metrics(self):
        # Arrange
        expectedReadabilityMetrics = ReadabilityMetrics()
        expectedReadabilityMetrics.setFRES(73.38560606060608)
        expectedReadabilityMetrics.setFKGL(4.243063973063972)
        expectedReadabilityMetrics.setGFI(39.74141414141414)
        expectedReadabilityMetrics.setARI(3.7023232323232307)
        expectedReadabilityMetrics.setSMOG(15.429909175157395)
        expectedReadabilityMetrics.setCLI(6.481481481481481)
        expectedReadabilityMetrics.setLWS(6.09090909090909)
        expectedReadabilityMetrics.setFRY(0.0)
        actualReadabilityMetrics = self.readability.computeReadabilityMetrics()
        self.assertEqual(expectedReadabilityMetrics, actualReadabilityMetrics)
