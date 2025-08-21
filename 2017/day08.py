#%%
from collections import defaultdict

f = 'data/day08.txt'

with open(file=f) as input:
    read_lines = input.readlines()
read_lines = [line.strip() for line in read_lines]
print('❄️⛄❄️')
#%%
max_reg = 0
register = defaultdict(int)

for instruction in read_lines:
    change, condition = instruction.split('if')
    reg, inc_dec, shift = change.split()
    shift = int(shift) * (-1 if inc_dec == 'dec' else 1)

    con_reg, equality, value = condition.split()
    condition = f'register["{con_reg}"] {equality} {value}'

    if eval(condition):
        register[reg] += shift
        max_reg = max(max_reg, register[reg])

print(f'max register at termination: {max(register.values())}')
print(f'max register during processing: {max_reg}')

#%%
