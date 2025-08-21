#%%
from tabulate import tabulate
from copy import deepcopy

f = 'data/day22.txt'
# f = 'data/day22.ex'

with open(file=f) as input:
    read_lines = input.readlines()
read_lines = [line.strip() for line in read_lines]
print('❄️⛄❄️')
#%%
blocks = {}
x_min = 0
x_max = 0
y_min = 0
y_max = 0
z_min = 0
z_max = 0
for i, line in enumerate(read_lines,start=0):
    end_1, end_2 = line.split('~')
    x1, y1, z1 = [int(v) for v in end_1.split(',')]
    x2, y2, z2 = [int(v) for v in end_2.split(',')]
    # z first
    end_1 = (z1,y1,x1) 
    end_2 = (z2,y2,x2)

    #! all sorted
    # if [end_1,end_2] != sorted((end_1, end_2)):
    #     print('no')
    #     print(end_1,end_2)
    char_values = 26  # A-Z, matches A-G of thev example
    count = i//char_values+1
    # print(i,chr(i%char_values+65)*count)
    blocks[chr(i%char_values+65)*count] = (end_1,end_2)
    x_min = min(x1,x2,x_min)
    x_max = max(x1,x2,x_max)
    y_min = min(y1,y1,y_min)
    y_max = max(y1,y1,y_max)
    z_min = min(z1,z2,z_min)
    z_max = max(z1,z2,z_max)

#! super bug, old method used the floor of the base_tower
# refactor needs the floor to slide down
blocks['🌋'] = ((0,0,0),(0,y_max,x_max))  # the floor is lava

#%%
# for x in range(x_min,x_max+1):
#     for y in range(y_min, y_max+1):
#         for z in range(z_min, z_max+1):
#             print(x,y,z)

base_tower = {}  # key is the z
for z in range(z_min, z_max+1):
    base_tower[z] = []
    for y in range(y_min, y_max+1):
        new_r = []
        for x in range(x_min,x_max+1):
            # print(z,y,x)  # better to reverse for looping
            if z == 0:
                new_r.append('_')
            else:
                new_r.append('.')
        base_tower[z].append(new_r)

def tower_builder(blocks):
    tower = deepcopy(base_tower)
    for block,ends in blocks.items():
        end_1, end_2 = ends
        z1,y1,x1 = end_1
        z2,y2,x2 = end_2
        assert z1 <= z2
        assert y1 <= y2
        assert x1 <= x2
        for z in range(z1,z2+1):
            for y in range(y1,y2+1):
                for x in range(x1,x2+1):
                    tower[z][y][x] = block
    return tower
#%%
def display_tower(tower):
    for z in range(z_max,0-1,-1):
        print(f'z level: {z}')
        print(tabulate(tower[z], tablefmt='plain'),'\n')

tower = tower_builder(blocks)
# display_tower(tower)
#%%
# blocks are provided in order.
# drop blocks from bottom to top as far as they can go



#%%
sliding = True
debug_blocks = ['HHHH', 'QQQQQQQQQQQQQQQQQ']
while sliding:
    print('sorting')
    # sort the blocks
    sorted_footballers_by_goals = sorted(blocks.items(), key=lambda x:x[1], reverse=False)
    blocks = dict(sorted_footballers_by_goals)
    print('sliding')
    sliding = False
    for block,ends in blocks.items():  #! ahh the true input isn't z! sorted.
        if block in debug_blocks:
            print(f'on block:{block} at ends:{ends}')
        (z1,y1,x1),(z2,y2,x2) = ends
        min_slide = float('inf')
        for b,e in blocks.items():  #! will need to go through in reverse?
            if block in debug_blocks:
                print(f'checking block: {b} at ends: {e}')
            (z1b,y1b,x1b),(z2b,y2b,x2b) = e
            if z2b >= z1:
                if block in debug_blocks:
                    print('base too high')
                continue
            s = False
            if (y1 <= y1b <= y2 or y1 <= y2b <= y2) and (x1 <= x1b <= x2 or x1 <= x2b <= x2):
                s = True
            elif (y1b <= y1 <= y2b or y1b <= y2 <= y2b) and (x1b <= x1 <= x2b or x1b <= x2 <= x2b):
                s = True
            elif (y1 <= y1b <= y2 or y1 <= y2b <= y2) and (x1b <= x1 <= x2b or x1b <= x2 <= x2b):
                s = True
            elif (y1b <= y1 <= y2b or y1b <= y2 <= y2b) and (x1 <= x1b <= x2 or x1 <= x2b <= x2):
                s = True
            if s:
                slide = z1-z2b-1  # don't intersect
                if block in debug_blocks:
                    print(f'\tslide: {slide}')
                min_slide = min(slide, min_slide)

        if min_slide < z_max*2 and min_slide != 0:
            sliding = True
            slide = min_slide
            end_1 = (z1-slide,y1,x1)
            end_2 = (z2-slide,y2,x2)
            
            if block in debug_blocks:
                print(f'block:{block} going down {slide}')
                print(f'was at: {blocks[block]}')
            blocks[block] = (end_1,end_2)
            if block in debug_blocks:
                print(f'now at {blocks[block]}')

