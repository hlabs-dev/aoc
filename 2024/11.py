from collections import Counter
from functools import cache
import aocd

def solve():

    @cache
    def getstones(stone):
        if stone == 0: return (1,)
        n,rem = 0,stone
        while(rem): rem, n = rem//10, n+1
        if n%2 == 0: return (stone%(10**(n//2)),stone//(10**(n//2)))
        return (stone*2024,)

    stones = Counter(map(int,aocd.get_data(day=11, year=2024).split()))

    def blink(cnt):
        newcnt = Counter()
        for stone in cnt:
            for nstone in getstones(stone):
                newcnt[nstone] += cnt[stone]
        return newcnt

    for i in range(75):
        if i==25: part1 = sum(stones.values())
        stones = blink(stones)

    print("part1:", part1, "part2:", sum(stones.values()))

solve()

