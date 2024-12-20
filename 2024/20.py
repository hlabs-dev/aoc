import aocd, heapq
from collections import Counter, deque
from functools import cache

data = aocd.get_data(day=20, year=2024).splitlines()
h,w = len(data), len(data[0])
dirs = [(1,0),(0,1),(-1,0),(0,-1)]
def getpos(data,c): return next((i,j) for i in range(h) for j in range(w) if data[i][j] == c)
def mand(a,b,c,d): return abs(a-c)+abs(b-d)

def getpath(data):
    start, end = getpos(data,"S"), getpos(data,"E")
    queue = deque([(0,*start)])
    pathd,pathl = {start:0}, [start]
    while queue:
        steps, pw, ph=queue.popleft()
        for dw,dh in dirs:
            nw,nh = pw+dw, ph+dh
            if (nw,nh) == end:
                pathd[(nw,nh)] = steps+1
                pathl.append((nw,nh))
                return pathd, pathl
            if (nw,nh) not in pathd and data[nw][nh] != "#":
                pathd[(nw,nh)] = len(pathl)
                pathl.append((nw,nh))
                queue.append((steps+1,nw,nh))

def part1(pd):
    return sum((px+2*dix,py+2*diy) in pd and pd[(px,py)]+102<=pd[(px+2*dix,py+2*diy)]
               for px,py in pd for dix,diy in dirs)

def getshortcuts(pl,i,di=20,sh=100):
    ret = set()
    j = i+sh+2
    while(j<len(pl)):
        dist = mand(*pl[i],*pl[j])
        gain = j - i - mand(*pl[i],*pl[j])
        if (dist<=di) and (gain>=sh):
            steps = di-dist+1
            for k in range(min(len(pl)-j, steps)): ret.add(pl[j+k])
            j += steps
        elif(dist<=di): j += (sh+1-gain)//2
        else: j += dist-di
    return ret

def getshortcutcount(pl,i,di=20,sh=100):
    ret = 0
    j = i+sh+2
    while(j<len(pl)):
        dist = mand(*pl[i],*pl[j])
        gain = j - i - mand(*pl[i],*pl[j])
        if (dist<=di) and (gain>=sh):
            steps = di-dist+1
            for k in range(min(len(pl)-j, steps)): ret+=1
            j += steps
        elif(dist<=di): j += (sh+1-gain)//2
        else: j += dist-di
    return ret

def solve(pl,pd,di=20,sh=100):
    s = getshortcuts(pl,0,di,sh)
    ret = len(s)
    for i in range(1,len(pl)-sh-2):
        px,py,nx,ny = *pl[i-1], *pl[i]
        dx, dy = nx-px,ny-py
        s.discard(pl[i+sh+1])
        for j in range(-di,di+1):
            dex, dey = dx*(di-abs(j))+dy*j, dy*(di-abs(j))+dx*j
            s.discard((px-dex, py-dey))
            nex,ney = (nx+dex, ny+dey)
            if (nex,ney) in pd:
                k = pd[(nex,ney)]
                if k - i - mand(*pl[i], nex,ney) >= sh: s.add((nex,ney))
        for j in range(i+sh+1, min(len(pl), i+sh+di)):
            if j - i - mand(*pl[i], *pl[j]) < sh: s.discard(pl[j])
        ret += len(s)
    return ret

pd,pl = getpath(data)

print("part1:", part1(pd), "part2:", solve(pl,pd,di=20,sh=100))



