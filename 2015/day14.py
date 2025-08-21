#%%
f = 'data/day14.txt'

with open(file=f) as input:
    read_lines = input.readlines()
read_lines = [l.strip() for l in read_lines]
print('🎅 🎄 🤶')
#%%
deer = {}

for l in read_lines:
    l = l.split()
    deer[l[0]] = [int(x) for x in [l[3], l[6], l[-2]]]


winner = ''
winner_d = 0
for d, stats in deer.items():
    t = 2503
    dist = 0
    runs = t // (stats[1] + stats[2])
    dist += runs * (stats[0] * stats[1])
    t -= runs * (stats[1] + stats[2])

    #* final distance
    dist += stats[0] * min(t,stats[1])
    deer[d].append(dist)

    if dist > winner_d:
        winner = d
        winner_d = dist

print(f'{winner} is the winner @ {winner_d} km.')

#%%
#! part 2

points = {}
positions = {}
for d in deer:
    points[d] = 0
    positions[d] = 0

for s in range(2503):
    for d, stats in deer.items():
        move = stats[1]
        cadence = (stats[1] + stats[2])
        if s%cadence < move:
            positions[d] += stats[0]
    
    max_p = max(positions.values()) # max(positions, key=lambda key: positions[key]) #* can't use due to tie rules 
    for d, p in positions.items():
        if p == max_p:
            points[d] += 1

winner = max(points, key=lambda key: points[key])

print(f'winner is {winner} @ {points[winner]} points.')
#%%
print()
print('⭐ ⭐')
