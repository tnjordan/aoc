#%%
f = 'data/day15.txt'

with open(file=f) as input:
    read_lines = input.readlines()
read_lines = [line.strip() for line in read_lines]
print('❄️⛄❄️')
#%%
init_nums = [int(x) for x in read_lines[0].split(',')]
#%%
nums_map = {}
# initialize game
for i,num in enumerate(init_nums):
    print(f'Turn {i+1}: Elf says {num}')
    nums_map[num] = [i]

# play the game
for i in range(len(init_nums), 30000000):
    if len(nums_map[num]) == 1:
        num = 0
    else:
        num = nums_map[num][1] - nums_map[num][0]
    
    if num not in nums_map:
        nums_map[num] = [i]
    elif len(nums_map[num]) == 2:
        nums_map[num][0], nums_map[num][1] = nums_map[num][1], i
    else:
        nums_map[num].append(i)
print(f'Turn {i+1}: Elf says {num}')
#%%
