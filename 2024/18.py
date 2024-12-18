from collections import deque
import aocd

data = aocd.get_data(day=18, year=2024).splitlines()
h,w = 71,71
M = [ tuple(map(int,line.split(","))) for line in data]
dirs = [(1,0),(0,1),(-1,0),(0,-1)]

def inrange(i,j): return 0<=i<w and 0<=j<h

def bfs(M,h,w):
    pix, visited, queue = set(M), set([(0,0)]), deque([(0,0,0)])
    
    while queue:
        steps, pw, ph=queue.popleft()
        for dw,dh in dirs:
            nw,nh = pw+dw, ph+dh
            if (nw,nh) == (h-1,w-1): return steps+1
            if inrange(nw,nh) and (nw,nh) not in visited and (nw,nh) not in pix:
                visited.add((nw,nh))
                queue.append((steps+1,nw,nh))
    return -1


mi,ma = 1024,len(M)
while (mi+1<ma):
    mid = (mi+ma)//2
    if bfs(M[:mid],h,w) == -1: ma = mid
    else: mi = mid

print("part1:", bfs(M[:1024],h,w), "part2:", data[ma-1])