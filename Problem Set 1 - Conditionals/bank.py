# Learning Python with CS50
# Home Federal Savings Bank
# https://cs50.harvard.edu/python/2022/psets/1/bank/

"""
def main():
    txt = input("Greeting: ").strip().lower()
    if txt[0:5] == "hello":
        print("$0")
    elif txt.startswith("h"):
        print("$20")
    else:
        print("$100")


main()
"""

# Code for 'Back to the Bank'
# https://cs50.harvard.edu/python/2022/psets/5/test_bank/


def main():
    txt = input("Greeting: ").strip().lower()
    print("$" + str(value(txt)))


def value(greeting):
    greeting = greeting.lower().strip()

    if greeting[0:5] == "hello":
        return 0
    elif greeting.startswith("h"):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
