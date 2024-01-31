import aocd

g = [[ch for ch in row] for row in aocd.get_data(day=3, year=2023).split('\n')]
h, w = len(g), len(g[0])
dirs = [(1, -1), (-1, -1), (1, 1), (-1, 1), (1, 0), (-1, 0), (0, -1), (0, 1)]

nums, syms, realnums, cur = [], [], set(), -1

for i,line in enumerate(g):
    for j,c in enumerate(line):
        if c.isdigit():
            if cur == -1: cur = int(c)
            else: cur = cur*10+int(c)
            g[i][j] = len(nums)
        else:
            if cur >= 0:
                nums.append(cur)
                cur = -1
            if c != ".":
                syms.append((i,j))
    if cur >= 0: nums.append(cur)

part2 = 0
for i,j in syms:
    snums = { g[i+di][j+dj] for di,dj in dirs if 0<=i+di<h and 0<=j+dj<w  and isinstance(g[i+di][j+dj], int)}
    realnums |= snums
    if g[i][j] == '*' and len(snums) == 2:
        n1, n2 = snums
        part2 += nums[n1]*nums[n2]

print("Part1:", sum(nums[idx] for idx in realnums), "Part2:", part2)