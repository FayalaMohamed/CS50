from jar import Jar
import pytest


def test_init():
    jar1 = Jar()
    assert jar1.capacity == 12
    assert jar1.size == 0
    jar1 = Jar(1)
    assert jar1.capacity == 1
    assert jar1.size == 0
    with pytest.raises(ValueError):
        jar1 = Jar(-1)


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar1 = Jar()
    jar1.deposit(5)
    assert jar1.size == 5
    jar1.deposit(5)
    assert jar1.size == 10
    with pytest.raises(ValueError):
        jar1.deposit(5)


def test_withdraw():
    jar1 = Jar()
    jar1.deposit(5)
    jar1.withdraw(1)
    assert jar1.size == 4
    jar1.withdraw(1)
    assert jar1.size == 3
    with pytest.raises(ValueError):
        jar1.withdraw(5)
