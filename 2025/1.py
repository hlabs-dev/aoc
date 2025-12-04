import aocd

data = [ (v[0], int(v[1:])) for v in aocd.get_data(day=1, year=2025).splitlines() ]
part1, part2, cur, pd = 0, 0, 50, "R"

for d,v in data:
    if d != pd: pd, cur = d, (100-cur)%100
    md, cur = divmod(cur+v,100)
    part1, part2 = part1 + (cur == 0), part2 + md
    
print("Part1:",part1,"Part2:",part2)
