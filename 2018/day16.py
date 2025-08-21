#%%
f = 'data/day16.txt'
# f = 'data/day16.ex'

with open(file=f) as input:
    read_lines = input.readlines()
read_lines = [li.strip() for li in read_lines]
print('🎅 🎄 🤶')
#%%
def addr(a, b, c, register):
    register = [x for x in register]  # prevent overwrite
    register[c] = register[a] + register[b]
    return register


def addi(a, b, c, register):
    register = [x for x in register]  # prevent overwrite
    register[c] = register[a] + b
    return register


def mulr(a, b, c, register):
    register = [x for x in register]  # prevent overwrite
    register[c] = register[a] * register[b]
    return register


def muli(a, b, c, register):
    register = [x for x in register]  # prevent overwrite
    register[c] = register[a] * b
    return register


def banr(a, b, c, register):
    register = [x for x in register]  # prevent overwrite
    register[c] = register[a] & register[b]
    return register


def bani(a, b, c, register):
    register = [x for x in register]  # prevent overwrite
    register[c] = register[a] & b
    return register


def borr(a, b, c, register):
    register = [x for x in register]  # prevent overwrite
    register[c] = register[a] | register[b]
    return register


def bori(a, b, c, register):
    register = [x for x in register]  # prevent overwrite
    register[c] = register[a] | b
    return register


def setr(a, b, c, register):
    register = [x for x in register]  # prevent overwrite
    register[c] = register[a]
    return register


def seti(a, b, c, register):
    register = [x for x in register]  # prevent overwrite
    register[c] = a
    return register


def gtir(a, b, c, register):
    register = [x for x in register]  # prevent overwrite
    register[c] = 1 if a > register[b] else 0
    return register


def gtri(a, b, c, register):
    register = [x for x in register]  # prevent overwrite
    register[c] = 1 if register[a] > b else 0
    return register


def gtrr(a, b, c, register):
    register = [x for x in register]  # prevent overwrite
    register[c] = 1 if register[a] > register[b] else 0
    return register


def eqir(a, b, c, register):
    register = [x for x in register]  # prevent overwrite
    register[c] = 1 if a == register[b] else 0
    return register


def eqri(a, b, c, register):
    register = [x for x in register]  # prevent overwrite
    register[c] = 1 if register[a] == b else 0
    return register


def eqrr(a, b, c, register):
    register = [x for x in register]  # prevent overwrite
    register[c] = 1 if register[a] == register[b] else 0
    return register

#* nifty trick I learned from some bad code
funs = [addr, addi, mulr, muli, banr, bani, borr, bori, setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr]
three_or_more = 0
for i, l in enumerate(read_lines):
    if l.startswith('Before:'):
        register_before = eval(l.split(": ")[1])
        instructions = [int(x) for x in read_lines[i + 1].split()]
        register_after = eval(read_lines[i + 2].split(": ")[1])
        fun_count = 0
        for fun in funs:
            if register_after == fun(instructions[1], instructions[2], instructions[3], register_before):
                fun_count += 1
                # print(fun.__name__)
                # print(f'fun_count: {fun_count}')
                if fun_count == 3:
                    three_or_more += 1
                    # print('+1')
                    break
print(f'part 1: {three_or_more}')

#%%
#! part 2

opt_code_options = {}
for i in range(16):
    opt_code_options[i] = set([addr, addi, mulr, muli, banr, bani, borr, bori, setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr])

funs = [addr, addi, mulr, muli, banr, bani, borr, bori, setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr]
three_or_more = 0
for i, l in enumerate(read_lines):
    if l.startswith('Before:'):
        register_before = eval(l.split(": ")[1])
        instructions = [int(x) for x in read_lines[i + 1].split()]
        register_after = eval(read_lines[i + 2].split(": ")[1])
        fun_count = 0
        for fun in funs:
            if register_after == fun(instructions[1], instructions[2], instructions[3], register_before):
                fun_count += 1
                # print(fun.__name__)
                # print(f'fun_count: {fun_count}')
            else:
                try:
                    opt_code_options[instructions[0]].remove(fun)
                except KeyError:
                    pass

#* the opt_code_options still had options, needed to solve puzzle
#* lucky one of the opt codes had only one option 
opt_codes = {}
for i in range(16):
    opt_codes[i] = None

for i in range(10):  #worked with for loop, was going to use while but inf loop :(
    for k, v in opt_code_options.items():
        if len(v) == 1:
            fun = v.pop()
            opt_codes[k] = fun
            for k2, v2 in opt_code_options.items():
                if k != k2 and fun in v2:
                    opt_code_options[k2].remove(fun)

#! solve the puzzle
register = [0, 0, 0, 0]

go_time = False
for i, l in enumerate(read_lines):
    if not go_time and l == '' and read_lines[i-2] == '':  # finds the triple '' lines
        go_time = True
    elif go_time:
        instructions = [int(x) for x in l.split()]
        register = opt_codes[instructions[0]](instructions[1], instructions[2], instructions[3], register)

print(register)
print(f'part 2: {register[0]}')
#%%
print()
print('⭐ ⭐')
