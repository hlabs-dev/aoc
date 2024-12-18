import re
import aocd

def combo(v,reg): return v if v<4 else reg[v-4]

def run(reg,mem):
    cur, out = 0, []
    while cur<len(mem): 
        op, ode = mem[cur:cur+2]
        if op in [0,6,7]: reg[[0,6,7].index(op)] = reg[0]>>combo(ode,reg)
        elif op == 1: reg[1] = reg[1]^ode
        elif op == 2: reg[1] = combo(ode,reg)%8
        elif op == 3: cur    = ode - 2 if reg[0] else cur
        elif op == 4: reg[1] = reg[1]^reg[2]
        elif op == 5: out.append(combo(ode,reg)%8)
        cur += 2       
    return out

def find_iter(start, suffix, mem):
    for i in range(start,start+8):
        if mem[suffix:] == run([i,0,0],mem) : yield i
        
def revreg(mem, cur, depth):
    if depth == 0: return cur
    else:
        for ncur in find_iter(cur*8, depth-1, mem):
            ret = revreg(mem, ncur, depth-1)
            if ret>=0: return ret
        return -1

reg, mem = [list(map(int,re.findall(r'\d+', part))) 
            for part in aocd.get_data(day=17, year=2024).split("\n\n")]

print("part1:",run(reg,mem), "part2:", revreg(mem,0,len(mem)))
