#%%
f = 'data/day24.txt'

with open(file=f) as input:
    read_lines = input.readlines()
read_lines = [line.strip() for line in read_lines]
print('❄️⛄❄️')
#%%
# https://backdrifting.net/postImages/hex_matplotlib_cube.png
directions = {
    'ne':   (0, 1, -1),
    'e':    (1, 0, -1),
    'se':   (1, -1, 0),
    'sw':   (0, -1, 1),
    'w':    (-1, 0, 1),
    'nw':   (-1, 1, 0),
}

tiles = {}
origin = (0,0,0)

def extract_direction(string):
    if string.startswith('ne'): return 'ne', string[2:]
    elif string.startswith('se'): return 'se', string[2:]
    elif string.startswith('sw'): return 'sw', string[2:]
    elif string.startswith('nw'): return 'nw', string[2:]
    return string[0], string[1:]

def walk_the_(line):
    k,j,i = origin
    while line:
        next_tile, line = extract_direction(line)
        dk,dj,di = directions[next_tile]
        k+=dk
        j+=dj
        i+=di
    if (k,j,i) in tiles:
        del tiles[(k,j,i)]
    else:
        tiles[(k,j,i)] = 1

for line in read_lines:
    walk_the_(line)

print(sum(tiles.values()))
#%%
from collections import defaultdict

def tile_life(tiles):
    # key is current color
    black_neighbors = {'black': defaultdict(int), 'white':  defaultdict(int)}
    
    # blacks get 0 to init since they check this condition
    for (k,j,i) in tiles:
        black_neighbors['black'][((k,j,i))] = 0
    
    for (k,j,i) in tiles:  # only blacks in tiles
        for d, (dk,dj,di) in directions.items():
            k_dk = k + dk
            j_dj = j + dj
            i_di = i + di
            if (k_dk,j_dj,i_di) in tiles:
                black_neighbors['black'][(k_dk,j_dj,i_di)] += 1
            else:
                black_neighbors['white'][(k_dk,j_dj,i_di)] += 1
    
    new_tiles = {}
    
    for tile, neighbors in black_neighbors['black'].items():
        if neighbors == 0 or neighbors > 2:
            continue  # white tile
        else:
            new_tiles[tile] = 1  # stay black
    for tile, neighbors in black_neighbors['white'].items():
        if neighbors ==  2:
            new_tiles[tile] = 1  # flip black
    return new_tiles

for _ in range(100):
    tiles = tile_life(tiles)

print(sum(tiles.values()))
#%%
