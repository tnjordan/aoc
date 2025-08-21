#%%
from tabulate import tabulate

f = 'data/day14.txt'
# f = 'data/day14.ex'

with open(file=f) as input:
    read_lines = input.readlines()
c = [line.strip() for line in read_lines]
print('❄️⛄❄️')
#%%
R = len(read_lines)
C = len(read_lines[0])

grid =  {}
for j, row in enumerate(read_lines):
    for i, c in enumerate(row):
        if c != '.':
            grid[(j,i)] = c


# roll up
def roll_up(grid):
    """roll the rounds stones (O) to the top of the grid"""
    new_grid = {}
    for i in range(C):
        fall_up = 0
        for j in range(R):
            if (j,i) in grid:
                c = grid[(j,i)]
                if c == '#':
                    new_grid[(j,i)] = '#'
                    fall_up = j+1
                if c == 'O':
                    # going up
                    new_grid[(fall_up, i)] = 'O'
                    fall_up += 1
    return new_grid


def calc_moment(grid):
    moment = 0
    for (j,i), r in grid.items():
        if r == 'O':
            moment +=  R - j
    return moment

#! part 1
print(f'🪨 moment: {calc_moment(roll_up(grid))}')

#! part 2

def rotate(grid):
    """rotates clockwise, N -> W -> S -> E are
    clockwise rotations to put the next direction
    at the top. rotation is done by transposing
    and reversing the columns. Note was (j,i) 
    transpose is (i,j), the reverse of the column
    is a reverse of j, which was the row but after
    the transpose is the column."""
    new_grid = {}
    for (j,i), c in grid.items():
        # transpose 
        # and reverse col
        new_grid[(i,R-j-1)] = c
    return new_grid


def print_grid(grid):
    """when you save your grid as a dict you need to convert
    it back to a table to see what is happening"""
    grid_rot = []
    for j in range(R):
        g_r = []
        for i in range(C):
            if (j,i) in grid:
                c = grid[(j,i)]
            else:
                c = '.'
            g_r.append(c)
        grid_rot.append(g_r)
    print(tabulate(grid_rot, tablefmt='plain'),'\n')


def cycle(grid):
    # 4 rotations
    for i in range(4):
        # print(f'going up i:{i}')
        grid = roll_up(grid)
        # print_grid(grid)
        # print('rotate grid')
        grid = rotate(grid)
        # print_grid(grid)
    return grid


seen_g = []
skip = False
c = 0
while c <  1000000000:  #! 🦂 I should copy paste the large number 1000000 != 1000000000
    c += 1
    grid = cycle(grid)

    if skip is False:
        if grid in seen_g:
            print(f'repeat! at {c}')
            idx = seen_g.index(grid) + 1
            print(f'prev seen at {idx}')
            grid_cycle = c - idx
            print(f'grid cycles in {grid_cycle}')
            print(f'fast forward {(1000000000-c)//grid_cycle * grid_cycle} cycles')
            c += (1000000000-c)//grid_cycle * grid_cycle
            print(f'cycle now at {c}')
            skip = True
        else:
            seen_g.append(grid)


moment = calc_moment(grid)
print(f'🧭 🪨 moment: {moment}')

#%%
# code to verify the rotation
# only works with squares

grid_raw = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
R = len(grid_raw)
C = len(grid_raw[0])
print(tabulate(grid_raw, tablefmt='plain'),'\n')
# encode grid
grid =  {}
for j, row in enumerate(grid_raw):
    for i, c in enumerate(row):
            grid[(j,i)] = c
for i in range(4):
    print('⤵️')
    grid = rotate(grid)
    grid_rot = []
    for j, row in enumerate(range(R)):
        g_r = []
        for i, c in enumerate(range(C)):
            c = grid[(j,i)]
            g_r.append(c)
        grid_rot.append(g_r)
    print(tabulate(grid_rot, tablefmt='plain'),'\n')
#%%
