import re
import aocd

data = aocd.get_data(day=13, year=2024)
data = [ tuple(map(int,re.findall(r'\d+', machine))) for machine in data.split("\n\n")]
part2 = 10000000000000

def solve(offset=0):
    ret = 0
    for a1, a2, b1, b2, c1, c2 in data:
        c1, c2 = c1+offset, c2+offset
        det = a1 * b2 - a2 * b1
        if det == 0: continue
        det_x, det_y = c1 * b2 - c2 * b1, a1 * c2 - a2 * c1
        if det_x%det or det_y%det: continue
        ret += 3*det_x // det + det_y // det
    return ret

print("part1:",solve(),"part2:",solve(part2))