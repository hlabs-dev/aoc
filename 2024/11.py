from collections import Counter
import aocd

stones = Counter(map(int,aocd.get_data(day=10, year=2024).split()))

def blink(cnt):
    newcnt = Counter()
    for k in cnt:
        if k == 0:
            newcnt[1] += cnt[k]
        elif len(str(k))%2 == 0:
            log10 = 10**(len(str(k))//2)
            newcnt[k%log10] += cnt[k]
            newcnt[k//log10] += cnt[k]
        else: newcnt[k*2024] += cnt[k]
    return newcnt

for i in range(75):
    if i==25: part1 = sum(stones.values())
    stones = blink(stones)

print("part1:", part1, "part2:", sum(stones.values()))