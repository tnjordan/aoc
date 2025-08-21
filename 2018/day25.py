#%%
from collections import deque

f = 'data/day25.txt'

with open(file=f) as input:
    read_lines = input.readlines()
read_lines = [l.strip() for l in read_lines]
print('🎅 🎄 🤶')
#%%
coords = []
for l in read_lines:
    coords.append([int(i) for i in l.split(',')])


def manhattan_distance(a, b):
    man_d = 0
    for i,j in zip(a,b):
        man_d += abs(i-j)
    if man_d <= 3:
        return True
    return False


constellations = []
for i in range(len(coords)):
    for j in range(i+1, len(coords)):
        if manhattan_distance(coords[i], coords[j]):
            constellations.append([i,j])
constellations = deque(constellations)

seen = set()
const = []
for i in range(len(coords)):
    if i not in seen:
        new_const = []
        new_star_queue = deque([i])
        while new_star_queue:
            star = new_star_queue.popleft()
            seen.add(star)
            new_const.append(star)
            for c in list(constellations):
                if star in c:
                    constellations.remove(c)
                    new_star_queue.append([s for s in c if s != star][0])
        const.append(new_const)

print(f'there are {len(const)} constellations')
#%%
# print()
# print('⭐ ⭐')