tower = tower_builder(blocks)

#%%
# find the supporters
supporters = {}
for z in range(z_max,0,-1):
        z_c = z - 1
        for y in range(y_max+1):
            for x in range(x_max+1):
                b = tower[z][y][x]
                b_c = tower[z_c][y][x]
                if b != '.':
                    if b not in supporters:
                        supporters[b] = set()
                    if b_c != '.' and b_c != b:
                        supporters[b].add(b_c)
supporters

print('why?')  # why was the lack of all support checks. Had bug with vertical and horziontal that intersected in their middles
for b,s in supporters.items():
    if s == set():
        print(b)
#%%
part_1 = False
if part_1:
    disintegrateable_blocks = set(supporters.keys())
    for b,s in supporters.items():
        if len(s) == 1:
            try:
                disintegrateable_blocks.remove(s.pop())
            except KeyError:
                pass  # '_' floor or already removed
    disintegrateable_blocks
    print()
    print(len(disintegrateable_blocks))
#%%

from collections import defaultdict

supporting = defaultdict(set)
for k,v in supporters.items():
    for sup in v:
        supporting[sup].add(k)

def dissenegrator(dissenegrate='🌋', dissenegrated=set()):
    # print(f'at {dissenegrate}')
    dissenegrated.add(dissenegrate)
    # print(f'supporting: {supporting[dissenegrate]}')
    for c_p in supporting[dissenegrate]:
        # print(f'\tchecking {c_p} which has supporters {supporters[c_p]}')
        if supporters[c_p].issubset(dissenegrated):
            
            # print(f'\t update! {c_p}')
            dissenegrated.update(dissenegrator(c_p, dissenegrated))
    return dissenegrated

collateral_damage = 0
for block in blocks:
    dissenegrated = dissenegrator(dissenegrate=block, dissenegrated=set())
    count_dissenegrated = len(dissenegrated)-1
    print(f'dissenegrating {block} dissenegrates {count_dissenegrated} blocks')
    if block != '🌋':
        collateral_damage += count_dissenegrated
print(f'total collateral damage: {collateral_damage}')

#%%
# def brute_colapse():
#     # colapse tower
#     collapse = True
#     while collapse:
#         collapse = False
#         for z in range(z_max,0,-1):
#             z_c = z - 1
#             blocks_on_lvl = set()
#             supported_blocks = set()
#             for y in range(y_max+1):
#                 for x in range(x_max+1):
#                     if tower[z][y][x] != '.':
#                         blocks_on_lvl.add(tower[z][y][x])
#                         if tower[z_c][y][x] != '.':
#                             supported_blocks.add(tower[z][y][x])
#             unsupported_blocks = blocks_on_lvl.difference(supported_blocks)
#             # print(unsupported_blocks)
#             for b in unsupported_blocks:
#                 collapse = True
#                 end_1, end_2 = blocks[b]
#                 z1,y1,x1 = end_1
#                 z2,y2,x2 = end_2
#                 end_1 = (z1-1,y1,x1)
#                 end_2 = (z2-1,y2,x2)
#                 blocks[b] = (end_1,end_2)
#                 tower = tower_builder(blocks)
# # display_tower(tower)
#%%
