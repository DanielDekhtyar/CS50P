# Learning Python with CS50
# Vanity Plates
# https://cs50.harvard.edu/python/2022/psets/2/plates/


def main():
    plate = input("Plate: ").upper().strip()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if (
        is_char_between_6_and_2(s)
        and is_start_with_2_letters(s)
        and is_first_number_zero(s)
        and check_special_chars(s)
        and is_numbers_after_letters(s)
    ):
        return True
    else:
        return False


def is_char_between_6_and_2(s):
    if len(s) >= 2 and len(s) <= 6:
        return True
    else:
        return False


def is_start_with_2_letters(s):  # DONE
    if s[0].isalpha() and s[1].isalpha():
        return True
    else:
        return False


def is_first_number_zero(s):  # DONE
    for char in s:
        if char.isnumeric():
            if char == "0":
                return False
            else:
                return True
        else:
            continue
    return True


def check_special_chars(s):  # DONE
    special_chars = ".<>,/:;'{[]}+-*!@#$%^&()_=?"
    for char in range(len(s)):
        if s[char].isspace() or s[char] in special_chars:
            return False
    else:
        return True


def is_numbers_after_letters(s):  # DONE
    number_encountered = False
    for char in s:
        if char.isnumeric():
            number_encountered = True
        elif char.isalpha() and number_encountered:
            return False
    return True


if __name__ == "__main__":
    main()
