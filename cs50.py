# Learning Python with CS50

import sys
import requests


def main():
    amountOfBitcoins = getBitcoinAmount()
    print(amountOfBitcoins)
    bitcoinPrice = getBitcoinPrice()
    priceToPay = float(amountOfBitcoins) * bitcoinPrice
    print(f"${priceToPay:,.4f}")


def getBitcoinAmount():
    while True:
        if len(sys.argv) != 2:
            sys.exit("Usage: ./bitcoin.py amountOfBitcoins")
        elif is_float(sys.argv[1]):
            amountOfBitcoins = sys.argv[1]
            return amountOfBitcoins
        else:
            sys.exit(1)


def getBitcoinPrice():
    url = "https://api.coindesk.com/v1/bpi/currentprice.json"
    bitcoinJSONresponse = requests.get(url)
    bitcoinJSONresponse = bitcoinJSONresponse.json()
    bitcoinPrice = float(bitcoinJSONresponse["bpi"]["USD"]["rate_float"])
    return bitcoinPrice


def is_float(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


main()
