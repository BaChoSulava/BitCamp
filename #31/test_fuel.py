import pytest
from fuel import convert
from fuel import gauge

def test_convert():
    assert convert("3/4") == 75
    assert convert("4/4") == 100
    assert convert("1/4") == 25
    assert convert("0/4") == 0

def test_gauge():
    assert gauge(75) == "75%"
    assert gauge(100) == "F"
    assert gauge(25) == "25%"
    assert gauge(0) == "E"

    

def test_errors():
    with pytest.raises(ZeroDivisionError):
        convert("4/0")
    with pytest.raises(ValueError):
        convert("three/four")
        convert("1.5/3")

