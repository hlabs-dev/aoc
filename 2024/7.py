import aocd
from collections import deque

data = aocd.get_data(day=7, year=2024)
data = [(int(a), list(map(int,b.split()))) 
        for line in data.splitlines() 
        for a,b in [line.split(":")] ]

def len10(x):
    t = 10
    while True:
        if x < t: return t
        t *= 10

def dfs(target,li,part2=False):
    bt = deque([(target,len(li)-1)])
    while len(bt):
        tgt, idx = bt.pop()
        v = li[idx]
        if idx == 0: 
            if v == tgt: return 1
        else:
            if v<tgt: bt.append((tgt-v,idx-1))
            if tgt%v == 0: bt.append((tgt//v,idx-1))
            if part2:
                lg = len10(v)
                if v<tgt and tgt%lg == v: bt.append((tgt//lg,idx-1))
    return 0

print("part1:",sum((dfs(v,li))*v for v,li in data),
    "part2",sum((dfs(v,li,2))*v for v,li in data))