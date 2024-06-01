import requests
from sys import argv, exit


argl = len(argv)

if argl != 2:
    exit("Missing command-line argument")
try:
    num = float(argv[1])
except NameError:
    exit("Command-line argument is not a number")

request = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
price = round((float(request.json()["bpi"]["USD"]["rate_float"]) * num), 4)

print(f"${price:,}")
