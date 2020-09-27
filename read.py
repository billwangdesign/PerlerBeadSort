import csv
from math import sqrt

cr = 100
cg = 50
cb = 20
cdistance = 1000
colorCompareList = []

with open('bead.csv') as csvfile:
    beadreader = csv.reader(csvfile, delimiter = ',')
    for row in beadreader:
        beadcolor = row[0]
        r = int(row[1])
        g = int(row[2])
        b = int(row[3])
        color_diff = sqrt(abs(r - cr)**2 + abs(g - cg)**2 + abs(b - cb)**2)
        color_calc = [row[0], color_diff]
        colorCompareList.append(color_calc)
        #print(color_diff, row[0])
x = min(color_diff)[1]
print(x)