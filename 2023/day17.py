#%%
from tabulate import tabulate

f = 'data/day17.txt'
# f = 'data/day17.ex'
# f = 'data/day17.ex2'

with open(file=f) as input:
    read_lines = input.readlines()
read_lines = [line.strip() for line in read_lines]
print('❄️⛄❄️')
#%%
grid = []
for line in read_lines:
    grid.append([int(k2) for k2 in list(line)])
#%%
R = len(grid)
C = len(grid[0])

# j, i
position = (0,0)
fwd_steps = 0

# j, i
machine_parts_factory = (R-1,C-1)

dj_di = [(1,0),(-1,0),(0,1),(0,-1)]
last_djdi = (0,1)

# (j, i) fwd steps, last_move
status = (position, fwd_steps, last_djdi)

min_heat_loss = float('inf')

# dict of min_heats for each status
min_heats_lost = {}

#%%

def search(position,fwd_steps,last_djdi,heat_loss):
    global min_heat_loss
    global min_heats_lost
    global grid
    
    j,i = position

    status = (position, fwd_steps, last_djdi)
    if status in min_heats_lost:
        m_h_l = min_heats_lost[status]
        if heat_loss >= m_h_l:
            return False
        else:
            min_heats_lost[status] = heat_loss
    else:
        min_heats_lost[status] = heat_loss
    
    if heat_loss >= min_heat_loss:
        return False
    
    if position == machine_parts_factory and 4 <= fwd_steps <= 10:
        min_heat_loss = heat_loss
        print(f'new min heat loss {min_heat_loss}')
        return True
    
    if fwd_steps < 4:
        potential_steps = [last_djdi]
    else:
        # all options
        potential_steps = [(1,0),(-1,0),(0,1),(0,-1)]
        # remove backwards step
        back_step = tuple([-k2 for k2 in last_djdi])
        potential_steps.remove(back_step)
        # can't go fwd more than 10x
        if fwd_steps >= 10:
            potential_steps.remove(last_djdi)
    
    for ps in potential_steps:
        dj,di = ps
        j_dj = j+dj
        i_di = i+di
        if 0<=j_dj<R and 0<=i_di<C:

            new_position = (j_dj,i_di)

            if ps == last_djdi:
                new_fwd_steps = fwd_steps + 1
            else:
                new_fwd_steps = 1
            
            new_heat_loss = heat_loss + grid[j_dj][i_di]

            search(new_position,new_fwd_steps,ps,new_heat_loss)

#! takes ~16 min for part 1
search(position,fwd_steps,last_djdi,0)

#%%
