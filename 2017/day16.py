#%%
f = 'data/day16.txt'

with open(file=f) as input:
    read_lines = input.readlines()
read_lines = [line.strip() for line in read_lines]
print('❄️⛄❄️')
#%%
dance_moves = read_lines[0].split(',')
dance_floor = [chr(ord('a') + i) for i in range(16)]


def spin(n):
    global dance_floor
    dance_floor = dance_floor[-n:] + dance_floor[:-n]


def exchange(a, b):
    global dance_floor
    dance_floor[a], dance_floor[b] = dance_floor[b], dance_floor[a]


def partner(a, b):
    global dance_floor
    a = dance_floor.index(a)
    b = dance_floor.index(b)
    exchange(a, b)


for move in dance_moves:
    if move[0] == 's':
        spin(int(move[1:]))
    elif move[0] == 'x':
        a, b = move[1:].split('/')
        exchange(int(a), int(b))
    elif move[0] == 'p':
        a, b = move[1:].split('/')
        partner(a, b)
print(f'programs end dance as: {"".join(dance_floor)}')

#%%
#! part 2
#! reset the dance floor
dance_floor = [chr(ord('a') + i) for i in range(16)]
seen = []
cycle = 0
while True:
    seen.append("".join(dance_floor))
    for move in dance_moves:
        if move[0] == 's':
            spin(int(move[1:]))
        elif move[0] == 'x':
            a, b = move[1:].split('/')
            exchange(int(a), int(b))
        elif move[0] == 'p':
            a, b = move[1:].split('/')
            partner(a, b)
    cycle += 1
    if "".join(dance_floor) in seen:
        break

cycle_floor = "".join(dance_floor)
print(f'programs cycle dance as: {"".join(dance_floor)}')
cycle_end = len(seen)
cycle_start = seen.index(cycle_floor)
cycle_length = cycle_end - cycle_start
# cycle = cycle length because dance repeats from the start
print(f'cycle length: {cycle_length}') 

remaining_cycles = (1000000000 - cycle) % cycle_length
for _ in range(remaining_cycles):
    for move in dance_moves:
        if move[0] == 's':
            spin(int(move[1:]))
        elif move[0] == 'x':
            a, b = move[1:].split('/')
            exchange(int(a), int(b))
        elif move[0] == 'p':
            a, b = move[1:].split('/')
            partner(a, b)
print(f'programs end dance as: {"".join(dance_floor)}')
#%%
