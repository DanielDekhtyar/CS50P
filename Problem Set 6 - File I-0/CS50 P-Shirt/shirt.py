# Learning Python with CS50
# CS50 P-Shirt
# https://cs50.harvard.edu/python/2022/psets/6/shirt/


import sys
from PIL import Image
from PIL import ImageOps
import os


def main():
    # Check that file extensions of the images are valid
    # Input extension
    root1, ext1 = os.path.splitext(sys.argv[1])
    # Output extension
    root2, ext2 = os.path.splitext(sys.argv[2])
    if ext1 != ".jpg" and ext1 != ".jpeg" and ext1 != ".png":
        print("Invalid output")
        sys.exit(1)
    elif ext1 != ext2:
        print("Input and output have different extensions")
        sys.exit(1)
    
    try:
        shirt = Image.open("shirt.png", mode= 'r')
        muppet = Image.open(sys.argv[1], mode='r')
    except FileNotFoundError:
        print("Input does not exist")
        sys.exit(1)
    
    size = shirt.size
    # Resize shirt to fit muppet
    muppet = ImageOps.fit(muppet, size)
    if shirt.size == muppet.size:
        # Paste shirt on muppet
        muppet.paste(shirt, shirt)
        muppet.save(sys.argv[2])


def is_argv_valid():
    if len(sys.argv) < 3:
        print("Too few command-line arguments")
        return False
    elif len(sys.argv) > 3:
        print("Too many command-line arguments")
        return False
    else:
        return True


if __name__ == "__main__":
    main()