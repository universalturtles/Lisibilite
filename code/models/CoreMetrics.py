import logging as LOG


class CoreMetrics:
    def __init__(self):
        LOG.debug(f"{__name__} init")
        self.totalWords = 0
        self.totalSentences = 0
        self.totalSyllables = 0
        self.totalComplexWords = 0
        self.totalEasyWords = 0
        self.totalCharacters = 0

    def setTotalWords(self, totalWords: int) -> None:
        """
        Set total words
        :param totalWords: The total number of words in the passage
        :return: None
        """
        LOG.debug(f'Setting total words as {totalWords}')
        self.totalWords = totalWords

    def getTotalWords(self) -> int:
        """
        Get the total words in the passage
        :return: The total words in the passage
        """
        LOG.debug(f'Getting total words. Total Words = {self.totalWords}')
        return self.totalWords

    def setTotalSentences(self, totalSentences: int) -> None:
        """
        Set total sentences
        :param totalSentences: The total number of sentences in the passage
        :return: None
        """
        LOG.debug(f'Setting total sentences as {totalSentences}')
        self.totalSentences =  totalSentences

    def getTotalSentences(self) -> int:
        """
        Get the total sentences in the passage
        :return: The total number of sentences in the passage
        """
        LOG.debug(f'Getting total sentences. Total Sentences = {self.totalSentences}')
        return self.totalSentences

    def setTotalSyllables(self, totalSyllables: int) -> None:
        """
        Set total syllables
        :param totalSyllables: The total syllables in the passage
        :return: None
        """
        LOG.debug(f'Setting total syllables as {totalSyllables}')
        self.totalSyllables = totalSyllables

    def getTotalSyllables(self) -> int:
        """
        Get the total syllables in the passage
        :return: The total syllables in the passage
        """
        LOG.debug(f'Getting total syllables. Total syllables = {self.totalSyllables}')
        return self.totalSyllables

    def setTotalComplexWords(self, totalComplexWords: int) -> None:
        """
        Set total complex words
        :param totalComplexWords: The total complex words in the passage
        :return: None
        """
        LOG.debug(f'Setting total complex words as {totalComplexWords}')
        self.totalComplexWords = totalComplexWords

    def getTotalComplexWords(self) -> int:
        """
        Get the total complex words  in the passage
        :return: The total complex words  in the passage
        """
        LOG.debug(f'Getting total complex words . Total complex words  = {self.totalComplexWords}')
        return self.totalComplexWords

    def setTotalEasyWords(self, totalEasyWords: int) -> None:
        """
        Set total easy words
        :param totalEasyWords: The total easy words in the passage
        :return: None
        """
        LOG.debug(f'Setting total easy words as {totalEasyWords}')
        self.totalEasyWords = totalEasyWords

    def getTotalEasyWords(self) -> int:
        """
        Get the total easy words  in the passage
        :return: The total easy words  in the passage
        """
        LOG.debug(f'Getting total easy words . Total easy words  = {self.totalEasyWords}')
        return self.totalEasyWords

    def setTotalCharacters(self, totalCharacters: int) -> None:
        """
        Set total characters
        :param totalCharacters: The total characters in the passage
        :return: None
        """
        LOG.debug(f'Setting total characters as {totalCharacters}')
        self.totalCharacters = totalCharacters

    def getTotalCharacters(self) -> int:
        """
        Get the total characters  in the passage
        :return: The total characters  in the passage
        """
        LOG.debug(f'Getting total characters . Total characters  = {self.totalCharacters}')
        return self.totalCharacters
