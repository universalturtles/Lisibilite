from unittest import TestCase
from models.Score import Score


class TestScore(TestCase):
    def setUp(self) -> None:
        self.score = Score(1.18991)

    def test_get_rounded_value(self):
        expectedValue = 1.19
        self.assertEqual(expectedValue, self.score.getRoundedValue())
