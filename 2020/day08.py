#%%
import copy
input = open('data/day8.txt')
read_lines = input.readlines()
# %%


boot_code = []

for l in read_lines:
    l = l.strip()
    command, value = l.split(sep=' ')
    value = int(value)
    boot_code.append([command,value])
# %%
boot_code_stable = copy.deepcopy(boot_code) #* make a copy for part 2

#* init command and accumulator
infinite = False
boot_pos = 0
accumulator = 0
command = boot_code[boot_pos][0]
value = boot_code[boot_pos][1]

while not infinite:
    if command == 'acc':
        boot_code[boot_pos][0] = 'bhdt' #*been here done that
        accumulator += value
        boot_pos += 1
        command = boot_code[boot_pos][0]
        value = boot_code[boot_pos][1]
    elif command == 'nop':
        boot_code[boot_pos][0] = 'bhdt' #*been here done that
        boot_pos += 1
        command = boot_code[boot_pos][0]
        value = boot_code[boot_pos][1]
    elif command == 'jmp':
        boot_code[boot_pos][0] = 'bhdt' #*been here done that
        boot_pos += value
        command = boot_code[boot_pos][0]
        value = boot_code[boot_pos][1]
    else:
        infinite = True

print(accumulator)

# %%
#! part 2
len_boot_code = len(boot_code)
for i, b_c in enumerate(boot_code_stable):
    boot_code = copy.deepcopy(boot_code_stable) #* reset for each run
    if b_c[0] == 'nop':
        boot_code[i][0] = 'jmp'
    elif b_c[0] == 'jmp':
        boot_code[i][0] = 'nop'
    
    #* check for infinite
    infinite = False
    boot_pos = 0
    accumulator = 0
    command = boot_code[boot_pos][0]
    value = boot_code[boot_pos][1]

    while not infinite:
        if command == 'acc':
            boot_code[boot_pos][0] = 'bhdt' #*been here done that
            accumulator += value
            boot_pos += 1
        elif command == 'nop':
            boot_code[boot_pos][0] = 'bhdt' #*been here done that
            boot_pos += 1
        elif command == 'jmp':
            boot_code[boot_pos][0] = 'bhdt' #*been here done that
            boot_pos += value
        else:
            infinite = True
        if boot_pos == len_boot_code - 1:
            print('End of the Line')
            print(accumulator)
            print('done')
            break
        else:
            command = boot_code[boot_pos][0] #* get next command and value
            value = boot_code[boot_pos][1]
# %%
