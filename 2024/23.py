from heapq import heapify, heappop, heappush
from collections import defaultdict
import aocd

data = aocd.get_data(day=23, year=2024)

M = defaultdict(set)

for line in data.splitlines():
    a,b = line.split("-")
    M[a].add(b)
    M[b].add(a)

def part1():
    visited = set()
    ret = 0
    for k in M:
        visited2 = set()
        for k2 in M[k]:
            if k2 not in visited:
                inter = M[k] & M[k2]
                for k3 in inter:
                    if k3 not in visited2 and k3 not in visited:
                        ret += any(v[:1]=='t' for v in [k,k2,k3])
            visited2.add(k2)
        visited.add(k)
    return ret

def part2():
    visited = set()
    heap = [(1,[k],M[k]) for k in M]
    heapify(heap)
    while len(heap):
        s,keys,rem = heappop(heap)
        for nk in rem:
            if all(key in M[nk] for key in keys):
                nkeys = sorted([nk]+keys)
                tkey = tuple(keys)
                if tkey not in visited:
                    visited.add(tkey)
                    nrem = {k for k in rem if k!=nk and k in M[nk]}
                    if len(nrem): heappush(heap,(s+1,nkeys,nrem))
                    else: ret = nkeys
    return ",".join(ret)
print("part1:",part1(),"part2:",part2())
