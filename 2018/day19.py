#%%
from day16 import addr, addi, mulr, muli, banr, bani, borr, bori, setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr


f = 'data/day19.txt'
# f = 'data/day19.ex'

with open(file=f) as input:
    read_lines = input.readlines()
read_lines = [l.strip() for l in read_lines]
print('🎅 🎄 🤶')
#%%
ip_register = int(read_lines[0].split(' ')[1])


instructions = []
for l in read_lines[1:]:
    i = l.split(' ')
    instructions.append([i[0], int(i[1]), int(i[2]), int(i[3])])

register = [0, 0, 0, 0, 0, 0]

part_2 = True  #! does not solve, run to get big number to factor
if part_2:
    register[0] = 1

ip = register[ip_register]

run = True
while run:
    register[ip_register] = ip
    instruction = instructions[ip]
    register = eval(instruction[0])(a=instruction[1], b=instruction[2], c=instruction[3], register=register)
    ip = register[ip_register]
    ip += 1
    if ip >= len(instructions):
        run = False
        print('HALT!')
        print(f'register 0 contains: {register[0]}')
        break
    if part_2:
        print(f'ip={ip} {register}')  # see the initialization
        if register[ip_register] == 1:
            print('initialization complete')
            init_number = register[3]
            print(f'number to sum factors of is: {init_number}')
            break

#! part 2
if part_2:
    # the program tries to find all factors of a large initialized number
    # i learned this from jpaulson: https://www.youtube.com/watch?v=74vojWBORpo
    # the answer is the sum of all factors of the initialized number

    # my input number was 10,551,425
    factors = [n for n in range(1, init_number+1) if init_number % n == 0]
    print(f'part 2: {sum(factors)}')


#%%
print()
print('⭐ ⭐')