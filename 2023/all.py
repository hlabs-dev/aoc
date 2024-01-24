import time
import aocd


START = time.time_ns()

def devnull(*args): return

for mday in range(22,23):
    start2 = time.time_ns()
    with open("2023/"+str(mday)+".py") as f:
        exec(f.read(),{"print": devnull})
    print(mday, ":", (time.time_ns()-start2)/1e9)
print(">>>", (time.time_ns()-START)/1e9)