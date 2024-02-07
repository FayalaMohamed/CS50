import sys
import requests

if len(sys.argv) == 1:
    sys.exit("Missing command-line argument ")
try:
    x = float(sys.argv[1])
except:
    sys.exit("Command-line argument is not a number")

if len(sys.argv) > 2:
    sys.exit("Command-line argument is not a number")

try:
    rep = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
except requests.RequestException:
    sys.exit("Could not connect to Coindesk API")

rep = rep.json()
amount = x * rep["bpi"]["USD"]["rate_float"]
print(f"${amount:,.4f}")
