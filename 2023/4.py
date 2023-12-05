import aocd
data = aocd.get_data(day=4, year=2023).splitlines()

part1, part2, n, cards = 0, 0, len(data), [1]*len(data)

for i, row in enumerate(data):
    win, hand = row.split(':')[1].split("|")
    match = len(set(win.split()).intersection(hand.split()))
    if match >= 1: part1 += 2**(match-1)
    for j in range(i+1, min(i+1+match, n)): cards[j] += cards[i]
    part2 += cards[i]

print("part1:", part1, "part2:", part2)