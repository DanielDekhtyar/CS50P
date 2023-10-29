# Learning Python with CS50
# Lines of Code
# https://cs50.harvard.edu/python/2022/psets/6/lines/


import sys


def main():
    if is_argv_valid():
        file_location = sys.argv[1].lstrip()
        line_counter = 0
        try:
            file = open(file_location, "r")
        except FileNotFoundError:
            print("File does not exist")
            sys.exit(1)
        for line in file:
            if line.strip().startswith('#') or line.isspace():
                continue
            else:
                line_counter += 1
        file.close()

        print(line_counter)
    else:
        sys.exit(1)


def is_argv_valid() -> bool:
    if len(sys.argv) < 2:
        print("Too few command-line arguments")
        return False
    elif len(sys.argv) > 2:
        print("Too many command-line arguments")
        return False
    elif not sys.argv[1].endswith(".csv"):
        print("Not a CSV file")
        return False
    else:
        return True


if __name__ == "__main__":
    main()
