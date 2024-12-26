from collections import defaultdict, deque
import aocd

data = aocd.get_data(day=24, year=2024)

V, R = data.split("\n\n")
V = { var:(int(val),int(var[1:])) for line in V.splitlines() for var,val in [line.split(": ")] }
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
                val1,l1,val2,l2 = *V[v1],*V[v2]
                nval = (val1 and val2) if op == "AND" else ((val1 or val2) if op == "OR" else (val1 != val2))
                if l1 == -1 or l2 == -1:
                    nl = -1
                elif l1 != l2:
                    nl = -1
                    wl.append(res)
                else: nl = l1 + 1
                V[res] = (nval,nl)
                solve.append(res)
                if res[0] == "z":
                    #print(res)
                    if nl != -1 and int(res[1:])+1 != nl:
                        wl.append(res)
                    ret += nval*(2**int(res[1:]))
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

part1 = solve(V,ridx)

for i in range(1,45):
    if not(any(l[2] in R[f'z{i:02}'][:2] for l in ridx[f'x{i:02}'] if l[1] == "XOR" and R[f'z{i:02}'][2] =="XOR")):
        print(i)
        print(R[f'z{i:02}'])
        print(ridx[f'x{i:02}'])

R['z05'],R['hdt'] = R['hdt'],R['z05']
R['z09'],R['gbf'] = R['gbf'],R['z09']
R['mht'],R['jgt'] = R['jgt'],R['mht']
R['z30'],R['nbf'] = R['nbf'],R['z30']

print("part1:", part1 ,"part2:", ".".join(sorted(['mht','jgt','z09','gbf','z05','hdt','z30','nbf'])))