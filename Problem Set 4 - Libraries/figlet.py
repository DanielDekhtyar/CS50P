# Learning Python with CS50
# Frank, Ian and Glen’s Letters
# https://cs50.harvard.edu/python/2022/psets/4/figlet/

import sys
import random
from pyfiglet import Figlet
def main():
    figlet = Figlet()
    if not (sys.argv[1] == '-f' or sys.argv[1] == '--font'):
        sys.exit(1)

    if len(sys.argv) == 3:
        figlet.setFont(font=sys.argv[2])
        textToPrint = input("Input : ")
        print(figlet.renderText(textToPrint))

    elif len(sys.argv) == 1:
        fontsList = figlet.getFonts()
        if sys.argv[2] not in fontsList:
            sys.exit(1)
        randomFontIndex = random.randint(0, len(fontsList))
        figlet.setFont(font = fontsList[randomFontIndex])
        textToPrint = input("Input : ")
        print(figlet.renderText(textToPrint))

    else:
        sys.exit("Usage: python cs50.py [text] [font]")


main()
