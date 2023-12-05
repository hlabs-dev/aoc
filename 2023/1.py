import aocd
data = aocd.get_data(day=1, year=2023)
T = data.split()

trans = {'one':'o1e', 'two':'t2o', 'three':'3e', 'four':'4',
         'five':'5e', 'six':'6', 'seven':'7n', 'eight':'e8t',
         'nine':'n9e'}

def tr(x):
    for s in trans: x = x.replace(s, trans[s])
    return x

def cal(x):
    l = [int(c) for c in x if c.isdigit()]
    return 10*l[0]+l[-1]

print("Part1:", sum(map(cal, T)), "Part2:",sum(map(cal, map(tr,T))))