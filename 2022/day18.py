#%%
from collections import deque 

f = 'data/day18.txt'

with open(file=f) as input:
    read_lines = input.readlines()
read_lines = [l.strip() for l in read_lines]
print('🎅 🎄 🤶')

read_lines = [x.split(',') for x in read_lines]

input = []
for l in read_lines:
    input.append([int(x) for x in l])

edges = 0
search = [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]

#* for part 2
min_x = float('inf')
max_x = float('-inf')
min_y = float('inf')
max_y = float('-inf')
min_z = float('inf')
max_z = float('-inf')

for cube in input:
    x,y,z = cube
    min_x = min(min_x,x)
    min_y = min(min_y,y)
    min_z = min(min_z,z)
    max_x = max(max_x,x)
    max_y = max(max_y,y)
    max_z = max(max_z,z)

    for s in search:
        dx,dy,dz = s
        if [x+dx,y+dy,z+dz] not in input:
            edges += 1
        
print(f'total edges: {edges}')

#%%
#! part 2
#* make a cube that contains the droplet. 
#* find all edges visible

def move_checker_edge_finder(pos,seen): #* bfs from day12.py
    valid_moves = []
    edges = 0
    x,y,z = pos
    moves = [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
    for move in moves:
        dx,dy,dz = move
        if min_x-1 <= x+dx <= max_x+1 and min_y-1 <= y+dy <= max_y+1 and min_z-1 <= z+dz <= max_z+1:
            if (x+dx,y+dy,z+dz) not in seen:
                if [x+dx,y+dy,z+dz] in input:
                    edges += 1
                    # print(f'edge {edges} found! at {[x+dx,y+dy,z+dz]}') #* This could have been more descriptive; however code worked on first go!
                else:
                    valid_moves.append((x+dx,y+dy,z+dz))
    return valid_moves, edges

start = [(min_x-1,min_y-1,min_z-1)]
seen = []
queue = deque(start)
count = 0
edge_count = 0
while queue:
    count += 1
    if count % 1000 == 0:
        print('.')
    pos = queue.popleft()
    valid_moves, edges = move_checker_edge_finder(pos,seen)
    edge_count += edges
    if valid_moves is not False:
        [queue.append(x) for x in valid_moves]
        [seen.append(x) for x in valid_moves] #* super 🐛 🐝 🐞 🐜 🕷 🦗 🦟 🦋

print(f'external edges: {edge_count}')
#%%
print()
print('⭐ ⭐')