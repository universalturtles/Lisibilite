import logging as LOG

from config.AppConfiguration import APP_LOGO_DAT
from utils.encoding.Base64 import decodeString
from inputoutput import FileReader


def printLogo() -> None:
    LOG.debug('Printing logo')
    reader = FileReader()
    data = reader.read(APP_LOGO_DAT)
    print(decodeString(data))
