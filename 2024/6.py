import aocd

data = aocd.get_data(day=6, year=2024)

data = [[c for j,c in enumerate(line)] for i,line in enumerate(data.splitlines())]
m, n = len(data), len(data[0])

def inrange(i,j): return 0<=i<m and 0<=j<n
def pmap(): print("\n".join("".join(c for c in line) for line in data))

di, dj= -1, 0
pi, pj = next((i,j) for i in range(m) for j in range(n) if data[i][j] == "^")
data[pi][pj] = "X"

fast = {}

for i in range(m):
    lObs, lObs2 = -2, 0
    for j in range(n):
        if data[i][j] == "#": lObs = j
        else: fast[(i,j,0,-1)] = (i,lObs+1,-1,0)
        if data[i][n-j-1] == "#": lObs2 = n-j-1
        else: fast[(i,n-j-1,0,1)] = (i,lObs2-1,1,0)

for j in range(n):
    lObs, lObs2 = -2, n+1
    for i in range(m):
        if data[i][j] == "#": lObs = i
        else: fast[(i,j,-1,0)] = (lObs+1,j,0,1)
        if data[m-i-1][j] == "#": lObs2 = m-i-1
        else: fast[(m-i-1,j,1,0)] = (lObs2-1,j,0,-1)

def solve(pi,pj,di,dj):
    part1, part2 = 1, 0
    cache = {(pi,pj,di,dj)}
    while(inrange(pi+di,pj+dj)):
        cell = data[pi+di][pj+dj]
        if cell == ".":
            part2 += isloop(pi,pj,dj,-di,pi+di,pj+dj,cache)
            pi, pj, part1 = pi+di, pj+dj, part1+1
            data[pi][pj] = "X"
        elif cell in {"#","0"}: di,dj = dj,-di
        else: pi, pj = pi+di, pj+dj
        cache.add((pi,pj,di,dj))
    print("part1:",part1,"part2:", part2)

def isloop(pi,pj,di,dj,oi,oj,cache):
    cache2 = set()
    while inrange(pi,pj):
        npi,npj,ndi,ndj = fast[pi,pj,di,dj]
        if ((oi == pi and di == 0 and (npj-oj)*(pj-oj)<0) or
            (oj == pj and dj == 0 and (npi-oi)*(pi-oi)<0)):
            pi,pj,di,dj = oi-di, oj-dj, ndi,ndj
        else: pi,pj,di,dj = npi,npj,ndi,ndj

        if (((pi,pj,di,dj) in cache2) or
            ((pi,pj,di,dj) in cache)): return 1
        cache2.add((pi,pj,di,dj))
    return 0

solve(pi,pj,di,dj)
