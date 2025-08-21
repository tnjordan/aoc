#%%
f = 'data/day14.txt'
# f = 'data/day14.ex'

with open(file=f) as input:
    read_lines = input.readlines()
read_lines = [l.strip() for l in read_lines]
print('🎅 🎄 🤶')

read_lines = [x.split(' -> ') for x in read_lines]

scan = []
for r in read_lines:
    scan_r = []
    for c in r:
        scan_r.append([int(i) for i in c.split(',')])
    scan.append(scan_r)

#* build map
rock_positions = set()
sand_positions = set()

min_x = float('inf')
max_x = float('-inf')
max_y = float('-inf')
for seam in scan:
    # print(seam)
    for corner1,corner2 in zip(seam[:-1], seam[1:]): #* for index bounds
        # print('\t',corner1,corner2)
        x1,y1 = corner1
        x2,y2 = corner2
        min_x = min(min_x,x1,x2)
        max_x = max(max_x,x1,x2)
        max_y = max(max_y,y1,y2)
        for x in range(min(x1,x2),max(x1,x2)+1):
            rock_positions.add((x,y1))
        # print(rock_positions)
        for y in range(min(y1,y2),max(y1,y2)+1):
            rock_positions.add((x1,y))
        # print(rock_positions)

def sands_of_time(rock_positions,sand_positions,min_x,max_x,max_y,start=(500,0)):
    blocked = rock_positions | sand_positions
    s_x,s_y = start
    moves = [(0,1), (-1,1), (1,1)] #* down, diag-left, diag-right
    rest = False
    while rest is False:
        for d_x, d_y in moves:
            # print(f'd_x:{d_x} d_y:{d_y}')
            # print(f'next move: {(s_x + d_x, s_y + d_y)}')
            if not min_x <= s_x + d_x <= max_x:
                print('over the edge of the world')
                return False
            elif s_y + d_y > max_y:
                print('oh sh!t there is a hole in the floor')
                return False
            elif (s_x + d_x, s_y + d_y) not in blocked:
                s_x += d_x
                s_y += d_y
                rest = False
                break
            else:
                rest = True
    return (s_x,s_y)

# for i in range(20):
#     s_p = sands_of_time(rock_positions,sand_positions)
#     print(f'resting sand at: {s_p}')
#     if s_p:
#         sand_positions.add(s_p)
#     else:
#         print(s_p)

#! part 1
s_p = True
while s_p:
    s_p = sands_of_time(rock_positions,sand_positions,min_x,max_x,max_y)
    # print(f'resting sand at: {s_p}')
    if s_p:
        sand_positions.add(s_p)
    else:
        print('all full')
        print(f'{len(sand_positions)} grains of sand')

#! part 2
#* add the floor
#* tan(45*) is 1: tan() = opp/adj so floor is tan()*adj
floor_height = max_y + 2
for x in range(500-floor_height, 500+floor_height+1): #* +1
    rock_positions.add((x,floor_height))

s_p = True
while s_p:
    s_p = sands_of_time(rock_positions,sand_positions,min_x=-1e8,max_x=1e8,max_y=floor_height)
    # print(f'resting sand at: {s_p}')
    if s_p:
        sand_positions.add(s_p)
    else:
        print('🐛 🐝 🐞 🐜 🕷 🦗 🦟 🦋')
    if s_p == (500,0):
        print('hole plugged')
        print(f'{len(sand_positions)} grains of sand')
        s_p = False

#%%
print()
print('⭐ ⭐')