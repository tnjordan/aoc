#%%
f = 'data/day12.txt'

with open(file=f) as input:
    read_lines = input.readlines()
read_lines = [line.strip() for line in read_lines]
print('❄️⛄❄️')
#%%
ship = [0, 0, 90] # vertical, horizontal, rotation

directions = {
    'N': (1, 0),
    'E': (0, 1),
    'S': (-1, 0),
    'W': (0, -1),
    # rotation directions for F
    '0': (1, 0),
    '90': (0, 1),
    '180': (-1, 0),
    '270': (0, -1),
}

for line in read_lines:
    command = line[0]
    value = int(line[1:])
    
    if command == 'R':
        ship[2] = (ship[2] + value) % 360
        continue
    elif command == 'L':
        ship[2] = (ship[2] - value) % 360
        continue
    
    if command == 'F':
        command = str(ship[2])  # get dv, dh of current heading
    dv, dh = directions[command]
    ship[0] += dv * value
    ship[1] += dh * value

print(ship)
print(abs(ship[0]) + abs(ship[1]))
#%%
waypoint = [1, 10]
ship = [0, 0]

for line in read_lines:
    command = line[0]
    value = int(line[1:])
    
    if command in 'NSEW':
        dv, dh = directions[command]
        waypoint[0] += dv * value
        waypoint[1] += dh * value
    elif command in 'LR':
        value = value % 360
        # only clockwise turns
        if command == 'L':
            value = 360 - value
        assert value % 90 == 0
        clockwise_rotations = value // 90
        for _ in range(clockwise_rotations):
            waypoint[0], waypoint[1] = -1*waypoint[1], waypoint[0]
    elif command == 'F':
        dv,dh = waypoint
        ship[0] += dv * value
        ship[1] += dh * value
    else:
        assert False
print(ship)
print(abs(ship[0]) + abs(ship[1]))
#%%
