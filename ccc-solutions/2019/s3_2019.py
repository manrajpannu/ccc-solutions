# CCC '19 S3 - Arithmetic Square
# Manraj Pannu
# 593368
# ICS4U0
# 6 sep 2018
from statistics import mean
grid = []

def list_into_int(list_of_strings):
    new = []
    for i in list_of_strings:
        if i != 'X':
            new.append(int(i))
        else: new.append(i)
    return new

def sequence(sublist):
    if not 'X' in sublist:
        return sublist

    if sublist.count('X') == 1:
        if sublist.index('X') == 0:
            sublist[0] = sublist[1] - (sublist[2] - sublist[1])

        elif sublist.index('X') == 1:
            sublist[1] = mean([sublist[0],sublist[2]])
        else: sublist[2] = (sublist[1] - sublist[0]) + sublist[1]
    return sublist

for i in range(3):
    grid.append(list_into_int(input().split()))

for sublist in grid:
    sublist = sequence(sublist)

for i in range(3):
    new = sequence([grid[0][i], grid[1][i], grid[2][i]])
    grid[0][i] = new[0]
    grid[1][i] = new[1]
    grid[2][i] = new[2]

for i in grid:
    print(*i, sep=" ")
