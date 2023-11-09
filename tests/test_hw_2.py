from io import StringIO
from unittest import Mock
import pytest
import hw

def test_greeting():
    g = hw.Greeting("x", "y")
    assert str(g) == "x y"

@pytest.fixture
def mock_greeting(monkeypatch):
    greeting = Mock(
        name="Greeting", return_value=Mock(
            name="Greeting instance",
            __str__=Mock(return_value="mock str output")
        )
    )
    monkeypatch.setattr(hw, 'Greeting', greeting)
    return greeting