import aocd
from collections import Counter

data = aocd.get_data(day=7, year=2023).split('\n')

def parse(s, part):
    cards = ['23456789TJQKA', 'J23456789TQKA']
    hand, bid = s.split()
    
    bid,cnt = int(bid), Counter(hand)
    
    if part == 2: js, cnt['J'] = cnt['J'], 0
    else: js = 0

    v = list(sorted(cnt.values(), reverse=True))
    v[0] += js
    return (v,tuple(map(cards[part-1].index,hand)),bid)

for part in [1,2]:
    T = sorted(map(lambda l:parse(l,part),data))
    res = sum( i*h[2] for i,h in enumerate(T[::],start=1) )
    print("Part"+str(part)+":",res)