#%%
from tabulate import tabulate
import copy

f = open('data\day25_input.txt', 'r')
read_lines = f.readlines()
f.close()

sea_map = []
new_sea_map = []
blank_sea_map = []
for l in read_lines:
    l = l.strip()
    s_m = []
    n_s_m = []
    b_s_m = []
    for c in l:
        s_m.append(c)
        n_s_m.append('.')
        b_s_m.append('.')
    sea_map.append(s_m)
    new_sea_map.append(n_s_m)
    blank_sea_map.append(b_s_m)

print('initial conditions')
print(tabulate(sea_map))

#* Note cords are in y,x to match sea_map[y][x] list call
sea_cumbers_moving = True
move_order = {'>':(0,1), 'v':(1,0)}
move_count = 0
while sea_cumbers_moving is True:
    sea_cumbers_moving = False
    move_count += 1
    for dir,move in move_order.items():
        for y,l in enumerate(sea_map):
            for x,c in enumerate(l):
                if c == dir:
                    #* check next position
                    new_y = y + move[0]
                    new_x = x + move[1]
                    #* check if next position is off the map
                    if new_y > len(sea_map) - 1:
                        new_y = 0
                    if new_x > len(l) - 1:
                        new_x = 0
                    if sea_map[new_y][new_x] == '.':
                        #* moving
                        new_sea_map[new_y][new_x] = c
                        sea_cumbers_moving = True
                    else:
                        new_sea_map[y][x] = c
                #* if the space is occupied the maintain the occupation
                elif c in move_order:
                    new_sea_map[y][x] = c
        sea_map = copy.deepcopy(new_sea_map)
        new_sea_map = copy.deepcopy(blank_sea_map)
    #print('move:', move_count)
    #print(tabulate(sea_map))

print('the cucumbers moved',move_count,'times')
# %%
