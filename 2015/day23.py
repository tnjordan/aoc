#%%
f = 'data/day23.txt'
# f = 'data/day23.ex'  # works fine

with open(file=f) as input:
    read_lines = input.readlines()
read_lines = [l.strip() for l in read_lines]
print('🎅 🎄 🤶')
#%%
instructions = {}

part_2 = True
if part_2:
    registers = {'a': 1, 'b': 0}
else:
    registers = {'a': 0, 'b': 0}

for i, l in enumerate(read_lines):
    if ',' in l:
        reg, offset = l.split(', ')
        inst, reg = reg.split(' ')
        offset = int(offset)
    elif 'jmp' in l:
        inst, offset = l.split(' ')
        offset = int(offset)
        reg = None
    else:
        inst, reg = l.split(' ')
        offset = 1
    instructions[i] = {'inst': inst, 'reg': reg, 'offset': offset}


def processor(i):
    print(f'instruction code: {i}')

    if i not in instructions:
        print('🎅 🎄 🤶')
        print(f'registers: {registers}')
        return False

    print(f'registers: {registers}')
    print(f'instructions: {instructions[i]}')
    print()
    inst, reg, offset = instructions[i].values()

    if reg == 'b':
        print('🐝')

    if inst == 'jmp':
        i += offset
    elif inst == 'jie':
        if registers[reg] % 2 == 0:
            i += offset
        else:
            i += 1
    elif inst == 'jio':
        if registers[reg] == 1:
            i += offset
        else:
            i += 1
    elif inst == 'hlf':
        registers[reg] /= 2
        i += 1
    elif inst == 'tpl':
        registers[reg] *= 3
        i += 1
    elif inst == 'inc':
        registers[reg] += 1
        i += 1
    else:
        print('🎅 🎄 🤶')
        print('unknown instruction')
        return False

    return i


i = 0
while i is not False:
    i = processor(i)

#%%
print()
print('⭐ ⭐')
