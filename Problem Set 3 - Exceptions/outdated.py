# Learning Python with CS50
# Outdated
# https://cs50.harvard.edu/python/2022/psets/3/outdated/

import re


def main():
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]
    # This code is a loop that prompts the user to enter a date. It then splits the date into its
    # individual parts (month, day, year) using regular expressions.
    while True:
        date = input("Date: ").strip()
        if "," in date or "/" in date:
            month, day, year = splitDate(date, months)
            if validDate(month, day, year):
                break
    if len(day) == 1:
        day = "0" + day
    if len(month) == 1:
        month = "0" + month
    print(year, month, day, sep="-")


def validDate(month, day, year):
    """
    The function `validDate` checks if a given date is valid by checking the format of the month, day,
    and year.

    :param month: The month parameter is the numerical representation of the month in the date. It
    should be a string containing a number between 1 and 12
    :param day: The day parameter is the day of the month. It should be a numeric value between 1 and 31
    :param year: The year parameter is the year of the date that needs to be checked for validity
    :return: a boolean value. It returns True if the date is valid, and False if the date is not valid.
    """
    # This function checks if the date is valid.
    if month.isalpha():
        return False
    if not re.match(r"\d{1,2}", day) or int(day) < 0 or int(day) > 31 or int(day) == 0:
        return False
    elif (
        not re.match(r"\d{1,2}", month)
        or int(month) < 0
        or int(month) > 12
        or int(month) == 0
    ):
        return False
    elif not re.match(r"\d{4}", year) or int(year) < 0:
        return False
    else:
        return True


def splitDate(date, months):
    """
    The function `splitDate` takes a date string and a list of months as input, and returns the month,
    day, and year as separate strings.

    :param date: The date parameter is a string representing a date. It can be in one of two formats:
    :param months: The `months` parameter is a list of month names
    :return: the month, day, and year values extracted from the input date.
    """
    if "/" in date:
        month, day, year = date.split("/")  # split the date by slashes
        return month, day, year
    if "," in date:
        parts = re.split(r"[ ]", date)  # split the date by commas and spaces
        for part in parts:
            parts[parts.index(part)] = part.strip(",")  # strip the ',' from the parts)
        month, day, year = parts
        if month in months:
            month = months.index(month) + 1
            month = str(month)

    return month, day, year


main()
