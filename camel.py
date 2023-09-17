# Learning Python with CS50
# camelCase
# https://cs50.harvard.edu/python/2022/psets/2/camel/


def main():
    camel = input("camelCase: ")
    print("snake_case: ", end="")
    for i in range(len(camel)):
        if camel[i].isupper():
            print("_", camel[i].lower(), end="", sep="")
        else:
            print(camel[i].lower(), end="")
    print("")


main()
