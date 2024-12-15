import aocd

data = aocd.get_data(day=15, year=2024)
M,D = data.split('\n\n')
M = M.splitlines()
h,w = len(M), len(M[0])

dirs = [(1,0),(0,1),(-1,0),(0,-1)]
c2d = "v>^<"
remap = {"#":"##","@":"@.",".":"..","O":"[]"}

MP = {(i,j):c for i,line in enumerate(M) for j,c in enumerate(line)}
MP2 = {(i,j*2+d):c for i,line in enumerate(M) for j,c in enumerate(line) for d,c in enumerate(remap[c])}
DL = [c2d.index(c) for c in D.replace("\n","")]

def getrobot(MP): return next(pos for pos in MP if MP[pos] == "@")
def getGPS(MP): return sum(100*posx + posy for posx, posy in MP if MP[(posx,posy)] in 'O[')
def printMap(M,h,w): print("\n".join("".join( MP[(i,j)] for j in range(w))  for i in range(h)))

def move(px, py, d, MP):
    dx, dy = dirs[d]
    cx, cys = px+dx, set([py+dy])
    tomove = [(px,py)]

    while len(cys) and not(any(MP[(cx,cy)] == "#" for cy in cys)):
        ncys = set()
        if dx!=0:
            for cy in cys:
                if MP[(cx,cy)] == "[": ncys.update({cy, cy+1})
                if MP[(cx,cy)] == "]": ncys.update({cy, cy-1})
                if MP[(cx,cy)] == "O": ncys.add(cy)
            cys = ncys
        if len(cys) == 0 or all(MP[(cx,cy)] == "." for cy in cys): break
        tomove.extend((cx,cy) for cy in cys)
        cx, cys = cx+dx, set( cy+dy for cy in cys)

    if not(any(MP[(cx,cy)] == "#" for cy in cys)):
        while len(tomove):
            cx,cy = tomove.pop()
            MP[(cx+dx,cy+dy)], MP[(cx,cy)] = MP[(cx,cy)], "."
        px,py = px+dx, py+dy
    return px, py

p1x, p1y, p2x, p2y = *getrobot(MP),*getrobot(MP2)

for d in DL:
    p1x, p1y, p2x, p2y = *move(p1x, p1y, d, MP), *move(p2x, p2y, d, MP2)

print("part1:", getGPS(MP), "part1:", getGPS(MP2))