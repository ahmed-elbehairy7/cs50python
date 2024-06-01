from numb3rs import validate


def main() -> None:
    test_bigger()
    test_negative()
    test_dots()
    test_correct()


def test_bigger():
    assert validate("256.0.0.0") == False
    assert validate("1000.010010.2032.0323") == False
    assert validate("10.666.666.666") == False


def test_negative():
    assert validate("-1.0.0.0") == False
    assert validate("-3.-53.32.-4") == False


def test_dots():
    assert validate("1.1.1.1.1") == False
    assert validate("1.1.1") == False


def test_correct():
    assert validate("0.0.0.0") == True
    assert validate("255.255.255.255") == True
    assert validate("12.43.123.67") == True


if __name__ == "__main__":
    main()
