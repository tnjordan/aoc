#%%
import numpy as np
import re
f = 'data/day06.txt'

with open(file=f) as input:
    read_lines = input.readlines()
read_lines = [l.strip() for l in read_lines]
print('🎅 🎄 🤶')
#%%
instructions = []
for l in read_lines:
    inst = []
    if 'turn on' in l:
        inst.append(1)
    elif 'toggle' in l:
        inst.append(-1)
    else:
        inst.append(0)

    coords = re.findall('\d+',l)
    coords = [int(x) for x in coords]
    inst.append(coords)
    instructions.append(inst)

#%%
lights = np.zeros((1000,1000))
for status, [x0,y0,x1,y1] in instructions:
    if status >= 0:
        lights[x0:x1+1,y0:y1+1] = status
    else:
        lights[x0:x1+1,y0:y1+1] = 1 - lights[x0:x1+1,y0:y1+1]

print(f'There are {int(lights.sum())} lights on for 🎅')
#%%
#! part 2
lights = np.zeros((1000,1000))
for status, [x0,y0,x1,y1] in instructions:
    if status == 0:
        lights[x0:x1+1,y0:y1+1] -= 1
        lights[x0:x1+1,y0:y1+1][lights[x0:x1+1,y0:y1+1] < 0] = 0
    elif status == 1:
        lights[x0:x1+1,y0:y1+1] += 1
    else:
        lights[x0:x1+1,y0:y1+1] += 2

print(f'There are {int(lights.sum())} lumens for 🎅')


#%%
print()
print('⭐ ⭐')

#%%
