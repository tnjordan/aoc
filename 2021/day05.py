#%%
import pandas as pd
import numpy as np
import re
#%%
#* Read file
fh = open('data/day5_input.txt')
read_lines = fh.readlines()
fh.close()

#%%
#* set variables to track max X and Y of coord system
max_x = 0
max_y = 0
grid_array = np.zeros((1000,1000), dtype=int)
line_x_range = []
line_y_range = []
#* List of coordinates
for line in read_lines:
    
    x0, y0, x1, y1 = [int(i) for i in re.findall(r'\d+',line)]
    print(x0, y0, x1, y1)
    if x0 == x1 or y0 == y1:
        """#* resize array
        if x0 or x1 > max_x:
            max_x = max(x0,x1)
            #grid_array.resize((max_x+1, max_y+1),refcheck=False)
        if y0 or y1 > max_y:
            max_y = max(y0,y1)
            #grid_array.resize((max_x+1, max_y+1),refcheck=False)
            print(np.size(grid_array, axis = 0), 'x', np.size(grid_array, axis = 1))"""
        #* ranges of points to plot
        line_x_range = [x0]
        line_y_range = [y0]
        if x0 < x1:
            line_x_range = [*range(x0,x1+1)]
        elif x0 > x1:
            line_x_range = [*range(x1,x0+1)]
        elif y0 < y1:
            line_y_range = [*range(y0,y1+1)]
        elif y0 > y1:
            line_y_range = [*range(y1,y0+1)]
        else:
            print('nothing_burger')
        for x in line_x_range:
            for y in line_y_range:
                grid_array[x,y] += 1

    
#%%
#* get the totals
count = 0
for el in np.nditer(grid_array):

    if el >= 2:
        count += 1
print(count)






# %%
