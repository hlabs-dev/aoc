import aocd

def solve15():
    data = aocd.get_data(day=15, year=2024)
    M,D = data.split('\n\n')
    MP = [[c for c in line] for line in M.splitlines()]
    h,w = len(MP), len(MP[0])

    dirs = [(1,0),(0,1),(-1,0),(0,-1)]
    c2d = "v>^<"
    remap = {"#":"##","@":"@.",".":"..","O":"[]"}

    MP2 = [[ c2 for c in line for c2 in remap[c]] for line in MP]
    DL = [c2d.index(c) for c in D.replace("\n","")]

    def getrobot(MP): return next((i,j) for i in range(h) for j in range(w) if MP[i][j] == "@" )
    def getGPS(MP): return sum(100*i + j for i in range(h) for j in range(len(MP[0])) if MP[i][j] in 'O[')
    def printMap(M): print("\n".join("".join(line)  for line in M))

    def move(px, py, d, MP):
        dx, dy = dirs[d]

        if dy:
            cy = py+dy
            while MP[px][cy] in "[]O": cy += dy
            if MP[px][cy] == '.':
                while cy != py: MP[px][cy], cy = MP[px][cy-dy], cy-dy
                MP[px][cy] = '.'
            else: return px, py
        else:
            cx, cys = px+dx, set([py])
            tomove = [(px,py)]
            while len(cys):
                ncys = set()
                for cy in cys:
                    if MP[cx][cy] == "#": return px, py
                    if MP[cx][cy] == "[": ncys.update({cy, cy+1})
                    if MP[cx][cy] == "]": ncys.update({cy, cy-1})
                    if MP[cx][cy] == "O": ncys.add(cy)
                cys = ncys
                tomove.extend((cx,cy) for cy in cys)
                cx += dx
            while len(tomove):
                cx,cy = tomove.pop()
                MP[cx+dx][cy], MP[cx][cy] = MP[cx][cy], "."
        return px+dx, py+dy

    p1x, p1y, p2x, p2y = *getrobot(MP),*getrobot(MP2)

    for d in DL:
        p1x, p1y, p2x, p2y = *move(p1x, p1y, d, MP), *move(p2x, p2y, d, MP2)

    print("part1:", getGPS(MP), "part2:", getGPS(MP2))

solve15()
