from collections import defaultdict
from heapq import heappop, heappush
from itertools import pairwise
import aocd

data = aocd.get_data(day=25, year=2023)
M = defaultdict(set)
for line in data.split("\n"):
    src,dst = line.split(': ')
    for de in dst.split():
        M[src].add(de)
        M[de].add(src)

def bfs(start, exclusions = {}, stop = -1):
    visited = {start:(0,[start])}
    heap = [(0,start,[start])]
    while len(heap)>0:
        dist, node, path = heappop(heap)
        for de in M[node]:
            if (node,de) in exclusions: continue
            if de not in visited:
                visited[de] = (dist+1, path+[de])
                if de == stop and False:
                    return len(visited),visited,stop
                heappush(heap,(dist+1,de,path+[de]))
    return (len(visited),visited, node)

def findcut():
    start = next(k for k in M)
    _,visited,stop = bfs(start)
    p1 = list(pairwise(visited[stop][1]))
    p1 = p1[len(p1)//2-1::-1]+p1[len(p1)//2:]
    for i,(s,d) in enumerate(p1):
        exclusions = {(s,d),(d,s)}
        _,visited2,_ = bfs(start, exclusions,stop)
        p2 = list(pairwise(visited2[stop][1]))
        p2 = p2[len(p2)//2-1::-1]+ p2[len(p2)//2:]
        for j, (s2,d2) in enumerate(p2):
            if (s2,d2) in p1: continue
            exclusions = {(s,d),(d,s), (s2,d2),(d2,s2)}
            _,visited3,_ = bfs(start, exclusions,stop)
            p3 = list(pairwise(visited3[stop][1]))
            p3 = p3[len(p3)//2-1::-1]+ p3[len(p3)//2:]
            for k,(s3,d3) in enumerate(p3):
                if (s3,d3) in p1 or (s3,d3) in p2: continue
                exclusions = {(s,d),(d,s), (s2,d2),(d2,s2), (s3,d3),(d3,s3)}
                lena,_,nstop = bfs(start, exclusions,stop)
                if len(M) != lena:
                   return (lena*(len(M)-lena))

print("AoC 2023:", findcut())