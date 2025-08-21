#%%
import re
from decimal import Decimal, getcontext

f = 'data/day13.txt'
# f = 'data/da13.ex'

with open(file=f) as input:
    read_lines = input.readlines()
read_lines = [line.strip() for line in read_lines]
print('🐟 🎄 🦈')
#%%
claws = []
for l in read_lines:
    digs = tuple(map(int,re.findall('(\d+)',l)))
    if 'Button A' in l:
        a = digs
    elif 'Button B' in l:
        b = digs
    elif 'Prize'in l:
        p = digs
    else:
        claws.append([a,b,p])
claws.append([a,b,p])  # boundaries +1
#%%
# x is i y is j

price_a = 3
price_b = 1

price_prizes = 0
for claw in claws:
    (ai,aj),(bi,bj),(pi,pj) = claw
    min_price = None
    for a_press in range(101):
        for b_press in range(101):
            i = a_press*ai + b_press*bi
            j = a_press*aj + b_press*bj
            if i == pi and j == pj:
                price = a_press*price_a + b_press*price_b
                if not min_price:
                    min_price = price
                min_price = min(price, min_price)
    if min_price:
        price_prizes += min_price
print(price_prizes)
#%%
getcontext().prec = 3

price_prizes = 0
for claw in claws:
    print(claw)
    (ai,aj),(bi,bj),(pi,pj) = claw
    pi += 10000000000000
    pj += 10000000000000

    if ai*bj == bi*aj:
        continue
    elif (ai,aj) == (bi,bj):
        print('edge case, use all b press if u can')
        assert False
    else:
        bp = (pj*ai - pi*aj)/(bj*ai - bi*aj)
        ap = (pi - bp*bi)/ai
        print(bp, ap)
        if bp >= 0 and ap >= 0 and (bp).is_integer() and (ap).is_integer():
            print('win!')
            price = ap*price_a + bp*price_b
            price_prizes += price
print(price_prizes)
#%%
