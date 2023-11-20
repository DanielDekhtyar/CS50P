# Learning Python with CS50
# Making Faces
# https://cs50.harvard.edu/python/2022/psets/0/faces/


def main():
    msg = input("Give me a text : ")
    print(convert(msg))


def convert(msg):
    return msg.replace(":)", "🙂").replace(":(", "🙁")


main()
