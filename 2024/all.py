import time
import aocd
from itertools import combinations

START = time.time_ns()

def devnull(*args): return

for mday in range(1,3):
    start2 = time.time_ns()
    with open("2024/"+str(mday)+".py") as f:
        for _ in range(1):
            exec(f.read(),{"print": devnull})
    print(mday, ":", (time.time_ns()-start2)/1e9)
print(">>>", (time.time_ns()-START)/1e9)