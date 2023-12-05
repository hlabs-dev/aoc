import aocd
data = aocd.get_data(day=5, year=2023).split("\n\n")

seeds = list(map(int,data[0].split()[1:]))
part1 = [(seed,seed+1) for seed in seeds]
part2 = [(seeds[2*i],seeds[2*i]+seeds[2*i+1])
         for i in range(len(seeds)//2)]

def desc2trans(desc): return [ (src,src+length,dest-src)
           for line in desc.split('\n')[1:]
           for dest,src,length in [map(int,line.split())]]

def step(s2,transitions):
    ret = []
    for sta,sto in s2:
        for start, stop, delta in transitions:
            if start <= sta < stop:
                ret.append((sta+delta,min(sto,stop)+delta))
                sta, sto = min(sto,stop), sto
        if sta<sto: ret.append((sta,sto))
    return ret

for desc in data[1:]:
    transitions = sorted(desc2trans(desc))
    part1 = step(part1,transitions)
    part2 = step(part2,transitions)

print("part1:",min(part1)[0],"part2:",min(part2)[0])