import aocd,math

data = aocd.get_data(day=8, year=2023).split('\n')
path, _, *data = data

graph = {}
for l in data: graph[l[:3]] = {'L':l[7:10],'R':l[12:15]}

def solve(node,part):
    for c in range(10**9):
        node = graph[node][path[c % len(path)]]
        if node == 'ZZZ' or (part == 2 and node[-1] == 'Z'):
            return c+1

nodes = [ k for k in graph if k[-1] == 'A']
part2 = 1

for node in nodes:
    c = solve(node, 2)
    part2 *= c//math.gcd(c, part2)

print("Part1:", solve("AAA",1), "Part2:", part2)