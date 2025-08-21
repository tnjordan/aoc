#%%
f = 'data/day01.txt'

with open(file=f) as input:
    read_lines = input.readlines()
read_lines = [li.strip() for li in read_lines]
print('🎅 🎄 🤶')
#%%

instructions = [(i[0], int(i[1:])) for i in read_lines[0].split(', ')]

turns = {
    'N': {'R': 'E', 'L': 'W'},
    'S': {'R': 'W', 'L': 'E'},
    'E': {'R': 'S', 'L': 'N'},
    'W': {'R': 'N', 'L': 'S'}
}

direction = 'N'
distance = {
    'N': 0,
    'S': 0,
    'E': 0,
    'W': 0
}

for turn, steps in instructions:
    direction = turns[direction][turn]
    distance[direction] += steps

shortest_path = abs(distance['N'] - distance['S']) + abs(distance['E'] - distance['W'])

print(f'Easter Bunny HQ is {shortest_path} blocks away!')

#%%
#! part 2
direction = 'N'
distance = {
    'N': 0,
    'S': 0,
    'E': 0,
    'W': 0
}

position = (0, 0)
previous_positions = set()

for turn, steps in instructions:
    direction = turns[direction][turn]
    for _ in range(steps):  #* Gah! need to track steps individually
        distance[direction] += 1
        position = (distance['N'] - distance['S'], distance['E'] - distance['W'])
        if position in previous_positions:
            print(f'Easter Bunny HQ is {abs(position[0]) + abs(position[1])} blocks away!')
            break
        previous_positions.add(position)
    else:  # escape the double loop
        continue
    break

#%%
print()
print('⭐ ⭐')
