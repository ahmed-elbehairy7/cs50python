from um import count


def main():
    test_one()
    test_in_words()
    test_cases()


def test_one():
    assert count("um") == 1
    assert count("um.") == 1


def test_in_words():
    assert count("yummy") == 0
    assert count("yum") == 0
    assert count("umt") == 0


def test_cases():
    assert count("Um") == 1
    assert count("UM.") == 1
