#%%
import re
from itertools import product
import matplotlib.pyplot as plt
import seaborn as sns
from collections import defaultdict

f = 'data/day15.txt'
example = False
if example:
    f = 'data/day15.ex'
    # f = 'data/day15.ex2' #* reduced for testing.

with open(file=f) as input:
    read_lines = input.readlines()
read_lines = [l.strip() for l in read_lines]
print('🎅 🎄 🤶')

regex = re.compile('x=(-?\d*), y=(-?\d*)')

# S = set()
# B = set()
# no_B = set()
# no_BB = set() #* used for boundaries
# no_BB_up = set()
# no_BB_down = set()
# no_BB_left = set()
# no_BB_right = set()

# BB_horizontal = defaultdict(list)
# BB_vertical = defaultdict(list)

# no_BB_plus = set()
# no_BB_neg = set()

# #* only care about this y, at least for part 1
# y = 2_000_000 
# if example:
#     y = 10 #* for example

# for idx,l in enumerate(read_lines,start = 1):
#     print(f'{idx/len(read_lines)*100:.0f}%')
#     s,b = [m for m in re.findall(regex,l)]
#     sx,sy = [int(m) for m in s]
#     bx,by = [int(m) for m in b]
#     S.add((sx,sy))
#     B.add((bx,by))

#     manhattan = abs(sx-bx) + abs(sy-by)

#     #* find manhattan distance bounds, used for debugging example
#     #* and now used for #! part 2 #* needed to reorder
#     for i in range(manhattan+1):
#         j = manhattan - i


#         if example:
#             #* worked for example not for the real deal
#             # BB_horizontal[sy+j*-1].append([sx+i*-1,sx+i*1])
#             # BB_horizontal[sy+j*1].append([sx+i*-1,sx+i*1])
#             # BB_vertical[sx+i*-1].append([sy+j*-1,sy+j*1])
#             # BB_vertical[sx+i*1].append([sy+j*-1,sy+j*1])
#             for i_multiplier, j_multiplier in [p for p in product([1,-1], repeat=2)]:
#                 no_BB.add((sx+i*i_multiplier,sy+j*j_multiplier))

#     if not (sy-manhattan <= y <= sy+manhattan):
#         # print('no overlap')
#         # print(f'\tsensor y {sy}')
#         # print(f'\tmanhattan {manhattan}')
#         # print('\t',sy-manhattan , y , sy+manhattan)
#         continue
#     # else:
#     #     print('overlap')
#     #     print(f'\tsensor y {sy}')
#     #     print(f'\tmanhattan {manhattan}')
#     #     print('\t',sy-manhattan , y , sy+manhattan)
    
#     #* add lines only to line y
#     for i in range(manhattan - abs(sy-y)+1):
#         for i_multiplier in [1,-1]:
#             no_B.add((sx+(i*i_multiplier),y))

# #* note the axis are not the same as the instructions
# if example:
#     plt.rc('axes', axisbelow=True)
#     plt.rcParams['axes.axisbelow'] = True
#     plt.figure(figsize=(12,12))
#     plt.minorticks_on()
#     plt.grid(visible=True, which='major', color='b', linestyle='-')
#     plt.grid(visible=True, which='minor', color='r', linestyle='--')
#     sns.scatterplot(x=[x[0] for x in [list(b) for b in no_BB]],y=[x[1] for x in [list(b) for b in no_BB]])
#     sns.scatterplot(x=[x[0] for x in [list(b) for b in no_BB_plus]],y=[x[1] for x in [list(b) for b in no_BB_plus]])
#     # sns.scatterplot(x=[x[0] for x in [list(b) for b in no_B]],y=[x[1] for x in [list(b) for b in no_B]]) #* part 1 plot
#     sns.scatterplot(x=[x[0] for x in [list(b) for b in B]],y=[x[1] for x in [list(b) for b in B]])
#     sns.scatterplot(x=[x[0] for x in [list(b) for b in S]],y=[x[1] for x in [list(b) for b in S]])
#     sns.scatterplot(x=[14],y=[11])
#     plt.show()

# #! part 1
# #* you can tell I plotted first #* and this was a horrible way for the non-example case
# blocked_count = len(no_B) #len([x[1] for x in [list(b) for b in no_B] if x[1] == y])
# beacons_count = len([x[1] for x in [list(b) for b in B] if x[1] == y])
# sensor_count = len([x[1] for x in [list(b) for b in S] if x[1] == y])

# print(f'positions on y={y} that cannot have a beacon: {blocked_count - beacons_count - sensor_count}')

#%%
#! part 2
#* round v, consulted the internet some more.
S = set()
B = set()

