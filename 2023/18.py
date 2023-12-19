import aocd
data = aocd.get_data(day=18, year=2023)
dirs = {'D':(1,0),'L':(0,-1),'U':(-1,0),'R':(0,1)}
dirs2 = [(1,0),(0,1),(-1,0),(0,-1)]
def tadd(a,b,c=1): return (a[0]+b[0]*c,a[1]+b[1]*c)
points = [ (d,int(n),c[2:-1],int(c[2:-2],16),int(c[-2:-1])) for line in data.split('\n') for d,n,c in [line.split()]]

prev1, prev2 = (0,0), (0,0)
area1=area2=peri1=peri2= 0

def newpoint(steps,di,pos,peri,area):
    npos = tadd(pos,di,steps)
    return npos, peri+steps, area + pos[0]*npos[1] - pos[1]*npos[0]

for point in points:
    prev1,peri1,area1 = newpoint(point[1],dirs[point[0]],prev1,peri1,area1)
    prev2,peri2,area2 = newpoint(point[3],dirs2[point[4]],prev2,peri2,area2)

print ("Part1: %d Part2: %d" % (((abs(area1)+peri1) // 2) + 1, ((abs(area2)+peri2) // 2) + 1))