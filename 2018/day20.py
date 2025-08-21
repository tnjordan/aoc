#%%
f = 'data/day20.txt'
f = 'data/day20.ex'

with open(file=f) as input:
    read_lines = input.readlines()
read_lines = [l.strip() for l in read_lines]
print('🎅 🎄 🤶')
#%%
regex = read_lines[0]
regex = regex[1:-1]

#%%
# print()
# print('⭐ ⭐')