for idx,l in enumerate(read_lines,start = 1):
    print(f'{idx/len(read_lines)*100:.0f}%')
    s,b = [m for m in re.findall(regex,l)]
    sx,sy = [int(m) for m in s]
    bx,by = [int(m) for m in b]
    S.add((sx,sy))
    B.add((bx,by))

    manhattan = abs(sx-bx) + abs(sy-by)
    manhattan += 1 #* for extended range

    for i in range(manhattan+1): #* search points along the boundary
        j = manhattan - i
        for i_multiplier, j_multiplier in [p for p in product([1,-1], repeat=2)]:
            search_x, search_y = (sx+i*i_multiplier,sy+j*j_multiplier)
            if 0 <= search_x <= 4000000 and 0 <= search_y <= 4000000:
                for idx_s,l_s in enumerate(read_lines,start = 1):
                    # print(f'\t{idx_s/len(read_lines)*100:.0f}%')
                    s_s,b_s = [m for m in re.findall(regex,l_s)]
                    sx_s,sy_s = [int(m) for m in s_s]
                    bx_s,by_s = [int(m) for m in b_s]
                    manhattan_s = abs(sx_s-bx_s) + abs(sy_s-by_s)
                    search_manhattan = abs(sx_s-search_x) + abs(sy_s-search_y)
                    if search_manhattan <= manhattan_s:
                        # print(f'point contained within sensor: {s_s} area of range {manhattan_s}')
                        break
                else:
                    print(f'distress beacon at {(sx+i*i_multiplier,sy+j*j_multiplier)}')
                    print(4000000*(sx+i*i_multiplier)+(sy+j*j_multiplier))
                    break


#%%
# #* round iv #* another example that works on the example
# S = set()
# B = set()
# no_BB = set() #* used for boundaries + 1 in part 2
# no_BB_plus = set()
# no_BB_neg = set()

# if example:
#     Beacon_Boundary_Box = set()
#     for idx,l in enumerate(read_lines,start = 1):
#         print(f'{idx/len(read_lines)*100:.0f}%')
#         s,b = [m for m in re.findall(regex,l)]
#         sx,sy = [int(m) for m in s]
#         bx,by = [int(m) for m in b]
#         manhattan = abs(sx-bx) + abs(sy-by)
#         for i in range(manhattan+1):
#             j = manhattan - i
#             for i_multiplier, j_multiplier in [p for p in product([1,-1], repeat=2)]:
#                 Beacon_Boundary_Box.add((sx+i*i_multiplier,sy+j*j_multiplier))

# for idx,l in enumerate(read_lines,start = 1):
#     print(f'{idx/len(read_lines)*100:.0f}%')
#     s,b = [m for m in re.findall(regex,l)]
#     sx,sy = [int(m) for m in s]
#     bx,by = [int(m) for m in b]
#     S.add((sx,sy))
#     B.add((bx,by))

#     manhattan = abs(sx-bx) + abs(sy-by)
#     manhattan += 1 #* for extended range

#     for i in range(manhattan+1):
#         j = manhattan - i

#         for i_multiplier, j_multiplier in [p for p in product([1,-1], repeat=2)]:
#             if i_multiplier*j_multiplier >= 0:
#                 no_BB_neg.add((sx+i*i_multiplier,sy+j*j_multiplier))
#             else: #* i_multiplier*j_multiplier < 0:
#                 no_BB_plus.add((sx+i*i_multiplier,sy+j*j_multiplier))

# #* note the axis are not the same as the instructions
# if example:
#     plt.rc('axes', axisbelow=True)
#     plt.rcParams['axes.axisbelow'] = True
#     plt.figure(figsize=(12,12))
#     plt.minorticks_on()
#     plt.grid(visible=True, which='major', color='b', linestyle='-')
#     plt.grid(visible=True, which='minor', color='r', linestyle='--')
#     sns.scatterplot(x=[x[0] for x in [list(b) for b in Beacon_Boundary_Box]],y=[x[1] for x in [list(b) for b in Beacon_Boundary_Box]])
#     sns.scatterplot(x=[x[0] for x in [list(b) for b in no_BB_plus]],y=[x[1] for x in [list(b) for b in no_BB_plus]])
#     sns.scatterplot(x=[x[0] for x in [list(b) for b in no_BB_neg]],y=[x[1] for x in [list(b) for b in no_BB_neg]])
#     sns.scatterplot(x=[x[0] for x in [list(b) for b in B]],y=[x[1] for x in [list(b) for b in B]])
#     sns.scatterplot(x=[x[0] for x in [list(b) for b in S]],y=[x[1] for x in [list(b) for b in S]])
#     sns.scatterplot(x=[14],y=[11])
#     plt.show()

