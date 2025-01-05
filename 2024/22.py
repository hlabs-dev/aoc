import numpy as np
import aocd

def day22():
    data = [int(line) for line in aocd.get_data(day=22, year=2024).splitlines()]
    npa = np.array(data)
    base = [npa%10]
    col = np.zeros(19**4, dtype=np.uint16)
    mo = 19**4
    for i in range(2000):
        npa ^= (npa << 6) & 16777215
        npa ^= npa >> 5
        npa ^= (npa << 11) & 16777215
        base.append(npa%10)
    base = np.array(base).T
    diff = base[:,:-1]-base[:,1:]+9
    for i,row in enumerate(diff):
        cv = row[:-3]+row[1:-2]*19+row[2:-1]*19**2+row[3:]*19**3
        unique_values, first_indices = np.unique(cv, return_index=True)
        np.add.at(col, unique_values, base[i][first_indices+4])
    print("part1:",sum(npa.astype(np.uint64)),"part2:",max(col))

day22()
