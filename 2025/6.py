import aocd
from functools import reduce

input = aocd.get_data(day=6, year=2025)
data = input.splitlines()

nums = [list(map(int,line.split())) for line in data[:-1]]
signs = data[-1].split()
part1 = sum(reduce((lambda x,y:x+y) if signs[i]=="+" else (lambda x,y:x*y),
                   (nums[j][i] for j in range(len(nums)))) for i in range(len(signs)))

part2 = 0
op = (lambda x,y:x+y)
bloc = 0
for j in range(len(data[0])):
    cur = 0
    for i in range(len(data)-1):
        c = data[i][j]
        if c !=" ": cur = cur*10+(ord(c)-48)

    if cur == 0:
        part2 += bloc
        bloc = 0
        op = (lambda x,y:x+y)

    else: bloc = op(bloc,cur)

    if data[-1][j]!=" ":
        op = (lambda x,y:x+y) if data[-1][j]=="+" else (lambda x,y:x*y)
part2 += bloc

print("Part1:",part1,"Part2:",part2)