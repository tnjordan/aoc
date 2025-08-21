#%%
import re
f = 'data/day07.txt'
# f = 'data/day07.ex'

with open(file=f) as input:
    read_lines = input.readlines()
read_lines = [l.strip() for l in read_lines]
print('🎅 🎄 🤶')
#%%
cmd_map = { 'AND':'&',
            'OR':'|',
            'RSHIFT':'>>',
            'LSHIFT':'<<',
            'NOT':'~'}
wires = {}
solved = []
for l in read_lines:
    i,o = l.split(' -> ')
    i_deps = re.findall('[a-z]+',i)
    if i_deps == []:
        i_deps = None
        i = int(i)
        solved.append(o)
        wires[o] = i
    else:
        for c,c_sym in cmd_map.items():
            if c in i:
                i = i.replace(c,c_sym)
                if c == 'NOT':
                    i += ' & 0xffff' #* from reddit, to make the NOT work
                break
        i = i.split()
        for i_dep in i_deps:
            for idx, i_val in enumerate(i):
                if i_val == i_dep:
                    i[idx] = f'wires["{i_dep}"]' #* oh the dangers of replace
        wires[o] = ' '.join(i)

#%%
part_2 = True
if part_2:
    wires['b'] = 16076 #* a answer of part 1

while type(wires['a']) is not int:
    for o,i in wires.items():
        if type(i) is int:
            continue
        try:
            wires[o] = eval(i)
            # print(f'o: {o} \t\t i: {i} \t\t wires[o]: {wires[o]}')
            if type(wires[o]) is int: #* used during debug
                solved.append(o)
        except Exception as e:
            # print(f'Error: ', e)
            pass

print(f'wire a: {wires["a"]}')


#%%
print()
print('⭐ ⭐')
