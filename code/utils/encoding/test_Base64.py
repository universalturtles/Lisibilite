from unittest import TestCase

from utils.encoding.Base64 import *


class Test(TestCase):
    def setUp(self) -> None:
        self.plainText = 'This is lisibilite'
        self.base64Encoded = 'VGhpcyBpcyBsaXNpYmlsaXRl'

    def test_decode_string(self):
        result = decodeString(self.base64Encoded)
        self.assertEqual(result, self.plainText)

    def test_encode_string(self):
        result = encodeString(self.plainText)
        self.assertEqual(result, self.base64Encoded)
