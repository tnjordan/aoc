#%%
import re

f = 'data/day25.txt'

with open(file=f) as input:
    read_lines = input.readlines()
read_lines = [l.strip() for l in read_lines]
print('🎅 🎄 🤶')
#%%

print(read_lines[0])
nums = [int(x) for x in re.findall('-?\d+', read_lines[0])]
grid_row, grid_col = nums


first_code = 20151125
multi_code = 252533
divide_code = 33554393

#%%

# test inputs
# grid_row = 1
# grid_col = 5

r = 1
c = 1
max_r = 1
count = 0

while True:
    if r == grid_row and c == grid_col:
        print(f'row {grid_row} col {grid_col} is count {count}')
        break

    r -= 1
    c += 1

    if r == 0:
        r = max_r
        c = 1
        max_r += 1

    count += 1

prev_code = first_code  # step 1
for _ in range(1, count):  # already done step 1
    code = prev_code * multi_code % divide_code
    prev_code = code

print(f'code {count} is {code}')
#%%
print()
print('⭐ ⭐')
