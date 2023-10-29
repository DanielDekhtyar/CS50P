# My own code to use later

def getPositiveInt(userInputToPrint=""):
    while True:
        number = input(userInputToPrint)
        if number.isdigit() and int(number) >= 1:
            return int(number)
        else:
            continue


def is_float(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
