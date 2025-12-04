import aocd
import numpy as np

input = aocd.get_data(day=4, year=2025)

mt = np.matrix([[c=="@" for c in line] for line in input.splitlines()])
h, w = mt.shape

def removable_rolls(mt):
    t = np.zeros((h,w))
    t[:h-1,:w-1] += mt[1:,1:]
    t[1:,1:] += mt[:h-1,:w-1]

    t[:h-1,:] += mt[1:,:]
    t[1:,:] += mt[:h-1,:]

    t[:,1:] += mt[:,:w-1]
    t[:,:w-1] += mt[:,1:]

    t[:h-1,1:] += mt[1:,:w-1]
    t[1:,:w-1] += mt[:h-1,1:]
    return np.logical_and((t<4),mt)

rm = removable_rolls(mt)
rm_size = np.matrix.sum(rm)
part1 = part2 = rm_size
while rm_size:
    mt = np.logical_xor(rm, mt)
    rm = removable_rolls(mt)
    rm_size = np.matrix.sum(rm)
    part2 += rm_size

print("Part1:",part1,"Part2:",part2)