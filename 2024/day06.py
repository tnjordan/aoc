#%%
from copy import deepcopy

f = 'data/day06.txt'

with open(file=f) as input:
    read_lines = input.readlines()
grid = [line.strip() for line in read_lines]
print('🐟 🎄 🦈')
#%%
grid = [list(g) for g in grid]

J = len(grid)
I = len(grid[0])

dirs = {
    '^': (-1,0),
    '>': (0,1),
    'v': (1,0),
    '<': (0,-1),
}

right_turn = {
    '^': '>',
    '>': 'v',
    'v': '<',
    '<': '^',
}

# find starting position
dir_pos = ('x',0,0)
for j,row in enumerate(grid):
    for d in dirs:
        if d in row:
            i = row.index(d)
            dir_pos = (d,j,i)
start = dir_pos
#%%
seen = set()
inside = True
while inside:
    d,j,i = dir_pos
    seen.add((j,i))
    dj, di = dirs[d]
    j_dj = j+dj
    i_di = i+di
    if 0 <= j_dj < J and 0 <= i_di < I:
        if grid[j_dj][i_di] == '#':
            d = right_turn[d]
            dir_pos = dir_pos = (d,j,i)
        else:
            dir_pos = (d,j_dj,i_di)
    else:
        inside = False
print(len(seen))
#%%
def loop_check(j_o,i_o,grid):
    if grid[j_o][i_o] != '.':
        return False  # position not valid for object
    
    grid = deepcopy(grid)
    grid[j_o][i_o] = '#'
    dir_pos = start
    seen = set()
    while True:
        d,j,i = dir_pos
        if dir_pos in seen:
            return True  # in a loop
        seen.add(dir_pos)
        dj, di = dirs[d]
        j_dj = j+dj
        i_di = i+di
        if 0 <= j_dj < J and 0 <= i_di < I:
            if grid[j_dj][i_di] == '#':
                d = right_turn[d]
                dir_pos = dir_pos = (d,j,i)
            else:
                dir_pos = (d,j_dj,i_di)
        else:
            return False  # outside grid

loop_positions = 0
for j_o in range(J):
    print(f'{j_o/J*100:.1f}%')
    for i_o in range(I):
        if loop_check(j_o,i_o,grid):
            loop_positions += 1
print(loop_positions)
#%%
