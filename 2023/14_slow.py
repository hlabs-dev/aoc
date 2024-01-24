import aocd

data = aocd.get_data(day=14, year=2023).split("\n")
n = len(data)
m = len(data[0])
sparse = {(i,j):data[i][j] for i in range(n) for j in range(m)}

def load(hs,n,m): return sum(n-i for i,_ in hs)

def rot(sparse,n,m): return {(j,n-i-1):sparse[(i,j)] 
                             for i,j in sparse},m,n

def slide(sparse,n,m):
    cur = [0]*m
    for j in range(m):
        for i in range(n):
            if (i,j) in sparse:
                if sparse[(i,j)] == 'O':
                    del sparse[(i,j)]
                    sparse[(cur[j],j)] = 'O'
                    cur[j] += 1
                elif sparse[(i,j)] == '#':
                    cur[j] = i+1

def fullrot(sparse, n, m):
    for _ in range(4):
        slide(sparse,n,m)
        sparse,n,m = rot(sparse,n,m)
    return sparse

def hash(sparse): return tuple(sorted(k for k in sparse if sparse[k] == 'O'))

slide(sparse,n,m)
print("Part1:", load(hash(sparse),n,m))

cache = {hash(sparse):0}
for c in range(1,10**9):
    sparse = fullrot(sparse, n, m)
    hs = hash(sparse)
    if hs in cache:
        start, length = cache[hs],c-cache[hs]
        val = start+(1000000000-start)%length
        print("Part2:",load(next(k for k in cache if cache[k] == val),n,m))
        break
    cache[hs] = c