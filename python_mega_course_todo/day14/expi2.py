import csv

with open("day.csv",'r') as file:
    data = list(csv.reader(file))
for row in data:
    print(row[1])
print(data)