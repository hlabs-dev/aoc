import aocd

data = aocd.get_data(day=23, year=2023).split("\n")
n, m = len(data), len(data[0])

def tadd(a,b): return (a[0]+b[0], a[1]+b[1])
dirs = [(0,1),(0,-1),(1,0),(-1,0)]
slopes = [".><",".<>",".v^",".^v"]

M = {(i,j):c for i,line in enumerate(data) for j, c in enumerate(line)}
S = (0,next(i for i,c in enumerate(data[0]) if c=='.'))
E = (n-1,next(i for i,c in enumerate(data[-1]) if c=='.'))

visited = {S}
stack = [(S,i) for i,di in enumerate(dirs) if tadd(S,di) in M and M[tadd(S,di)] in '.<>^v']

graph = {}
idx = 0
nm = {S:0}

def graphadd(graph, s, d, cost):
    if s not in graph: graph[s] = {}
    graph[s][d] = cost

oneway,oneway2,border = set(),set(),{0}

while len(stack):
    start,direction = stack.pop(0)
    prev, cpos, le = start, tadd(start,dirs[direction]), 1
    visited.add(cpos)
    way = slopes[direction].index(M[cpos])
    ndirs = [(i,npos in visited) for i,di in enumerate(dirs)
             for npos in [tadd(cpos,di)] if npos in M and M[npos] != '#']
    while len(ndirs) == 2:
        direction = next(di for di,_ in ndirs if prev != tadd(cpos,dirs[di]))
        prev, cpos, le = cpos, tadd(cpos,dirs[direction]), le+1
        way |= slopes[direction].index(M[cpos])
        visited.add(cpos)
        ndirs = [(i,npos in visited) for i,di in enumerate(dirs)
                 for npos in [tadd(cpos,di)] if npos in M and M[npos] != '#']
    
    if cpos not in nm:
        idx += 1
        nm[cpos] = idx
        
    if way == 1: oneway.add((nm[cpos], nm[start]))
    else: oneway.add((nm[start], nm[cpos]))

    graphadd(graph, nm[start], nm[cpos], le)
    graphadd(graph, nm[cpos], nm[start], le)

    if len(ndirs) == 3 and nm[start] in border:
        border.add(nm[cpos])
        oneway2.add((nm[cpos],nm[start]))

    for di in [di2 for di2,vis in ndirs if not(vis)]: stack.append((cpos,di))

def longuestpath(oneway):
    fwd, lmax = {}, 0

    stack = [(0,0,0,0)]
    while len(stack):
        p,l,v,d = stack.pop()
        if d == (idx) // 2:
            if p not in fwd: fwd[p] = []
            fwd[p].append((l,v))
            continue
        for n in graph[p]:
            if (p,n) in oneway or v & 1<<n: continue
            stack.append((n,l+graph[p][n],v|1<<p,d+1))
    for n in fwd: fwd[n].sort(reverse=True)
    
    stack = [(nm[E],0,0,0)]
    while len(stack):
        p,l,v,d = stack.pop()
        if d == (idx+1) // 2:
            continue
        if p == 0: 
            lmax = max(lmax, l)
            continue
        if p in fwd:
            for fl,fv in fwd[p]:
                if lmax > l+fl: break
                if (v|1<<p) & fv: continue
                lmax = max(lmax, l+fl)
        for n in graph[p]:
            if (n,p) in oneway or v & 1<<n: continue
            stack.append((n,l+graph[p][n],v|1<<p,d+1))
    return lmax

print("Part1:", longuestpath(oneway), "Part2:", longuestpath(oneway2))