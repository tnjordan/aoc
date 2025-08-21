#%%
from collections import defaultdict
from itertools import islice, product

f = 'data/day03.txt'

with open(file=f) as input:
    read_lines = input.readlines()
read_lines = [line.strip() for line in read_lines]
print('❄️⛄❄️')
#%%
input = int(read_lines[0])

def dir_change(dir_idx):
    dir_idx = (dir_idx + 1)%4
    # print(f'going {dirs[dir_idx]} {["➡️","⬆️","⬅️","⬇️"][dir_idx]}')
    return dir_idx

max_row = 0
min_row = 0
r = 0
max_column = 0
min_column = 0
c = 0
spiral = {1:(0,0)}
directions = {'right':(1,0),'up':(0,1),'left':(-1,0),'down':(0,-1)}
dirs = list(directions.keys())
dir_idx = 0
for point in range(2,input+1):
    d_c,d_r=directions[dirs[dir_idx]]
    c += d_c
    r += d_r
    if c > max_column:
        max_column += 1
        dir_idx = dir_change(dir_idx)
    elif c < min_column:
        min_column -= 1
        dir_idx = dir_change(dir_idx)
    elif r > max_row:
        max_row += 1
        dir_idx = dir_change(dir_idx)
    elif r < min_row:
        min_row -= 1
        dir_idx = dir_change(dir_idx)
    spiral[point] = (c,r)
distance = sum([abs(k2) for k2 in spiral[input]])
print(f'distance: {distance}')
#%%
#! part 2
values = defaultdict(int)
values[(0,0)] = 1  # init the origin
neighbors = list(product([1,0,-1],repeat=2))
neighbors.remove((0,0))
for k,v in spiral.items():  #islice(spiral.items(),23):
    c,r = v
    for d_c,d_r in neighbors:
        values[v] += values[(c+d_c, r+d_r)]
    if values[v] > input:
        print(f'next larger value: {values[v]}')
        break

#%%
print()
print('⭐⭐')
