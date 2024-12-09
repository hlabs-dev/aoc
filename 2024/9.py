import aocd
from heapq import heapify, heappop, heappush
from collections import defaultdict

input = aocd.get_data(day=9, year=2024)
max_file = (len(input) - 1)//2

def addfile(addr, id, length, su): 
    return addr+length, su + id*length*(2*addr+length-1)//2

def part1():
    data = [int(c) for c in input]
    ret, idx, cur, cur_end = 0, 0, 0, max_file*2
    while cur<=cur_end:
        idx, ret = addfile(idx, cur//2, data[cur], ret)
        if cur == cur_end: break
        while data[cur+1]>0:
            swap = min(data[cur+1], data[cur_end])
            idx, ret = addfile(idx, cur_end//2, swap, ret)
            data[cur_end] -= swap
            data[cur+1] -= swap
            if data[cur_end] == 0: cur_end -= 2
        cur += 2
    return ret

def part2():
    data = [int(c) for c in input]
    moved = set()
    gaps, freeslots = defaultdict(list), defaultdict(list)

    for i in range(1,len(data),2):
        if data[i]: heappush(freeslots[data[i]],i)

    for i in range( max_file*2, -2, -2):
        _,slotsize = min(((freeslots[size][0], size) for size in range(data[i],10) 
                          if freeslots[size] and freeslots[size][0]<i), default=(0,0))
        if slotsize:
            idx = heappop(freeslots[slotsize])
            moved.add(i)
            heappush(gaps[idx],-i)
            if slotsize>data[i]: heappush(freeslots[slotsize-data[i]], idx)

    idx, ret = 0, 0

    for i in range(0,len(data),2):
        if i not in moved: idx, ret = addfile(idx, i//2, data[i], ret)
        else: idx += data[i]
        if i+1 == len(data): break

        nidx = idx + data[i+1]
        while gaps[i+1]:
            file = -heappop(gaps[i+1])
            idx, ret = addfile(idx, file//2, data[file], ret)
        idx = nidx
    return ret 

print("part1:",part1(),"part2:",part2())    
