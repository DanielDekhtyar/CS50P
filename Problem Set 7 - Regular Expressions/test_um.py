# Learning Python with CS50
# Regular, um, Expressions
# https://cs50.harvard.edu/python/2022/psets/7/um/


from um import count


def test_string():
    assert count("hello world") == 0
    assert count("hello") == 0
    assert count("world um world") == 1
    assert count("um") == 1
    assert count("um um") == 2
    assert count("Helloum") == 0
    assert count("uM") == 1


def test_numbers():
    assert count("hello 123 world") == 0
    assert count("hello 123") == 0
    assert count("123 um 123") == 1
    assert count("123 um") == 1
    assert count("123 123") == 0


def test_special():
    assert count("hello world!") == 0
    assert count("hello!") == 0
    assert count("! um ! um") == 2
    assert count("! um") == 1
    assert count("!") == 0
