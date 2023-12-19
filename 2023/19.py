import aocd, math

data = aocd.get_data(day=19, year=2023)
W,P = data.split("\n\n")
P = [{ k:int(v) for item in part[1:-1].split(",") for k,v in [item.split("=")]} 
     for part in P.split('\n')]
W = { k:[ c.split(":") for c in v[:-1].split(",")] 
     for w in W.split("\n") for k,v in [w.split("{")]}

part1 = 0
for p in P:
    cur = 'in'
    while cur not in ['A','R']:
        cur = next(( c[1] for c in W[cur][:-1] if eval(c[0], {}, p)),W[cur][-1][0])
    if cur == 'A': part1 += sum(p.values())

def countparts(di): return math.prod(di[k][1]-di[k][0]+1 for k in di)

def part2(w,di):
    if w == "A": return countparts(di)
    elif w == "R": return 0
    else:
        di = {k:v for k,v in di.items()}
        ret = 0
        for c in W[w][:-1]:
            p, op, val = c[0][0], c[0][1], int(c[0][2:])
            start,stop = di[p]
            if op == "<":
                if start<val:
                    di[p] = (start,min(stop,val-1))
                    ret += part2(c[1],di)
                if val<=stop:
                    di[p] = (max(start,val),stop)
                else: return ret
            else:
                if stop>val:
                    di[p] = (max(start,val+1),stop)
                    ret += part2(c[1],di)
                if val>=start:
                    di[p] = (start,min(stop,val))
                else: return ret
        ret += part2(W[w][-1][0],di)
        return ret
    
print("Part1: %d Pert2: %d" % (part1, part2('in',{k:(1,4000) for k in 'xmas'})))