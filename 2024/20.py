import aocd
from collections import deque,defaultdict
import bisect

data = aocd.get_data(day=20, year=2024).splitlines()
h,w = len(data), len(data[0])
dirs = [(1,0),(0,1),(-1,0),(0,-1)]
def getpos(data,c): return next((i,j) for i in range(h) for j in range(w) if data[i][j] == c)
def mand(a,b,c,d): return abs(a-c)+abs(b-d)

def diagidx(pathl):
    idxp,idxm = defaultdict(list), defaultdict(list)
    for i,pos in enumerate(pathl):
        idxp[sum(pos)].append((*pos,i))
        idxm[pos[0]-pos[1]].append((*pos,i))
    for i in idxp: 
        idxp[i].sort()
    for i in idxm: idxm[i].sort()
    return idxp,idxm

def getneb(idxp,idxm,posx,posy,d,dx,dy,mini):
    ret = set()
    #dag 1
    if dx+dy>0: mi,ma = (posx,posy+d,mini), (posx+d,posy,10000)
    else: mi,ma = (posx-d,posy,0), (posx,posy-d,10000)
    arr = idxp[posx+posy+d*(dx+dy)]
    idx = bisect.bisect_left(arr, mi)
    while idx<len(arr) and arr[idx]<=ma:
        if arr[idx][2]>=mini: ret.add(arr[idx][:2])
        idx += 1

    #dag 2
    if dx-dy>0: mi,ma = (posx,posy-d,mini), (posx+d,posy,10000)
    else: mi,ma = (posx-d,posy,0), (posx,posy+d,10000)
    arr = idxm[posx-posy+d*(dx-dy)]
    idx = bisect.bisect_left(arr, mi)
    while idx<len(arr) and arr[idx]<=ma:
        if arr[idx][2]>=mini: ret.add(arr[idx][:2])
        idx += 1
    return ret
        

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

def getshortcuts(pl,i,di,sh):
    ret = set()
    j = i+sh+2
    while(j<len(pl)):
        dist = mand(*pl[i],*pl[j])
        gain = j - i - dist
        if (dist<=di) and (gain>=sh):
            steps = di-dist+1
            for k in range(min(len(pl)-j, steps)): ret.add(pl[j+k])
            j += steps
        elif(dist<=di): j += (sh+1-gain)//2
        else: j += dist-di
    return ret

def solve(pl,di,sh,idxp,idxm):
    s = getshortcuts(pl,0,di,sh)
    ret = len(s)
    for i in range(1,len(pl)-sh-2):
        px,py,nx,ny = *pl[i-1], *pl[i]
        dx, dy = nx-px,ny-py
        for dex, dey in getneb(idxp,idxm,px,py,di,-dx,-dy,i+119): s.discard((dex, dey))
        for dex, dey in getneb(idxp,idxm,nx,ny,di,dx,dy,i+120): s.add((dex,dey))
        j, jmax = i+sh+1, min(len(pl), i+sh+di)
        while j<jmax:
            gain = j - i - mand(*pl[i], *pl[j])
            if gain < sh-2: j += (sh-gain-3)//2
            elif gain < sh: s.discard(pl[j])
            else: j += (gain-sh)//2 + 1
            j += 1
        ret += len(s)
    return ret
pd,pl = getpath(data)
idxp,idxm = diagidx(pl)
print ("part1:", part1(pd), "part2:", solve(pl,20,100,idxp,idxm))