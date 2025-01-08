import aocd

dirs = [(0,-1),(-1,0),(0,1),(1,0)]
def tuple2idx(pi,pj,pd,n): return (((pj+1)+(pi+1)*(n+2)) << 2) + pd

def buildfast(data):
    m, n = len(data), len(data[0])
    fast = [0]*4*(m+2)*(n+2)
    for i in range(m):
        lObs, lObs2 = -2, n+1
        for j in range(n):
            if data[i][j] == "#": lObs = j
            else: fast[tuple2idx(i,j,0,n)] = (i,lObs+1,1)
            if data[i][n-j-1] == "#": lObs2 = n-j-1
            else: fast[tuple2idx(i,n-j-1,2,n)] = (i,lObs2-1,3)
    for j in range(n):
        lObs, lObs2 = -2, m+1
        for i in range(m):
            if data[i][j] == "#": lObs = i
            else: fast[tuple2idx(i,j,1,n)] = (lObs+1,j,2)
            if data[m-i-1][j] == "#": lObs2 = m-i-1
            else: fast[tuple2idx(m-i-1,j,3,n)] = (lObs2-1,j,0)
    return fast


def solve(input):
    data = [[c for c in line] for line in input.splitlines()]
    m, n = len(data), len(data[0])
    pi, pj = next((i,j) for i in range(m) for j in range(n) if data[i][j] == "^")
    data[pi][pj] = "X"
    pd = 1
    part1, part2 = 1, 0
    cache = {(pi,pj,pd)}

    fast = buildfast(data)

    def isloop(pi,pj,pd,oi,oj):
        cache2 = set()
        while 0<=pi<m and 0<=pj<n:
            npi,npj,nd = fast[tuple2idx(pi,pj,pd,n)]
            di,dj = dirs[pd]
            if ((oi == pi and di == 0 and (npj-oj)*(pj-oj)<=0) or
                (oj == pj and dj == 0 and (npi-oi)*(pi-oi)<=0)):
                pi,pj,pd = oi-di, oj-dj, nd
            else: pi,pj,pd = npi,npj,nd

            if (((pi,pj,pd) in cache) or
                ((pi,pj,pd) in cache2)):
                return 1
            cache2.add(((pi,pj,pd)))
        return 0

    di,dj = dirs[pd]
    ni,nj = pi+di,pj+dj

    while 0<=ni<m and 0<=nj<n:
        #print("pos",pi,pj,di,dj)
        cell = data[ni][nj]
        if cell in ".":
            part2 += isloop(pi,pj,(pd+1)%4,ni,nj)
            data[ni][nj] = "X"
            part1 += 1
            pi,pj = ni, nj
        elif cell == "#":
            di,dj,pd = dj,-di,(pd+1)%4
        else: pi,pj = ni, nj
        cache.add(((pi,pj,pd)))
        ni, nj = pi+di,pj+dj
    print("part1:",part1,"part2:", part2)

solve(aocd.get_data(day=6, year=2024))