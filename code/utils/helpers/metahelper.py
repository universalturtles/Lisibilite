import logging as LOG
from utils.io.FileReader import FileReader
from utils.encoding.Base64 import decodeString
from config.AppConfiguration import APP_LOGO_DAT

def printLogo() -> None:
    LOG.debug('Printing logo')
    reader = FileReader()
    data = reader.read(APP_LOGO_DAT)
    print(decodeString(data))
