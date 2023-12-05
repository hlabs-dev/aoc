import aocd
from collections import defaultdict
data = aocd.get_data(day=2, year=2023)

part1 = part2 = 0

for i, g in enumerate(data.split("\n")):
    _,l = g.split(": ")
    p1 = i+1
    maxes = defaultdict(int)
    for u in l.split("; "):
        for t in u.split(", "):
            n, c = t.split(" ")
            n = int(n)
            if not((c == "red" and n <= 12) 
                or (c == "green" and n <= 13) 
                or (c == "blue" and n <= 14)): p1 = 0
            maxes[c] = max(maxes[c], n)
    part1 += p1
    p2 = 1
    for k in maxes: p2 *= maxes[k]
    part2 += p2
print(part1,part2)