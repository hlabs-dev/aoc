from multiprocessing import Pool
import aocd, time
"""12: garden groups"""
from collections import deque

NORTH = 1
EAST = 4
SOUTH = 16
WEST = 64

# Corner checking BS
UL = NORTH | WEST
UR = NORTH | EAST
LL = SOUTH | WEST
LR = SOUTH | EAST

DIRS = [
    (-1, 0, NORTH),
    (0, 1, EAST),
    (1, 0, SOUTH),
    (0, -1, WEST),
]


class Solver():
    def __init__(self, input: str):

        grid = list(input.strip().split("\n"))
        height = len(grid)

        seen_grid = [0] * height
        cur = deque([])

        self.p1 = 0
        self.p2 = 0

        for gr in range(height):
            for gc in range(height):
                if not contains(seen_grid, gr, gc):
                    corners = 0
                    perimeter = 0
                    area = 0
                    v = grid[gr][gc]
                    cur.append((gr, gc))
                    insert(seen_grid, gr, gc)
                    while cur:
                        r, c = cur.popleft()

                        area += 1

                        num_edges = 4
                        dir_map = 0

                        for dr, dc, dir in DIRS:
                            nr = r + dr
                            nc = c + dc

                            if nr < 0 or nr >= height or nc < 0 or nc >= height:
                                continue

                            nv = grid[nr][nc]

                            if nv == v:
                                dir_map |= dir

                                num_edges -= 1
                                if not contains(seen_grid, nr, nc):
                                    insert(seen_grid, nr, nc)
                                    cur.append((nr, nc))

                        # upper left
                        ul = dir_map & UL
                        if ul == 0 or (ul == UL and grid[r - 1][c - 1] != v):
                            corners += 1

                        # upper right
                        ur = dir_map & UR
                        if ur == 0 or (ur == UR and grid[r - 1][c + 1] != v):
                            corners += 1

                        # lower left
                        ll = dir_map & LL
                        if ll == 0 or (ll == LL and grid[r + 1][c - 1] != v):
                            corners += 1

                        # lower right
                        lr = dir_map & LR
                        if lr == 0 or (lr == LR and grid[r + 1][c + 1] != v):
                            corners += 1

                        perimeter += num_edges

                    self.p1 += perimeter * area

                    # corners is equal to sides
                    self.p2 += corners * area

    def part_one(self) -> int:
        return self.p1

    def part_two(self) -> int:
        return self.p2


def contains(seen_grid, r, c) -> bool:
    return seen_grid[r] & 1 << c != 0


def insert(seen_grid, r, c):
    seen_grid[r] |= 1 << c


if __name__ == '__main__':
    STARTO = time.time_ns()
    solver = Solver(aocd.get_data(day=12, year=2024))
    print(solver.part_one())
    print(solver.part_two())
    print(">>>", (time.time_ns()-STARTO)/1e9)