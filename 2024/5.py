import aocd
from functools import cmp_to_key

data = aocd.get_data(day=5, year=2024)

prio, pages = data.split("\n\n")
prio = { tuple(line.split("|")) for line in prio.splitlines() }
pages = list(list(line.split(",")) for line in pages.splitlines())

def cmp(a,b): return ((b,a) in prio) - ((a,b) in prio)

part1, part2 = 0, 0

for page in pages:
    sorted_page = sorted(page,key=cmp_to_key(cmp))
    mid = int(sorted_page[len(page)//2])
    if page == sorted_page: part1 += mid
    else: part2 += mid
                                
print("part1:", part1, "part2:", part2)