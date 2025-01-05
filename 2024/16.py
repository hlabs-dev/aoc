import aocd, heapq
from collections import defaultdict

data = aocd.get_data(day=16, year=2024).splitlines()
h,w = len(data), len(data[0])
dirs = [(1,0),(0,1),(-1,0),(0,-1)]

def getpos(data,c): return next((i,j) for i in range(h) for j in range(w) if data[i][j] == c)
def seg(a,b,c,d): return tuple(v for t in sorted([(a,b),(c,d)]) for v in t)

def countsegs(segset):
    ret, points = 0,set()
    for a,b,c,d in segset:
        ret += abs(a-c) + abs(b-d) - 1
        points.update({(a,b),(c,d)})
    return ret + len(points)

def unfold(posx,posy,posdi,distances):
    segs = set()
    points = set()
    points.add((posx,posy,posdi))
    stack = [(posx,posy,posdi)]
    while len(stack):
        px,py,di = stack.pop()
        if (px,py,di) in distances:
            for nx,ny,ndi in distances[(px,py,di)][1]:
                segs.add(seg(px,py,nx,ny))
                if (nx,ny,ndi) not in points:
                    points.add((nx,ny,ndi))
                    stack.append((nx,ny,ndi))
    return countsegs(segs)
  

def dijkstra(data,start,end):
    distances = defaultdict(lambda:(float("inf"), set()))
    distances[(start[0],start[1],1)]=(0,set())
    queue=[(0,*start,1)]
    
    while queue:
        dist,px,py,di=heapq.heappop(queue)
        for ndi in range(-1,2):
            dix, diy = dirs[(di+ndi)%4]
            npx, npy, ndist = px+dix, py+diy, dist + 1 + 1000*(ndi!=0)
            
            while(data[npx][npy] != "#" and data[npx+diy][npy+dix] == "#" and data[npx-diy][npy-dix] == "#"):
                npx, npy, ndist = npx+dix, npy+diy, ndist + 1

            if (npx, npy) == end:
                distances[(npx, npy, (di+ndi)%4)] = (ndist, {(px,py,di)})

                return (ndist, unfold(*end,(di+ndi)%4,distances))

            if data[npx][npy] != "#":
                o_dist, o_set = distances[(npx, npy, (di+ndi)%4)]
                if o_dist == ndist:
                    o_set.add((px,py,di))
                elif o_dist > ndist:
                    distances[(npx, npy, (di+ndi)%4)] = (ndist, {(px,py,di)})
                    heapq.heappush(queue,(ndist,npx,npy,(di+ndi)%4))

start, end = getpos(data,"S"), getpos(data,"E")
p1,p2 = dijkstra(data,start,end)

print("part1:",p1,"part2:",p2)