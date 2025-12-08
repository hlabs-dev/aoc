import aocd
from collections import Counter

input = aocd.get_data(day=7, year=2025)
data = input.splitlines()
beams = Counter({i:1 for i,v in enumerate(data[0]) if v == "S"})
part1 = 0

for line in data[2::2]:
    keys = [k for k in beams.keys()]
    for i in keys:
        if line[i] == "^":
            part1 += 1
            p = beams.pop(i)
            beams[i+1] += p
            beams[i-1] += p
part2 = sum(beams.values())

print("Part1:",part1,"Part2:",part2)