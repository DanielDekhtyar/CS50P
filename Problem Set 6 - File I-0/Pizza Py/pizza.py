# Learning Python with CS50
# Pizza Py
# https://cs50.harvard.edu/python/2022/psets/6/pizza/


import sys
import csv
import tabulate

def main():
    if is_argv_valid():
        file_location = sys.argv[1]
        try:
            with open(file_location, 'r') as csv_file:
                csv_reader = csv.reader(csv_file)
                data = [row for row in csv_reader]
        except FileNotFoundError:
            sys.exit(1)
        
        # Print the data in a grid format
        table = tabulate.tabulate(data, headers='firstrow', tablefmt='grid')
        print(table)
    else:
        sys.exit(1)


def is_argv_valid():
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
