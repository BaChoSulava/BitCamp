import requests
import sys

#check for correct command-line inputs
if len(sys.argv) < 2:
        sys.exit("Missing command-line argument")
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")


#check for float numbering
try:
    bitcoins = float(sys.argv[1])
except ValueError:
    sys.exit("Error: Invalid number of bitcoins")


#take data from url
try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    response.raise_for_status()
    data = response.json()
    # print(data)
    price = data["bpi"]["USD"]["rate_float"]
    # print(price)
except requests.RequestException:
    sys.exit("Error: could not retrieve bitcoin price")

# Calculate
cost = bitcoins * price
print(f"${cost:,.4f}")