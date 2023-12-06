import aocd, math

data = aocd.get_data(day=6, year=2023).split('\n')
races = list(zip(*map(lambda line: list(map(int,line.split()[1:])), data)))
t,d = map(lambda line: int(line.split(":")[1].replace(" ","")), data)

def win(t,d): return(t-1-int((t-math.sqrt(t*t -4*d))/2)*2)
print("part1:", math.prod(win(t,d) for t,d in races), "part2:", win(t,d))