# Learning Python with CS50
# Regular, um, Expressions
# https://cs50.harvard.edu/python/2022/psets/7/um/


import re


def main():
    print(count(input("Text: ")))


def count(string):
    matches = re.findall(r"\b" + re.escape("um") + r"\b", string, flags=re.IGNORECASE)
    return len(matches)


if __name__ == "__main__":
    main()