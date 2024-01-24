import aocd

data = [[c for c in line] for line in aocd.get_data(day=14, year=2023).split("\n")]
n,m = len(data), len(data[0])

def slidenorth(data):
    for j in range(m):
        c = 0
        for i in range(n):
            if data[i][j] == 'O': data[c][j],data[i][j],c = data[i][j], data[c][j], c+1
            elif data[i][j] == '#': c = i+1
    return data

def slidesouth(data):
    for j in range(m):
        c = n-1
        for i in range(n-1,-1,-1):
            if data[i][j] == 'O': data[c][j],data[i][j],c = data[i][j], data[c][j], c-1
            elif data[i][j] == '#': c = i-1
    return data

def slideeast(data):
    for i in range(n):
        c = m-1
        for j in range(m-1,-1,-1):
            if data[i][j] == 'O': data[i][c],data[i][j],c = data[i][j], data[i][c], c-1
            elif data[i][j] == '#': c = j-1
    return data

def slidewest(data):
    for i in range(n):
        c = 0
        for j in range(m):
            if data[i][j] == 'O': data[i][c],data[i][j],c = data[i][j],data[i][c],c+1
            elif data[i][j] == '#': c = j+1
    return data

def load(hs): return sum(n-i for (i,j) in hs)
def hash(data): return tuple((i,j) for i in range(n) for j in range(m) if data[i][j] == 'O')

slidenorth(data)
print("Part1:", load(hash(data)))

cache = {hash(data):0}
revcache = {0:hash(data)}
for c in range(1,10**9):
    data = slideeast(slidesouth(slidewest(slidenorth(data))))
    hs = hash(data)
    if hs in cache:
        start, length = cache[hs],c-cache[hs]
        val = start+(1000000000-start)%length
        print("Part2:",load(revcache[val]))
        break
    cache[hs] = c
    revcache[c] = hs