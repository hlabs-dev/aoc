import aocd
from more_itertools import dotproduct

data = aocd.get_data(day=9, year=2023).split('\n')
data = list(map(lambda x: list(map(int,x.split())),data))

lg = [len(data[0])]
for i in range(2,lg[0]+1): lg.append(-lg[-1]*(lg[0]-i+1)//i)

print("Part1:", sum(dotproduct(l[::-1],lg) for l in data),
      "Part2:", sum(dotproduct(l,lg) for l in data))