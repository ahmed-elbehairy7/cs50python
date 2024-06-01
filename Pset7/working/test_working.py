from working import convert
import pytest


def main():
    test_format1()
    test_format2()
    test_both()
    test_errors()
    test_out_of_range_times()


def test_format1():
    assert convert("5:30 AM to 7:00 PM") == "05:30 to 19:00"


def test_format2():
    assert convert("5 AM to 7 PM") == "05:00 to 19:00"


def test_both():
    assert convert("5:00 AM to 7 PM") == "05:00 to 19:00"


def test_errors():
    with pytest.raises(ValueError):
        convert(" to ")
    with pytest.raises(ValueError):
        convert("3:00 AM to 5:00 PM to 6 PM")


def test_out_of_range_times():
    with pytest.raises(ValueError):
        convert("13:00 AM to 4 PM")
    with pytest.raises(ValueError):
        convert("4:60 AM to 5 PM")
