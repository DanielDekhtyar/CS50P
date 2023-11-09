# Learning Python with CS50
# NUMB3RS
# https://cs50.harvard.edu/python/2022/psets/7/numb3rs/


from numb3rs import validate


def test_numbers():
    assert validate("1.2.3.4") == True
    assert validate("167.17.89.212") == True
    assert validate("346.679.235.683") == False
    assert validate("684.125.21.21") == False
    assert validate("32.437.23.13") == False
    assert validate("127.184.357.13") == False
    assert validate("212.179.63.765") == False
    assert validate("36.46") == False
    assert validate("4547.45673.3456.1245") == False


def test_strings():
    assert validate("hello world") == False
    assert validate("cat") == False
