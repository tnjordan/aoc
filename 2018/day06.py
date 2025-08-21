#%%
# f = 'data/day06_ex.txt'
f = 'data/day06.txt'

with open(file=f) as input:
    read_lines = input.readlines()
read_lines = [l.strip() for l in read_lines]
print('🎅 🎄 🤶')
#%%
coords = [(int(x),int(y)) for x,y in [l.split(', ') for l in read_lines]]

x_c = [x for x,_ in coords]
y_c = [y for _,y in coords]

max_x = max(x_c)
min_x = min(x_c)
max_y = max(y_c)
min_y = min(y_c)

#* shift min to be zero (turns out this wasn't needed but also didn't hurt)
coords = [(x-min_x, y-min_y) for x,y in coords]

x_c = [x for x,_ in coords]
y_c = [y for _,y in coords]

max_x = max(x_c)
min_x = min(x_c)
max_y = max(y_c)
min_y = min(y_c)

#%%
def min_man_d(point,coords):
    """takes a point and returns the index of the closest point
        or if there is a tie a -1. Decided to use the point index
        as the point identifier."""
    x,y = point
    min_d = float('inf')
    min_idx = -1
    for i, (x_c,y_c) in enumerate(coords):
        man_d = abs(x-x_c)+abs(y-y_c)
        if man_d < min_d:
            min_d = man_d
            min_idx = i
        elif man_d == min_d:
            min_idx = -1
    return min_idx

closest_points = [[0 for _ in range(max_x+1)] for _ in range(max_y+1)]
cp_list = []
for y in range(max_y+1):
    for x in range(max_x+1):
        cp = min_man_d(point=(x,y),coords=coords)
        closest_points[y][x]= cp
        cp_list.append(cp)


#* the boundaries are inf, if coord is on boundary treat it as inf
#* i realized after this might not be the case since the boundaries
#* were set so tight. Not sure about this edge case.
inf_coords = set()
for y in range(max_y+1):
    for x in [0,max_x]:
        inf_coords.add(closest_points[y][x])

for cp in closest_points[0]:
    inf_coords.add(cp)

for cp in closest_points[max_y]:
    inf_coords.add(cp)
area = []
for i in range(len(coords)):
    if i in inf_coords:
        area.append(-1)
    else:
        i_count = cp_list.count(i)
        area.append(i_count)
        
print(max(area))
#%%
#! part 2
def man_d_counter(point,coords):
    """ returns the sum of the manhatan distances for a point.
        might have gotten lucky didn't need to expand the search area
        all safe points were within the max_y,max_x range"""
    x,y = point
    distance_sum = 0
    for i, (x_c,y_c) in enumerate(coords):
        man_d = abs(x-x_c)+abs(y-y_c)
        distance_sum += man_d
    if distance_sum < 10_000:
        return 1
    else:
        return 0
    
safe_point_list = []
for y in range(max_y+1):
    for x in range(max_x+1):
        safe_point_list.append(man_d_counter(point=(x,y),coords=coords))

print(sum(safe_point_list))

#%%
print()
print('⭐ ⭐')
#%%
