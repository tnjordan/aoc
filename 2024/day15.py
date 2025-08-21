#%%
from tabulate import tabulate as gp
from collections import deque

f = 'data/day15.txt'
# f = 'data/da15.ex'  # works on example need wifi to submit
# f = 'data/da15.ex2'  # par2 works here

with open(file=f) as input:
    read_lines = input.readlines()
read_lines = [line.strip() for line in read_lines]
print('🐟 🎄 🦈')
#%%
direcions = ''
grid = []
robo = ()

for l in read_lines:
    l = l.replace('#','##')
    l = l.replace('.','..')
    l = l.replace('O', '[]')
    l = l.replace('@', '@.')
    if '#' in l:
        grid.append(list(l))
        if '@' in l:
            robo = (len(grid)-1,l.find('@'))
    else:
        direcions += l

print(gp(grid))

# easier here
walls = set()
lef_boxes = set()
righ_boxes = set()
# box_id = 0
for j,row in enumerate(grid):
    for i,c in enumerate(row):
        if c == '[':
            # boxes[box_id] = (j,i)
            # box_id += 1
            lef_boxes.add((j,i))
        elif c == ']':
            righ_boxes.add((j,i))
        elif c == '#':
            walls.add((j,i))

dir_map = {
    '^': (-1,0),
    'v': (1,0),
    '>': (0,1),
    '<': (0,-1)
}

J = len(grid)
I = len(grid[0])

def grid_disp(walls, robo, lef_boxes, righ_boxes):
    grid = [['⬛' for _ in range(I)] for _ in range(J)]
    for j,i in walls:
        assert grid[j][i] == '⬛'
        grid[j][i] = '🧱'
    for j,i in [(robo)]:
        assert grid[j][i] == '⬛'
        grid[j][i] = '🤖'
    for j,i in lef_boxes:
        assert grid[j][i] == '⬛'
        grid[j][i] = '🎁'
    for j,i in righ_boxes:
        assert grid[j][i] == '⬛'
        grid[j][i] = '📦'
    for g in grid:  # more compact
        print(''.join(g))
#%%
def push(d,robo):
    j,i = robo
    dj,di = dir_map[d]
    j_dj = j+dj
    i_di = i+di

    if (j_dj,i_di) in walls:
        return (j,i)  # no move
    elif (j_dj,i_di) not in (lef_boxes | righ_boxes):
        return (j_dj, i_di)  # no box or wall move
    else:
        boxes_could_move = []
        moving_boxes = deque()
        # are we moving a lef or righ box
        if (j_dj,i_di) in lef_boxes:
            print('hit lef box!')
            moving_boxes.append(((j_dj,i_di),(j_dj,i_di+1)))
        elif (j_dj,i_di) in righ_boxes:
            print('hit righ box!')
            moving_boxes.append(((j_dj,i_di-1),(j_dj,i_di)))

        # too move need an empty space ahead of all boxes
        while moving_boxes:
            print('moving boxes:', moving_boxes)
            mb = moving_boxes.popleft() # 
            boxes_could_move.append(mb)  # boxes that will need to move if possible
            print('boxes_could_move:', boxes_could_move)
            for mb_j, mb_i in mb:
                mb_j_dj = mb_j + dj
                mb_i_di = mb_i + di
                if (mb_j_dj,mb_i_di) in mb:
                    print('same box')
                    continue
                elif (mb_j_dj, mb_i_di) not in walls and (mb_j_dj, mb_i_di) not in (lef_boxes | righ_boxes):
                    print('continue  # empty space, this part of box can move')
                    continue  # empty space, this part of box can move
                elif (mb_j_dj, mb_i_di) in walls:
                    print('no move, box hit wall')
                    return (j,i)  # no move, box hit wall
                elif (mb_j_dj,mb_i_di) in lef_boxes:
                    if ((mb_j_dj,mb_i_di),(mb_j_dj,mb_i_di+1)) not in boxes_could_move:
                        print('box chain react on left')
                        moving_boxes.append(((mb_j_dj,mb_i_di),(mb_j_dj,mb_i_di+1)))
                elif (mb_j_dj,mb_i_di) in righ_boxes:
                    if ((mb_j_dj,mb_i_di-1),(mb_j_dj,mb_i_di)) not in boxes_could_move:
                        print('box chain react on right')
                        moving_boxes.append(((mb_j_dj,mb_i_di-1),(mb_j_dj,mb_i_di)))
        
        moving_order = list(set(boxes_could_move))  # two box halves could move same box
        if d in '^':
            # move up -> down
            moving_order = sorted(moving_order, key=lambda tup: tup[1], reverse=False)
        elif d in 'v':
            # move down -> up
            moving_order = sorted(moving_order, key=lambda tup: tup[1], reverse=True)
        print('moving ',len(moving_order),' boxes: ', moving_order)
        for (lb_j, lb_i), (rb_j, rb_i) in moving_order:
            print('moving box: ', (lb_j, lb_i), (rb_j, rb_i))
            
            lb_j_dj = lb_j + dj
            lb_i_di = lb_i + di
            rb_j_dj = rb_j + dj
            rb_i_di = rb_i + di

            print('\tto: ', (lb_j_dj,lb_i_di), (rb_j_dj,rb_i_di))

            lef_boxes.remove((lb_j, lb_i))
            righ_boxes.remove((rb_j, rb_i))

            # combining boxes on moving day
            assert (lb_j_dj,lb_i_di) not in lef_boxes
            assert (rb_j_dj,rb_i_di) not in righ_boxes

            lef_boxes.add((lb_j_dj,lb_i_di))
            righ_boxes.add((rb_j_dj,rb_i_di))
    
    return (j_dj, i_di)  # robo and boxes move
#%%
d_idx = -1
grid_disp(walls, robo, lef_boxes, righ_boxes)
#%%
#! debug code - run one by one
# print(len(lef_boxes))
# for _ in range(len(direcions)):
#     d_idx += 1
#     d = direcions[d_idx]
#     print('command: ', d, ' idx: ', d_idx)
#     robo = push(d, robo)
#     grid_disp(walls, robo, lef_boxes, righ_boxes)
#     print('')
# print(len(lef_boxes))
#%%
for d in direcions:
    print(d, robo)
    robo = push(d, robo)

#%%
sum([j*100+i for (j,i) in lef_boxes])
#%%
