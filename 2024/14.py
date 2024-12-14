import re
import aocd
from collections import Counter

data = [tuple(map(int,re.findall(r'[-]*\d+', machine))) for machine in aocd.get_data(day=14, year=2024).splitlines()]
m, n = 101, 103

def post(px,py,vx,vy,t,m=m,n=n):
    return ((px+t*vx)%m,(py+t*vy)%n)

def prtree(s):
    print("\n".join("".join("■" if (i,j) in s else "." for i in range(m)) for j in range(n)))

def part1():
    quads = [0,0,0,0]
    for px,py,vx,vy in data:
        nx, ny = post(px,py,vx,vy,100,m,n)
        if nx!=(m-1)//2 and ny!=(n-1)//2:
            quads[(2*nx)//m + 2*((2*ny)//n)] += 1
    return (quads[0]*quads[1]*quads[2]*quads[3])

def getdim():
    mx,ix,my,iy = 0, 0, 0, 0
    for t in range(max(m,n)):
        lx, ly = [0]*m, [0]*n
        for px,py,vx,vy in data:
            nx, ny = post(px,py,vx,vy,t,m,n)
            lx[nx], ly[ny] = lx[nx]+1, ly[ny]+1
        mxt, myt = max(lx), max(ly)
        if mxt > mx: mx, ix = mxt, t
        if myt > my: my, iy = myt, t
    return ix, iy

def solve_congruences( r1, r2, k1=m, k2=n):
    n = k1 * k2
    m1 = n // k1
    m2 = n // k2
    inv1 = pow(m1, -1, k1)  # m1^-1 mod k1
    inv2 = pow(m2, -1, k2)  # m2^-1 mod k2
    t = (r1 * m1 * inv1 + r2 * m2 * inv2) % n
    return t

part2 = solve_congruences(*getdim())

print("part1:",part1(),"part2:",part2)

#prtree(Counter(post(px,py,vx,vy,part2,m,n) for px,py,vx,vy in data))

