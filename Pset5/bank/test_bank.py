from bank import value


def main():
    test_hello()
    test_h()
    test_else()


def test_hello():
    assert value("hello Ahmed") == 0
    assert value("HeLlO Ahmed") == 0


def test_h():
    assert value("hey Ahmed") == 20
    assert value("HeY Ahmed") == 20


def test_else():
    assert value("Whassup Ahmed") == 100
    assert value("WhaSSuP Ahmed") == 100


if __name__ == "__main__":
    main()
