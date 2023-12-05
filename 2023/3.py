import aocd
from collections import defaultdict

data = aocd.get_data(day=3, year=2023)

mp = defaultdict(str)
T = data.split('\n')
n = len(T)
m = len(T[0])

for i,l in enumerate(T):
    for j,c in enumerate(l):
        if c != '.': 
            mp[(i,j)] = c

part1 = part2 = 0
gears = defaultdict(list)
tmp, ispart, cgear = 0, False, set()

for i in range(n):
    for j in range(m):
        if mp[(i,j)].isdigit():
            tmp = tmp*10+int(mp[(i,j)])
            for k in range(-1,2):
                for l in range(-1,2):
                    if mp[(i+k,j+l)] != '' and not(mp[(i+k,j+l)].isdigit()):
                        ispart = True
                    if mp[(i+k,j+l)] == '*': cgear.add((i+k,j+l))           
        else:
            if ispart:
                part1 += tmp
                for g in cgear: gears[g].append(tmp)
            tmp, ispart, cgear = 0, False, set()
    if ispart: 
        part1 += tmp
        for g in cgear: gears[g].append(tmp)
    tmp, ispart, cgear = 0, False, set()

for g in gears:
    if len(gears[g]) == 2:
        part2 += gears[g][0]*gears[g][1]
print("part1:",part1,"part2:",part2)