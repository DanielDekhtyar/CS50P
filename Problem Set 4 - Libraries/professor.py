# Learning Python with CS50
# Little Professor
# https://cs50.harvard.edu/python/2022/psets/4/professor/

import random
def main():
    level = get_level()
    score = 0
    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        answer = x + y
        for i in range(3):
            print(x, "+", y, "= ", end="")
            userAnswer = int(input())
            if answer == userAnswer:
                score += 1
                break
            else:
                if i < 2: # 'i' initialized as 0 at the start of the 'for' loop and goes up to 2; aka 3 times
                    print("EEE")
                    continue
                else:
                    print(x, "+", y, "=", (x + y))
    print("Score:", score)


def get_level():
    while True:
        level = input()
        if level.isdigit():
            level = int(level)
        else:
            continue
        if level == 1 or level == 2 or level == 3:
            return level
        else:
            continue


def generate_integer(level):
    if level == 1:
        number = random.randint(0, 9)
    elif level == 2:
        number = random.randint(10, 99)
    else:
        number = random.randint(100, 999)
    return number


if __name__ == "__main__":
    main()
