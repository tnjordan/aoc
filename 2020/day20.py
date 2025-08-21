#%%
from collections import deque
from tabulate import tabulate

f = 'data/day20.txt'
f = 'data/day20ex.txt'

with open(file=f) as input:
    read_lines = input.readlines()
read_lines = [line.strip() for line in read_lines]
print('❄️⛄❄️')
#%%
tiles = {}
tile_id = None
for line in read_lines:
    if 'Tile' in line:
        tile_id = line.replace('Tile ', '').strip().split(':')[0]
        tiles[tile_id] = []
    elif line == '':
        tile_id = None
    elif tile_id is not None:
        tiles[tile_id].append(list(line))

tile_edges = {
    tile_id: {
        'top': ''.join(grid[0]),
        'bottom': ''.join(grid[-1]),
        'left': ''.join(row[0] for row in grid),
        'right': ''.join(row[-1] for row in grid)
    }
    for tile_id, grid in tiles.items()
}

def rotate_90(tile_id):
    prev_grid = tiles[tile_id]
    grid = [list(reversed(col)) for col in zip(*prev_grid)]
    
    tiles[tile_id] = grid
    tile_edges[tile_id] = {
        'top': ''.join(grid[0]),
        'bottom': ''.join(grid[-1]),
        'left': ''.join(row[0] for row in grid),
        'right': ''.join(row[-1] for row in grid)
    }

def flip_vertical(tile_id):
    prev_grid = tiles[tile_id]
    grid = [list(reversed(row)) for row in prev_grid]
    
    tiles[tile_id] = grid
    tile_edges[tile_id] = {
        'top': ''.join(grid[0]),
        'bottom': ''.join(grid[-1]),
        'left': ''.join(row[0] for row in grid),
        'right': ''.join(row[-1] for row in grid)
    }

def flip_horizontal(tile_id):
    prev_grid = tiles[tile_id]
    grid = [row for row in prev_grid[::-1]]
    
    tiles[tile_id] = grid
    tile_edges[tile_id] = {
        'top': ''.join(grid[0]),
        'bottom': ''.join(grid[-1]),
        'left': ''.join(row[0] for row in grid),
        'right': ''.join(row[-1] for row in grid)
    }
#%%
tile_matches = {}

tile_matches = {
    tile_id: {
    'top': None,
    'bottom': None,
    'left': None,
    'right': None
    }
    for tile_id in tiles
}

dir_map = {
    'top': 'bottom',
    'bottom': 'top',
    'left': 'right',
    'right': 'left'
}

# start with any tile and build out from there
tile_id = list(tiles.keys())[-1]

searching = deque()
searching.append(tile_id)
matched = set()
matched.add(tile_id)
while searching:
    tile_id = searching.popleft()
    print(f'searching for matching tiles for tile: {tile_id}')
    
    for dir, edge in tile_edges[tile_id].items():
        print(f'\tchecking {dir}')
        if tile_matches[tile_id][dir] is None:
            
            for search_tile in tiles:
                if search_tile == tile_id: continue
                
                print(f'\t\tchecking {search_tile}')
                
                if search_tile in matched: # no operations only check edges
                    if edge == tile_edges[search_tile][dir_map[dir]]:
                        print(f'MATCH!: {tile_id} {dir} to {search_tile} {dir_map[dir]}')
                        tile_matches[tile_id][dir] = search_tile
                        tile_matches[search_tile][dir_map[dir]] = tile_id
                        matched.add(search_tile)  # store so no more rotations of tile
                        searching.append(search_tile)
                        break  # matched edge, go on to next edge
                else:
                    # no rotation
                    if edge == tile_edges[search_tile][dir_map[dir]]:
                        print(f'MATCH!: {tile_id} {dir} to {search_tile} {dir_map[dir]}')
                        tile_matches[tile_id][dir] = search_tile
                        tile_matches[search_tile][dir_map[dir]] = tile_id
                        matched.add(search_tile)  # store so no more rotations of tile
                        searching.append(search_tile)
                        break  # matched edge, go on to next edge
                    
                    prev_op = None
                    found_match = False
                    for op in [ rotate_90, 
                                flip_vertical, 
                                flip_vertical,  # return
                                flip_horizontal,
                                flip_horizontal,  # return
                                ] * 4:
                        print(f'\t\t\tperforming op: {op}')
                        op(search_tile)
                        
                        if prev_op == op: continue
                        
                        if edge == tile_edges[search_tile][dir_map[dir]]:
                            print(f'MATCH!: {tile_id} {dir} to {search_tile} {dir_map[dir]}')
                            tile_matches[tile_id][dir] = search_tile
                            tile_matches[search_tile][dir_map[dir]] = tile_id
                            matched.add(search_tile)  # store so no more rotations of tile
                            searching.append(search_tile)
                            found_match = True
                            break  # stop operations! 
                    if found_match:
                        break  # matched edge, go on to next edge
