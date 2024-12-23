from collections import Counter
import aocd

numd = {"A":(2,3),"0":(1,3),"1":(0,2),"2":(1,2),"3":(2,2),"4":(0,1),"5":(1,1),"6":(2,1),"7":(0,0),"8":(1,0),"9":(2,0)}
numdrev = {b:a for a,b in numd.items()}
dird = {"A":(2,0),"^":(1,0),"<":(0,1),"v":(1,1),">":(2,1)}
dirdrev = {b:a for a,b in dird.items()}
dirrev = {">":(1,0),"v":(0,1),"<":(-1,0),"^":(0,-1)}

dials = { (x-x1,y-y1) for x,y in dird.values() for x1,y1 in dird.values() if (x,y)!=(x1,y1)}
dialrules = [{}]
for x,y in dials:
    if x*y == 0:
        val = ">"*max(0, x) + "v"*max(0, y) + "<"*max(0, -x) + "^"*max(0, -y)
        for di in dialrules: di[(x,y)] = val
    else:
        vals = [">"*max(0, x) + "<"*max(0, -x) + "v"*max(0, y) + "^"*max(0, -y),
                "v"*max(0, y) + "^"*max(0, -y) + ">"*max(0, x) + "<"*max(0, -x)]
        dialrules = [{**di, **{(x,y):val}} for di in dialrules for val in vals]


def decode(s,pad,padrev):
    ret = ""
    posx,posy = pad["A"]
    for c in s:
        if c in dirrev:
            dx,dy = dirrev[c]
            posx,posy = posx+dx,posy+dy
            if (posx,posy) not in padrev: print("houston")
        elif c == "A":
            ret += padrev[(posx,posy)]
        else:
            print("Oups")
    return ret

def transall(s,pad,padrev,quick=True,fd=dict()):
    ret = [Counter()]
    for k in s:
        posx,posy = pad["A"]
        st = k+"A"
        for c in st:
            dstx, dsty = pad[c]
            mx, my = dstx-posx, dsty-posy
            #print(mx,my)
            if not(quick) and mx and my:
                tmpret = []
                if (posx+mx,posy) in padrev:
                    ne = ">"*max(0, mx) + "<"*max(0, -mx) + "v"*max(0, my) + "^"*max(0, -my)
                    tmpret += [ di+Counter({ne:s[k]}) for di in ret]
                if (posx,posy+my) in padrev:
                    ne = "v"*max(0, my) + "^"*max(0, -my) + ">"*max(0, mx) + "<"*max(0, -mx)
                    tmpret += [ di+Counter({ne:s[k]}) for di in ret]
                ret = tmpret
            else:
                if (mx,my) in fd:
                    move = fd[(mx,my)]
                    if posx == 0 and my == -1: move = ">"*mx+"^"
                    if posy == 0 and posx+mx == 0: move = "v"+"<"*(-mx)
                else: 
                    #print("nomatch", (mx,my))
                    move = ">"*max(0, mx) + "v"*max(0, my) + "<"*max(0, -mx) + "^"*max(0, -my)
                ret = [ di+Counter({move:s[k]}) for di in ret]
            posx,posy = dstx, dsty
    return ret

def solve(s, cnt=2, fd=dict()):
    l = transall(s,numd, numdrev, False)
    for i in range(cnt):
        l = [ s2 for s1 in l for s2 in transall(s1,dird, dirdrev, fd=fd)]
    return min((sum(s[k]*(len(k)+1) for k in s)) for s in l)

def parts(n,data,bestdial):
    ret = 0
    for line in data:
        a,b = int(line[:3]),solve(Counter([line[:3]]),n,fd=dialrules[bestdial])
        ret += a*b
    return ret

bestdial = sorted([(solve(Counter(["179"]),5,fd=dialrules[i]),i) for i in range(32)])[0][1]

data = aocd.get_data(day=21, year=2024).splitlines()
    
print("part1:", parts(2,data, bestdial), "part2:", parts(25,data, bestdial))