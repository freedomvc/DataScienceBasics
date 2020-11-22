
# Importing python built-in CSV package
import csv

with open ('addressbook.csv', newline='') as sourcefile:
    sourcereader = csv.reader(sourcefile, delimiter=',')
    for row in sourcereader:
        print(row)
