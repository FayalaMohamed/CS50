from fuel import convert
from fuel import gauge
import pytest

def test_gauge():
    assert gauge(0) == "E"
    assert gauge(100) == "F"
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(50) == "50%"
    assert gauge(98) == "98%"


def test_convert():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")
    with pytest.raises(ValueError):
        convert("2/1")
    assert convert("3/4") == 75
    assert convert("1/2") == 50
    assert convert("1/1") == 100
    assert convert("0/4") == 0
