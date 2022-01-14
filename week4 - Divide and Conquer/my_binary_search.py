import math as m

minmax = input().split()
low = int(minmax[0])
high = int(minmax[1])

while True:
    point = m.floor((low+high)/2)
    print(point)
    cool = input()
    if cool == "min":
        low = point + 1
    else:
        high = point - 1




