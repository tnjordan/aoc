#%%
from copy import deepcopy
import matplotlib.pyplot as plt

f = 'data/day23.txt'
# f = 'data/day23.ex'

with open(file=f) as input:
    read_lines = input.readlines()
read_lines = [l.strip() for l in read_lines]
# print('🎅 🎄 🤶')

elf_count = 0
elfs = {}
search_order = ['N','S','W','E']
for r,line in enumerate(read_lines):
    for c, char in enumerate(line):
        if char == '#':
            elfs[elf_count] = [(-r,c), (-r,c)] #* current position, proposed position
            elf_count += 1

alone = [(1,-1),(1,0),(1,1),(-1,-1),(-1,0),(-1,1),(0,-1),(0,1)]
search = {  'N':[(1,-1),(1,0),(1,1)],
            'S':[(-1,-1),(-1,0),(-1,1)],
            'W':[(-1,-1),(0,-1),(1,-1)],
            'E':[(-1,1),(0,1),(1,1)]
        }

def elf_scaner(elf_pos, search, elf_positions):
    r,c = elf_pos
    for dr,dc in search:
        if (r+dr,c+dc) in elf_positions:
            return True
    return False

def elf_plotter(positions):
    y = []
    x = []
    for p in positions:
        y.append(p[0])
        x.append(p[1])
    plt.scatter(x=x,y=y)
    plt.show()

# all_alone = 0 #! p2
rounds = 0
# while all_alone < len(elfs): #! part 2, but too slow for full input. refactor
for i in range(10): #! part 1
    rounds += 1
    if rounds % 10 == 0:
        print(rounds)
    all_alone = 0 #* reset
    elf_positions = [elf[0] for elf in elfs.values()]
    # elf_plotter(positions = elf_positions)
    for elf, pos in elfs.items():
        c_pos,p_pos = pos
        #* check if alone
        if elf_scaner(c_pos,alone,elf_positions) is False:
            # print(f'elf {elf} is alone')
            elfs[elf] = [c_pos,c_pos]
            # all_alone += 1 #! p2
            continue
        for searach_dir in search_order:
            if elf_scaner(c_pos,search[searach_dir],elf_positions) is False:
                r,c = c_pos
                dr,dc = search[searach_dir][1] #* the actual move is the middle element
                p_pos = (r+dr,c+dc)
                # print(f'no elf {searach_dir} of elf {elf} @ {c_pos} elf proposing move to {p_pos}')
                elfs[elf] = [c_pos,p_pos]
                break
    
    prop_elf_positions = [elf[1] for elf in elfs.values()]
    for elf, pos in elfs.items():
        c_pos,p_pos = pos
        if prop_elf_positions.count(p_pos) == 1:
            elfs[elf] = [p_pos,p_pos]
        else:
            # print(f'potential collision detected at {p_pos}! Elf {elf} will remain at {c_pos}')
            elfs[elf] = [c_pos,c_pos]
    
    search_order = search_order[1:] + [search_order[0]]

elf_positions = [elf[0] for elf in elfs.values()]
min_r = float('inf')
min_c = float('inf')
max_r = -float('inf')
max_c = -float('inf')

for r,c in elf_positions:
    min_r = min(min_r,r)
    min_c = min(min_c,c)
    max_r = max(max_r,r)
    max_c = max(max_c,c)

#! part 1
print(f'the {len(elfs)} elves bound [{min_r},{max_r}] rows and [{min_c},{max_c}] columns')
area = ((max_r-min_r)+1) * ((max_c-min_c)+1) #* +1 !
print(f'this is an area of {area} spaces')
empty = area - len(elfs)
print(f'there are {empty} locations')

# print(f'all elves are all alone after {rounds} rounds') #! p2

#%%
#! part 2
#* run faster.


#%%
# # print()
# # print('⭐ ⭐')