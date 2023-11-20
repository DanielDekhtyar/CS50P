# Learning Python with CS50
# Adieu, Adieu
# https://cs50.harvard.edu/python/2022/psets/4/adieu/


def main():
    nameList = []
    while True:
        try:
            nameInput = input()
            nameList.append(nameInput)
        except EOFError:
            break
    if len(nameList) == 0:
        print("No names were entered")
    elif len(nameList) == 1:
        print("Adieu, adieu, to", nameList[0])
    elif len(nameList) == 2:
        print("Adieu, adieu, to", nameList[0], "and", nameList[1])
    else:
        print("Adieu, adieu, to", nameList[0], end=", ")
        for nameIndex in nameList[1:-1]:
            print(nameIndex, end=", ")
        print("and", nameList[-1])


main()
