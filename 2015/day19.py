#%%
f = 'data/day19.txt'

with open(file=f) as input:
    read_lines = input.readlines()
read_lines = [l.strip() for l in read_lines]
print('🎅 🎄 🤶')
#%%
subs = []
for l in read_lines:
    if l == '':
        break
    i,o = l.split(' => ')
    subs.append((i,o))
molecule = read_lines[-1]

#%%
new_molecules = set()


#* stack overflow
def replace_nth(sub, repl, txt, nth):
    nth += 1  #* makes 0 based count
    arr = txt.split(sub)
    part1 = sub.join(arr[:nth])
    part2 = sub.join(arr[nth:])
    return part1 + repl + part2


for i, o in subs:
    for nth in range(molecule.count(i)):
        new_molecules.add(replace_nth(sub=i, repl=o, txt=molecule, nth=nth))

#%%
#? go in reverse, start with molecule and go to e
subs = {}

for l in read_lines:
    if l == '':
        break
    i,o = l.split(' => ')
    subs[o] = i #* outputs are unique
molecule = read_lines[-1]

#%%
new_molecule = molecule
count = 0
while new_molecule != 'e':  #? I think I just got lucky with the inputs
    for o, i in subs.items():
        count += new_molecule.count(o)
        new_molecule = new_molecule.replace(o, i)
    print(f'count:{count} len new molecule:{len(new_molecule)}')

#%%
print()
print('⭐ ⭐')
