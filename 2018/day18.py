#%%
from tabulate import tabulate
from copy import deepcopy

f = 'data/day18.txt'
# f = 'data/day18.ex'

with open(file=f) as input:
    read_lines = input.readlines()
read_lines = [l.strip() for l in read_lines]
print('🎅 🎄 🤶')
#%%
grid = []
for line in read_lines:
    grid.append(list(line))

# print(f'minute: {0}')
# print(tabulate(grid, tablefmt='plain'))
# print()

neighbor_dir = [(0,1), (0,-1), (1,0), (-1,0), (1,1), (-1,-1), (1,-1), (-1,1)]

for m in range(10):
    new_grid = deepcopy(grid)
    for j in range(len(grid)):
        for i in range(len(grid[j])):
            neighbors = []
            for dy, dx in neighbor_dir:
                if 0 <= i+dx < len(grid[0]) and 0 <= j+dy < len(grid):
                    neighbors.append(grid[j+dy][i+dx])
            if grid[j][i] == '.':
                if neighbors.count('|') >= 3:
                    new_grid[j][i] = '|'
            elif grid[j][i] == '|':
                if neighbors.count('#') >= 3:
                    new_grid[j][i] = '#'
            elif grid[j][i] == '#':
                if neighbors.count('#') < 1 or neighbors.count('|') < 1:
                    new_grid[j][i] = '.'
    # print(f'minute: {m+1}')
    # print(tabulate(new_grid, tablefmt='plain'))
    # print()
    grid = deepcopy(new_grid)

print(f'count: {sum([l.count("|") for l in new_grid]) * sum([l.count("#") for l in new_grid])}')
#%%
#! part 2

# reset grid
grid = []
for line in read_lines:
    grid.append(list(line))

# find the repeating cycle
seen = []
for m in range(1000):
    new_grid = deepcopy(grid)
    for j in range(len(grid)):
        for i in range(len(grid[j])):
            neighbors = []
            for dy, dx in neighbor_dir:
                if 0 <= i+dx < len(grid[0]) and 0 <= j+dy < len(grid):
                    neighbors.append(grid[j+dy][i+dx])
            if grid[j][i] == '.':
                if neighbors.count('|') >= 3:
                    new_grid[j][i] = '|'
            elif grid[j][i] == '|':
                if neighbors.count('#') >= 3:
                    new_grid[j][i] = '#'
            elif grid[j][i] == '#':
                if neighbors.count('#') < 1 or neighbors.count('|') < 1:
                    new_grid[j][i] = '.'
    grid = deepcopy(new_grid)
    seen.append(grid)
    if grid in seen[:-1]:
        cycle_at = len(seen)
        cycle_start = seen.index(grid) + 1  #* issue was index is not min. index starts at 0 min starts at 1.
        cycle_length = cycle_at - cycle_start
        print(f'cycle at: {cycle_at} repeat: {cycle_start} length: {cycle_length}')
        break

# calculate the remaining runs. grid is at cycle_start so we can skip n cycles and just do the remaining runs
runs = (1000000000 - cycle_at) // cycle_length
remaining_runs = (1000000000 - cycle_length * (runs)) - cycle_at
for i in range(remaining_runs):
    new_grid = deepcopy(grid)
    for j in range(len(grid)):
        for i in range(len(grid[j])):
            neighbors = []
            for dy, dx in neighbor_dir:
                if 0 <= i+dx < len(grid[0]) and 0 <= j+dy < len(grid):
                    neighbors.append(grid[j+dy][i+dx])
            if grid[j][i] == '.':
                if neighbors.count('|') >= 3:
                    new_grid[j][i] = '|'
            elif grid[j][i] == '|':
                if neighbors.count('#') >= 3:
                    new_grid[j][i] = '#'
            elif grid[j][i] == '#':
                if neighbors.count('#') < 1 or neighbors.count('|') < 1:
                    new_grid[j][i] = '.'
    grid = deepcopy(new_grid)

print(f'count: {sum([l.count("|") for l in new_grid]) * sum([l.count("#") for l in new_grid])}')

#%%
print()
print('⭐ ⭐')
