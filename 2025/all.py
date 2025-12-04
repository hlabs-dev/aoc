import time
import aocd
import numpy

def devnull(*args): return
iter = 200
START = time.time_ns()
res = []

for mday in range(1,5):
    start2 = time.time_ns()
    for _ in range(iter):       
        with open("2025/"+str(mday)+".py") as f:
            for _ in range(1):
                exec(f.read(),{"print": devnull})
    res.append(((time.time_ns()-start2)/1e9/iter, mday))
    print(mday, ":", res[-1][0])
    #print(">>>", (time.time_ns()-START)/1e9)
print(">>>", (time.time_ns()-START)/1e9/iter)
res.sort(reverse=True)
for ti,idx in res:
    print(idx,":",ti)