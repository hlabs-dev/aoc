import time
start_time = time.time()

import aocd
from functools import cache

def parseline(line):
    m,l = line.split()
    l = tuple(map(int,l.split(',')))
    return(m,l)

data = list(map(parseline, aocd.get_data(day=12, year=2023).split('\n')))

@cache
def dp(s,l):
    ret, delta = 0, len(s)-sum(l)-len(l)+1
    if delta < 0: return 0
    if len(l) == 0: return all(c in '?.' for c in s)
    ret = dp(s[1:], l) if s[0] in '.?' else 0
    if all(c in '?#' for c in s[:l[0]]) and (len(s) == l[0] or s[l[0]] in '.?'):
        ret += dp(s[l[0]+1:], l[1:])
    return ret

print("Part1: %d Part2: %d" % (sum(dp(s,l) for s,l in data), sum(dp('?'.join([s]*5),l*5) for s,l in data)))

print("--- %s seconds ---" % (time.time() - start_time))