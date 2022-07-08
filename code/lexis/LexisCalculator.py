import logging as LOG

import nltk
import syllables
from nltk import sent_tokenize

from models.CoreMetrics import CoreMetrics


class LexisCalculator:
    def __init__(self, inputText: str):
        """
        Lexis Calculator init
        """
        LOG.debug(f'{__name__} init')

        self.inputText = inputText
        self.hardWordSyllableThreshold = 3

    def computeMetrics(self) -> CoreMetrics:
        LOG.debug(f'Computing core metrics')
        if len(self.inputText.strip()) == 0:
            LOG.error("The input text is empty.")
            return CoreMetrics()
        sentenceCount: int = 0
        wordCount: int = 0
        characterCount: int = 0
        syllableCount: int = 0
        hardWords: int = 0
        easyWords: int = 0

        sentences = sent_tokenize(self.inputText)
        sentenceCount = len(sentences)
        for sentence in sentences:
            sentence = sentence.strip()
            words = sentence.split()
            wordCount += len(words)
            for word in words:
                characterCount += len(word)
                syllableCountInWord = syllables.estimate(word)
                syllableCount += syllableCountInWord
                if syllableCount > self.hardWordSyllableThreshold:
                    hardWords += 1
                else:
                    easyWords += 1

        coreMetrics = CoreMetrics()
        coreMetrics.setTotalSentences(sentenceCount)
        coreMetrics.setTotalWords(wordCount)
        coreMetrics.setTotalComplexWords(hardWords)
        coreMetrics.setTotalEasyWords(easyWords)
        coreMetrics.setTotalCharacters(characterCount)
        coreMetrics.setTotalSyllables(syllableCount)

        return coreMetrics
