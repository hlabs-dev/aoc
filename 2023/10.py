import aocd
from itertools import count

data = aocd.get_data(day=10, year=2023).split('\n')
m,n = len(data), len(data[0])

dirs = [(1,0),(-1,0),(0,1),(0,-1)]
maps = {'-':{(1,0):(1,0), (-1,0):(-1,0)},
        '|':{(0,1):(0,1), (0,-1):(0,-1)},
        'L':{(0,1):(1,0), (-1,0):(0,-1)},
        'J':{(0,1):(-1,0), (1,0):(0,-1)},
        '7':{(1,0):(0,1), (0,-1):(-1,0)},
        'F':{(0,-1):(1,0), (-1,0):(0,1)},
        '.':{}}

data = {(i,j):c for j,line in enumerate(data) for i,c in enumerate(line)}
S = next(pos for pos in data if data[pos] == 'S')

def tadd(a,b): return (a[0]+b[0],a[1]+b[1])

for di in dirs:
    path, di0, pos = {S}, di, S
    for l in count():
        pos = tadd(pos,di)
        if pos in data and data[pos] in '-|LJ7F' and di in maps[data[pos]]:
            di = maps[data[pos]][di]
            path.add(pos)
        else: break
    if pos == S:
        data[S] = next(l for l in maps if di in maps[l] and maps[l][di] == di0)
        break

part2 = 0
for i in range(m):
    isin = False
    for j in range(n):
        if (i,j) not in path and isin:
            part2+= 1
        elif (i,j) in path and data[(i,j)] in '-LJ7F':
            if data[(i,j)] == '-':
                isin = not(isin)
            elif data[(i,j)] == 'F':
                isin = [2,1][isin]
            elif data[(i,j)] == '7':
                isin = [1,2][isin]
            elif data[(i,j)] == 'L':
                isin = (isin == 1)
            elif data[(i,j)] == 'J':
                isin = (isin == 2)

print("Part1:", len(path)//2, "Part2:", part2)