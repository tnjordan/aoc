#%%
from tabulate import tabulate
from collections import deque

f = 'data/day10.txt'
# f = 'data/day10.ex'
# f = 'data/day10.ex2'
# f = 'data/day10.ex3'
# f = 'data/day10.ex4'
# f = 'data/day10.ex5'
f = 'data/day10.ex6'
# f = 'data/day10.ex7'

with open(file=f) as input:
    read_lines = input.readlines()
read_lines = [line.strip() for line in read_lines]
print('❄️⛄❄️')
#%%
connections = {}  # global variable for part 2

# add empty border, enables the flood of part 2 to inundate all sides
grid = []
grid.append('.' * (len(read_lines[0]) + 2))
for line in read_lines:
    grid.append('.' + line + '.')
grid.append('.' * (len(read_lines[0]) + 2))

R = len(grid)
C = len(grid[0])

# contained grid uses emojis, empty is ⬜, pipes are 🟥, and the flood is 🟦
contained_grid = [['⬜' for _ in range(C)] for _ in range(R)]

# pipes are a function which takes in a position and velocity and returns the next position and velocity
pipes = {
    '|': lambda j, i, dj, di: (j + dj, i + di, dj, di),
    '-': lambda j, i, dj, di: (j + dj, i + di, dj, di),
    'L': lambda j, i, dj, di: (j + di, i + dj, di, dj),
    'J': lambda j, i, dj, di: (j - di, i - dj, -di, -dj),
    '7': lambda j, i, dj, di: (j + di, i + dj, di, dj),
    'F': lambda j, i, dj, di: (j - di, i - dj, -di, -dj),
}

# find start:
for j, row in enumerate(grid):
    for i, c in enumerate(row):
        if c == 'S':
            start = (j, i)


def valid_next(j, i, dj, di):
    assert dj == 0 or di == 0
    pipe = grid[j][i]
    if pipe != 'S':
        j, i, dj, di = pipes[pipe](j, i, dj, di)
        next_pipe = grid[j][i]
    else:
        if j + dj >= 0 and j + dj < R and i + di >= 0 and i + di < C:
            next_pipe = grid[j + dj][i + di]
        else:
            return False
    if dj > 0:  # from the above
        valid_next_pipe = ['L', 'J', '|', 'S']
    elif dj < 0:  # from the below
        valid_next_pipe = ['7', 'F', '|', 'S']
    elif di > 0:  # from the left
        valid_next_pipe = ['7', 'J', '-', 'S']
    elif di < 0:  # from the right
        valid_next_pipe = ['F', 'L', '-', 'S']  # comma 🐛 ['F','L''-','S']
    if next_pipe in valid_next_pipe:
        return True
    return False


def pipe_step(j, i, dj, di):
    """takes in a position and velocity and returns the next position and velocity
    if the next position is valid, otherwise returns False"""
    pipe = grid[j][i]
    if valid_next(j, i, dj, di):
        j, i, dj, di = pipes[pipe](j, i, dj, di)
        return j, i, dj, di
    return False, False, False, False


def step_counter(start, velocity):
    """steps through the pipes from start and returns the number of steps taken.
    in my input, the start could only go in two directions, which were part of the loop.
    Updated for part 2 to keep track of the connections between pipes, since the start
    is run from both valid velocities, this function will run twice, making connections
    from a -> b and b -> a. Not efficient, but it works."""
    global contained_grid  # for part 2
    global connections  # for part 2

    j, i = start
    dj, di = velocity
    # determines if the start can connect to the next pipe in the velocity direction
    if not valid_next(j, i, dj, di):
        # print('start will not connect!')
        return False

    # fist step is manual based on input velocity
    # 'S' is not in the pipes dict, so it is handled manually
    # 'S' can be any of the pipe types.
    j += dj
    i += di
    p = grid[j][i]
    steps = 1

    # each valid pipe connects to two other pipes.
    if (j, i) in connections:
        connections[(j, i)].append((j - dj, i - di))
    else:
        connections[(j, i)] = [(j - dj, i - di)]

    while p != 'S' or steps == 0:  # run until you get back to the start
        steps += 1
        j, i, dj, di = pipe_step(j, i, dj, di)

        # returns False if you hit a dead end
        # not needed for working program, but useful expansion that could have been required
        # if the start connected to multiple valid pipes that were not part of the loop.
        if dj is False:
            return dj

        if (j, i) in connections:
            connections[(j, i)].append((j - dj, i - di))
        else:
            connections[(j, i)] = [(j - dj, i - di)]

        p = grid[j][i]
        contained_grid[j][i] = '🟥'  # fill pipes you have been through
    return steps


