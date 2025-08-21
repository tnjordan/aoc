#%%
f = 'data/day01.txt'

with open(file=f) as input:
    read_lines = input.readlines()
read_lines = [l.strip() for l in read_lines]
print('🎅 🎄 🤶')
#%%
stairs = read_lines[0]
ups = stairs.count('(')
downs = stairs.count(')')

print(f'🎅 should go to floor: {ups-downs}')

#%%
#! part 2

santa = 0
for i, s in enumerate(stairs):
    if s == '(':
        santa += 1
    elif s == ')':
        santa -= 1
    if santa == -1:
        print(f'🎅 should go to basement at step: {i+1}')
        break
#%%
print()
print('⭐ ⭐')
