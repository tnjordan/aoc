#%%
from collections import deque 
from tabulate import tabulate
import string

f = 'data/day12.txt'
# f = 'data/day12.ex'

with open(file=f) as input:
    read_lines = input.readlines()
map = [l.strip() for l in read_lines]
print('🎅 🎄 🤶')


for i,l in enumerate(map):
    try:
        S_pos = l.index('S')
        start = (i,S_pos)
        map[i] = l.replace('S','a')
    except ValueError:
        pass

for i,l in enumerate(map): #* 🐛 🐝 🐞 🐜 🕷 🦗 🦟 🦋 loop through 2x because start and end on same line
    try:
        Z_pos = l.index('E')
        goal = (i,Z_pos)
        map[i] = l.replace('E','z')
    except ValueError:
        pass

def move_checker(pos,map,seen):
    rows = len(map)
    cols = len(map[0])
    valid_moves = []
    row,  col = pos
    current_char = map[row][col]
    # print(f'on {current_char} at {pos}')
    moves = {'down':(1,0), 'up':(-1,0), 'right':(0,1), 'left':(0,-1)}
    for dir,delta in moves.items():
        delta_r,delta_c = delta
        if 0 <= row+delta_r < rows and 0 <= col+delta_c < cols and (row+delta_r, col+delta_c) not in seen:
            check_char = map[row+delta_r][col+delta_c]
            if ord(current_char) - ord(check_char) >= -1:
                if (row+delta_r, col+delta_c) == goal: #* check for escape condition
                    return False #* don't need to continue
                valid_moves.append((row+delta_r, col+delta_c))
                # print(f'\tvalid move {dir} to {check_char}')
        else:
            continue
    return valid_moves

#* tester
# seen = []
# for r in range(3):
#     for c in range(3):
#         move_checker((r,c),map,seen)
#         seen.append((r,c))

seen = []
queue = deque([start])
bfs_path = {}
count = 0
while queue:
    count += 1
    if count % 1000 == 0:
        print('.')
    pos = queue.popleft()
    valid_moves = move_checker(pos,map,seen)
    if valid_moves is not False:
        [queue.append(x) for x in valid_moves]
        [seen.append(x) for x in valid_moves] #* super 🐛 🐝 🐞 🐜 🕷 🦗 🦟 🦋 was only adding seen for pos; however this made a queue with crazy duplicates. It worked for the demo but not the full size.
        for m in valid_moves:
            bfs_path[m] = pos
        # seen.append(pos) #* this was the bug
    else:
        bfs_path[goal] = pos
        break

#* find shortest path
pos = goal
path = []
while pos != start:
    path.append(pos)
    pos = bfs_path[pos]

print(f'steps to Z: {len(path)}')

#%%
#! part 2
a_positions = []
for i,l in enumerate(map):
    [a_positions.append((i,index)) for index, char in enumerate(l) if char == 'a']

seen = []
queue = deque(a_positions)
bfs_path = {}
count = 0
while queue:
    count += 1
    if count % 1000 == 0:
        # print('.')
        pass
    pos = queue.popleft()
    valid_moves = move_checker(pos,map,seen)
    if valid_moves is not False:
        [queue.append(x) for x in valid_moves]
        [seen.append(x) for x in valid_moves] #* super 🐛 🐝 🐞 🐜 🕷 🦗 🦟 🦋 was only adding seen for pos; however this made a queue with crazy duplicates. It worked for the demo but not the full size.
        for m in valid_moves:
            bfs_path[m] = pos
        # seen.append(pos) #* this was the bug
    else:
        bfs_path[goal] = pos
        break

#* find shortest path
pos = goal
path = []
while pos not in a_positions:
    path.append(pos)
    pos = bfs_path[pos]

print(f'shortest scenic trail steps a to z: {len(path)}')
#%%
#* works for small demo, but gets overwhelmed
# a_positions = []
# for i,l in enumerate(map):
#     [a_positions.append((i,index)) for index, char in enumerate(l) if char == 'a']

# min_trail = float('inf')

# for i, a_pos in enumerate(a_positions, start=1):
#     if i % (len(a_positions)//10) == 0:
#         print(f'{i}',end=' ')
#     # print(f'at an a at {a_pos}')
#     seen = []
#     queue = deque([a_pos])
#     bfs_path = {}
#     count = 0
#     while queue:
#         count += 1
#         if count % 1000 == 0:
#             # print('.')
#             pass
#         pos = queue.popleft()
#         valid_moves = move_checker(pos,map,seen)
#         if valid_moves is not False:
#             [queue.append(x) for x in valid_moves]
#             [seen.append(x) for x in valid_moves] #* super 🐛 🐝 🐞 🐜 🕷 🦗 🦟 🦋 was only adding seen for pos; however this made a queue with crazy duplicates. It worked for the demo but not the full size.
#             for m in valid_moves:
#                 bfs_path[m] = pos
#             # seen.append(pos) #* this was the bug
#         else:
#             bfs_path[goal] = pos
#             break
#     #* find shortest path
#     pos = goal
#     path = []
#     if goal not in bfs_path:
#         # print('no path to the top')
#         pass
#     else:
#         while pos != a_pos:
#             path.append(pos)
#             pos = bfs_path[pos]
#         # print(f'steps to Z: {len(path)}')
#         min_trail = min(min_trail,len(path))

# print(f'scenic summit: {min_trail}')
#%%
print()
print('⭐ ⭐') #* got both stars but needed help of BFS