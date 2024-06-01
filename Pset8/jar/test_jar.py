from jar import Jar


def main():
    test_init()
    test_deposit()
    test_withdraw()
    test_str()


def test_init():
    assert Jar()


def test_deposit():
    test_rat = Jar()
    test_rat.deposit(3)
    assert test_rat.size == 3


def test_withdraw():
    test_rat = Jar()
    test_rat.deposit(3)
    test_rat.withdraw(2)
    assert test_rat.size == 1


def test_str():
    test_rat = Jar()
    test_rat.deposit(5)
    assert str(test_rat) == "🍪🍪🍪🍪🍪"
