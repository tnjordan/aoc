#%%
from itertools import permutations
f = 'data/day13.txt'

with open(file=f) as input:
    read_lines = input.readlines()
read_lines = [l.strip() for l in read_lines]
print('🎅 🎄 🤶')
#%%
fam = {}
for l in read_lines:
    l = l.replace('lose ', '-')
    l = l.replace('gain ', '+')
    l = l[:-1]
    l = l.split()
    if l[0] not in fam:
        fam[l[0]] = {}
    fam[l[0]][l[-1]] = int(l[2])

members = fam.keys()
table_orders = permutations(members)

happenis = []
for t_o in table_orders:
    h = 0
    for i in range(len(t_o)):
        h += fam[t_o[i]][t_o[(i+1) % len(t_o)]]
        h += fam[t_o[i]][t_o[(i-1) % len(t_o)]]
    happenis.append(h)

print(f'max happenis: {max(happenis)}') #* works on example

#%%
#! part 2

fam['Todd'] = {} # init self
for f in members:
    fam['Todd'][f] = 0
    fam[f]['Todd'] = 0

members = fam.keys()
table_orders = permutations(members)

happenis = []
for t_o in table_orders:
    h = 0
    for i in range(len(t_o)):
        h += fam[t_o[i]][t_o[(i+1) % len(t_o)]]
        h += fam[t_o[i]][t_o[(i-1) % len(t_o)]]
    happenis.append(h)

print(f'max happenis: {max(happenis)}') #* works on example

#%%
print()
print('⭐ ⭐')
