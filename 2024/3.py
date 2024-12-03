import re, aocd

data = aocd.get_data(day=3, year=2024)
part1, part2, m = 0, 0, 1

for ma in re.finditer("mul\\(([\\d]{1,3}),([\\d]{1,3})\\)|(do\\(\\))|(don't\\(\\))", data):
    if ma.group(0) == "do()": m = 1
    elif ma.group(0) == "don't()": m = 0
    else:
        part1 += int(ma.group(1)) * int(ma.group(2))
        part2 += int(ma.group(1)) * int(ma.group(2)) * m
print("part1:", part1, "part2:", part2)
