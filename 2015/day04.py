#%%
import hashlib

f = 'data/day04.txt'

with open(file=f) as input:
    read_lines = input.readlines()
read_lines = [l.strip() for l in read_lines]
print('🎅 🎄 🤶')
#%%
input = read_lines[0]

i = 0
while True:
    i += 1
    m = hashlib.md5()
    m.update(f'{input}{i}'.encode('utf-8'))
    if m.hexdigest().startswith('00000'):
        break

print(f'🎅 hash number is {i}')
#%%
#! part 2

i = 0
while True:
    i += 1
    m = hashlib.md5()
    m.update(f'{input}{i}'.encode('utf-8'))
    if m.hexdigest().startswith('000000'):
        break

print(f'🎅 hash number is {i}')

#%%
print()
print('⭐ ⭐')
