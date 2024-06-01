from fuel import convert, gauge
import pytest


def main():
    test_convert()
    test_gauge()
    return 1


def test_convert():
    assert convert("3/4") == 75
    assert convert("1/2") == 50
    with pytest.raises(ZeroDivisionError):
        convert("1/0")
    with pytest.raises(ValueError):
        convert("3/2")
        convert("cat/dog")


def test_gauge():
    assert convert("3/4") == 75 and gauge(75) == "75%"
    assert convert("1/100") == 1 and gauge(1) == "E"
    assert convert("99/100") == 99 and gauge(99) == "F"
