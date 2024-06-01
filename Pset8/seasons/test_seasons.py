from seasons import convert


def main():
    test_convert()
    test_minus


def test_convert():
    assert convert(42) == "Forty-two"


def test_minus():
    assert convert(-32) != "one"
