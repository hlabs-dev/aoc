import aocd
from functools import reduce

data = aocd.get_data(day=15, year=2023)
def hiter(c,ch): return (c+ord(ch))*17%256
def hash(s): return reduce(hiter,s,0)

print("Part1", sum(hash(s) for s in data.split(',')))

boxes = [dict() for _ in range(256)]
for s in data.split(','):
    label = s.strip('-').split('=')
    box = boxes[hash(label[0])]
    if len(label) == 1: box.pop(label[0],0)
    else: box[label[0]] = int(label[1])
        
print("Part2", sum(i*j*f for i,b in enumerate(boxes, 1)
                for j,f in enumerate(b.values(), 1)))