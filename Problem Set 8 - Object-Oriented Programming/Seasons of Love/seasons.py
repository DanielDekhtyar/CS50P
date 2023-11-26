# Learning Python with CS50
# Seasons of Love
# https://cs50.harvard.edu/python/2022/psets/8/seasons/

import sys
import re
from datetime import date
import inflect


def main():
    date_input = input("Date of Birth: ")
    # re checks if the date is valid yyyy/mm/dd
    if re.search(r"^\d{4}-\d{2}-\d{2}$", date_input):
        # get the number of minutes since birth as int
        time_from_birth_minutes = int(date_to_minutes(date_input))
        # convert minutes (int) to words
        time_in_words = numbers_to_words(time_from_birth_minutes)
        print(f"{time_in_words} minutes")
    else:
        print("Invalid date")
        sys.exit(1)


def numbers_to_words(time_from_birth_minutes: int) -> str:
    p = inflect.engine()
    time_in_words = p.number_to_words(time_from_birth_minutes, andword="")
    # make the first letter capital
    time_in_words = time_in_words.capitalize()
    return time_in_words


def date_to_minutes(date_input: str) -> int:
    year, month, day = date_input.split("-")
    # return how many minutes from birth as int
    return (date.today() - date(int(year), int(month), int(day))).total_seconds() / 60


if __name__ == "__main__":
    main()
