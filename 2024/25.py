import aocd
from bisect import bisect_left

data = aocd.get_data(day=25, year=2024).split("\n\n")

def parse(key):
    lines = key.splitlines()
    iskey = lines[0][0] == "."
    idx = [bisect_left(lines,1,key=lambda x:x[i]=='.#'[iskey]) for i in range(5)]
    return (iskey, tuple(6-v if iskey else v-1 for v in idx))

keys, locks = set(), set()
for key in data:
    iskey, keyhash = parse(key)
    (keys if iskey else locks).add(keyhash)

print("part1:",sum( all(ki+li<=5 for ki,li in zip(k,l)) for k in keys for l in locks))