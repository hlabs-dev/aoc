import numpy as np
import aocd

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.size = [1] * n
        self.count = n

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a, b):
        ra = self.find(a)
        rb = self.find(b)
        if ra == rb: return False
        if self.rank[ra] < self.rank[rb]: ra, rb = rb, ra
        self.parent[rb] = ra
        self.size[ra] += self.size[rb]
        if self.rank[ra] == self.rank[rb]: self.rank[ra] += 1
        self.count -= 1
        return True

    def component_sizes(self):
        return [self.size[i] for i in range(len(self.parent)) if self.parent[i] == i]

    def largest_k(self, k=3):
        return sorted(self.component_sizes(), reverse=True)[:k]

input = aocd.get_data(day=8, year=2025)
data = [tuple(map(int,line.split(","))) for line in input.splitlines()]

X = np.asarray(data, dtype=np.int64)

G = X @ X.T
sq = np.sum(X**2, axis=1)
dist2 = sq[:, None] + sq[None, :] - 2*G
i, j = np.triu_indices(len(X), k=1)
order = np.argsort(dist2[i, j], kind="quicksort")

uf = UnionFind(1000)
for k, (ii, jj) in enumerate(np.column_stack((i[order], j[order]))):
    if uf.union(ii, jj):
        if uf.count == 1:
            part2 = (data[ii][0]*data[jj][0])
            break
    if k == 999:
        a,b,c = uf.largest_k()
        part1 = a*b*c
        
print("Part1:",part1,"Part2:",part2)