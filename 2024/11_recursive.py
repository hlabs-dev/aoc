from functools import cache
import aocd

stones = list(map(int,aocd.get_data(day=11, year=2024).split()))

@cache
def blink(stone, level):
    if level == 0: return 1
    if stone == 0: return blink(1, level-1)
    if len(str(stone))%2 == 0:
        log10 = 10**(len(str(stone))//2)
        return blink(stone%log10, level-1) + blink(stone//log10, level-1)
    return blink(stone*2024, level-1)


print("part1:", sum(blink(stone,25) for stone in stones),"part2:", sum(blink(stone,75) for stone in stones))