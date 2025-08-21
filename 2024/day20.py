#%%
from collections import deque

f = 'data/day20.txt'
# f = 'data/da20.ex'

with open(file=f) as input:
    read_lines = input.readlines()
read_lines = [line.strip() for line in read_lines]
print('🐟 🎄 🦈')
#%%
pos = (0,0)
end = (0,0)
dj_di = [(0,1), (0,-1), (1, 0), (-1, 0)]

grid = []
walls = set()
for j,row in enumerate(read_lines):
    gr = []
    for i, c in enumerate(row):
        gr.append(c)
        if c == 'S': pos = (j,i)
        elif c == 'E': end = (j,i)
        elif c == '#': walls.add((j,i))
    grid.append(gr)

J=len(grid)
I=len(grid[0])

cheat_walls = {}
for wall in walls:
    j,i = wall
    if j != 0 and i != 0 and j != J-1 and i != I-1:
        cheat_walls[(j,i)] = []
        for dj,di in dj_di:
            j_dj = j + dj
            i_di = i + di
            if grid[j_dj][i_di] == '.' or grid[j_dj][i_di] == 'E':
                cheat_walls[(j,i)].append((j_dj,i_di))
#%%
def race(pos):
    path = {}
    j,i = pos
    moves = 0
    path[pos] = moves
    q = deque()
    q.append((j,i,moves))
    seen = set()
    while q:
        (j,i,moves) = q.popleft()
        moves += 1
        seen.add((j,i))
        for dj,di in dj_di:
            j_dj = j + dj
            i_di = i + di
            if 0 <= j_dj < J and 0 <= i_di < I:
                if (j_dj,i_di) in walls:
                    continue
                if (j_dj,i_di) == end:
                    print('done!')
                    path[(j_dj,i_di)] = moves
                    return path
                if (j_dj,i_di) not in seen and (j_dj,i_di,moves) not in q:
                    path[(j_dj,i_di)] = moves
                    q.append((j_dj,i_di,moves))
    return False
#%%
race_track = race(pos)
#%%
savings = []
for cw,spaces in cheat_walls.items():
    print('wall',cw)
    if len(spaces) < 2:
        continue  # no cheat here
    print('spaces', spaces)
    for o, s1 in enumerate(spaces):
        for p, s2 in enumerate(spaces):
            if o < p:
                save = abs(race_track[s1] - race_track[s2]) - 2
                savings.append(save)
                print(f"Position: {s1}, Time: {race_track[s1]}")
                print(f"Position: {s2}, Time: {race_track[s2]}")
                print(f"Save Status: {save}")
    print()

#%%
count = {}
for value in savings:
    if value in count:
        count[value] += 1
    else:
        count[value] = 1
sorted_count = dict(sorted(count.items(), key=lambda x: x))
sorted_count
#?  4: 13, in example should be 4: 14,
#%%
sum([1 if s >= 100 else 0 for s in savings])  # works on full input
#%%
# par2
super_savings = []
for pos,moves in race_track.items():
    j,i = pos
    # print(pos,moves)
    ends = set()
    for dj_cheat_moves in range(20+1):
        for di_cheat_moves in range(0,20+1-dj_cheat_moves):
            cheat_moves = dj_cheat_moves + di_cheat_moves  # 20 moves max
            for djx,dix in [(1,1), (1,-1), (-1, 1), (-1, -1)]: # can also go neg
                if (djx,dix) == (1,-1) and di_cheat_moves == 0: continue  # dream about the puzzle solve
                if (djx,dix) == (1,-1) and dj_cheat_moves == 0: continue  # awake and code solution
                if (djx,dix) == (-1,1) and di_cheat_moves == 0: continue
                if (djx,dix) == (-1,1) and dj_cheat_moves == 0: continue
                j_dj = j + dj_cheat_moves*djx
                i_di = i + di_cheat_moves*dix
                # print(cheat_moves , dj_cheat_moves , di_cheat_moves)
                if 0 <= j_dj < J and 0 <= i_di < I and cheat_moves >= 2:
                    if grid[j_dj][i_di] == '.' or grid[j_dj][i_di] == 'E':
                        save = race_track[(j_dj,i_di)] - race_track[(j,i)] - cheat_moves
                        # print('\tsave:',save,' to ', (j_dj,i_di), ' at ', race_track[(j_dj,i_di)], ' moves using ', cheat_moves, 'cheat_moves')
                        if save > 0:
                            super_savings.append(save)
#%%
sum([1 if s >= 100 else 0 for s in super_savings])
# 600,000 low 1,103,878 high, 999,556 is good
#%%
