import aocd
data = aocd.get_data(day=17, year=2023).split('\n')
sparse = {(i,j):int(c) for i,line in enumerate(data) for j,c in enumerate(line)}
n,m = len(data), len(data[0])
def tadd(a,b): return (a[0]+b[0],a[1]+b[1])
dirs = [(1,0), (0,-1), (-1,0), (0,1)]

def solve(mi,ma):
    ha = [[] for _ in range((n+m)*9)]
    visited = [False for _ in range(n*m*4)]
    ha[0] = [((0,0),0),((0,0),3)]
    ret = 1000
    for cost, bucket in enumerate(ha):
        for pos, di in bucket:
            dcost = 0
            if visited[pos[0]*m+pos[1]+di*n*m] : continue
            visited[pos[0]*m+pos[1]+di*n*m] = True
            if cost+mi>ret: break
            dir1 = (di+1)%4
            dir2 = (di-1)%4
            for step in range(ma):
                pos = tadd(pos,dirs[di]) 
                if pos not in sparse: break
                dcost += sparse[pos]
                if step+1 >= mi:
                    if pos == (n-1,m-1):
                        ret = min(ret, cost+dcost)
                    if visited[pos[0]*m+pos[1]+dir1*n*m] == False:
                        ha[cost+dcost].append((pos,dir1))
                        ha[cost+dcost].append((pos,dir2))
    return ret
print("Part1: %d Part2: %d" % (solve(1,3),solve(4,10)))