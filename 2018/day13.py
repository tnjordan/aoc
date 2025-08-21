#%%
from tabulate import tabulate
from copy import deepcopy
f = 'data/day13.txt'
# f = 'data/day13.ex'
# f = 'data/day13.ex2'

with open(file=f) as input:
    read_lines = input.readlines()
read_lines = [list(l)[:-1] for l in read_lines] # the [:-1] removes '\n' from each line
print('🎅 🎄 🤶')
#%%
grid = read_lines
turns = ['left', 'straight', 'right']
turn_char = ['<','v','>','^'] # turns to the left +1 right -1

turn_dict = {}
for i,c in enumerate(turn_char):
    turn_dict[c] = {
                    'left':turn_char[(i+1)%4],
                    'straight': c,
                    'right': turn_char[(i-1)%4]
                    }

#%%
carts = []
for y,row in enumerate(grid):
    for x,char in enumerate(row):
        if char in ['<','>','^','v']:
            carts.append([(y,x),char,0])
            if char in ['<','>']: # remove carts from grid
                grid[y][x] = '-'
            else:
                grid[y][x] = '|'

shift = {
        '<':(0,-1), # coordinates are (y,x) to match grid[y][x]
        '>':(0,+1),
        '^':(-1,0),
        'v':(+1,0)
        }

def move(cart):
    (y,x),char,turn = cart
    dy,dx = shift[char]
    y += dy
    x += dx
    track = grid[y][x]
    if track in ['-','|']: # straights
        pass
    elif track == '/':
        if char == '<':
            char = turn_dict[char]['left']
        elif char == '>':
            char = turn_dict[char]['left']
        elif char == '^':
            char = turn_dict[char]['right']
        elif char == 'v':
            char = turn_dict[char]['right']
    elif track == '\\': # turns
        if char == '<':
            char = turn_dict[char]['right']
        elif char == '>':
            char = turn_dict[char]['right']
        elif char == '^':
            char = turn_dict[char]['left']
        elif char == 'v':
            char = turn_dict[char]['left']
    else: # intersections
        # print('🐛'*10) dumb bug had char == ... not char = ...
        turn_dir = turns[turn%3]
        char = turn_dict[char][turn_dir]
        turn += 1
    return [(y,x),char,turn]

def crash_check(carts):
    seen = set()
    for (y,x) in [x[0] for x in carts if x[0] != (-1,-1)]:
        if (y,x) in seen:
            return (y,x)
        else:
            seen.add((y,x))
    return False

def grid_printer(carts):
    print_grid = deepcopy(grid)
    for cart in carts:
        (y,x),char,turn = cart
        print_grid[y][x] = char
    print(tabulate(print_grid, tablefmt='plain', colalign='right'))

#%%
#! part 1
part_1 = False
if part_1:
    crash = False
    ticks = 0
    verbose = False

    while not crash:
        if verbose:
            print(f'tick {ticks}')
            grid_printer(carts)
            print()
        carts.sort(key=lambda x: x[0][0]*len(grid[0])+x[0][1])
        for i, cart in enumerate(carts):
            carts[i] = move(cart)
            if crash_check(carts):
                (y,x) = crash_check(carts)
                print(f'Crash at X:{x} Y:{y}! {x},{y}')
                crash = True
                break
        ticks += 1

#%%
#! part 2
ticks = 0
verbose = False

while len(carts) > 1:
    if verbose:
        print(f'tick {ticks}')
        grid_printer(carts)
        print()
    carts.sort(key=lambda x: x[0][0]*len(grid[0])+x[0][1])
    for i, cart in enumerate(carts):
        if cart[0] == (-1,-1): # crashed carts don't move
            # print('already dead!') #! this will never print with the code on line 134
            continue
        carts[i] = move(cart)
        if crash_check(carts):
            (y,x) = crash_check(carts)
            #! this is not the same, as 135-137. it does not overwrite the carts in the loop, the assignment does.
            # carts = [cart if cart[0] != (y,x) or cart[0] == (-1,-1) else [(-1,-1),-1,-1] for cart in carts]
            k2 = [cart if cart[0] != (y,x) or cart[0] == (-1,-1) else [(-1,-1),-1,-1] for cart in carts]
            for i,c in enumerate(k2):
                carts[i] = c
    carts = [cart for cart in carts if cart[0] != (-1,-1)] # remove the crashed carts
    ticks += 1

print(f'Final cart is at x,y: {carts[0][0][1]},{carts[0][0][0]}')

#%%
print()
print('⭐ ⭐')