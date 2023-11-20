# Learning Python with CS50
# Code for 'Back to the Bank'
# https://cs50.harvard.edu/python/2022/psets/5/test_bank/

from bank import value


def test_0():
    assert value("Hello") == 0
    assert value("H") != 0
    assert value("Hello World") == 0
    assert value("Hello World!") == 0
    assert value("Hi") != 0


def test_20():
    assert value("Hi") == 20
    assert value("Hello") != 20
    assert value("Hello World") != 20
    assert value("Howdy !") == 20
    assert value("Good bye") != 20


def test_100():
    assert value("Hello World") != 100
    assert value("Hello World!") != 100
    assert value("Howdy !") != 100
    assert value("Good bye") == 100
    assert value("Goodbye") == 100
    assert value("!@#$%^&*()") == 100
    assert value("1234567890") == 100
    assert value("1 2 3 4 5 6 7 8 9 0") == 100
