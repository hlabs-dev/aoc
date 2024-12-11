import aocd
from collections import defaultdict

def solve():
    data = [list(map(int,line)) for line in aocd.get_data(day=10, year=2024).splitlines()]
    m, n = len(data), len(data[0])
    dirs = [(-1,0),(1,0),(0,1),(0,-1)]
    def inrange(i,j): return 0<=i<m and 0<=j<n

    it_list = [(i,j) for i in range(m) for j in range(n) if data[i][j] == 9]
    it_part1 = defaultdict(set) | {pos:{pos} for pos in it_list}
    it_part2 = defaultdict(int) | {pos:1 for pos in it_list}

    for i in range(9):
        next_it_list = set()
        for i,j in it_list:
            for di, dj in dirs:
                ti,tj = i+di, j+dj
                if  0<=ti<m and 0<=tj<n and (data[i][j])-1 == (data[ti][tj]):
                    it_part1[(ti,tj)].update(it_part1[(i,j)])
                    it_part2[(ti,tj)] += it_part2[(i,j)]
                    next_it_list.add((ti,tj))
        it_list = next_it_list

    part1, part2 = 0, 0
    for pos in it_list:
        part1 += len(it_part1[pos])
        part2 += it_part2[pos]

    print("part1:",part1,"part2:",part2)

solve()