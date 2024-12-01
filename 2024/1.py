import aocd
from collections import Counter

data = aocd.get_data(day=1, year=2024)
l1, l2 = map(sorted,zip(*(list(map(int,line.split())) for line in data.splitlines())))
c = Counter(l2)

print('part1:', sum(abs(a-b) for a,b in zip(l1,l2)),
      'part2:', sum(k*c[k] for k in l1))