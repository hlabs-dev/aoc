import aocd
from ortools.linear_solver import pywraplp
import numpy as np
from itertools import combinations
from functools import reduce
from operator import xor

input = aocd.get_data(day=10, year=2025)

def parse(line):
    tokens = line.split(" ")
    target = list(map(int,tokens[-1][1:-1].split(",")))
    buttons = [ [1 if i in tokenlist else 0  for i in range(len(target))] 
               for token in tokens[1:-1] 
               for tokenlist in [list(map(int,token[1:-1].split(",")))]]
    buttons_t = list(zip(*buttons))
    lights_t =  sum(1<<i for i,c in enumerate(tokens[0][1:-1]) if c == "#")
    buttons_v = [ sum(1<<i if i in tokenlist else 0  for i in range(len(target))) 
                 for token in tokens[1:-1] 
                 for tokenlist in [list(map(int,token[1:-1].split(",")))]]
    
    return {"target":target, "buttons":buttons, "buttons_t":buttons_t,
            "line":line, "lights_t":lights_t, "buttons_v":buttons_v}

def solve2(A,b):
    b = np.array(b, dtype=int)
    A = np.array(A, dtype=int)
    m, n = A.shape
    solver = pywraplp.Solver.CreateSolver("CBC")
    x = [solver.IntVar(0, int(max(b)), f"x{i}") for i in range(n)]
    for i in range(m):
        solver.Add(sum(A[i, j] * x[j] for j in range(n)) == b[i])
    solver.Minimize(solver.Sum(x))
    solver.Solve()
    return round(solver.Objective().Value())

data = [parse(line) for line in input.splitlines()]

part1 = sum(next( len(li) for r in range(len(machine["buttons_v"])) 
                 for li in combinations(machine["buttons_v"],r+1) 
                 if reduce(xor,li) == machine["lights_t"]) for machine in data )
part2 = sum(solve2(machine["buttons_t"],machine["target"]) for machine in data )

print("Part1:",part1,"Part2:",part2)