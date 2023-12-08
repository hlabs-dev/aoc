import aocd,math,itertools

path, _, *data = aocd.get_data(day=8, year=2023).split('\n')
graph = {l[:3]:{'L':l[7:10],'R':l[12:15]} for l in data}

def solve(node,part):
    for c in itertools.count():
        node = graph[node][path[c % len(path)]]
        if node == 'ZZZ' or (part == 2 and node[-1] == 'Z'):
            return c+1

nodes = [ k for k in graph if k[-1] == 'A']

print("Part1:", solve("AAA",1), "Part2:", math.lcm(*(solve(node, 2) for node in nodes)))