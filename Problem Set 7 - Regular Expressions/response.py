# Learning Python with CS50
# Response Validation
# https://cs50.harvard.edu/python/2022/psets/7/response/


import validators


def main():
    email = input("What's your email address? ")
    if validators.email(email):
        print("Valid")
    else:
        print("Invalid")


if __name__ == "__main__":
    main()
