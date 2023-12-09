import aocd

data = aocd.get_data(day=9, year=2023).split('\n')
data = list(map(lambda x: list(map(int,x.split())),data))

def d(l): return [b-a for a,b in zip(l[:-1], l[1:])]
def solve(l): return l[-1] + solve(d(l)) if any(l) else 0

print("Part1:", sum(solve(l) for l in data),
      "Part2:", sum(solve(l[::-1]) for l in data))