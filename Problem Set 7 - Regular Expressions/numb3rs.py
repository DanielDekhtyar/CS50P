# Learning Python with CS50
# NUMB3RS
# https://cs50.harvard.edu/python/2022/psets/7/numb3rs/


import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if ip := re.search(r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$", ip):
        for num in range(4):
            if int(ip.group(num + 1)) > 255:
                return False
        return True
    else:
        return False


if __name__ == "__main__":
    main()
