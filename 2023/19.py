import aocd, math, time

data = aocd.get_data(day=19, year=2023)
START = time.time_ns()
W,P = data.split("\n\n")
P = [{ k:int(v) for item in part[1:-1].split(",") for k,v in [item.split("=")]} 
     for part in P.split('\n')]

W = { k:[ c.split(":") for c in v[:-1].split(",")] 
     for w in W.split("\n") for k,v in [w.split("{")]}

for w in W:
    for i,c in enumerate(W[w][:-1]):
        p, op, val = c[0][0], c[0][1], int(c[0][2:])
        r = (0,val-1) if op == '<' else (val+1,4000)
        W[w][i] = (p,r,c[1])

part1 = 0
for p in P:
    cur = 'in'
    while cur not in ['A','R']:
        cur = next(( n for t,r,n in W[cur][:-1] if r[0]<=p[t]<=r[1] ),W[cur][-1][0])
    if cur == 'A': part1 += sum(p.values())

def countparts(di): return math.prod(di[k][1]-di[k][0]+1 for k in di)


def part2(w,di):
    if w == "A": 
        return countparts(di)
    elif w == "R": return 0
    else:
        di = {k:v for k,v in di.items()}
        ret = 0
        for t,r,n in W[w][:-1]:
            start,stop = max(di[t][0],r[0]), min(di[t][1],r[1])
            if start<=stop:
                di[t] = (start,stop)
                ret += part2(n,di)
        ret += part2(W[w][-1][0],di)
        return ret
    
print("Part1: %d Pert2: %d" % (part1, part2('in',{k:(1,4000) for k in 'xmas'})))

print(">>>", (time.time_ns()-START)/1e9)