# Learning Python with CS50
# Meal Time
# https://cs50.harvard.edu/python/2022/psets/1/meal/


def main():
    time = input("What time is it? ")
    time = convert(time)
    if 7.0 <= time <= 8.0:
        print("breakfast time")
    elif 12.0 <= time <= 13.0:
        print("lunch time")
    elif 18.0 <= time <= 19.0:
        print("dinner time")


def convert(time):
    h, m = time.split(":")
    time = int(h) + int(m) / 60
    return time


if __name__ == "__main__":
    main()
