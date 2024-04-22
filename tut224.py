# Work with CSV files using python
#read csv files
from csv import DictReader
with open('zalina.csv','r') as f:
    next
    csv_reader=DictReader(f)
    for row in csv_reader:
        print(row)

