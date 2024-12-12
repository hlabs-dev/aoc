import aocd
from collections import defaultdict

data = aocd.get_data(day=12, year=2024).splitlines()
m, n = len(data), len(data[0])

def inrange(i,j): return 0<=i<m and 0<=j<n
def isout(i,j,di,dj): return not(inrange(i+di,j+dj)) or data[i+di][j+dj] != data[i][j]

dirs = [(1,0),(0,1),(-1,0),(0,-1)]

fenced = set()
part1, part2 = 0, 0

def fence(i,j):
    visited = set()
    fences = 0
    corners = defaultdict(int)
    stack = [(i,j)]
    out = defaultdict(set)
    while len(stack):
        pi,pj = stack.pop()
        if (pi,pj) not in visited:
            visited.add((pi,pj))
            ldi, ldj = dirs[-1]
            lastout = isout(pi,pj,ldi,ldj)
            for di, dj in dirs:
                ni,nj = pi+di, pj+dj
                if isout(pi,pj,di,dj):
                    if lastout:
                        corners[(pi*2+di+ldi,pj*2+dj+ldj)] += 1
                    for odi, odj in out[(ni,nj)]:
                        if odi+di != 0 and odj+dj != 0:
                            corners[(ni*2-di-odi,nj*2-dj-odj)] += 1
                    out[(ni,nj)].add((di, dj))
                    fences += 1
                    lastout = True
                else:
                    if (ni,nj) not in visited: stack.append((ni,nj))
                    lastout = False
                ldi, ldj = di, dj
    return (fences,sum( 2 if corners[k]>1 else 1 for k in corners),visited)    

for i in range(m):
    for j in range(n):
        if (i,j) not in fenced:
            fij, cij, sij = fence(i,j)
            fenced.update(sij)
            part1 += fij * len(sij)
            part2 += cij * len(sij)

print("part1:",part1,"part2:",part2)
