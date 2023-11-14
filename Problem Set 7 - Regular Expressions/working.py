# Learning Python with CS50
# Working 9 to 5
# https://cs50.harvard.edu/python/2022/psets/7/working/


import re
import sys


def main():
    converted_time = convert(input("Hours: "))
    if converted_time is not ValueError:
        print(converted_time)
    else:
        print("ValueError")
        sys.exit(1)


def convert(s):
    time = re.search(
        r"^(.|.{2})(:[0-5][0-9])? (AM|PM) to (.|.{2})(:[0-5][0-9])? (AM|PM)$", s)
    if time is not None:
        time1 = time.group(1)
        time2 = time.group(4)
        time1 = re.sub(r"^(.)$", r"0\1", time1)
        time2 = re.sub(r"^(.)$", r"0\1", time2)
        if time.group(3) == "PM" and time1 != "12":
            time1 = int(time1) + 12
        if time.group(6) == "PM" and time2 != "12":
            time2 = int(time2) + 12
        if time1 == "12" and time.group(3) == "AM":
            time1 = "00"
        if time2 == "12" and time.group(6) == "AM":
            time2 = "00"
        if time.group(2) is not None:
            time1 = f"{time1}{time.group(2)}"
        else:
            time1 = f"{time1}:00"
        if time.group(5) is not None:
            time2 = f"{time2}{time.group(5)}"
        else:
            time2 = f"{time2}:00"
        return f"{time1} to {time2}"
    else:
        return ValueError


if __name__ == "__main__":
    main()
