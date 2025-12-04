import aocd

def neighbours(i, j):
    return [(i, j - 1), (i - 1, j), (i, j + 1), (i + 1, j)]


def grow_region(grid, region, pos):
    region |= {pos}
    for n in neighbours(*pos):
        if n not in region and grid.get(n) == grid[pos]:
            region |= grow_region(grid, region, n)
    return region


explored = set()

regions = []
data = aocd.get_data(day=12, year=2024).splitlines()
grid = {(i,j):c for i,line in enumerate(data) for j,c in enumerate(line)}

for (i, j), c in grid.items():
    if (i, j) in explored:
        continue
    region = grow_region(grid, set(), (i, j))
    regions.append(region)
    explored |= region


def price(region):
    perim = sum(n not in region for pos in region for n in neighbours(*pos))
    return perim * len(region)


print(sum(price(region) for region in regions))


def diag(i, j):
    return [(i - 1, j - 1), (i - 1, j + 1), (i + 1, j + 1), (i + 1, j - 1)]


def price_2(region):
    corners = 0
    for pos in region:
        for c, s1, s2 in zip(
            diag(*pos), neighbours(*pos), [*neighbours(*pos)[1:], neighbours(*pos)[0]]
        ):
            if c in region:
                corners += s1 not in region and s2 not in region
            else:
                corners += (s1 in region) == (s2 in region)
    return len(region) * corners


print(sum(price_2(region) for region in regions))