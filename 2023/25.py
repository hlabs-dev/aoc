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


def bfs(start, exclusions = {}):
    visited = {start:(0,[start])}
    heap = [(0,start,[start])]
    while len(heap)>0:
        dist, node, path = heappop(heap)
        for de in M[node]:
            if (node,de) in exclusions: continue
            if de not in visited:
                visited[de] = (dist+1, path+[de])
                heappush(heap,(dist+1,de,path+[de]))
    return (len(visited),visited, node)

def findcut():
    start = next(k for k in M)
    _,visited,stop = bfs(start)
    for s,d in pairwise(visited[stop][1]):
        exclusions = {(s,d),(d,s)}
        _,visited2,_ = bfs(start, exclusions)
        for s2,d2 in pairwise(visited2[stop][1]):
            exclusions = {(s,d),(d,s), (s2,d2),(d2,s2)}
            _,visited3,_ = bfs(start, exclusions)
            for s3,d3 in pairwise(visited3[stop][1]):
                exclusions = {(s,d),(d,s), (s2,d2),(d2,s2), (s3,d3),(d3,s3)}
                lena,_,_ = bfs(start, exclusions)
                if len(M) != lena:
                   print((s,d), (s2,d2), (s3,d3))
                   return (lena*(len(M)-lena))

print("AoC 2023:", findcut())