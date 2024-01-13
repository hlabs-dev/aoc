import aocd
import networkx as nx

data = aocd.get_data(day=23, year=2023).split("\n")
n, m = len(data), len(data[0])

def tadd(a,b): return (a[0]+b[0], a[1]+b[1])
dirs = [(0,1),(0,-1),(1,0),(-1,0)]
slopes = [".><",".<>",".v^",".^v"]

M = {(i,j):c for i,line in enumerate(data) for j, c in enumerate(line)}
S = (0,next(i for i,c in enumerate(data[0]) if c=='.'))
E = (n-1,next(i for i,c in enumerate(data[-1]) if c=='.'))

visited = {S}
stack = [(S,i) for i,di in enumerate(dirs) if tadd(S,di) in M and M[tadd(S,di)] in '.<>^v']
graphs = [nx.DiGraph(), nx.Graph()]
while len(stack):
    start,direction = stack.pop()
    prev, cpos, le = start, tadd(start,dirs[direction]), 1
    visited.add(cpos)
    way = slopes[direction].index(M[cpos])
    ndirs = [(i,npos in visited) for i,di in enumerate(dirs)
             for npos in [tadd(cpos,di)] if npos in M and M[npos] != '#']
    while len(ndirs) == 2:
        direction = next(di for di,_ in ndirs if prev != tadd(cpos,dirs[di]))
        prev, cpos, le = cpos, tadd(cpos,dirs[direction]), le+1
        way |= slopes[direction].index(M[cpos])
        visited.add(cpos)
        ndirs = [(i,npos in visited) for i,di in enumerate(dirs)
                 for npos in [tadd(cpos,di)] if npos in M and M[npos] != '#']
    if way == 1: graphs[0].add_edge(start, cpos, cost=le)
    else: graphs[0].add_edge(cpos, start, cost=le)
    graphs[1].add_edge(start, cpos, cost=le)

    for di in [di2 for di2,vis in ndirs if not(vis)]: stack.append((cpos,di))

for i,graph in enumerate(graphs[:1],1):
    res = max(nx.path_weight(graph, path, "cost") for path in nx.all_simple_paths(graph, S, E))
    print("Part%d: %d" % (i,res))


import matplotlib.pyplot as plt

G = nx.convert_node_labels_to_integers(graphs[1], first_label=0, ordering='default', label_attribute=None)
pos = nx.spring_layout(G, seed=1)  # positions for all nodes - seed for reproducibility
nx.draw_networkx_nodes(G, pos, node_size=200, node_color = "white", edgecolors= "black")
nx.draw_networkx_edges(G, pos, width=1)
nx.draw_networkx_labels(G, pos, font_size=5, font_family="sans-serif", labels={l:("S" if l==0 else "D" if l==35 else str(l)) for l in G.nodes()})
edge_labels = nx.get_edge_attributes(G, "cost")
nx.draw_networkx_edge_labels(G, pos, edge_labels, font_size=5)

plt.axis("off")
plt.tight_layout()
plt.show()