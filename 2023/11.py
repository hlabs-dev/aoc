import aocd
from itertools import combinations
from bisect import bisect

data = aocd.get_data(day=11, year=2023).split('\n')
n,m = len(data), len(data[0])
hgaps = [ i for i in range(n) if all(data[i][j] == "." for j in range(m))]
vgaps = [ j for j in range(m) if all(data[i][j] == "." for i in range(n))]

sparse = [(i,j) for i in range(n) for j in range(m) if data[i][j] == '#']

raw  = sum(abs(x1-x2)+abs(y1-y2) for (x1,y1),(x2,y2)  in combinations(sparse,2))
gaps = sum(abs(bisect(hgaps,x1) - bisect(hgaps, x2)) +
           abs(bisect(vgaps,y1) - bisect(vgaps, y2))
           for (x1,y1),(x2,y2)  in combinations(sparse,2))

print("Part1: %d Part2: %d" % (raw+gaps, raw+gaps*999999))