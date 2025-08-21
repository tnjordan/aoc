#%%
from collections import defaultdict
from itertools import permutations
f = 'data/day09.txt'

with open(file=f) as input:
    read_lines = input.readlines()
read_lines = [l.strip() for l in read_lines]
print('🎅 🎄 🤶')
#%%
points = set()
dist = defaultdict(dict)

for l in read_lines:
    l = l.split()
    a = l[0]
    b = l[2]
    d = int(l[-1])
    points.add(a)
    points.add(b)
    dist[a][b] = d
    dist[b][a] = d

trips = []
for perm in permutations(points):
    trip = 0
    start = perm[0]
    for end in perm[1:]:
        trip += dist[start][end]
        start = end
    trips.append(trip)

print(f'min trip: {min(trips)}')
print(f'max trip: {max(trips)}')

#%%
print()
print('⭐ ⭐')
