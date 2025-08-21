#%%
f = 'data/day12.txt'

with open(file=f) as input:
    read_lines = input.readlines()
read_lines = [l.strip() for l in read_lines]
print('🎅 🎄 🤶')
#%%
register = {
    'a': 0,
    'b': 0,
    'c': 1,
    'd': 0
}

instructions = []
for line in read_lines:
    ins = line[:3]
    command = line[4:].split()
    instructions.append((ins,command))

i = 0
while i < len(instructions):
    ins, command = instructions[i]
    if ins == 'cpy':
        x,y = command
        if x in register:
            register[y] = register[x]
        else:
            register[y] = int(x)
    elif ins == 'jnz':
        x,y = command
        if x in register:
            x_v = register[x]
        else:
            x_v = int(x)
        if y in register:
            y_v = register[y]
        else:
            y_v = int(y)
        if x_v != 0:
            i += int(y)
            continue
    elif ins == 'inc':
        x, = command
        register[x] += 1
    elif ins == 'dec':
        x, = command
        register[x] -= 1
    i += 1

print(register['a'])
#%%
# print()
# print('⭐ ⭐')
