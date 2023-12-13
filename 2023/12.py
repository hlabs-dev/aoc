import time
from functools import cache
import aocd

def parseline(line):
    m,l = line.split()
    return(m,tuple(map(int,l.split(','))))

data = list(map(parseline, aocd.get_data(day=12, year=2023).split('\n')))

start_time = time.time()

@cache
def dp(S,L):
    s,l = len(S), len(L)
    if s < sum(L)+l : return 0
    if l == 0: return all(c in '?.' for c in S)
    ret = dp(S[1:], L) if S[0] in '.?' else 0
    if all(c in '?#' for c in S[:L[0]]) and (s<L[0] or S[L[0]] in '.?'):
        ret += dp(S[L[0]+1:], L[1:])
    return ret

print("Part1: %d Part2: %d" % (sum(dp(s+".",l) for s,l in data), 
                               sum(dp((s+'?')*5,l*5)  for s,l in data)))

print("--- %s seconds ---" % (time.time() - start_time))