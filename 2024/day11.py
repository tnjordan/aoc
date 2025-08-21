#%%
from collections import defaultdict
f = 'data/day11.txt'

with open(file=f) as input:
    read_lines = input.readlines()
read_lines = [line.strip() for line in read_lines]
print('🐟 🎄 🦈')
#%%
rocks = [int(r) for r in read_lines[0].split()]

def blink(rocks):
    blink_rocks = []
    for r in rocks:
        if r == 0:
            blink_rocks.append(1)
        elif len(str(r))%2 == 0:
            mid = len(str(r))//2  # mid must be int so //
            blink_rocks.append(int(str(r)[:mid]))
            blink_rocks.append(int(str(r)[mid:]))
        else:
            blink_rocks.append(r*2024)
    return blink_rocks

for _ in range(25):
    rocks = blink(rocks)
print(len(rocks))
#%%
# # because you should try
# for _ in range(50):  # need an improved approach
#     rocks = blink(rocks)
#     print(len(rocks))
#%%
rocks = [int(r) for r in read_lines[0].split()]
rocks_sum = defaultdict(int)
for r in rocks:
    rocks_sum[r] += 1

def blink_sum(rocks_sum):
    blink_rocks_sum = defaultdict(int)
    for r,c in rocks_sum.items():
        if r == 0:
            blink_rocks_sum[1] += c
        elif len(str(r))%2 == 0:
            mid = len(str(r))//2  # mid must be int so //
            lef = int(str(r)[:mid])
            righ = int(str(r)[mid:])
            blink_rocks_sum[lef] += c
            blink_rocks_sum[righ] += c
        else:
            blink_rocks_sum[r*2024] += c
    return blink_rocks_sum

for _ in range(75):
    rocks_sum = blink_sum(rocks_sum)

sum(rocks_sum.values())
#%%
