import aocd

data = [ v.split("-") for v in aocd.get_data(day=2, year=2025).split(",") ]
part1, part2 = 0, 0

def bad(fro, to, rep):
    min_l = (len(fro)-1)//rep+1
    max_l = len(to)//rep
    if min_l>max_l: return set()
    mi = (10**(min_l-1)) if len(fro)%rep else (int(fro[:min_l]) + (fro[:min_l]*(rep-1)<fro[min_l:]))
    ma = (10**(max_l)-1) if len(to)%rep else (int(to[:max_l]) - (to[:max_l]*(rep-1)>to[max_l:]))
    return {int(str(v)*rep) for v in range(mi,ma+1)}

for fro,to in data:
    s = set(bad(fro,to,2))
    part1 += sum(s)
    for k in range(3,len(to)+1): s.update(bad(fro,to,k))
    part2 += sum(s)

print("Part1:",part1,"Part2:",part2)