#%%
f = 'data/day02.txt'

with open(file=f) as input:
    read_lines = input.readlines()
read_lines = [l.strip() for l in read_lines]
print('🎅 🎄 🤶')
#%%
count_2x = 0
count_3x = 0
for l in read_lines:
    found_2x = False
    found_3x = False
    for c in set(l):
        count_c = l.count(c)
        if count_c == 2:
            found_2x = True
        elif count_c == 3:
            found_3x = True
    if found_2x:
        count_2x += 1
    if found_3x:
        count_3x += 1
print(f'checksum: {count_2x*count_3x}')
#%%
#* copilot answer
from collections import Counter

twos = 0
threes = 0

for x in read_lines:
    c = Counter(x)
    if 2 in c.values():
        twos += 1
    if 3 in c.values():
        threes += 1
print(f'checksum: {twos*threes}')
#%% 
#! part 2
for i,l1 in enumerate(read_lines):
    for l2 in read_lines[i:]:
        for j in range(len(l1)):
            if l1 != l2:
                if l1[:j] +l1[j+1:] == l2[:j] +l2[j+1:]:
                    print(f'difference at {j} {l1[j]} vs {l2[j]}')
                    print(f'common letters: {l1[:j] +l1[j+1:]}')
                    break
#%%
#* copilot answer
for i,l1 in enumerate(read_lines):
    for l2 in read_lines[i:]:
        if sum([x!=y for x,y in zip(l1,l2)]) == 1:
            print(f'{l1}, {l2}')
            print(f'common letters: {"".join([x for x,y in zip(l1,l2) if x==y])}')
            break

#%%
print()
print('⭐ ⭐')