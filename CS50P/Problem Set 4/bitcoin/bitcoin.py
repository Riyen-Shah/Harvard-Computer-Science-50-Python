import sys
import requests

def number_of_bitcoins():
    try:
        bitcoin = sys.argv[1]
        bitcoin = float(bitcoin)
        return bitcoin
    except IndexError:
        sys.exit("Missing command-line argument")
    except ValueError:
        sys.exit("Command-line argument is not a number")

def exchange():
    while True:
        try:
            request = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=09872f34aa722e8114994430774834d01e0cae41c3aa42594e0b521a84d2b901")
            request = request.json()
            exchange_rate = request["data"]["priceUsd"]
            exchange_rate = float(exchange_rate)
            return exchange_rate
        except requests.RequestException:
            pass

def bitcoin_value(bitcoin, exchange_rate):
    price_USD = bitcoin * exchange_rate
    print(f"${price_USD:,.4f}")

bitcoin = number_of_bitcoins()
exchange_rate = exchange()
price_USD = bitcoin_value(bitcoin, exchange_rate)

