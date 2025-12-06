import aocd

data = [ v.split("-") for v in aocd.get_data(day=2, year=2025).split(",") ]
part1, part2 = 0, 0

def bad(fro, to, rep):
    ret = 0
    min_l, max_l = (len(fro)-1)//rep+1, len(to)//rep

    if min_l>max_l: return ret

    mi = (10**(min_l-1)) if len(fro)%rep else (int(fro[:min_l]) + (fro[:min_l]*(rep-1)<fro[min_l:]))
    ma = (10**(max_l)-1) if len(to)%rep else (int(to[:max_l]) - (to[:max_l]*(rep-1)>to[max_l:]))
    mil, mal = len(str(mi)), len(str(ma))

    for l in range(mil,mal+1):
        tmi, tma = mi if l == mil else 10*(mil-1), ma if l == mal else 10*(mil) - 1
        ret += (tmi+tma)*(tma-tmi+1)//2*sum((10**(k*l)) for k in range(rep))
        
    return ret

for fro,to in data:
    s = bad(fro,to,2)
    part1 += s
    part2 += s
    for k in [3,5]: part2 += k//abs(k)*bad(fro,to,abs(k))

print("Part1:",part1,"Part2:",part2)