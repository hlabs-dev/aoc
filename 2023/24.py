import aocd, numpy as np
from itertools import combinations

data = aocd.get_data(day=24, year=2023)

L = [ list(map(int,l.replace(' @',',').split(', '))) for l in data.split('\n')]
mi, ma, part1 = 200000000000000, 400000000000000, 0

for a,b in combinations(L,2):
    if (b[4]/b[3] - a[4]/a[3]) == 0: continue
    x = (a[1]-b[1] + b[4]*b[0]/b[3] - a[4]*a[0]/a[3])/(b[4]/b[3] - a[4]/a[3])
    t1, t2 = (x-a[0])/a[3] , (x-b[0])/b[3]
    y = a[1]+a[4]*t1
    part1 += (t1>=0 and t2>=0 and mi<=x<=ma and mi<=y<=ma)

print("Part1: ", part1)

x1,x2,x3,x4 = L[:4]

a = np.array([[(x2[4] - x1[4]), (x1[3] - x2[3]),0,(x1[1] - x2[1]),(x2[0] - x1[0]),0],
            [(x2[5] - x1[5]),0, (x1[3] - x2[3]),(x1[2] - x2[2]),0,(x2[0] - x1[0])],
            [(x3[4] - x1[4]), (x1[3] - x3[3]),0,(x1[1] - x3[1]),(x3[0] - x1[0]),0],
            [(x3[5] - x1[5]),0, (x1[3] - x3[3]),(x1[2] - x3[2]),0,(x3[0] - x1[0])],
            [(x4[4] - x1[4]), (x1[3] - x4[3]),0,(x1[1] - x4[1]),(x4[0] - x1[0]),0],
            [(x4[5] - x1[5]),0, (x1[3] - x4[3]),(x1[2] - x4[2]),0,(x4[0] - x1[0])]])
b = np.array([-x1[0]*x1[4] + x2[0]*x2[4] + x1[1]*x1[3] - x2[1]*x2[3],
            -x1[0]*x1[5]+x2[0]*x2[5]+x1[2]*x1[3]-x2[2]*x2[3],
            -x1[0]*x1[4]+x3[0]*x3[4]+x1[1]*x1[3]-x3[1]*x3[3],
            -x1[0]*x1[5]+x3[0]*x3[5]+x1[2]*x1[3]-x3[2]*x3[3],
            -x1[0]*x1[4]+x4[0]*x4[4]+x1[1]*x1[3]-x4[1]*x4[3],
            -x1[0]*x1[5]+x4[0]*x4[5]+x1[2]*x1[3]-x4[2]*x4[3]])
x = list(map(round,np.linalg.solve(a, b)))

# answers lack precision, need to round them and rebase from real points
t1 = round((x[0]-x1[0]) / (x[3]-x1[3]))
print("Part2: ",sum(x1[:3])-t1*(sum(x1[3:])-sum(x[3:])))

