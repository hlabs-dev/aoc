import aocd,math,itertools
path, _, *data = aocd.get_data(day=8, year=2023).split('\n')
graph = {l[:3]:(l[7:10],l[12:15]) for l in data}

def gdepth(nodes):
    for i in itertools.count(1):
        nodes = { dest for node in nodes for dest in graph[node] }
        if any(node[-1]=='Z' for node in nodes): return i

cycles = {node:gdepth({node})*len(path) for node in graph if node[-1] == 'A'}

print('Part1:', cycles['AAA'], 'Part2', math.lcm(*cycles.values()))