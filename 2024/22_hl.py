from collections import Counter
import aocd

mo = 19**4

def nextsecret(n):
    n1 = (n^((n<<6)&16777215))
    n2 = (n1>>5)^n1
    return ((n2<<11)^n2)&16777215

def combs(n,cbs):
    visited = set()
    base = [n%10]
    for i in range(2000):
        n = nextsecret(n)
        base.append(n%10)
    ret = Counter()
    diffs = [9+a-b for a,b in zip(base[1:],base)]
    cur = diffs[0]*(19**2)+diffs[1]*(19)+diffs[2]
    for i,v in enumerate(diffs[3:]):
        cur = (cur*19+v)%mo
        if cur not in visited:
            cbs[cur] += base[i+4]
            visited.add(cur)
    return n

data = [int(line) for line in aocd.get_data(day=22, year=2024).splitlines()]
cbs = [0]*(19**4)

print("part1:",sum(combs(n,cbs) for n in data),"part2",max(cbs))
