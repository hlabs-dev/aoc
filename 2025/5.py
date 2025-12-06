import aocd
import bisect

input = aocd.get_data(day=5, year=2025)
R,L = input.split("\n\n")
R = sorted((tuple(map(int,r.split("-"))) for r in R.splitlines()))
L = list(map(int,L.splitlines()))

R2 = []
cur = -1
for a,b in R:
    if a <= cur:
        if b>=cur:
            R2[-1] = (R2[-1][0],b)
            cur = b+1
    elif a > cur:
        R2.append((a,b))
        cur = b+1
        
part1 = sum(v>=R2[p][0] for v in L for p in [bisect.bisect_left(R2,v,key=lambda x:x[1])] if p<len(R2))

print("Part1:",part1,"Part2:",sum(b-a+1 for a,b in R2))
