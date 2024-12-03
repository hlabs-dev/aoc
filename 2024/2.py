import aocd
from collections import Counter

data = aocd.get_data(day=2, year=2024)
T = list(list(map(int,line.split())) for line in data.splitlines())

def isgood(line):
    cnt = Counter(a-b for a,b in zip(line[:-1],line[1:]))
    return all(0<k<4 for k in cnt) or all(0<-k<4 for k in cnt)

def ispart(line):
    if isgood(line): return 1
    elif any(isgood(line[:i]+line[i+1:]) for i in range(len(line))): return 2
    return 0

res = Counter(map(ispart,T))

print('part1:', res[1], 'part2:', res[1]+res[2])