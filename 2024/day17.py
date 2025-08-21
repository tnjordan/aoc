#%%
f = 'data/day17.txt'
f = 'data/da17.ex'

with open(file=f) as input:
    read_lines = input.readlines()
read_lines = [line.strip() for line in read_lines]
print('🐟 🎄 🦈')
#%%
regs = {}
for l in read_lines:
    if 'Register' in l:
        _,r,v = l.split()
        regs[r[:-1].lower()] = int(v)
    elif 'Program: ' in l:
        l = l.lstrip('Program: ')
        prog = list(map(int, l.split(',')))
#%%
def combo_operand_value(operand):
    if operand in (0,1,2,3):
        return operand
    elif operand == 4:
        return regs['a']
    elif operand == 5:
        return regs['b']
    elif operand == 6:
        return regs['c']
    assert False

def adv(combo):
    combo = combo_operand_value(combo)
    num = regs['a']
    denom = 2**combo
    res = int(num/denom)
    regs['a'] = res

def bxl(literal):
    res = regs['b'] ^ literal
    regs['b'] = res

def bst(combo):
    combo = combo_operand_value(combo)
    res = combo%8
    regs['b'] = res

def jnz(literal):
    global pointer
    if regs['a'] != 0:
        pointer = literal
        return 1  #? need handle no += 2 for pointer

def bxc(legacy_ignore_it):
    bxl(regs['c'])  # verifys

def out(combo):
    global output
    combo = combo_operand_value(combo)
    res = combo%8
    output.append(res)

def bdv(combo):
    combo = combo_operand_value(combo)
    num = regs['a']
    denom = 2**combo
    res = int(num/denom)
    regs['b'] = res

def cdv(combo):
    combo = combo_operand_value(combo)
    num = regs['a']
    denom = 2**combo
    res = int(num/denom)
    regs['c'] = res

opcodes = {
    0:adv,
    1:bxl,
    2:bst,
    3:jnz,
    4:bxc,
    5:out,
    6:bdv,
    7:cdv
}
#%%
def run_program(regs, par2=False):
    global pointer 
    pointer = 0
    global output 
    output = []
    #? detect inf loops?
    while 0 <= pointer < len(prog):
        # print(f'pointer {pointer}')
        opcode = prog[pointer]
        operand = prog[pointer+1]
        fun = opcodes[opcode]
        # print(f'\topcode: {opcode} fun:{fun.__name__} operand:{operand}')
        if not fun(operand):
            pointer += 2
        
        if par2 and opcode == 5:
            if output != prog[:len(output)]:
                return output #! no need to continue
        # print(f'\t{regs}')
    # print(','.join(map(str,output)))
    return output
run_program(regs)  # part 1
#%%
a = 0
while output != prog:
    a += 1
    # reset
    regs = {'a': a, 'b': 0, 'c': 0}
    output = run_program(regs, par2=True)
print(f'par2: {a}')
#%%
