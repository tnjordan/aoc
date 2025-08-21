#%%
f = 'data/day06.txt'

with open(file=f) as input:
    read_lines = input.readlines()
read_lines = [line.strip() for line in read_lines]
print('❄️⛄❄️')
#%%
memory = [int(k2) for k2 in read_lines[0].split('\t')]

memory_states = set()
memory_states.add(tuple(memory))


def redistribution(memory):
    memory = memory[:]
    banks = len(memory)
    max_mem = max(memory)
    max_idx = memory.index(max_mem)
    memory[max_idx] = 0
    for i in range(1, max_mem + 1):
        memory[(max_idx + i) % banks] += 1
    return memory


seen = False
cycles = 0
while not seen:
    cycles += 1
    memory = redistribution(memory=memory)
    if tuple(memory) in memory_states:
        seen = True
    else:
        memory_states.add(tuple(memory))
print(f'redistribution cycles: {cycles}')
#%%
#! part 2
inf_cycle = memory[:]
seen = False
cycles = 0
while not seen:
    cycles += 1
    memory = redistribution(memory=memory)
    if memory == inf_cycle:
        seen = True
print(f'infinite loop cycles: {cycles}')
#%%
