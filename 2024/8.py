import aocd

data = aocd.get_data(day=7, year=2024)
data = [(int(a), list(map(int,b.split()))) 
        for line in data.splitlines() 
        for a,b in [line.split(":")] ]

def len10(x):
    t = 10
    while True:
        if x < t:
            return t
        t *= 10

def recur_test(nums, acc, part2=False) :
    if len(nums) == 0:
        return acc == 0

    *rest, last = nums

    if (acc >= last and recur_test(rest, acc - last, part2) ) :
        return True
    if (acc % last == 0 and recur_test(rest, acc // last, part2) ):
        return True
    if (part2 and acc % len10(last) == last and recur_test(rest, acc // len10(last), part2)):
        return True

res1 = (sum(res for res, nums in data if recur_test(nums, res, False)) )
res2 = (sum(res for res, nums in data if recur_test(nums, res, True)))
