import aocd

keys, locks = [],[]
for key in aocd.get_data(day=25, year=2024).split("\n\n"):
    [keys,locks][key[0] == '.'].append(sum((c=="#")*(1<<(i-i//6)) for i,c in enumerate(key[6:-6])))
    
print("part1:", sum(k & l == 0 for k in keys for l in locks))