from sys import argv, exit
from tabulate import tabulate
import csv

if len(argv) != 2 or not argv[1].endswith(".csv"):
    exit("Usage: python pizza.py file.csv")
try:
    with open(argv[1]) as file:
        final = []
        reader = csv.DictReader(file)
        headers = reader.fieldnames
        for line in reader:
            tmp = []
            for l in line:
                print(line[l])
                tmp.append(line[l])
            final.append(tmp)
        print(tabulate(final, headers, tablefmt="grid"))

except FileNotFoundError:
    exit("File not found")
