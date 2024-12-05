import aocd

data = aocd.get_data(day=4, year=2024).splitlines()
m, n = len(data), len(data[0])

dirs = [(1,0),(0,1),(1,1),(-1,1)]

T = list('XMAS'), list('SAMX')

part1 = sum( line.count('XMAS') + line.count('SAMX') for line in data)

part1 += sum( col.count('XMAS') + col.count('SAMX')
             for j in range(m)
             for col in ["".join(data[i][j] for i in range(n))])

part1 += sum( col.count('XMAS') + col.count('SAMX')
             for j in range(-m, n)
             for col in ["".join(data[i][j+i] for i in range(max(0,-j),min(m,m-j)) if 0<=i+j<n)])

part1 += sum( col.count('XMAS') + col.count('SAMX')
             for j in range(0, n+m)
             for col in ["".join(data[i][j-i] for i in range(max(0,j-m),min(m,j)) if 0<=j-i<n)])


part2 = sum( data[i][j] == "A" and 
            "SSMM" in "".join([data[i+1][j+1],data[i+1][j-1],
                             data[i-1][j-1],data[i-1][j+1]])*2
            for i in range(1,m-1)
            for j in range(1,n-1))

print("part1:", part1, "part2:", part2)