# #* potential search:
# search_points = no_BB_plus & no_BB_neg
# search_points = search_points - S
# search_points = search_points - B
# #%%
# for i,j in search_points:
#     #* verify range
#     if 0 <= i <= 20 and 0 <= j <= 20:
#         print(i,j)
#         #* just loop again
#         for idx,l in enumerate(read_lines,start = 1):
#             s,b = [m for m in re.findall(regex,l)]
#             sx,sy = [int(m) for m in s]
#             bx,by = [int(m) for m in b]
#             manhattan = abs(sx-bx) + abs(sy-by)
#             manhattan_sp = abs(sx-i) + abs(sy-j)
#             if manhattan_sp <= manhattan:
#                 # print(f'point contained within sensor: {s} area of range {manhattan}')
#                 break
#         else:
#             print(f'distress beacon at {i,j}')
#             break

#%%
# #* round iii
# if example:
#     search_r = range(0,20+1)
#     for i in search_r:
#         for j in search_r:
#             #* find empty
#             for bb_h in BB_horizontal[i]:
#                 if j in range(bb_h[0],bb_h[1]+1):
#                     break
#             else:
#                 print(i)
#                 for j in search_r:
#                     for bb_v in BB_vertical[j]:
#                         if i in range(bb_v[0],bb_v[1]+1):
#                             break
#                     else:
#                         print(f'distress beacon at {i,j}')

#%%
# #* round ii
# blocked = no_BB | B | S
# search = [(0,1),(0,-1),(1,0),(-1,0)]
# if example:
#     search_r = range(0,20+1)
#     for i in search_r:
#         for j in search_r:
#             if (i,j) not in blocked:
#                 if (i+0,j+1) not in no_BB_down: #* oh man this is confusing. Up the up has to be in the lower bounds
#                     continue
#                 if (i+0,j-1) not in no_BB_up:
#                     continue
#                 if (i+1,j+0) not in no_BB_left:
#                     continue
#                 if (i-1,j+0) not in no_BB_right:
#                     continue
#                 else:
#                     print(f'distress beacon at {i,j}')

#%%
# #* get all the boundaries. The point is the only one that has boundary lines on each side of it
# #? :( did not work, overlaps made many valid points
# #* learned debugging that actually need all edges and beacons and signals
# blocked = no_BB | B | S
# search = [(0,1),(0,-1),(1,0),(-1,0)]
# if example:
#     search_r = range(0,20+1)
#     for i in search_r:
#         for j in search_r:
#             if (i,j) not in blocked:
#                 for di,dj in search:
#                     if (i+di,j+dj) not in no_BB:
#                         break
#                 else:
#                     print(f'distress beacon at {i,j}')

#%%
print()
print('⭐ ⭐')
#%%
#* worked for the example, archiving here for TTT review
# import re
# from itertools import product
# import matplotlib.pyplot as plt
# import seaborn as sns

# f = 'data/day15.txt'
# f = 'data/day15.ex'

# with open(file=f) as input:
#     read_lines = input.readlines()
# read_lines = [l.strip() for l in read_lines]
# print('🎅 🎄 🤶')

# regex = re.compile('x=(-?\d*), y=(-?\d*)')

# S = set()
# B = set()
# no_B = set()

# for l in read_lines:
#     s,b = [m for m in re.findall(regex,l)]
#     sx,sy = [int(m) for m in s]
#     bx,by = [int(m) for m in b]
#     S.add((sx,sy))
#     B.add((bx,by))

#     manhattan = abs(sx-bx) + abs(sy-by)

#     #* for every distance with the manhattan
#     for m in range(manhattan+1): #* tricky double loop. with only a single loop only manhattan boundary points displayed
#         for i in range(m+1):
#             j = m - i
#             #* +/- are both valid
#             # for k in [1,-1]:
#             for i_multiplier, j_multiplier in [p for p in product([1,-1], repeat=2)]:
#                 no_B.add((sx+i*i_multiplier,sy+j*j_multiplier))
#                 # print((sx+i*i_multiplier,sy+j*j_multiplier))

# #* note the axis are not the same as the example
# plt.figure(figsize=(8,6))
# sns.scatterplot(x=[x[0] for x in [list(b) for b in no_B]],y=[x[1] for x in [list(b) for b in no_B]])
# sns.scatterplot(x=[x[0] for x in [list(b) for b in B]],y=[x[1] for x in [list(b) for b in B]])
# sns.scatterplot(x=[x[0] for x in [list(b) for b in S]],y=[x[1] for x in [list(b) for b in S]])

# #%%
# #! part 1
# #* you can tell I plotted first
# y = 2_000_000 #* y = 10 for example
# blocked_count = len([x[1] for x in [list(b) for b in no_B] if x[1] == y])
# beacons_count = len([x[1] for x in [list(b) for b in B] if x[1] == y])
# sensor_count = len([x[1] for x in [list(b) for b in S] if x[1] == y])

# print(f'positions that cannot have a beacon: {blocked_count - beacons_count - sensor_count}')
