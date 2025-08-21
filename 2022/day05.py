#%%
import re
from collections import deque
#%%
f = 'data/day05.txt'

with open(file=f) as input:
    read_lines = input.readlines()
read_lines = [l.strip() for l in read_lines]
print('🎅 🎄 🤶')

split_index = read_lines.index('')

crate_lines = read_lines[:split_index]
instruction_lines = read_lines[split_index+1:] #* drop empty line

def crate_locator_9001(crate_lines):
    crates = {}
    for l in crate_lines:
        l = l.ljust(35) #* prevent index errors
        for i,idx in enumerate(range(1,35,4), start=1):
            c = l[idx]
            if c.isupper():
                if i not in crates:
                    crates[i] = deque(c)
                else:
                    crates[i].append(c)
    return crates

#%%
#! part 1
crates = crate_locator_9001(crate_lines)
regex = re.compile('move (\d*) from (\d*) to (\d*)')

for l in instruction_lines:
    quantity, start, end = [int(x) for x in regex.match(l).groups()]
    for q in range(quantity):
        crates[end].appendleft(crates[start].popleft()) #* should read documentation. had append() and pop()

msg = ''
for i in range(1,len(crates)+1):
    msg += crates[i][0]

print(msg)

#%%
#! part 2
crates = crate_locator_9001(crate_lines)
for l in instruction_lines:
    quantity, start, end = [int(x) for x in regex.match(l).groups()]
    # print(l)
    # print(crates[start])
    # print(crates[end])
    crane_crates = deque()
    for q in range(quantity):
        crane_crates.appendleft(crates[start].popleft()) #* crane crates are held in reverse order of the stack.
    # print(crane_crates)
    for c in list(crane_crates):
        crates[end].appendleft(c)
    # print(crates[start])
    # print(crates[end])

msg = ''
for i in range(1,len(crates)+1):
    msg += crates[i][0]

print(msg)
#%%
print()
print('⭐ ⭐')