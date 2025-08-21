#%%
from collections import defaultdict

f = 'data/day17.txt'

with open(file=f) as input:
    read_lines = input.readlines()
read_lines = [line.strip() for line in read_lines]
print('❄️⛄❄️')
#%%
active_cubes = set()
k = 0
for j, line in enumerate(read_lines):
    for i, c in enumerate(line):
        if c == '#':
            active_cubes.add((k,j,i))
for _ in range(6):
    checked_cubes = defaultdict(int)
    new_active_cubes = set()
    for cube in active_cubes:
        k,j,i = cube
        options = [-1,0,1]
        for dk in options:
            for dj in options:
                for di in options:
                    if dk == dj == di == 0:
                        continue
                    k_dk = k + dk
                    j_dj = j + dj
                    i_di = i + di
                    checked_cubes[(k_dk, j_dj, i_di)] += 1
    for checked_cube, activated_neighbors in checked_cubes.items():
        if checked_cube in active_cubes and 2 <= activated_neighbors <= 3:
            new_active_cubes.add(checked_cube)
        elif activated_neighbors == 3:
            new_active_cubes.add(checked_cube)
    active_cubes = new_active_cubes.copy()
print(len(active_cubes))
#%%
#* part 2: a copy paste with a fourth dimension
active_cubes = set()
w = 0
k = 0
for j, line in enumerate(read_lines):
    for i, c in enumerate(line):
        if c == '#':
            active_cubes.add((w, k,j,i))
for _ in range(6):
    checked_cubes = defaultdict(int)
    new_active_cubes = set()
    for cube in active_cubes:
        w, k,j,i = cube
        options = [-1,0,1]
        for dw in options:
            for dk in options:
                for dj in options:
                    for di in options:
                        if dw == dk == dj == di == 0:
                            continue
                        w_dw = w + dw
                        k_dk = k + dk
                        j_dj = j + dj
                        i_di = i + di
                        checked_cubes[(w_dw, k_dk, j_dj, i_di)] += 1
    for checked_cube, activated_neighbors in checked_cubes.items():
        if checked_cube in active_cubes and 2 <= activated_neighbors <= 3:
            new_active_cubes.add(checked_cube)
        elif activated_neighbors == 3:
            new_active_cubes.add(checked_cube)
    active_cubes = new_active_cubes.copy()
print(len(active_cubes))
#%%
