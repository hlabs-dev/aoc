import aocd

data = aocd.get_data(day=22, year=2023)
heights,tops = [], []

L = [[int(c) for c in line.replace('~',',').split(',')] for line in data.split('\n')]
L.sort(key=lambda x:x[2])
supporting = [[] for _ in range(len(L))]
supported = [[] for _ in range(len(L))]

for i,b in enumerate(L):
    ma = 1
    B = []
    for j in range(i-1,-1,-1):
        b2 = L[j]
        if tops[j]<ma: break
        if b2[3]>=b[0] and b2[0]<=b[3] and b2[4]>=b[1] and b2[1]<=b[4]:
            if (b2[5]-b2[2])+heights[j]+1 >= ma:
                ma = (b2[5]-b2[2])+heights[j]+1
                B.append((ma,j))
    heights.append(ma)
    for h,j in B:
        if h == ma:
            supported[i].append(j)
            supporting[j].append(i)
    if len(tops)==0 or tops[-1]<(b[5]-b[2])+ma+1:
        tops.append((b[5]-b[2])+ma+1)
    else: tops.append(tops[-1])

unremovable = {v for l in supported if len(l)==1 for v in l}
print((len(L) - len(unremovable)))
part2 = 0
for i in unremovable:
    dis = {i}
    fifo = [i]
    while len(fifo):
        cur = fifo.pop(0)
        for j in supporting[cur]:
            if all(s in dis for s in supported[j]):
                fifo.append(j)
                dis.add(j)
    part2 += len(dis)-1
    
print("Part1: %d Part2: %d" % (len(L) - len(unremovable),part2))