#%%
f = 'data/day05.txt'

with open(file=f) as input:
    read_lines = input.readlines()
read_lines = [line.strip() for line in read_lines]
print('❄️⛄❄️')
#%%
part_2 = True
instructions = [int(k2) for k2 in read_lines]
steps = 0
position = 0
while 0 <= position < len(instructions):
    steps += 1
    p_value = instructions[position]
    if part_2 and p_value >= 3:
        instructions[position] = p_value - 1
    else:
        instructions[position] = p_value + 1
    position += p_value
print(f'steps: {steps}')
#%%
