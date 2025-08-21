#%%
import numpy as np
from tabulate import tabulate

f = 'data/day15.txt'

with open(file=f) as input:
    read_lines = input.readlines()
read_lines = [li.strip() for li in read_lines]
print('🎅 🎄 🤶')
#%%
board = []
cols = len(read_lines)  #* y, first coord
rows = len(read_lines[0])  #* x, second coord

elves = []
goblins = []

for j, c in enumerate(read_lines):
    for i, r in enumerate(c):
        if r == 'E':
            elves.append([j, i, 300])
            board.append(0)
        elif r == 'G':
            goblins.append([j, i, 300])
            board.append(0)
        elif r == '.':
            board.append(0)
        else:
            board.append(1e2)  #* increase if needed 1e6

board = np.array(board).reshape((cols, rows))

def nex_move(player1, bad_guys):
    y,x,_ = player1
    # Create a 32x32 grid
    grid = np.indices((cols, rows)).transpose(1, 2, 0)  #? gpt

    given_point = np.array([y, x])

    # Calculate the Manhattan distance from the given point to every other point
    manhattan_distances = np.sum(np.abs(grid - given_point), axis=-1)
    
    min_man = float('inf')
    min_man_coords = []
    for (y_bad, x_bad, _) in bad_guys:
        for (dy, dx) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  #* up, down, left, right
            if 0 <= y_bad + dy < cols and 0 <= x_bad + dx < rows:
                man_d = manhattan_distances[y_bad + dy][x_bad + dx]
                if man_d < min_man:
                    min_man = man_d
                    min_man_coords = [(y_bad + dy, x_bad + dx)]
                elif man_d == min_man:
                    min_man_coords.append((y_bad + dy, x_bad + dx))
    manhattan_distances += board.astype(int)  #* add the board
    return manhattan_distances

#%%
# print()
# print('⭐ ⭐')
