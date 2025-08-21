#%%
from collections import deque
f = 'data/day12.txt'

with open(file=f) as input:
    read_lines = input.readlines()
read_lines = [line.strip() for line in read_lines]
print('❄️⛄❄️')
#%%
connections = {}
for line in read_lines:
    p, ps = line.split(' <-> ')
    connections[int(p)] = [int(x) for x in ps.split(',')]

q = deque()
q.append(0)

group = set()
while q:
    for p in connections[q.pop()]:
        if p not in group:
            group.add(p)
            q.append(p)
print(f'group 0 programs: {len(group)}')
#%%
#! part 2

group = set()
groups = set()
group_count = 0
difference = set(connections).difference(groups)
while difference:
    group_count += 1
    q = deque()
    q.append(difference.pop())

    group = set()
    while q:
        for p in connections[q.pop()]:
            if p not in group:
                group.add(p)
                q.append(p)
    groups = groups | group
    difference = set(connections).difference(groups)
print(f'there are {group_count} groups')
#%%
