from itertools import combinations
import aocd

input = aocd.get_data(day=9, year=2025)
data = [tuple(map(int,line.split(","))) for line in input.splitlines()]
n = len(data)

part1 = max( (abs(a[0]-b[0])+1)*(abs(a[1]-b[1])+1) for a,b in combinations(data,2))
part2 = 0

segments = sorted([ (data[i][1],min(data[i][0],data[(i+1)%n][0]),max(data[i][0],data[(i+1)%n][0])) for i in range(n) if data[i][1] == data[(i+1)%n][1]])
#segments = sorted([ (data[i][0],min(data[i][1],data[(i+1)%n][1]),max(data[i][1],data[(i+1)%n][1])) for i in range(n) if data[i][0] == data[(i+1)%n][0]])


lines_left, lines_right, points  = set(), set(), []

for x, miy, may in segments:
    for xp,yp,miyp,mayp in points:
        if miyp<=miy<=mayp: part2 = max(part2, (x-xp+1)*(abs(yp-miy)+1))
        if miyp<=may<=mayp: part2 = max(part2, (x-xp+1)*(abs(yp-may)+1))

    if miy in lines_left:
        if may in lines_right:
            lines_left.remove(miy)
            lines_right.remove(may)
            points = [ (xp,yp,miyp if yp<miy else max(may+1,miyp),mayp if yp>may else min(miy-1,mayp)) for xp,yp,miyp,mayp in points if yp<miy or yp>may ]

            continue
        else:
            lines_left.remove(miy)
            lines_left.add(may)
            npoints = [ (xp,yp,max(miyp,may),mayp) for xp,yp,miyp,mayp in points if may<=yp ]
            nmay = min(v for v in lines_right if v>may)
            npoints.append((x,may,may,nmay))
            points = npoints
            continue

    if may in lines_right:
            lines_right.remove(may)
            lines_right.add(miy)
            npoints = [ (xp,yp,miyp,min(mayp,miy)) for xp,yp,miyp,mayp in points if miy>=yp ]
            nmiy = max(v for v in lines_left if v<miy)
            npoints.append((x,miy,nmiy,miy))
            points = npoints
            continue
    
    points.append((x,miy,miy,may))
    points.append((x,may,miy,may))
    lines_left.add(miy)
    lines_right.add(may)

print("Part1:",part1,"Part2:",part2)
