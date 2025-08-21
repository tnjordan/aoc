#%%
f = 'data/day10.txt'
# f = 'data/da10.ex'

with open(file=f) as input:
    read_lines = input.readlines()
read_lines = [line.strip() for line in read_lines]
print('🐟 🎄 🦈')
grid = [list(map(int,list(l))) for l in read_lines]
#%%
head = []
for j, row in enumerate(grid):
    for i, v in enumerate(row):
        if v == 0:
            head.append((j,i))
#%%
# fuck me and my copy paste code was fine had diagonals
# dj_di = [(0,1), (0,-1), (1, 1), (1, 0), (1, -1), (-1, 1), (-1, 0), (-1,-1)]
dj_di = [(0,1), (0,-1), (1, 0), (-1, 0)]
J = len(grid)
I = len(grid[0])
#%%
# I think this might be part 2
# it was! merr chrismas. all i want is a working keyboard
def find_9_part2(v,j,i):
    # print(v,j,i)
    if v == 9:
        # print('found 9!')
        return 1
    trails =  0
    nv = v + 1
    for dj,di in dj_di:
        j_dj = j + dj
        i_di = i + di
        if 0 <= j_dj < J and 0 <= i_di < I:
            if grid[j_dj][i_di] == nv:
                trails += find_9_part2(nv,j_dj,i_di)
    return trails

def find_9(v,j,i):
    # print(v,j,i)
    if v == 9:
        # print('found 9!')
        # return j*J+i
        return (j,i)
    trail_heights =  []
    nv = v + 1
    for dj,di in dj_di:
        j_dj = j + dj
        i_di = i + di
        if 0 <= j_dj < J and 0 <= i_di < I:
            if grid[j_dj][i_di] == nv:
                trail_heights.append(find_9(nv,j_dj,i_di))
    return trail_heights

#! stackoverflow https://stackoverflow.com/questions/72335176/get-all-elements-of-nested-lists-with-recursion
# too confused by recursion to figure this out
def flatten(nested):
    flat = []
    def helper(nested):
        for e in nested:
            if isinstance(e, list):
                helper(e)
            else:
                flat.append(e)
    helper(nested)
    return flat

part_1 = 0
for j,i in head:
    # print('head: ',j,i)
    res = set(flatten(find_9(0,j,i)))
    # print('\r',res, len(res))
    part_1 += len(set(flatten(find_9(0,j,i))))
print(part_1)
#%%
part_2 = 0
for j,i in head:
    part_2 += find_9_part2(0,j,i)
print(part_2)
#%%
