import aocd
from math import lcm

data = aocd.get_data(day=20, year=2023)
modules = { s[1:]:(s[0],d.split(', ')) for line in data.split("\n") for s,d in [line.split(" -> ")]}
mem = {}
for m in modules:
    if modules[m][0] == '%':
        mem[m] = False
    for d in modules[m][1]:
        if d in modules and modules[d][0] == '&':
            if d in mem: mem[d][m] = False
            else: mem[d] = {m:False}

def flow(s,d,ishigh):
    if modules[d][0] == "%":
        if ishigh: return []
        else: ne = mem[d] = not(mem[d])
    else:
        mem[d][s] = ishigh
        ne = any(not(v) for v in mem[d].values())
    return [(m, ne) for m in modules[d][1]]

def button(cpt):
    fifo = [('roadcaster',d,False) for d in modules['roadcaster'][1]]
    cpt[0] += 1
    while len(fifo):
        s,d,ishigh = fifo.pop(0)
        li = flow(s,d,ishigh)
        for nd,nishigh in li:
            cpt[nishigh] += 1
            if nd == 'lv' and nishigh and d not in part2: part2[d] = i
            if nd in modules: fifo.append((d,nd,nishigh))
    return cpt
cpt, i, part2 = [0,0], 1, {}
for i in range(1,10000):
    cpt = button(cpt)
    if i == 1000: print("Part1: ", cpt[0]*cpt[1])
    if len(part2) == 4:
        print("Part2: ", lcm(*(part2.values())))
        break