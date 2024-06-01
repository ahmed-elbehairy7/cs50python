from plates import is_valid


def main():
    test_alphabet_start()
    test_length()
    test_numbers_front_end_only()
    test_spaces()
    test_number_not_start_with_zero()


def test_alphabet_start():
    assert is_valid("he") == True
    assert is_valid("12") == False
    assert is_valid("2h") == False
    assert is_valid("h2") == False


def test_length():
    assert is_valid("c") == False
    assert is_valid("hello, world") == False


def test_numbers_front_end_only():
    assert is_valid("cs50") == True
    assert is_valid("cs5o") == False


def test_spaces():
    assert is_valid("cs 50") == False


def test_number_not_start_with_zero():
    assert is_valid("cs05") == False


if __name__ == "__main__":
    main()
