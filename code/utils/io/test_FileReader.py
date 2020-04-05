from unittest import TestCase
import mock
from utils.io.FileReader import FileReader


class TestFileReader(TestCase):
    def test_read(self):
        data = "MOCKED"
        with mock.patch('builtins.open', mock.mock_open(read_data=data), create=True) as mockFile:
            reader = FileReader()
            result = reader.read("path")
        self.assertEqual(result, data)
