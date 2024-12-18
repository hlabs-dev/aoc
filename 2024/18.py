from collections import deque
import aocd, heapq

data = aocd.get_data(day=18, year=2024).splitlines()
h,w = 71,71

M = [[len(data)]*h for _ in range(w)]
for t,line in enumerate(data):
    i,j = map(int,line.split(","))
    M[i][j] = t

dirs = [(1,0),(0,1),(-1,0),(0,-1)]

def inrange(i,j): return 0<=i<w and 0<=j<h

def part1(M,h,w):
    queue = deque([(0,0,0)])
    visited = [[False]*h for _ in range(w)]
    while queue:
        steps, pw, ph=queue.popleft()
        for dw,dh in dirs:
            nw,nh = pw+dw, ph+dh
            if (nw,nh) == (h-1,w-1): return steps+1
            if inrange(nw,nh) and not(visited[nw][nh]) and M[nw][nh] >= 1024:
                visited[nw][nh] = True
                queue.append((steps+1,nw,nh))

def part2(M,h,w):
    heap = [(-M[0][0],0,0)]
    visited = [[False]*h for _ in range(w)]
    while heap:
        maxt, pw, ph = heapq.heappop(heap)
        for dw,dh in dirs:
            nw,nh = pw+dw, ph+dh
            if inrange(nw,nh) and not(visited[nw][nh]) and M[nw][nh]>=1024:
                nmaxt = min(M[nw][nh], -maxt)
                if (nw,nh) == (h-1,w-1): return nmaxt
                visited[nw][nh] = True
                heapq.heappush(heap,(-nmaxt,nw,nh))

print("part1:", part1(M,h,w), "part2:", data[part2(M,h,w)])