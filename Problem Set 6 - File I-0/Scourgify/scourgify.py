# Learning Python with CS50
# Scourgify
# https://cs50.harvard.edu/python/2022/psets/6/scourgify/


import csv
import sys


def main():
    if is_argv_valid():
        before_csv = sys.argv[1]
        after_csv = sys.argv[2]
        
        try:
            before = open(before_csv, 'r')
            reader = csv.DictReader(before) 
        except FileNotFoundError:
            print(f"Could not read {before_csv}")
            sys.exit(1)
            
        with open(after_csv, 'w', newline = '') as after:
            writer = csv.DictWriter(after, fieldnames = ["first", "last", "house"])
            writer.writeheader()
            for row in reader:
                last, first = row["name"].split(",")
                house = row["house"]
                writer.writerow({"first" : first.strip(), "last" : last.strip(), "house" : house.strip()})
        
        before.close()
    
    else:
        sys.exit(1)


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
