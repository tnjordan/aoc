#%%
import math

f = 'data/day08.txt'
# f = 'data/day08.ex'

with open(file=f) as input:
    read_lines = input.readlines()
read_lines = [line.strip() for line in read_lines]
print('❄️⛄❄️')
#%%
# 🐛 super bug! had 1 for L and 0 for R which sends you into an infinite loop
# still think 0, 1 was a clever choice, but the 🐛 in the rush got me
directions = [0 if d == 'L' else 1 for d in read_lines[0]]

map = {}
for line in read_lines[2:]:
    line = line.split(' = ')
    map[line[0]] = line[1][1:-1].split(', ')

steps = 0
node = 'AAA'
while node != 'ZZZ':
    for direction in directions:
        node = map[node][direction]  # direction is 0 or 1 -> L or R
        steps += 1
        if node == 'ZZZ':
            print('🐫🐫🐫')
            break
print(f'AAA -> ZZZ in {steps} steps')

#%%
#! part 2
ghost_nodes = []
for node in map:
    if node.endswith('A'):  # ghost starting nodes
        ghost_nodes.append(node)

steps = 0
all_z_cycles = False  # when all ghosts have found a cycle
# key z node seen/visited by ghost, value is steps when seen
# input was provided such that seen_nodes was same as cycle
# from z to z, so you would only need to know how long to z first time.
# I also tracked with dictionaries thinking the ghosts might have cycles
# of different lengths to different z nodes. This was not the case, each
# ghost had one z node that it cycled to.
seen_nodes = [{} for _ in range(len(ghost_nodes))]
# key z node seen again by ghost, values is cycle length of between first and second sighting
cycle_nodes = [{} for _ in range(len(ghost_nodes))]
while not all_z_cycles:
    for direction in directions:
        steps += 1
        for i, node in enumerate(ghost_nodes):
            ghost_nodes[i] = map[node][direction]
            if ghost_nodes[i].endswith('Z'):
                if ghost_nodes[i] in seen_nodes[i] and ghost_nodes[i] not in cycle_nodes[i]:
                    print(f'👻 {i} visited {ghost_nodes[i]} again!')
                    cycle_nodes[i][ghost_nodes[i]] = steps - seen_nodes[i][ghost_nodes[i]]
                    print(f'\t👻 cycle: {cycle_nodes[i][ghost_nodes[i]]}')
                    continue
                else:
                    seen_nodes[i][ghost_nodes[i]] = steps

    for cycle in cycle_nodes:
        if cycle != {}:
            continue
        else:
            break
    else:
        all_z_cycles = True
        print('🐫🐫🐫')

# least common multiple of all cycles
cycles = [list(cycle_nodes[i].values())[0] for i in range(len(ghost_nodes))]
lcm_cycles = math.lcm(*cycles)

print(f'ghost end on Z in {lcm_cycles} steps')
#%%
