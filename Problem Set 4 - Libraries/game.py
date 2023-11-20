# Learning Python with CS50
# Guessing Game
# https://cs50.harvard.edu/python/2022/psets/4/game/

import random


def main():
    n = getPositiveInt("Level: ")
    randomNum = random.randint(1, n)
    while True:
        userGuess = getPositiveInt("Guess: ")
        if userGuess < randomNum:
            print("Too small!")
            continue
        elif userGuess > randomNum:
            print("Too large!")
            continue
        else:
            print("Just right!")
            exit(0)


def getPositiveInt(inputText):
    while True:
        number = input(inputText)
        if number.isdigit() and int(number) >= 1:
            return int(number)
        else:
            pass


main()
