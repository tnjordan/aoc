#%%
import numpy as np
f = 'data/day11.txt'

with open(file=f) as input:
    read_lines = input.readlines()
read_lines = [l.strip() for l in read_lines]
print('🎅 🎄 🤶')
#%%
serial_number = int(read_lines[0])

grid = np.zeros((300,300))

for y in range(300):
    for x in range(300):
        rack_id = x + 10
        power_level = rack_id * y
        power_level += serial_number
        power_level *= rack_id
        if power_level < 100: #* no 100s digit for string
            power_level = 0
        else:
            power_level = int(str(power_level)[-3])
        power_level -= 5
        grid[y][x] = power_level

max_power = float('-inf')
max_power_xy = ()
for i in range(300-3):
    for j in range (300-3):
        grid_power = grid[i:i+3,j:j+3].sum()
        if grid_power > max_power:
            max_power_xy = (j,i)
            max_power = grid_power
print(f'max power {max_power} at {max_power_xy}')
#%%
#! part 2
max_power = float('-inf')
max_power_xyk = ()
for k in range(2,300): #* ignoring 1 size square
    for i in range(300-k):
        for j in range (300-k):
            grid_power = grid[i:i+k,j:j+k].sum()
            if grid_power > max_power:
                max_power_xyk = (j,i,k)
                max_power = grid_power
    print(f'max power {max_power} at {max_power_xyk}') #* for input max level is at k=13, once this levels off you can interrupt
print(f'final answer!')
print(f'max power {max_power} at {max_power_xyk}')

#%%
print()
print('⭐ ⭐')