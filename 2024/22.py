from collections import Counter
import aocd

def nextsecret(n):
    n1 = (n^((n<<6)&16777215))
    n2 = (n1>>5)^n1
    return ((n2<<11)^n2)&16777215

def combs(n,k):
    base = [n%10]
    for i in range(k):
        n = nextsecret(n)
        base.append(n%10)
    ret = Counter()
    diffs = [a-b for a,b in zip(base[1:],base)]
    for i in range(len(diffs)-3):
        tu = tuple(diffs[i:i+4])
        if tu not in ret: ret[tu] = base[i+4]
    return n,ret

data = [int(line) for line in aocd.get_data(day=22, year=2024).splitlines()]

part1, part2 = 0, Counter()
for v in data:
    n, cnts = combs(v,2000)
    part1 += n
    part2 += cnts

print("part1",part1,"part2",max(part2.values()))
