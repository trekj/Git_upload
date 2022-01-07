import csv
from pathlib import Path

csvpath = Path("quarterly_data.csv")

print(csvpath)

with open(csvpath) as csvfile:
    data = csv.reader(csvfile)
    for row in data:
        print(row)