#%%
corner_tile_product = 1
for tile, matches in tile_matches.items():
    if sum([m == None for m in matches.values()]) == 2:
        corner_tile_product *= int(tile)
        if matches['top'] == matches['left'] == None:
            top_left = tile
print(corner_tile_product)
#%%
sea_monster = [
    "                  # ",
    "#    ##    ##    ###",
    " #  #  #  #  #  #   "
]

# First find all coordinates where # appears
absolute_coords = []
for i, line in enumerate(sea_monster):
    for j, char in enumerate(line):
        if char == '#':
            absolute_coords.append((j, i))

# Find the leftmost # (minimum j value)
min_j = min(j for j, i in absolute_coords)
min_i = min(i for j, i in absolute_coords if j == min_j)

# Create relative coordinates
monster_coords = [(j - min_j, i - min_i) for j, i in absolute_coords]

# remove (0,0) that is the search start
monster_coords.remove((0,0))

print(monster_coords)
#%%
def monster_search(grid):
    monster_count = 0
    J = len(grid)
    I = len(grid[0])
    for j, row in enumerate(grid):
        for i, c in enumerate(row):
            if c == '#':
                for dj,di in monster_coords:
                    j_dj = j + dj
                    i_di = i + di
                    if 0 <= j_dj < J and 0 <= i_di < I:
                        if grid[j_dj][i_di] == '#':
                            continue
                        else:
                            break
                    else:
                        break
                else:
                    monster_count += 1
    return monster_count
#%%
for tile_id in tiles:
    tiles[tile_id] = tiles[tile_id][1:-1]
    tiles[tile_id] = [row[1:-1] for row in tiles[tile_id]]
#%%
grid = tiles[top_left]
grid_build = deque()
grid_build.append(tile_matches[top_left]['right'])
next_bottom = tile_matches[top_left]['bottom']
dir = 'right'
j = 0
while grid_build:
    print(tabulate(grid))
    next_tile = grid_build.popleft()
    print(f'adding tile: {next_tile} to {dir}')
    
    if dir == 'right':
        for dj, row in enumerate(tiles[next_tile]):
            grid[j + dj].extend(row)
    elif dir == 'bottom':
        grid.extend(tiles[next_tile])
        j += len(tiles[next_tile])
    
    if tile_matches[next_tile]['right'] != None:
        dir = 'right'
        grid_build.append(tile_matches[next_tile]['right'])
    else:
        if next_bottom:
            dir = 'bottom'
            grid_build.append(next_bottom)
            next_bottom = tile_matches[next_bottom]['bottom']
#%%
tiles['grid'] = grid  # lazy way to reuse lazy functions

# wave count
wave_count = sum(row.count('#') for row in grid)

prev_op = None
for op in [ rotate_90, 
            flip_vertical, 
            flip_vertical,  # return
            flip_horizontal,
            flip_horizontal,  # return
            ] * 4:
    print(f'\t\t\tperforming op: {op}')
    op('grid')
    grid = tiles['grid']

    if prev_op == op: continue
    
    monsters = monster_search(grid)
    if monsters:
        print(f'Found {monsters} monsters!')
        print(f'Water roughness: {wave_count - monsters * sum(row.count("#") for row in sea_monster)}')
        break
#%%