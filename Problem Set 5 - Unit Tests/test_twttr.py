# Learning Python with CS50
# Testing my twttr
# https://cs50.harvard.edu/python/2022/psets/5/test_twttr/

from twttr import shorten


def main():
    test_text()
    test_num()
    test_special_char()


def test_text():
    assert shorten("twitter") == "twttr"
    assert shorten("Twitter") == "Twttr"
    assert shorten("HELLO") == "HLL"
    assert shorten("Twitter is awesome") == "Twttr s wsm"
    assert shorten("Hello World") == "Hll Wrld"
    assert shorten("Hello World!") == "Hll Wrld!"


def test_num():
    assert shorten("123") == "123"
    assert shorten("123 456") == "123 456"
    assert shorten("-1") == "-1"
    assert shorten("-1 -2") == "-1 -2"
    assert shorten("0") == "0"
    assert shorten("1.852") == "1.852"
    assert shorten("1.852.852") == "1.852.852"
    assert shorten("-5.612") == "-5.612"


def test_special_char():
    assert shorten("!@#$%^&*()_+-={}[]:;'<>?,./") == "!@#$%^&*()_+-={}[]:;'<>?,./"
    assert shorten("`~@#$%^&*()_+-={}[]:;'<>?,./") == "`~@#$%^&*()_+-={}[]:;'<>?,./"


if __name__ == "__main__":
    main()
