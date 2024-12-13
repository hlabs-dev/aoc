from collections import Counter
import aocd

stones = list(map(int,aocd.get_data(day=11, year=2024).split()))

def getattractionset(stones):
    ret = set()
    bl = list(stones)
    it = 0
    while len(bl):
        stone = bl.pop()
        if stone not in ret:
            ret.add(stone)
            if stone == 0:
                bl.append(1)
            else:
                n,rem = 0,stone
                while(rem): rem, n = rem//10, n+1
                if n%2 == 0:
                    bl.append(stone%(10**(n//2)))
                    bl.append(stone//(10**(n//2)))
                else: bl.append(stone*2024)
        it += 1
    return ret

aps = list(getattractionset(stones))
rev_ap = { ap:i for i,ap in enumerate(aps) }
n = len(aps)
lookup = []
for i in range(n):
    stone = aps[i]
    if stone == 0:
        lookup.append([rev_ap[1]])
    else:
        n,rem = 0,stone
        while(rem): rem, n = rem//10, n+1
        if n%2 == 0: lookup.append([rev_ap[stone%(10**(n//2))],rev_ap[stone//(10**(n//2))]])
        else: lookup.append([rev_ap[stone*2024]])



stones2 = { rev_ap[k]:v for k,v in Counter(stones).items()}

def blink(cnt):
    newcnt = Counter()
    for stone in cnt:
        for nstone in lookup[stone]:
            newcnt[nstone] += cnt[stone]
    return newcnt

for i in range(75):
    if i==25: part1 = sum(stones2.values())
    stones2 = blink(stones2)

print("part1:", part1, "part2:", sum(stones2.values()))


