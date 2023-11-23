# Learning Python with CS50
# Seasons of Love
# https://cs50.harvard.edu/python/2022/psets/8/seasons/


from seasons import date_to_minutes


def test_date_to_minutes():
    assert date_to_minutes("1999-01-01") == 13089600
    assert date_to_minutes("2001-01-01") == 12036960
    assert date_to_minutes("1995-01-01") == 15193440
    assert date_to_minutes("1998-06-20") == 13370400
    assert date_to_minutes("2003-07-27") == 10687680
