#%%
from tabulate import tabulate
from itertools import product

f = 'data/day03.txt'
# f = 'data/day03.ex'

with open(file=f) as input:
    read_lines = input.readlines()
read_lines = [line.strip() for line in read_lines]
print('❄️⛄❄️')
#%%
engine = []
for line in read_lines:
    new_line = []
    part_number = []
    for c in line:
        if c.isdigit():
            part_number.append(c)
            continue
        if part_number:
            for _ in range(len(part_number)):
                new_line.append(int(''.join(part_number)))
            part_number = []
        if c == '.':
            c = '.'  # for easier 🐛 creation use ''
        new_line.append(c)
    if part_number:  # this was my 🦋
        for _ in range(len(part_number)):
            new_line.append(int(''.join(part_number)))
    engine.append(new_line)
print(tabulate(engine))
#%%
directions = list(product([-1, 0, 1], repeat=2))
directions.remove((0, 0))

engine_parts_list = []
engine_sum = 0
last_part = None
gears = {}
for j, row in enumerate(engine):
    last_part = None
    for i, part in enumerate(row):
        if isinstance(part, str):
            last_part = None
        if isinstance(part, int) and part != last_part:
            for d_i, d_j in directions:
                i_star = i + d_i
                j_star = j + d_j
                if j_star < 0 or j_star >= len(engine):
                    continue
                if i_star < 0 or i_star >= len(row):
                    continue
                if engine[j_star][i_star] != '.' and not isinstance(engine[j_star][i_star], int) and last_part != part:
                    engine_sum += part
                    # print(f'counting part {part} at {j} {i}')
                    # print(f'\tadjacent part {engine[j_star][i_star]} {d_j} {d_i} at {j_star} {i_star}')
                    last_part = part
                    engine_parts_list.append(part)
                    if engine[j_star][i_star] == '*':
                        if gears.get((j_star, i_star), 0) != 0:
                            count, ratio = gears[(j_star, i_star)]
                            gears[(j_star, i_star)] = (count + 1, ratio * part)
                        else:
                            gears[(j_star, i_star)] = (1, part)
print(f'engine parts sum: {engine_sum}')

gear_ratio = 0
for k, v in gears.items():
    if v[0] == 2:
        gear_ratio += v[1]
print(f'gondola gear ratio: {gear_ratio}')
#%%
