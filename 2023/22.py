import aocd
data = aocd.get_data(day=22, year=2023)

L = [(list(map(int,l.split(','))),list(map(int,r.split(',')))) 
     for line in data.split('\n') for l,r in [line.split('~')]]
L.sort(key=lambda x:x[0][2])
def xing(a,b): return not((a[1][0]<b[0][0] or a[0][0]>b[1][0]) 
                          or (a[1][1]<b[0][1] or a[0][1]>b[1][1]))
heights, supported = [], []

for i,b in enumerate(L):
    B = list(((b2[1][2]-b2[0][2])+heights[j]+1,j) for j,b2 in enumerate(L[:i]) if xing(b,b2))
    heights.append(max((b[0] for b in B),default=1))
    supported.append([j for h,j in B if h == heights[i]])

unremovable = {v for l in supported if len(l)==1 for v in l}

part2 = 0
for i in unremovable:
    dis = {i}
    for j in range(i+1,len(L)):
        if len(supported[j]) and all(s in dis for s in supported[j]):
            part2 += 1
            dis.add(j)
print("Part1: %d Part2: %d" % (len(L) - len(unremovable),part2))