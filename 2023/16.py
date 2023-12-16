import aocd

dirs = [(0,1),(-1,0),(0,-1),(1,0)]
ndirs = {('/'):[[1],[0],[3],[2]], ('\\'):[[3],[2],[1],[0]],
         ('-'):[[0],[0,2],[2],[0,2]],('|'):[[1,3],[1],[1,3],[3]],
         ('.'):[[0],[1],[2],[3]]}
def tadd(a,b): return (a[0]+b[0],a[1]+b[1])


data = aocd.get_data(day=16, year=2023).split('\n')
n,m = len(data), len(data[0])
sparse = { (i,j):data[i][j] for i in range(n) for j in range(m)}

def dfs(pos,di):
    energized = {pos}
    beams = [(pos,ndir) for ndir in ndirs[sparse[pos]][di]]
    visited = set(beams)
    while len(beams):
        pos,di = beams.pop()
        npos = tadd(pos,dirs[di])
        if npos in sparse:
            if npos not in energized: energized.add(npos)
            for ndir in ndirs[sparse[npos]][di]:
                if (npos,ndir) not in visited:
                    visited.add((npos,ndir))
                    beams.append((npos,ndir))
    return len(energized)

print("Part1: %d Part2: %d" % (dfs((0,0),0),
      max(dfs((i,j),d) for d in range(4) 
          for i in (range(n) if d%2==0 else [0,n-1])
          for j in (range(m) if d%2==1 else [0,m-1]))))