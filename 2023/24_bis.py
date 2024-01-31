import aocd, time
START = time.time_ns()
from itertools import combinations

data = aocd.get_data(day=24, year=2023)
print(">>>", (time.time_ns()-START)/1e9)
L = [ list(map(int,l.replace(' @',',').split(', '))) for l in data.split('\n')]
mi, ma, part1 = 200000000000000, 400000000000000, 0

print(">>>", (time.time_ns()-START)/1e9)
for a,b in combinations(L,2):
    if (b[4]/b[3] - a[4]/a[3]) == 0: continue
    x = (a[1]-b[1] + b[4]*b[0]/b[3] - a[4]*a[0]/a[3])/(b[4]/b[3] - a[4]/a[3])
    t1, t2 = (x-a[0])/a[3] , (x-b[0])/b[3]
    y = a[1]+a[4]*t1
    part1 += (t1>=0 and t2>=0 and mi<=x<=ma and mi<=y<=ma)

print("Part1: ", part1)
print(">>>", (time.time_ns()-START)/1e9)

x1,x2,x3,x4,x5 = L[:5]

a = [[(x2[4] - x1[4]), (x1[3] - x2[3]),(x1[1] - x2[1]),(x2[0] - x1[0])],
     [(x3[4] - x1[4]), (x1[3] - x3[3]),(x1[1] - x3[1]),(x3[0] - x1[0])],
     [(x4[4] - x1[4]), (x1[3] - x4[3]),(x1[1] - x4[1]),(x4[0] - x1[0])],
     [(x5[4] - x1[4]), (x1[3] - x5[3]),(x1[1] - x5[1]),(x5[0] - x1[0])]]
b = [-x1[0]*x1[4] + x2[0]*x2[4] + x1[1]*x1[3] - x2[1]*x2[3],
     -x1[0]*x1[4] + x3[0]*x3[4] + x1[1]*x1[3] - x3[1]*x3[3],
     -x1[0]*x1[4] + x4[0]*x4[4] + x1[1]*x1[3] - x4[1]*x4[3],
     -x1[0]*x1[4] + x5[0]*x5[4] + x1[1]*x1[3] - x5[1]*x5[3]]

for i in range(len(a)-1):
    for j in range(i+1,len(a)):
        if a[j][i] == 0: continue
        b[j] = b[j]*a[i][i]-b[i]*a[j][i]
        for k in range(i+1,len(a)):
             a[j][k] = a[j][k]*a[i][i]-a[i][k]*a[j][i]
        a[j][i] = 0

for i in range(len(a)-1,-1,-1):
    for j in range(i+1,len(a)):
        b[i] -= a[i][j]*b[j]
    if b[i] != 0 or a[i][i] != 0: 
        b[i] = b[i]//a[i][i]

x0,y0,vx,vy = b
t1 = -(x0-x1[0])//(vx-x1[3])
t2 = -(x0-x2[0])//(vx-x2[3])
z1 = x1[2] + x1[5]*t1
z2 = x2[2] + x2[5]*t2
z0 = z1 - t1*(z1-z2)//(t1-t2)

print("Part2: ",sum(b[:2])+z0)
print(">>>", (time.time_ns()-START)/1e9)


