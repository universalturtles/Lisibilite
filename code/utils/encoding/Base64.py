import base64
import logging as LOG

CHAR_ENCODING = 'ascii'

def decodeString(encodedString: str) -> str:
    LOG.debug("Decoding Base 64 message from string")
    encodedBytes = encodedString.encode(CHAR_ENCODING)
    base64Bytes = base64.b64decode(encodedBytes)
    base64Message = base64Bytes.decode('ascii')
    return base64Message


def encodeString(decodedString: str) -> str:
    LOG.debug("Encoding Base 64 message from string")
    decodedBytes = decodedString.encode(CHAR_ENCODING)
    base64Bytes = base64.b64encode(decodedBytes)
    base64String = base64Bytes.decode('ascii')
    return base64String
