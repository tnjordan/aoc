
#%%
from itertools import combinations
from day05_intcode_computer import intcode_computer

f = 'data/day7.txt'
with open(f) as input:
    read_lines = input.readlines()
data = read_lines[0].strip().split(sep=',')
data = [int(x) for x in data]
# memory_init = data.copy()
# %%

#* make all combinations of
# phase_options = combinations(range(5),5)
phase_options = [(3,1,2,4,0)]

max_amp_output = float('-inf')
for phase_o in phase_options:
    # phase_a, phase_b, phase_c, phase_d, phase_e = phase_o
    amp_input = 0
    for i, phase in enumerate(phase_o):
        print(f'at phase: {phase} for amp number {i}')
        memory_init = data.copy() #* init memory
        _, memory_state = intcode_computer(input=phase, memory=memory_init)
        amp_output, _ = intcode_computer(input=amp_input, memory=memory_state)
        amp_input = amp_output
        print(amp_input)
    if amp_output > max_amp_output:
        max_amp_output = amp_output
        max_amp_phases = phase_o
print(f'max output: {max_amp_output} at phases: {phase_o}')

# %%
