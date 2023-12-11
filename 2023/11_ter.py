import aocd

data = aocd.get_data(day=11, year=2023).split('\n')
n,m = len(data), len(data[0])

lines = [ (i,c) for i in range(n) for c in [data[i].count('#')] if c>0 ]
rows = [ (j,c) for j in range(m) 
        for c in [sum(data[i][j]=="#" for i in range(n))] if c>0 ]

def rawgap(li,raw=0,gap=0):
    total = serie = li[0][1]
    prev =  li[0][0]
    prev_gaps = 0
    for i,cnt in li[1:]:
        raw += cnt*serie
        prev_gaps += (i-prev-1)*total
        gap += cnt*prev_gaps
        total += cnt
        serie += total
        prev = i
    return raw,gap

raw,gap = rawgap(rows,*rawgap(lines))

print("Part1: %d Part2: %d" % (raw+gap*2, raw+gap*10**6))