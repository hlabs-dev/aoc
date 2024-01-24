import aocd
data = aocd.get_data(day=17, year=2023).split('\n')
h,w = len(data), len(data[0])
data1d = [int(c) for line in data for c in line]
d2i = {-1:0, 1:1, w:2, -w:3}

def solve(mi,ma):
    ha = [[] for _ in range((w+h)*9)]
    visited = [False for _ in range(w*h*4)]
    ha[0] = [(0,1),(0,w)]
    ret = 1000
    for cost, bucket in enumerate(ha):
        for pos, di in bucket:
            dcost = 0
            if visited[pos+d2i[di]*w*h] : continue
            visited[pos+d2i[di]*w*h] = True
            if cost+mi>ret: break
            dir1 = w//di
            dir2 = -w//di
            for step in range(ma):
                pos += di
                if pos<0 or pos>=w*h or (di==1 and pos%w == 0) or (di==-1 and pos%w == w-1): break
                dcost += data1d[pos]
                if step+1 >= mi:
                    if pos == (w*h-1):
                        ret = min(ret, cost+dcost)
                    if visited[pos+d2i[dir1]*w*h] == False:
                        ha[cost+dcost].append((pos,dir1))
                        ha[cost+dcost].append((pos,dir2))
    return ret
print("Part1: %d Part2: %d" % (solve(1,3),solve(4,10)))