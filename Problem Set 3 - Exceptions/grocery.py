# Learning Python with CS50
# Grocery List
# https://cs50.harvard.edu/python/2022/psets/3/grocery/


def main():
    fuel = fuelGauge()
    print(fuel, "%", sep="")


def fuelGauge():
    while True:
        try:
            fuel = input("Fraction: ")
            x, y = fuel.split("/")
            fuel = (int(x) / int(y)) * 100
            fuel = round(fuel)
            if fuel <= 1 and fuel >= 0:
                return "E"
            elif fuel >= 99 and fuel <= 100:
                return "F"
            elif fuel > 1 and fuel < 99:
                return fuel
        except (ValueError, ZeroDivisionError):
            pass


main()
