import aocd
from collections import defaultdict
from itertools import combinations

data = aocd.get_data(day=8, year=2024).splitlines()
m, n = len(data), len(data[0])
ants_dict = defaultdict(set)

def inrange(i,j): return 0<=i<m and 0<=j<n
def pgcd(a, b): return a if b == 0 else pgcd(b, a % b)

for i in range(m):
    for j in range(n):
        if data[i][j] != '.': ants_dict[data[i][j]].add((i,j))

part1, part2 = set(), set()

for ants in ants_dict.values():
    for a,b in combinations(ants,2):
        #part 1
        di,dj = a[0]-b[0], a[1]-b[1]
        p1,p2 = (a[0] + di, a[1] + dj), (b[0] - di, b[1] - dj)
        if inrange(*p1): part1.add(p1)
        if inrange(*p2): part1.add(p2)

        #part 2
        steps = pgcd(di,dj)
        di,dj = di//steps, dj//steps
        cur = a
        while(inrange(*cur)):
            part2.add(cur)
            cur = cur[0]+di, cur[1]+dj
        cur = a[0]-di, a[1]-dj
        while(inrange(*cur)):
            part2.add(cur)
            cur = cur[0]-di, cur[1]-dj

print("part1:", len(part1), "part2:", len(part2))