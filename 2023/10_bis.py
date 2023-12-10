import aocd
from itertools import product

def offset(pos,di): return (pos[0]+dirs[di][0],pos[1]+dirs[di][1])

dirs = [(1,0),(0,1),(-1,0),(0,-1)]
letters = "-F7LJ|S."
maps = [{0,2},{0,1},{1,2},{0,3},{2,3},{1,3},{0,1,2,3},{}]
parity = [1,0.5,-0.5,-0.5,0.5,0]

data = aocd.get_data(day=10, year=2023).split('\n')
m,n = len(data), len(data[0])
s = letters.index('S')

sparse = {(i,j):letters.index(data[j][i]) for i,j in product(range(n),range(m))}
neighbours = {pos:{offset(pos, di) for di in maps[idx]} for pos, idx in sparse.items()}
S = next(pos for pos in sparse if sparse[pos] == s)

for next_s in neighbours[S]:
    pos, path, next_pos = S, {S}, next_s
    while next_pos in sparse and pos in neighbours[next_pos] and sparse[next_pos] < 6:
        path.add(next_pos)
        pos, next_pos = next_pos, next(p for p in neighbours[next_pos] if p!=pos)
    if next_pos == S:
        sparse[S] = next( k for k in range(1,len(maps))
                       if {next_s, pos} == {offset(S,di) for di in maps[k]})
        break

part2 = 0
for i,j in product(range(m),range(n)):
    if (i,j) in path: s += parity[sparse[(i,j)]]
    else: part2+= int(s)%2

print("Part1:", len(path)//2, "Part2:", part2)