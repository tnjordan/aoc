#%%
f = 'data/day03.txt'

with open(file=f) as input:
    read_lines = input.readlines()
read_lines = [l.strip() for l in read_lines]
print('🎅 🎄 🤶')
#%%
instructions = read_lines[0]
directions = {'^': (0, 1), 'v': (0, -1), '>': (1, 0), '<': (-1, 0)}

houses = set()

santa = (0, 0)
houses.add(santa)
for i in instructions:
    dx, dy = directions[i]
    santa = (santa[0] + dx, santa[1] + dy)
    houses.add(santa)

print(f'🎅 delivers to {len(houses)} houses')
#%%
#! part 2

santa = (0, 0)
robot = (0, 0)

houses = set()
houses.add(santa)

for c, i in enumerate(instructions):
    dx, dy = directions[i]
    if c % 2 == 0:
        santa = (santa[0] + dx, santa[1] + dy)
        houses.add(santa)
    else:
        robot = (robot[0] + dx, robot[1] + dy)
        houses.add(robot)

print(f'🎅 and 🤖 deliver to {len(houses)} houses')
#%%
print()
print('⭐ ⭐')
