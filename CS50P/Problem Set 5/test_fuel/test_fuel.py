import pytest
from fuel import convert
from fuel import gauge


def test_negative():
        with pytest.raises(ValueError):
            convert("-1/5")

def test_neumerator():
        with pytest.raises(ValueError):
            convert("5/2")

def test_nonfraction():
        with pytest.raises(ValueError):
            convert("Cat")
def test_str():
      with pytest.raises(ValueError):
            convert("5")
            convert("False")
            convert("6.5")

def test_denominator():
        with pytest.raises(ZeroDivisionError):
            convert("10/0")
            convert("1/-5")

def test_convert():
    assert convert("1/4") == 25
    assert convert("1/2") == 50

def test_gauge():
    assert gauge(67) == "67%"
    assert gauge(50) == "50%"
    assert gauge(1) == "E"
    assert gauge(99) == "F"
