from io import StringIO
from unittest import TestCase
from unittest.mock import Mock, patch
import hw

class TestGreeting(TestCase):
    def test(self):
        g = hw.Greeting("x", "y")
        self.assertEqual(str(g), "x y")

class TestMain(TestCase):
    def setUp(self):
        self.mock_greeting = Mock(
            name="Greeting", return_value=Mock(
                name="Greeting instance",
                __str__=Mock(return_value="mock str output")
            )
        )
        self.mock_stdout = StringIO()