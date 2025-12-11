import aocd
from functools import cache

input = aocd.get_data(day=11, year=2025)

di = { src:dst.split() for line in input.splitlines() for src,dst in [line.split(': ')] }

@cache
def solve1(val="you"):
    if di[val][0] == "out": return 1
    else:
        return sum(solve1(val2) for val2 in di[val])
    
@cache
def solve2(val="svr",fft=False,dac=False):
    if di[val][0] == "out": return 1 if fft and dac else 0
    else:
        return sum(solve2(val2,fft or (val=="fft"),dac or (val=="dac")) for val2 in di[val])

part1, part2 = solve1(),solve2()

print("Part1:",part1,"Part2:",part2)