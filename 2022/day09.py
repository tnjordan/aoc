#%%
f = 'data/day09.txt'

with open(file=f) as input:
    read_lines = input.readlines()
read_lines = [l.strip() for l in read_lines]
print('🎅 🎄 🤶')

tail_history = set()
tail_history.add((0,0))
tail_pos = [0,0]
head_pos = [0,0]

head_moves = {'U':(0,1),'D':(0,-1),'R':(1,0),'L':(-1,0)}

def tail_moves(head_pos,tail_pos):
    delta_x = head_pos[0] - tail_pos[0]
    delta_y = head_pos[1] - tail_pos[1]
    manhattan = abs(delta_x) + abs(delta_y)

    if abs(delta_x) <= 1 and abs(delta_y) <= 1: #* no move
        return tail_pos
    else:
        if manhattan >= 3: #* diagonal
            tail_pos[0] += delta_x/abs(delta_x)
            tail_pos[1] += delta_y/abs(delta_y)
        elif abs(delta_x) > 1: #* linear in x
            tail_pos[0] += delta_x/abs(delta_x)
        elif abs(delta_y) > 1: #* horizontal in y
            tail_pos[1] += delta_y/abs(delta_y)
    return tail_pos

for l in read_lines:
    print(l)
    direction, quantity = l.split()
    quantity = int(quantity)
    delta_x,delta_y = head_moves[direction]
    for _ in range(quantity):
        head_pos[0] += delta_x
        head_pos[1] += delta_y
        print(f'head at: {head_pos}')
        tail_pos = tail_moves(head_pos,tail_pos)
        print(f'tail at: {tail_pos}')
        tail_history.add(tuple(tail_pos))

print(f'tail has been in {len(tail_history)} positions')

#%%
#! part 2
tail_history = set()
tail_history.add((0,0))

positions = {}
for i in range(10): #* head is now 0
    positions[i] = [0,0]

for l in read_lines:
    print()
    print('🏄',l)
    direction, quantity = l.split()
    quantity = int(quantity)
    delta_x,delta_y = head_moves[direction]
    for q in range(quantity):
        print()
        print(f'🤺 {q+1} of {quantity}')
        positions[0][0] += delta_x #* update head position
        positions[0][1] += delta_y #! AHH! BUG had positions[0][0] both times. All the emojis were for this
        for i in range(1,len(positions)): #* update all other positions
            print('⛷')
            print(f'{i-1} at: {positions[i-1]}')
            positions[i] = tail_moves(positions[i-1],positions[i])
            print(f'{i} at: {positions[i]}')
        tail_history.add(tuple(positions[len(positions)-1])) #* add tail which is last position

print(f'tail has been in {len(tail_history)} positions')
#%%
print()
print('⭐ ⭐')
# %%
