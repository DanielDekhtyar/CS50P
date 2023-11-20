# Learning Python with CS50
# Emojize
# https://cs50.harvard.edu/python/2022/psets/4/emojize/

import sys
import emoji


def main():
    emojiTextFormat = input("Input: ")
    emojiPicFormat = emoji.emojize(emojiTextFormat)
    print("Output: " + emojiPicFormat)


main()