step_counts = []
j, i = start
for dj, di in [(1, 0), (-1, 0), (0, 1), (0, -1)]:  # initial velocity options for the start
    steps = step_counter(start, (dj, di))
    if steps is False:
        continue
    step_counts.append(steps)
print(f'🦊 max of {int(step_counts[0] / 2)} steps away')

#%%
#! part 2


def the_flood():
    flooded = deque()
    flooded.append((0, 0))  # start at origin, which is guaranteed to be empty because of the border
    flooded_gaps = deque()
    seen = set()
    seen_gaps = set()
    while flooded or flooded_gaps:
        # print(tabulate(contained_grid, tablefmt='plain'))
        if flooded:
            flood = flooded.popleft()
            j, i = flood

            contained_grid[j][i] = '🟦'  # the flood

            # check neighbors
            for dj, di in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if j + dj >= 0 and j + dj < R and i + di >= 0 and i + di < C:
                    j_dj = j + dj
                    i_di = i + di

                    if (j_dj, i_di) in seen:
                        continue
                    else:
                        seen.add((j_dj, i_di))

                    if contained_grid[j_dj][i_di] == '⬜':
                        flooded.append((j_dj, i_di))
                    elif contained_grid[j_dj][i_di] == '🟥':  # found a pipe
                        # check the gaps
                        # gaps to search determined by the direction (dj, di) the pipe was approached from the flood
                        # one of the directions will be 0, the other will be 1 or -1
                        if dj == 0:
                            dj_gap = [1, -1]
                        else:
                            dj_gap = [dj, dj]
                        if di == 0:
                            di_gap = [1, -1]
                        else:
                            di_gap = [di, di]

                        # these variable are only starting too get out of hand!
                        # checks the adjacent gaps (+1, -1) for flood spreading
                        for dj_g, di_g in zip(dj_gap, di_gap):
                            gap_j = j + dj_g
                            gap_i = i + di_g
                            # don't need to check out of bounds because of extra space for the flood
                            if contained_grid[gap_j][gap_i] == '🟥' or contained_grid[gap_j][gap_i] == '⬜':  # flood the whites to get the diagonals
                                if (gap_j, gap_i) not in connections[(j_dj, i_di)]:
                                    flooded_gaps.append(((j_dj, i_di), (gap_j, gap_i)))

        elif flooded_gaps:
            f_g = flooded_gaps.pop()
            a, b = f_g
            if (a, b) in seen_gaps:  # been there, done that
                continue
            seen_gaps.add((a, b))
            seen_gaps.add((b, a))  # don't bother with saving the fractions, just add both directions

            j = (a[0] + b[0]) / 2
            i = (a[1] + b[1]) / 2

            # find the fraction, it determines the direction of the gap
            if j % 1 == 0.5:
                dj = [0, 0]
                di = [-1, 1]
            elif i % 1 == 0.5:
                dj = [-1, 1]
                di = [0, 0]

            # check the 6 possible adjacent gaps for gap flood spreading
            for dj_g, di_g in zip(dj, di):

                a_j, a_i = a
                b_j, b_i = b

                a_j_dj_g = a_j + dj_g
                a_i_di_g = a_i + di_g
                a_g = (a_j_dj_g, a_i_di_g)

                b_j_dj_g = b_j + dj_g
                b_i_di_g = b_i + di_g
                b_g = (b_j_dj_g, b_i_di_g)

                # the 6 possible adjacent gaps options, determined by drawing
                # blue is current position, yellow is the gap, red are potential pipes
                #
                # 🟥🟨🟥🟨🟥
                # 🟨  🟦  🟨
                # 🟥🟨🟥🟨🟥
                # OR, depending on the direction of the gap
                # 🟥🟨🟥
                # 🟨  🟨
                # 🟥🟦🟥
                # 🟨  🟨
                # 🟥🟨🟥
    
                potential_gaps = [(a_g, b_g), (a, a_g), (b, b_g)]
                for gap in potential_gaps:
                    # flood the empty touched by the gap
                    for j_g, i_g in gap:
                        if contained_grid[j_g][i_g] == '⬜':
                            flooded.append((j_g, i_g))

                    a_g, b_g = gap
                    a_j_g, a_i_g = a_g
                    b_j_g, b_i_g = b_g

                    if contained_grid[a_j_g][a_i_g] == '🟥' and contained_grid[b_j_g][b_i_g] == '🟥':  # the gap is between two pipes
                        if (b_j_g, b_i_g) not in connections[(a_j_g, a_i_g)]:
                            flooded_gaps.append(((a_j_g, a_i_g),(b_j_g, b_i_g)))  # flood the gap


the_flood()
part_2 = 0
for row in contained_grid:
    part_2 += row.count('⬜')
print(f'🦊 could be hiding in {part_2} spaces')

#%%
print(tabulate(contained_grid, tablefmt='plain'))
#%%
