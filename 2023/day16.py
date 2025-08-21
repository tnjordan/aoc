#%%
from tabulate import tabulate
from collections import deque

f = 'data/day16.txt'
# f = 'data/day16.ex'


with open(file=f) as input:
    read_lines = input.readlines()
read_lines = [line.strip() for line in read_lines]
print('❄️⛄❄️')
#%%
grid = []
for line in read_lines:
    grid.append(line)

R = len(grid)
C = len(grid[0])




def split_horziontal(j, i, dj, di):
    if dj != 0:
        assert di == 0
        return (j, i+dj, 0, dj), (j, i-dj, 0, -dj)
    else:
        return (j+dj, i+di, dj, di), (None)

def split_vertical(j, i, dj, di):
    if di != 0:
        assert dj == 0
        return (j+di, i, +di, 0), (j-di, i, -di, 0)
    else:
        return (j+dj, i+di, dj, di), (None)


mirrors_and_splitters = {
    # nothing just keep going
    '.': lambda j, i, dj, di: ((j + dj, i + di, dj, di),(None)),
    # inverse mirror - to +, + to -
    '\\': lambda j, i, dj, di: ((j + di, i + dj, di, dj),(None)),
    # same mirror + to +, - to -
    '/': lambda j, i, dj, di: ((j - di, i - dj, -di, -dj),(None)),
    '-': lambda j, i, dj, di: split_horziontal(j, i, dj, di),
    '|': lambda j, i, dj, di: split_vertical(j, i, dj, di),
}


start = (0,0,0,1)  # at (0,0) moving in the +i at 1
def light_it(start):
    # lit uses emojis, non-lit are ⬛, lit are ⬜
    lit = [['⬛' for _ in range(C)] for _ in range(R)]

    lit_q = deque()
    lit_q.append(start)
    seen = set()
    while lit_q:
        # print(tabulate(['⬛'*C]+grid+['⬛'*C]))
        # print(tabulate(lit, tablefmt='plain'))
        # print()
        new_lit = lit_q.popleft()
        j,i,dj,di = new_lit
        if  0 <= j < R and 0 <= i < C:
            lit[j][i] = '⬜'
            if new_lit in seen:
                continue
            else:
                seen.add(new_lit)
            a, b = mirrors_and_splitters[grid[j][i]](j,i,dj,di)
            lit_q.append(a)
            if b is not None:
                lit_q.append(b)
    part_1 = 0
    for row in lit:
        part_1 += row.count('⬜')
    return part_1

#%%
m = 0
for j,dj in [(0,1),(R,-1)]:
    for i in range(C):
        m = max(m, light_it((j,i,dj,0)))

for j,di in [(0,1),(C,-1)]:
    for j in range(R):
        m = max(m, light_it((j,i,0,di)))
print(m)

#%%
