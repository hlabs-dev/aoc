import aocd
from itertools import combinations

data = aocd.get_data(day=11, year=2023).split('\n')
n,m = len(data), len(data[0])

lines = [ (i,c) for i in range(n) for c in [data[i].count('#')] if c>0 ]
rows = [ (j,c) for j in range(m) 
        for c in [sum(data[i][j]=="#" for i in range(n))] if c>0 ]

def rawgap(a,b):
     raw, gap, cnt = b[0]-a[0], b[1][0]-a[1][0], b[1][1]*a[1][1]
     return (raw*cnt, (gap-raw)*cnt)

raw,gap = map(sum,zip(*(rawgap(a,b) for a,b in combinations(enumerate(lines),2)),
              *(rawgap(a,b) for a,b in combinations(enumerate(rows),2))))

print("Part1: %d Part2: %d" % (raw+gap*2, raw+gap*10**6))
