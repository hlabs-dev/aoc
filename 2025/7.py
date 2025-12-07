import aocd
from collections import Counter

input = aocd.get_data(day=7, year=2025)
data = input.splitlines()
beams = {i:1 for i,v in enumerate(data[0]) if v == "S"}
part1 = 0

for line in data[2::2]:
    nbeams = Counter()
    for i,c in beams.items():
        if line[i] == "^":
            part1 += 1
            nbeams[i+1] += c
            nbeams[i-1] += c
        else: nbeams[i] += c
    beams = nbeams
part2 = sum(beams.values())

print("Part1:",part1,"Part2:",part2)