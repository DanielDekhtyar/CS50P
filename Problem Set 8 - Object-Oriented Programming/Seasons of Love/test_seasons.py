# Learning Python with CS50
# Seasons of Love
# https://cs50.harvard.edu/python/2022/psets/8/seasons/


from seasons import numbers_to_words


def test_date_to_minutes():
    assert numbers_to_words(10694880) == "Ten million, six hundred ninety-four thousand, eight hundred eighty"
    assert numbers_to_words(13096800) == "Thirteen million, ninety-six thousand, eight hundred"
    assert numbers_to_words(1833120) == "One million, eight hundred thirty-three thousand, one hundred twenty"
    assert numbers_to_words(13377600) == "Thirteen million, three hundred seventy-seven thousand, six hundred"
    assert numbers_to_words(12044160) == "Twelve million, forty-four thousand, one hundred sixty"
    