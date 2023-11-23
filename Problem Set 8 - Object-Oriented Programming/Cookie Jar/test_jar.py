# Learning Python with CS50
# Cookie Jar
# https://cs50.harvard.edu/python/2022/psets/8/jar/

from jar import Jar


def test_init():
    jar = Jar()
    assert jar.capacity == 12
    jar2 = Jar(15)
    assert jar2.capacity == 15


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(2)
    assert jar.size == 2


def test_withdraw():
    jar = Jar(8)
    jar.deposit(8)
    jar.withdraw(2)
    assert jar.size == 6
