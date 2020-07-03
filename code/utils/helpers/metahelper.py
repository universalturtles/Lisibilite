import logging as LOG

from config.AppConfiguration import APP_LOGO_DAT
from inputoutput.FileReader import FileReader
from utils.encoding.Base64 import decodeString


def printLogo() -> None:
    LOG.debug('Printing logo')
    reader = FileReader()
    data = reader.read(APP_LOGO_DAT)
    print(decodeString(data))
