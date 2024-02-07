import sys
import csv
from tabulate import tabulate

if (len(sys.argv) < 2):
    sys.exit("Too few command-line arguments")
if (len(sys.argv) > 2):
    sys.exit("Too many command-line arguments")
l = len(sys.argv[1])
if sys.argv[1][l-4:] != ".csv":
    sys.exit("Not a CSV file")

items=[]
with open(sys.argv[1]) as file:
    reader = csv.DictReader(file)
    for row in reader:
        items.append(row)

print(tabulate(items, headers="keys", tablefmt="grid"))