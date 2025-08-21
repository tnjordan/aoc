#%%

import numpy as np
import re

f = open('data/day22_input.txt', 'r')
read_lines = f.readlines()
f.close()

#%%
#! Part 1
# initilize @ 101, to cover -50 to +50
grid = np.zeros((101,101,101))

count = 0
for l in read_lines:
    # only read first 20 lines
    count += 1
    if count <= 20:
        l = l.strip()
        print(l)
        groups = re.search(r"(\w+) x=(\S+)\.\.(\S+),y=(\S+)\.\.(\S+),z=(\S+)\.\.(\S+)", l).groups
        state, x_min, x_max, y_min, y_max, z_min, z_max = groups(0) 
        # convert to ints and shft +50 to use np index
        x_min = int(x_min) + 50
        x_max = int(x_max) + 50
        y_min = int(y_min) + 50
        y_max = int(y_max) + 50
        z_min = int(z_min) + 50
        z_max = int(z_max) + 50

        if state == 'on':
            state = 1
        elif state == 'off':
            state = 0

        for i in range(x_min,x_max+1):
            for j in range(y_min,y_max+1):
                for k in range(z_min,z_max+1):
                    #* This didn't work, too much looping, instead put loop to limit first 20 lines
                    # # if i,j or k are out of bounds skip
                    # if i < 0 or i > 100 or j < 0 or j > 100 or k < 0 or k > 100:
                    #     pass
                    # else:
                    grid[i,j,k] = state

#%% 
#! Part 2
