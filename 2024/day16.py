#%%
import heapq

f = 'data/day16.txt'
# f = 'data/da16.ex'
# f = 'data/da16.ex2'

with open(file=f) as input:
    read_lines = input.readlines()
read_lines = [line.strip() for line in read_lines]
print('🐟 🎄 🦈')
#%%
grid = []
for l in read_lines:
    grid.append(list(l))

for j,row in enumerate(grid):
    for i,c in enumerate(row):
        if c == 'S':
            pos = (j,i)
        elif c == 'E':
            end_pos = (j,i)
            grid[j][i] = '.'

J = len(grid)
I = len(grid[0])

dj_di = [(0,1), (0,-1), (1, 0), (-1, 0)]
heading = ((0,1))
#%%
def show_grid(pos, path=None, gif=False):
    emoji_grid = [['⬛' for _ in range(I)] for _ in range(J)]
    for j,row in enumerate(grid):
        for i,c in enumerate(row):
            if c == '#':
                emoji_grid[j][i] = '🧱'
    j,i = end_pos
    emoji_grid[j][i] = '🏁'
    if path:
        for (j,i) in path[:-1]:
            emoji_grid[j][i] = '💩'
            if gif:
                for g in emoji_grid:  # more compact
                    print(''.join(g))
                print()
    j,i = pos
    emoji_grid[j][i] = '🦌'
    for g in emoji_grid:  # more compact
        print(''.join(g))
show_grid(pos, path=None)
#%%
max_score = 1e6
min_score = {}
def random_deer_walk(pos,heading,path,score,par2=False):
    seen = set()
    best_seats = set()
    hq = []
    heapq.heappush(hq, (score,pos,heading,path))
    while hq:
        (score,pos,heading,path) = heapq.heappop(hq)
        # show_grid(pos)
        # print((score,pos,heading,path))
        j,i = pos
        seen.add(pos)
        for dj,di in dj_di:
            j_dj = j + dj
            i_di = i + di
            if not par2 and (j_dj, i_di) in seen:
                continue  # been here in another life
            if (j_dj, i_di) in path:
                continue  # no going back
            if grid[j_dj][i_di] == '.':
                # a valid path option
                new_pos = (j_dj, i_di)
                new_heading = (dj,di)
                new_path = path + [new_pos]
                if (dj,di) == heading:
                    new_score = score + 1  # one small steep for deerkind
                else:
                    new_score = score +  1001  # rotate and make move
                
                if new_score > max_score:
                    continue  # too much turning

                if new_pos == end_pos:
                    if par2:
                        for p in new_path:  # Add each position in the path
                            best_seats.add(p)
                        # print('best_seats! ', len(best_seats))
                        continue
                    else:
                        return new_score, new_path
                
                if (new_pos,new_heading) in min_score:
                    ms = min_score[(new_pos,new_heading)]
                    if new_score > ms:
                        continue
                    else:
                        min_score[(new_pos,new_heading)] = new_score  #  might be equal too
                else:
                    min_score[(new_pos,new_heading)] = new_score

                heapq.heappush(hq, (new_score,new_pos,new_heading,new_path))
    if par2: 
        return best_seats
#%%
score, path = random_deer_walk(pos,heading,[pos],0)
print(score)
max_score = score  # used for par
#%%
show_grid(pos=end_pos, path=path, gif=False)
#%%
best_seats = random_deer_walk(pos,heading,[pos],0,par2=True)
print(len(best_seats))
show_grid(pos=end_pos, path=list(best_seats))
#%%
