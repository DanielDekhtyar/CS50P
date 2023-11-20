# Learning Python with CS50
# Deep Thought
# https://cs50.harvard.edu/python/2022/psets/1/deep/


def main():
    txt = (
        input(
            "What is the Answer to the Great Question of Life, the Universe, and Everything?"
        )
        .strip()
        .lower()
    )
    if txt == "42":
        print("Yes")
    elif txt == "forty two":
        print("Yes")
    elif txt == "forty-two":
        print("Yes")
    else:
        print("No")


main()
