import aocd
import numpy as np

def day22():
    data = [int(line) for line in aocd.get_data(day=22, year=2024).splitlines()]
    UNIQUE_SEQUENCES = 19**4
    npa = np.array(data, dtype=np.uint32)
    prev = npa%10
    base = [prev]
    cv = []
    col = np.zeros(UNIQUE_SEQUENCES, dtype=np.uint32)
    
    for i in range(2000):
        npa ^= (npa << 6) & 16777215
        npa ^= npa >> 5
        npa ^= (npa << 11) & 16777215
        curr = npa%10
        delta = curr-prev+9
        prev = curr
        if i == 0: roll = delta
        else: roll = (roll*19 + delta)% UNIQUE_SEQUENCES
        if i>3:
            base.append(curr)
            cv.append(roll)
        prev = curr
    base = np.array(base).T
    cv = np.array(cv).T
    for a,b in zip(cv,base):
        unique_values, first_indices = np.unique(a, return_index=True)
        np.add.at(col, unique_values, b[first_indices+1])
    print("part1:",sum(npa.astype(np.uint64)),"part2:",max(col))

day22()