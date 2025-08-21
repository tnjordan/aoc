#%%
from collections import defaultdict
f = 'data/day23.txt'
# f = 'data/da23.ex'

with open(file=f) as input:
    read_lines = input.readlines()
read_lines = [line.strip() for line in read_lines]
print('🐟 🎄 🦈')
#%%
connections = defaultdict(list)
for l in read_lines:
    a,b = l.split('-')
    connections[a].append(b)
    connections[b].append(a)
#%%
threesomes = set()
dup = []
for comp, lans in connections.items():
    # print('comp',comp,'lans',lans)
    # if 't' not in comp: continue  # bug! learn to read
    if not comp.startswith('t'): continue
    for j,c1 in enumerate(lans[:-1]):
        for c2 in lans[j+1:]:
            # print('\tc1',c1,'c2',c2)
            if c2 in connections[c1]:  # and c1 in connections[c2], no need
                # other_connections = set(connections[c1]) & set(connections[c2])
                # print('other connections',other_connections)
                # for oc in other_connections:
                #     print('\t\toc',oc)
                #     if oc in lans:
                #         print('too many for a threesome')
                #         break
                # else:
                threesomes.add(tuple(sorted((comp,c1,c2))))
                dup.append((comp,c1,c2))
threesomes
print(len(threesomes))

# de_dup = [''.join(sorted(d)) for d in dup]  # working to find bug
# de_dup = set(de_dup)
# print(len(de_dup))
#%%
from collections import deque
max_lan = []
for comp, lans in connections.items():
    # print('comp',comp,'lans',lans)
    if not comp.startswith('t'): continue
    for j,c1 in enumerate(lans[:-1]):
        for c2 in lans[j+1:]:
            # print('\tc1',c1,'c2',c2)
            if c2 in connections[c1]:
                other_connections = set(connections[c1]+[c1]) & set(connections[c2]+[c2]) & set(lans+[comp])
                
                verified_solutions = set([comp,c1,c2])
                # q = deque()
                # q.append(list(other_connections))
                # while q:
                #     oc = q.popleft()
                for oc in other_connections:

                    new_oc = other_connections & set(connections[oc]+[oc])

                    if len(new_oc) == len(other_connections):
                        verified_solutions.add(oc)
    
    print(len(verified_solutions), verified_solutions)

    if len(verified_solutions) > len(max_lan):
        max_lan = verified_solutions
print(','.join(sorted(max_lan)))
                
                
                # print('other connections',other_connections)
                # print(len(other_connections))
                # if len(other_connections) > 12:
                #     print(','.join(sorted(other_connections)))
                # verified_solutions = [comp,c1,c2]
                # for oc in other_connections:
                #     print('\t\toc',oc)
                    
#%%
