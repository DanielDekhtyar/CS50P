# Learning Python with CS50
# Coke Machine
# https://cs50.harvard.edu/python/2022/psets/2/coke/


def main():
    toPay = 50
    while toPay > 0:
        print("Amount Due:", toPay)
        coins = int(input("Insert Coin:"))
        if coins == 25 or coins == 10 or coins == 5:
            toPay = toPay - coins
        else:
            continue
    print("Change Owed:", abs(toPay))


main()
