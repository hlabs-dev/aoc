import aocd

data = aocd.get_data(day=7, year=2024)
data = [(int(a), list(map(int,b.split()))) 
        for line in data.splitlines() 
        for a,b in [line.split(":")] ]

def isok(target,li,part=1):
    cur = [target]
    for v in li[:0:-1]:
        ncur = []
        for res in cur:
            if v<res: ncur.append(res-v)
            if res%v == 0: ncur.append(res//v)
            if part == 2:
                sv, sres = str(v), str(res)
                if len(sres)>len(sv) and sres[-len(sv):] == sv:
                    ncur.append(int(sres[:-len(sv)]))
        if len(ncur) == 0: return 0
        cur = ncur
    return li[0] in cur

print("part1:",sum((isok(v,li))*v for v,li in data),
    "part2",sum((isok(v,li,2))*v for v,li in data))