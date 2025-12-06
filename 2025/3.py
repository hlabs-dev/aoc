import aocd

def getjolt(batt,k):
    res, ret, cur, n = batt[-k:], 0, -1, len(batt)

    for i in range(len(batt)):
        while cur>=0 and res[cur]<batt[i] and n-i>=k-cur: cur -= 1
        if cur<k-1: res[cur+1], cur = batt[i], cur+1

    for v in res: ret = ret*10+v
    
    return ret

input = aocd.get_data(day=3, year=2025)
data = [[int(char) for char in line] for line in input.splitlines()]

print("Part1:",sum(map(lambda x:getjolt(x,2),data)),"Part1:",sum(map(lambda x:getjolt(x,12),data)))