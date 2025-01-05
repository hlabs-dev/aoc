import aocd
from bisect import bisect_left

data = aocd.get_data(day=25, year=2024).split("\n\n")

def parse(key):
    lines = key.splitlines()
    iskey = lines[0][0] == "."
    keyhash = sum(((1<<bisect_left(lines[1:-1],1,key=lambda x:x[i]==lines[6][0]))-1) << (i*5) for i in range(5))
    return (iskey, keyhash)

def solve(data):
    keys, locks = set(), set()
    for key in data:
        iskey, keyhash = parse(key)
        (keys if iskey else locks).add(keyhash)
    print("part1:",sum( l & k == l for k in keys for l in locks))

solve(data)