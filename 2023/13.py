import aocd
data = aocd.get_data(day=13, year=2023)
patts = [line.split() for line in data.split("\n\n")]

def eval(pat, s, rot):
    if rot: pat = tuple(zip(*pat))
    return(next((i for i in range(1,len(pat))
                if sum(t!=b for lt,lb in zip(pat[i-1::-1],pat[i:])
                       for t,b in zip(lt,lb)) == s),0))
for s in range(2):
    print("Part%d: %d"% ((s+1,sum(eval(pat, s, True)+
                                  100*eval(pat, s, False)
                                  for pat in patts))))