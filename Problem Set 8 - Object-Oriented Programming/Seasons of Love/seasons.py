# Learning Python with CS50
# Seasons of Love
# https://cs50.harvard.edu/python/2022/psets/8/seasons/


from datetime import date
import inflect
import sys


def main():
    date_input = input("Date of Birth: ")
    if date_input.count("-") != 2:
        print("Invalid date")
        sys.exit(1)
    time_from_birth_minutes = int(date_to_minutes(date_input))
    time_in_words = numbers_to_words(time_from_birth_minutes)
    time_in_words = time_in_words.capitalize()
    print(f"{time_in_words} minutes")


def numbers_to_words(time_from_birth_minutes):
    p = inflect.engine()
    return p.number_to_words(time_from_birth_minutes, andword="")


def date_to_minutes(date_input):
    year, month, day = date_input.split("-")
    return (date.today() - date(int(year), int(month), int(day))).total_seconds() / 60


if __name__ == "__main__":
    main()
