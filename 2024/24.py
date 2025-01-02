from collections import defaultdict, deque
import aocd

data = aocd.get_data(day=24, year=2024)

V, R = data.split("\n\n")
V = { var:int(val) for line in V.splitlines() for var,val in [line.split(": ")] }
R = {res:(v1,v2,op) for line in R.splitlines() for v1,op,v2,_,res in [line.split(" ")]}

def getRuleIdx(R):
    ridx = defaultdict(list)
    for r in R:
        v1,v2,op = R[r]
        ridx[v1].append([v2,op,r])
        ridx[v2].append([v1,op,r])
    return ridx

def solve(V,ridx):
    solve = deque(V.keys())
    ret = 0
    wl=[]
    while len(solve):
        v1 = solve.popleft()
        for v2,op,res in ridx[v1]:
            if v2 in V and res not in V:
                val1,val2 = V[v1],V[v2]
                nval = (val1 and val2) if op == "AND" else ((val1 or val2) if op == "OR" else (val1 != val2))
                V[res] = nval
                solve.append(res)
                if res[0] == "z":ret += nval*(2**int(res[1:]))
    return ret 

def setvar(V,var,val):
    for i in range(45):
        V[var+f'{i:02}'] = (val%2,i)
        val = val//2

def su(a,b,ridx):
    temp = {}
    setvar(temp,"x",a)
    setvar(temp,"y",b)
    return solve(temp,ridx)

ridx = getRuleIdx(R)

part2 = []
for i in range(1,45):
    if not(any(l[2] in R[f'z{i:02}'][:2] for l in ridx[f'x{i:02}'] if l[1] == "XOR" and R[f'z{i:02}'][2] =="XOR")):
        xor1 = next(v[2] for v in ridx[f'x{i:02}'] if v[1] == "XOR")
        if R[f'z{i:02}'][2] != "XOR":
            xor2 = next(v[2] for v in ridx[xor1] if v[1] == "XOR")
            part2 += [f'z{i:02}', xor2]
        else:
            and1 = next(v[2] for v in ridx[f'x{i-1:02}'] if v[1] == "AND")
            or1 = next(v[2] for v in ridx[and1] if v[1] == "OR")
            xor2 = next(v[0] for v in ridx[or1] if v[1] == "XOR")
            part2 += [xor1, xor2]

print("part1:", solve(V,ridx) ,"part2:", ".".join(sorted(part2)))