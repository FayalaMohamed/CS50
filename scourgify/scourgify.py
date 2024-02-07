import sys
import csv

if (len(sys.argv) < 3):
    sys.exit("Too few command-line arguments")
if (len(sys.argv) > 3):
    sys.exit("Too many command-line arguments")
l = len(sys.argv[1])
if sys.argv[1][l-4:] != ".csv":
    sys.exit("Not a CSV file")
l = len(sys.argv[2])
if sys.argv[2][l-4:] != ".csv":
    sys.exit("Not a CSV file")

items = []
with open(sys.argv[1], 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        items.append(row)

res = []
for item in items:
    last,first = item["name"].strip().split(',')
    res.append({"first": first.strip(),
               "last": last.strip(), "house": item["house"]})

with open(sys.argv[2], 'w') as file:
    writer = csv.DictWriter(file, fieldnames=['first', 'last', 'house'])
    writer.writeheader()
    for row in res:
        writer.writerow(row)
