#%%
from copy import deepcopy

f = 'data/day24.txt'

with open(file=f) as input:
    read_lines = input.readlines()
read_lines = [line.strip() for line in read_lines]
print('🐟 🎄 🦈')
#%%
wires = {}
gates = {}
z_out = {}
x_in = {}
y_in = {}
for l in read_lines:
    if ':' in l:
        n,v = l.split(': ')
        wires[n] = int(v)
        if n.startswith('x'):
            x_in[n] = int(v)
        elif n.startswith('y'):
            y_in[n] = int(v)

    elif '->' in l:
        i,o = l.split(' -> ')
        i0,op,i1 = i.split()
        if op == 'AND':
            op = '&'
        elif op == 'OR':
            op = '|'
        elif op == 'XOR':
            op = '^'

        gates[o] = f'wires["{i0}"] {op} wires["{i1}"]'
        if o.startswith('z'):
            z_out[o] = None  # no z in i0 or i1
        if o not in wires:
            wires[o] = None
        if i0 not in wires:
            wires[i0] = None
        if i0 not in wires:
            wires[i1] = None

x_in = dict(sorted(x_in.items(),reverse=True))
y_in = dict(sorted(y_in.items(),reverse=True))
bin_x = ''.join(map(str,x_in.values()))
bin_y = ''.join(map(str,y_in.values()))
dec_x = int(bin_x,2)
dec_y = int(bin_y,2)
x_y = dec_x + dec_y


print('bin x:', bin_x)
print('\tx:',dec_x)
print('bin y:', bin_y)
print('\ty:',dec_y)
print('sum:',x_y)

#%%
def z_solve(z_out, wires, gates):
    z_out = deepcopy(z_out)
    wires = deepcopy(wires)
    gates = deepcopy(gates)
    while None in z_out.values():
        for g,op_eval in gates.items():
            if wires[g] != None: continue
            w0,o,w1 = op_eval.split()
            if eval(w0) != None and eval(w1) != None:
                gate_eval = eval(op_eval)
                assert gate_eval in [0,1]
                wires[g] = gate_eval
                if g.startswith('z'):
                    z_out[g] = gate_eval
    z_out = dict(sorted(z_out.items(),reverse=True))
    bin_z = ''.join(map(str,z_out.values()))
    dec_z = int(bin_z,2)
    print('bin z:', bin_z)
    print('\tz:',dec_z)
    if dec_z == x_y:
        return True
    return False
#%%
#* par1
_ = z_solve(z_out, wires, gates)
#%%
# wrong = 1
# while wrong:
#     swap_gates = deepcopy(gates)

#%%
from itertools import combinations
# len(list(combinations(gates,8)))  # crash and burn!
#%%
