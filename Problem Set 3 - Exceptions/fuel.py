# Learning Python with CS50
# Fuel Gauge
# https://cs50.harvard.edu/python/2022/psets/3/fuel/


def main():
    fuel = fuelGauge()
    if fuel <= 1 and fuel >= 0:
        print("E")
    elif fuel >= 99 and fuel <= 100:
        print("F")
    elif fuel > 1 and fuel < 99:
        print(fuel, '%', sep='')

def fuelGauge():
    while True:
        try:
            fuel = input("Fraction: ")
            x, y = fuel.split('/')
            x = int(x)
            y = int(y)
            if x > y:
                continue
            elif not isinstance(x, int) or not isinstance(y, int):
                continue
            fuel = (x / y)*100
            fuel = round(fuel)
            return fuel
        except (ValueError, ZeroDivisionError):
            pass



main()


'''
# Code for 'Refueling'
# https://cs50.harvard.edu/python/2022/psets/5/test_fuel/


def main():
    fuel = convert(input("Fraction: "))
    print(gauge(fuel))
    


def convert(fraction):
    while True:
        try:
            x, y = fraction.split('/')
            x = int(x)
            y = int(y)
            if x > y:
                continue
            elif not isinstance(x, int) or not isinstance(y, int):
                continue
            fuel = (x / y)*100
            fuel = round(fuel)
            return fuel
        except (ValueError, ZeroDivisionError):
            pass


def gauge(fuel):
    if fuel <= 1 and fuel >= 0:
        return "E"
    elif fuel >= 99 and fuel <= 100:
        return "F"
    elif fuel > 1 and fuel < 99:
        return (f"{fuel}%")


if __name__ == "__main__":
    main()
'''