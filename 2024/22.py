import aocd
import numpy as np

def day22():
    data = [int(line) for line in aocd.get_data(day=22, year=2024).splitlines()]
    npa = np.array(data, dtype=np.uint32)
    base = []
    col = np.zeros(19**4, dtype=np.uint32)
    
    for _ in range(2000):
        npa ^= (npa<<6)&16777215
        npa ^= npa>>5
        npa ^= (npa<<11)&16777215
        base.append(npa%10)

    base = np.stack(base[::-1], axis=1)
    prices = base % 10
    diffs = np.diff(prices, axis=1) + 9
    cv = sum(diffs[:, i : 2000 + i - 4]*(19**i) for i in range(4))

    for c,b in zip(cv,prices[:, :-4]): col[c] += b

    print ("part1:",sum(npa.astype(np.uint64)),"part2:",max(col))

day22()