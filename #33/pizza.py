import sys
import csv
from tabulate import tabulate


if len(sys.argv) <= 1:
    sys.exit("Too few command-line arguments") 
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif not sys.argv[1].endswith('.csv'):
    sys.exit("Not a CSV file")

path = sys.argv[1]

with open(path, "r") as file:
    reader = csv.DictReader(file)
    dict = [single_row for single_row in reader]
    print(tabulate(dict, headers="firstrow", tablefmt="grid"))
