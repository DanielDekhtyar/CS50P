# Learning Python with CS50
# Code for 'Re-requesting a Vanity Plate'
# https://cs50.harvard.edu/python/2022/psets/5/test_plates/


from plates import is_valid


def main():
    test_check_special_chars()
    test_is_char_between_6_and_2()
    test_is_first_number_zero()
    test_is_start_with_2_letters()


def test_is_char_between_6_and_2():
    assert is_valid("Hello") == True
    assert is_valid("MAMAMIA") == False
    assert is_valid("AB") == True
    assert is_valid("AB12") == True
    assert is_valid("ABCDEF") == True
    assert is_valid("A") == False


def test_is_start_with_2_letters():
    assert is_valid("Hello") == True
    assert is_valid("A") == False
    assert is_valid("12") == False
    assert is_valid("HELLO") == True
    assert is_valid("AB") == True


def test_is_first_number_zero():
    assert is_valid("HI10") == True
    assert is_valid("CS50") == True
    assert is_valid("CS05") == False
    assert is_valid("Good12") == True


def test_check_special_chars():
    assert is_valid("Hi") == True
    assert is_valid("Hi!!") == False
    assert is_valid("Hi???") == False


def test_is_numbers_after_letters():
    assert is_valid("HI10") == True
    assert is_valid("HI10A") == False
    assert is_valid("HI10A10") == False


if __name__ == "__main__":
    main()
