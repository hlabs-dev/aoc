import aocd
from heapq import heapify, heappop, heappush
from collections import defaultdict,Counter
import bisect

data = aocd.get_data(day=23, year=2024)

M = defaultdict(set)

for line in data.splitlines():
    a,b = line.split("-")
    M[a].add(b)
    M[b].add(a)

def part1():
    visited = set()
    ret = 0
    for k in [k for k in M if k[:1] == 't']:
        visited2 = set()
        for k2 in M[k]:
            if k2 not in visited:
                inter = M[k] & M[k2]
                for k3 in inter:
                    if k3 not in visited2 and k3 not in visited:
                        ret += 1
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
                bs = bisect.bisect_right(keys, nk)
                nkeys = keys[:bs]+[nk]+keys[bs:]
                if len(nkeys) == 13: return ",".join(nkeys)
                tkey = tuple(keys)
                if tkey not in visited:
                    visited.add(tkey)
                    nrem = {k for k in rem if k!=nk and k in M[nk]}
                    if s+1+len(nrem) >= 13: heappush(heap,(s+1,nkeys,nrem))

def part2_hack():
    visited = set()
    heap = [(1,[k],M[k]) for k in M]
    heapify(heap)

    for k in M:
        visited.add(k)
        se = M[k] | {k}
        fail = 0
        good = 0
        for nk in M[k]:
            if nk in visited:
                fail += 1
                if fail == 2: break
                else: continue
            nse = se & (M[nk] | {nk})
            if len(nse)>=13:
                se = nse
                good += 1
                visited.add(nk)
            else:
                fail += 1
                if fail == 2: break
                else: continue
        if fail < 2: return ",".join(sorted(se))
print("part1:",part1(),"part2:",part2_hack())
