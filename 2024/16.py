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
        ret += abs(a-c) + abs(b-d) + 1 - ((a,b) in points) - ((c,d) in points)
        points.update({(a,b),(c,d)})
    return ret

def dijkstra(data,start,end):
    distances = defaultdict(lambda:(float("inf"), set()))
    distances[start[0],start[1],1]=(0,set())
    queue=[(0,*start,1)]
    
    while queue:
        dist,px,py,di=heapq.heappop(queue)
        _, p_set = distances[(px,py,di)]
        for ndi in range(-1,2):
            dix, diy = dirs[(di+ndi)%4]
            npx, npy, ndist = px+dix, py+diy, dist + 1 + 1000*(ndi!=0)
            
            while(data[npx][npy] != "#" and data[npx+diy][npy+dix] == "#" and data[npx-diy][npy-dix] == "#"):
                npx, npy, ndist = npx+dix, npy+diy, ndist + 1

            nset =  p_set | {seg(px,py,npx, npy)}

            if (npx, npy) == end:
                return (ndist, countsegs(nset))

            if data[npx][npy] != "#":
                o_dist, o_set = distances[(npx, npy, (di+ndi)%4)]
                if o_dist == ndist:
                    if any((pos not in o_set) for pos in nset):
                        o_set.update(nset)
                        heapq.heappush(queue,(ndist,npx,npy,(di+ndi)%4))
                elif o_dist > ndist:
                    distances[(npx, npy, (di+ndi)%4)] = (ndist, nset)
                    heapq.heappush(queue,(ndist,npx,npy,(di+ndi)%4))

start, end = getpos(data,"S"), getpos(data,"E")
p1,p2 = dijkstra(data,getpos(data,"S"),getpos(data,"E"))
print("part1:",p1,"part2:",p2)