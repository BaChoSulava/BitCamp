import requests
import sys


try:
    user_bitcoin = float(input("How many to buy? "))
except requests.RequestException:
    ...
except ValueError:
    sys.exit("Error: Invalid number of bitcoins")

url = "https://api.coindesk.com/v1/bpi/currentprice.json"

print(f"${user_bitcoin:,.4f}")