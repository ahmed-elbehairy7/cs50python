from twttr import shorten


def main():
    test_lower()
    test_upper()
    test_numbers()
    test_punctuation()


def test_lower():
    assert shorten("ahmed") == "hmd"
    assert shorten("alaa") == "l"
    assert shorten("behairy") == "bhry"


def test_upper():
    assert shorten("AHMED") == "HMD"
    assert shorten("ALAA") == "L"
    assert shorten("BEHAIRY") == "BHRY"


def test_numbers():
    assert shorten("elbehairy7") == "lbhry7"
    assert shorten("2005") == "2005"


def test_punctuation():
    assert shorten("!?.,") == "!?.,"


if __name__ == "__main__":
    main()
