#%%
import numpy as np

f = 'data/day17.txt'
# f = 'data/day17.ex'

with open(file=f) as input:
    read_lines = input.readlines()
read_lines = [l.strip() for l in read_lines]
print('🎅 🎄 🤶')
#%%
lines = []
min_y = float('inf')
max_y = float('-inf')
min_x = float('inf')
max_x = float('-inf')
for l in read_lines:
    x0, x1, y0, y1 = 0, 0, 0, 0
    a, b = l.split(', ')
    if a.startswith('x='):
        x0, x1 = [int(a.removeprefix('x='))] * 2
        y0, y1 = [int(i) for i in b.removeprefix('y=').split('..')]
    elif a.startswith('y='):
        y0, y1 = [int(a.removeprefix('y='))] * 2
        x0, x1 = [int(i) for i in b.removeprefix('x=').split('..')]
    min_y = min(min_y, y0, y1)
    max_y = max(max_y, y0, y1)
    min_x = min(min_x, x0, x1)
    max_x = max(max_x, x0, x1)
    lines.append([(x0, y0), (x1, y1)]) # wish i did y, x to always have y first

#%% plots
#* asked gpt to plot this
plot = False
if plot:
    import matplotlib.pyplot as plt

    # Coordinates list
    coordinates = lines

    # Extracting x and y coordinates from the list
    x_coords = [[x[0] for x in coord_pair] for coord_pair in coordinates]
    y_coords = [[y[1] for y in coord_pair] for coord_pair in coordinates]

    # Create a larger figure
    plt.figure(figsize=(20, 20))  # Set the figure size to 8 inches wide and 6 inches tall

    # Plotting the lines
    for x, y in zip(x_coords, y_coords):
        plt.plot(x, y)

    # Invert the y-axis
    plt.gca().invert_yaxis()

    # Adding labels and titles
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Lines from Coordinates')

    # Show the plot
    plt.grid(True)
    plt.show()


#%%
def x_con(x):
    return x  # removed shift in frustration at having points on the edges
    return x - min_x


def y_con(y):
    # return y
    return y - min_y


min_y_shift = y_con(min_y)
max_y_shift = y_con(max_y)
min_x_shift = x_con(min_x)
max_x_shift = x_con(max_x)

grid = np.zeros((max_y_shift + 1, max_x_shift + 1 + 1))  # added an extra +1 because flow went to the left of left most wall

for l in lines:
    (x0, y0), (x1, y1) = l
    y0 = y_con(y0)
    y1 = y_con(y1)
    x0 = x_con(x0)
    x1 = x_con(x1)
    x0, x1 = min(x0, x1), max(x0, x1)
    y0, y1 = min(y0, y1), max(y0, y1)
    for j in range(y0, y1 + 1):
        for i in range(x0, x1 + 1):
            grid[j][i] = 8

#%%
water_source = set()
water_source.add((x_con(500), 0))
water_reach = 0

while water_source:
    w_s = water_source.pop()
    ws_x, ws_y = w_s
    grid[ws_y][ws_x] = 2 # flow sources became 2
    while grid[ws_y + 1][ws_x] == 0:
        ws_y += 1
        grid[ws_y][ws_x] = 1
        if ws_y == max_y_shift:
            # print('i want to break free! this water source is done')
            break  # i want to break free! this water source is done
    if ws_y == max_y_shift:
        # print('i have broken free! lets continue on')
        continue
    left_clay = None
    lc = ws_x
    right_clay = None
    rc = ws_x
    while left_clay is None and lc > 0:
        grid[ws_y][lc] = 1 # all the 1 assignments are for the down flows
        lc -= 1
        if grid[ws_y + 1][lc] == 0:  # empty below
            left_clay = False
            water_source.add((lc, ws_y))  # empty add new water source
            # print('add water source left side')
        elif grid[ws_y + 1][lc] == 1 or grid[ws_y + 1][lc] == 2:
            left_clay = False
            pass  # been there done that
        elif grid[ws_y][lc] == 8:
            left_clay = True
    
    while right_clay is None and rc < max_x_shift + 1:
        grid[ws_y][rc] = 1
        rc += 1
        if grid[ws_y + 1][rc] == 0:  #  empty below
            right_clay = False
            water_source.add((rc, ws_y))  # empty add new water source
            # print('add water source right side')
        elif grid[ws_y + 1][rc] == 1 or grid[ws_y + 1][rc] == 2:
            right_clay = False
            pass  # been there done that
        elif grid[ws_y][rc] == 8:
            right_clay = True
    
    if left_clay is True and right_clay is True:
        for x in range(lc + 1, rc):
            grid[ws_y][x] = 3  # three was trapped water
        # break
        water_source.add((ws_x, ws_y - 1))  # water source moves up the stream
    
    # print(f'water source {water_source}')
    # print(grid)

# print(grid)

#* make gpt do the maths
# Create a boolean mask for elements > 0 and < 8
mask = (grid > 0) & (grid < 8)

# Count the elements that satisfy the condition
count = np.count_nonzero(mask)

print(f'part 1: {count}')
mask = (grid == 3)
count = np.count_nonzero(mask)
print(f'part 2: {count}')

#%%
print()
print('⭐ ⭐')
