#%%
from tabulate import tabulate
import re

f = 'data/day08.txt'

with open(file=f) as input:
    read_lines = input.readlines()
read_lines = [li.strip() for li in read_lines]
print('🎅 🎄 🤶')
#%%
screen = [[0] * 50 for _ in range(6)]
# print(tabulate(screen))


def rect(a, b):
    for i in range(a):
        for j in range(b):
            screen[j][i] = 1


def rotate_row(a, b):
    current_row = screen[a]
    new_row = [0] * len(current_row)
    for i, v in enumerate(current_row):
        new_row[(i + b) % len(current_row)] = v
    screen[a] = new_row


def rotate_column(a, b):
    current_col = [r[a] for r in screen]
    new_col = [0] * len(current_col)
    for i, v in enumerate(current_col):
        new_col[(i + b) % len(current_col)] = v
    for i, r in enumerate(screen):
        r[a] = new_col[i]


command_map = {'rect': rect, 'rotate row': rotate_row, 'rotate col': rotate_column}
for li in read_lines:
    digits = [int(x) for x in re.findall(r'\d+', li)]
    for c, f in command_map.items():
        if c in li:
            f(*digits)


print(f'🔳💡:{sum([sum(r) for r in screen])}')

#! part 2
print(tabulate([['X' if x == 1 else ' ' for x in k2] for k2 in screen]))

#%%
print()
print('⭐ ⭐')
