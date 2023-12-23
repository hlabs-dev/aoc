import aocd

data = aocd.get_data(day=22, year=2023)
heights, supported = [], []
L = [[int(c) for c in line.replace('~',',').split(',')] for line in data.split('\n')]
L.sort(key=lambda x:x[2])

for i,b in enumerate(L):
    B = list(((b2[5]-b2[2])+heights[j]+1,j) 
             for j,b2 in enumerate(L[:i])
             if b2[3]>=b[0] and b2[0]<=b[3] and b2[4]>=b[1] and b2[1]<=b[4])
    heights.append(max((b[0] for b in B),default=1))
    supported.append([j for h,j in B if h == heights[i]])

unremovable = {v for l in supported if len(l)==1 for v in l}

part2 = 0
for i in unremovable:
    dis = {i}
    for j in range(i+1,len(L)):
        if len(supported[j]) and all(s in dis for s in supported[j]): dis.add(j)
    part2 += len(dis)-1
    
print("Part1: %d Part2: %d" % (len(L) - len(unremovable),part2))