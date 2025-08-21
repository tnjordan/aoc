#%%
f = 'data/day11.txt'
# f = 'data/day11.ex'

with open(file=f) as input:
    read_lines = input.readlines()
read_lines = [line.strip() for line in read_lines]
print('❄️⛄❄️')
#%%
g = []  # g -> grid
empty_rows = []
empty_cols = []
cols_with_things = set()
for j, line in enumerate(read_lines):
    n_g = []
    if '#' not in line:
        empty_rows.append(j)
    for i, v in enumerate(line):
        if v == '#':
            cols_with_things.add(i)
        n_g.append(v)
    g.append(n_g)

empty_cols = list(set(range(len(line))).difference(cols_with_things))

# add rows
exp_g = []
for j, row in enumerate(g):
    if j in empty_rows:
        exp_g.append(['.'] * len(row))
    exp_g.append(row)

# add columns
gg = []  # gg -> galaxy grid, expanded rows and columns for part 1
for j, row in enumerate(exp_g):
    n_g = []
    for i, v in enumerate(row):
        if i in empty_cols:
            n_g.append('.')
        n_g.append(v)
    gg.append(n_g)

galaxies = set()
for j, row in enumerate(gg):
    for i, v in enumerate(row):
        if v == '#':
            gg[j][i] = (j, i)
            galaxies.add((j, i))

pairs = set()
while galaxies:
    a = galaxies.pop()
    for b in galaxies:
        pairs.add((a, b))


def min_distance(pair):
    a,b = pair
    a_j, a_i = a
    b_j, b_i = b
    return abs(a_j - b_j) + abs(a_i - b_i)


part_1 = 0
for pair in pairs:
    part_1 += min_distance(pair)
print(f'🌌 are {part_1} apart')

#%%
#! part 2
# galaxies in the original grid coordinate system
galaxies = set()
for j, row in enumerate(g):
    for i, v in enumerate(row):
        if v == '#':
            g[j][i] = (j, i)
            galaxies.add((j, i))

pairs = set()
while galaxies:
    a = galaxies.pop()
    for b in galaxies:
        pairs.add((a, b))


def min_distance_expansion(pair):
    a,b = pair
    a_j, a_i = a
    b_j, b_i = b
    d = abs(a_j - b_j) + abs(a_i - b_i)
    row_adder = 0
    for v in empty_rows:
        x, y = min(a_j, b_j), max(a_j, b_j)
        if x < v < y:
            row_adder += 1
    col_adder = 0
    for v in empty_cols:
        x, y = min(a_i, b_i), max(a_i, b_i)
        if x < v < y:
            col_adder += 1
    d += (row_adder + col_adder) * (1_000_000 - 1)
    return d


part_2 = 0
for pair in pairs:
    part_2 += min_distance_expansion(pair)
print(f'🌌 are {part_2} apart')
#%%
