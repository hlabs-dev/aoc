import re
import aocd

def combo(v,regc):
    if v<4: return v
    if v==7: print("invalid combo")
    else: return regc[v-4]

def step(cur,mem,regs,out):
    op, ode = mem[cur:cur+2]
    if op == 0:
        regs[0] = regs[0]>>combo(ode,regs)
        cur += 2
    elif op == 1:
        regs[1] = regs[1]^ode
        cur += 2
    elif op == 2:
        regs[1] = combo(ode,regs)%8
        cur += 2
    elif op == 3:
        if regs[0]: cur = ode
        else: cur += 2
    elif op == 4:
        regs[1] = regs[1]^regs[2]
        cur += 2
    elif op == 5:
        out.append(combo(ode,regs)%8)
        cur += 2
    elif op == 6:
        regs[1] = regs[0]>>combo(ode,regs)
        cur += 2
    elif op == 7:
        regs[2] = regs[0]>>combo(ode,regs)
        cur += 2
    return cur,out

def run(regr,mem):
    cur = 0
    out = []
    while cur<len(mem):
        cur, out = step(cur,mem,regr,out)
    return out

def find(start,suffix):
    for i in range(0,64):
        if mem[len(mem)-suffix:] == run([start+i,0,0],mem):
            return start+i
        
def part2(mem):
    ret = 0
    for i in range(len(mem)):
        ret = find(ret*8,i+1)
    return ret

reg, mem = [list(map(int,re.findall(r'\d+', part))) for part in aocd.get_data(day=17, year=2024).split("\n\n")]

print("part1:",run(reg,mem), "part2:", part2(mem))