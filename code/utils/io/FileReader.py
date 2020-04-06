import logging as LOG
from customexceptions.ReadabilityErrors import IOError


class FileReader:
    def __init__(self):
        """
        File Reader init
        """
        LOG.debug(f'{__name__} init')

    def read(self, filename: str) -> str:
        """
        Read the contents of a file
        :param filename: The name of the file to read
        :return: The file contents if read is successful. Else None
        """
        LOG.debug(f'Reading file {filename}')
        try:
            with open(filename, 'r', encoding='utf-8') as reader:
                return reader.read()
        except FileNotFoundError as fnf_error:
            LOG.error(f'File {filename} not found. Error: {fnf_error}')
            raise IOError(f'File {filename} not found. Error: {fnf_error}')
        except Exception as error:
            LOG.error(f'Error in reading the file {filename}. Error: {error}')
            raise IOError(f'Error in reading the file {filename}. Error: {error}')
