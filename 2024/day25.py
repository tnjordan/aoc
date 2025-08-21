#%%
f = 'data/day25.txt'
# f = 'data/da25.ex'

with open(file=f) as input:
    read_lines = input.readlines()
read_lines = [line.strip() for line in read_lines]
print('🐟 🎄 🦈')
#%%
keys = []
locks = []
new_key = []
new_lock = []
for l in read_lines:
    print(l)
    if l == '':
        if new_key:
            keys.append(new_key)
            new_key = []
        if new_lock:
            locks.append(new_lock)
            new_lock = []
    if new_key:
        for j,c in enumerate(l):
            if c == '#':
                new_key[j] += 1
    elif new_lock:
        for j,c in enumerate(l):
            if c == '#':
                new_lock[j] += 1
    elif l == '.....':
        new_key = [0,0,0,0,0]
    elif l == '#####':
        new_lock = [1,1,1,1,1]
#%%
possible = 0
for key in keys:
    for lock in locks:
        possible += all([1 if k + l <= 7 else 0 for k, l in zip(key, lock)])
possible
#%%