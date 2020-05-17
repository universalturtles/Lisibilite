import logging as LOG
import math

from models.CoreMetrics import CoreMetrics
from models.ReadabilityMetrics import ReadabilityMetrics


class ReadabilityCalculator:
    def __init__(self, coreMetrics: CoreMetrics):
        """
        Readability Calculator init
        """
        LOG.debug(f'{__name__} init')
        self.coreMetrics = coreMetrics

    def computeFRES(self) -> float:
        """
        Compute Flesch Reading Ease Score
        :return: Flesch Reading Ease Score
        """
        fres = 206.835 - \
            (1.015 * self.coreMetrics.getTotalWords() / self.coreMetrics.getTotalSentences()) - \
            (84.6 * self.coreMetrics.getTotalSyllables() / self.coreMetrics.getTotalWords())
        return fres

    def computeFKGL(self) -> float:
        """
        Compute Flesch-Kincaid Grade Level
        :return: Flesch-Kincaid Grade Level
        """
        fkgl = (0.39 * self.coreMetrics.getTotalWords() / self.coreMetrics.getTotalSentences()) + \
               (11.8 * self.coreMetrics.getTotalSyllables() / self.coreMetrics.getTotalWords()) - \
            15.59
        return fkgl

    def computeGFI(self) -> float:
        """
        Compute Gunning Fog Index
        :return: Gunning Fog Index
        """
        gfi = 0.4 * \
            ((self.coreMetrics.getTotalWords() / self.coreMetrics.getTotalSentences()) +
             (100 * (self.coreMetrics.getTotalComplexWords() / self.coreMetrics.getTotalWords())))
        return gfi

    def computeARI(self) -> float:
        """
        Compute Automated Readability Index
        :return: Automated Readability Index
        """
        ari = (4.71 * self.coreMetrics.getTotalCharacters() / self.coreMetrics.getTotalWords()) + \
              (0.5 * self.coreMetrics.getTotalWords() / self.coreMetrics.getTotalSentences()) - 21.43
        return ari

    def computeSMOG(self) -> float:
        """
        Compute Simple Measure of Gobbledygook
        :return: Simple Measure of Gobbledygook
        """
        smog = (1.0430 * math.sqrt(self.coreMetrics.getTotalComplexWords()
                                   * (30 / self.coreMetrics.getTotalSentences()))) + 3.1291
        return smog

    def computeCLI(self) -> float:
        """
        Compute Coleman-Liau Index
        :return: Coleman-Liau Index
        """
        cli = (0.0588 * (self.coreMetrics.getTotalCharacters() / self.coreMetrics.getTotalWords() * 100)) - \
              (0.296 * (self.coreMetrics.getTotalSentences() / self.coreMetrics.getTotalWords() * 100)) - 15.8
        return cli

    def computeLWS(self) -> float:
        """
        Compute Linsear Write Score
        :return: Linsear Write Score
        """
        intermediateScore = ((1 * (self.coreMetrics.getTotalEasyWords() / self.coreMetrics.getTotalWords() * 100)) +
                             (3 * (self.coreMetrics.getTotalComplexWords() / self.coreMetrics.getTotalWords() * 100))) \
            / (self.coreMetrics.getTotalSentences() / self.coreMetrics.getTotalWords() * 100)
        if intermediateScore > 20:
            lws = intermediateScore / 2
        else:
            lws = (intermediateScore - 2) / 2

        return lws

    def computeFRY(self) -> float:
        """
        Compute Fry Readability Formula
        :return: Fry Readability Formula
        """
        return 0.0

    def computeReadabilityMetrics(self) -> ReadabilityMetrics:
        readabilityMetrics = ReadabilityMetrics()
        readabilityMetrics.setFRES(self.computeFRES())
        readabilityMetrics.setFKGL(self.computeFKGL())
        readabilityMetrics.setGFI(self.computeGFI())
        readabilityMetrics.setARI(self.computeARI())
        readabilityMetrics.setSMOG(self.computeSMOG())
        readabilityMetrics.setCLI(self.computeCLI())
        readabilityMetrics.setLWS(self.computeLWS())
        readabilityMetrics.setFRY(self.computeFRY())
        return readabilityMetrics
