from collections import Counter
import aocd

def setmapping(M, posd, na):
    for k in posd:
        for k2 in posd:
            px,py,dx,dy = *posd[k],*posd[k2]
            mx, my = dx-px, dy-py
            if (mx*my == 0) or (mx>0 and ((px,dy) != na)) or (mx<0 and ((dx,py) != na)):
                M[(k,k2)] = "<"*max(0, -mx) + "v"*max(0, my) + "^"*max(0, -my) + ">"*max(0, mx)
            else: M[(k,k2)] = ">"*max(0, mx) + "v"*max(0, my) + "^"*max(0, -my) + "<"*max(0, -mx)

def transall(s):
    ret = Counter()
    for k in s:
        cur, st = "A", k+"A"
        for c in st:
            ret += Counter({M2[(cur,c)]:s[k]})
            cur = c
    return ret

def solve(s, cnt):
    l = transall(s)
    for _ in range(cnt): l = transall(l)
    return sum(l[k]*(len(k)+1) for k in l)

numd = {"A":(2,3),"0":(1,3),"1":(0,2),"2":(1,2),"3":(2,2),"4":(0,1),"5":(1,1),"6":(2,1),"7":(0,0),"8":(1,0),"9":(2,0)}
dird = {"A":(2,0),"^":(1,0),"<":(0,1),"v":(1,1),">":(2,1)}
M2 = {}
setmapping(M2, numd, (0,3))
setmapping(M2, dird, (0,0))
data = {l[:-1]:int(l[:-1]) for l in aocd.get_data(day=21, year=2024).splitlines()}

print ("part1:", solve(data,2), "part2:", solve(data,25))