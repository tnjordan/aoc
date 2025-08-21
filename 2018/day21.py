#%%
from day16 import addr, addi, mulr, muli, banr, bani, borr, bori, setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr

f = 'data/day21.txt'

with open(file=f) as input:
    read_lines = input.readlines()
read_lines = [l.strip() for l in read_lines]
print('🎅 🎄 🤶')
#%%
# copy pasta from day19.py
ip_register = int(read_lines[0].split(' ')[1])

instructions = []
for l in read_lines[1:]:
    i = l.split(' ')
    instructions.append([i[0], int(i[1]), int(i[2]), int(i[3])])

register = [0, 0, 0, 0, 0, 0]

min_instruction = float('inf')

for i in range(100):
    ip_register = int(read_lines[0].split(' ')[1])
    register = [0, 0, 0, 0, 0, 0]
    ip = register[ip_register]
    register[0] = i
    instruction_count = 0
    run = True
    while run:
        instruction_count += 1
        register[ip_register] = ip
        instruction = instructions[ip]
        print(f'ip: {ip} {instruction[0]}({instruction[1]}, {instruction[2]}, {instruction[3]}, {register})')
        register = eval(instruction[0])(a=instruction[1], b=instruction[2], c=instruction[3], register=register)
        ip = register[ip_register]
        ip += 1
        if ip >= len(instructions) or ip < 0:
            run = False
            print('HALT!')
            if instruction_count < min_instruction:
                min_instruction = instruction_count
                print(f'new min_instruction: {min_instruction} at register[0] = {i}')
            break

#%%
# print()
# print('⭐ ⭐')
