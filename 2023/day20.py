#%%
from collections import deque
from math import lcm

f = 'data/day20.txt'
# f = 'data/day20.ex'

with open(file=f) as input:
    read_lines = input.readlines()
read_lines = [line.strip() for line in read_lines]
print('❄️⛄❄️')
#%%
class Module:
    def __init__(self, name, type, outputs):
        self.name = name
        self.type = type
        self.outputs = outputs
        if type == '%':
            self.memory = 'off'
        else:
            self.memory = {}
    def __repr__(self):
        return  f'{self.name} type: {self.type}, outputs: {self.outputs}, memory: {self.memory}'
            
modules = {}
broadcast_targets = []

for line in read_lines:
    l, r = line.split(' -> ')
    outputs = r.split(', ')
    if l == 'broadcaster':
        broadcast_targets = outputs
    else:
        type = l[0]
        name = l[1:]
        modules[name] = Module(name, type, outputs)

for name, module in modules.items():
    for output in module.outputs:
        if output in modules and modules[output].type == '&':
            modules[output].memory[name] = 'lo'
#%%

(feed,) = [name for name, module in modules.items() if 'rx' in module.outputs]

cycle_lengths = {}
seen = {name: 0 for name, module in modules.items() if feed in module.outputs}

cycles = lo = hi = 0
while not all(seen.values()):
    cycles += 1
    lo += 1
    # origin, target, pulse
    q = deque([('broadcaster', x, 'lo') for x in broadcast_targets])
    
    while q:
        origin, target, pulse = q.popleft()
        if pulse == 'lo':
            lo += 1
        else:
            hi += 1
        
        if target not in modules:
            continue
        
        module = modules[target]
        
        if module.name == feed and pulse == 'hi':
            seen[origin] += 1
            
            if origin not in cycle_lengths:
                cycle_lengths[origin] = cycles
            else:
                assert cycles == seen[origin] + cycle_lengths[origin]
        
        if all(seen.values()):
            print(cycle_lengths)
            x = 1
            for cycle in cycle_lengths.values():
                x = lcm(x, cycle)
            print(f'Part 2: {x}')
            break
        
        if module.type == '%':
            if pulse == 'lo':
                module.memory = 'on' if module.memory == 'off' else 'off'
                outgoing = 'hi' if module.memory == 'on' else 'lo'
                for x in module.outputs:
                    q.append((module.name, x, outgoing))
        else:
            module.memory[origin] = pulse
            outgoing = 'lo' if all (x == 'hi' for x in module.memory.values()) else 'hi'
            for x in module.outputs:
                q.append((module.name, x, outgoing))
    if cycles == 1000:
        print(f'Part 1: {hi*lo}')
#%%
#* solution from HyperNeutrino: https://www.youtube.com/watch?v=lxm6i21O83k
