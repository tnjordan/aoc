#%%
import re
from tabulate import tabulate

f = 'data/day14.txt'

with open(file=f) as input:
    read_lines = input.readlines()
read_lines = [line.strip() for line in read_lines]
print('🐟 🎄 🦈')
#%%
J = 103
I = 101

robos = {}
for r,l in enumerate(read_lines):
    digs = tuple(map(int,re.findall('(-?\d+)',l)))
    a,b,c,d = digs  # lazy remap fix
    digs = (b,a,d,c)
    robos[r] = digs
# j,i,dj,di = digs  # for ref  # wooops, lets change it too match this

def quad(robos, par_2=0):  # par_2 is offset for mid rows
    
    j_down = int(J/2)-1
    j_up = j_down + 2

    i_down = int(I/2) - 1
    i_up = i_down + 2

    if par_2:
        j_down -= par_2
        j_up += par_2
        i_down -= par_2
        i_up += par_2

    # J bounds I bounds
    q1 = (0, j_down, 0, i_down)
    q2 = (j_up, J-1, 0, i_down)
    q3 = (0, j_down, i_up, I-1)
    q4 = (j_up, J-1, i_up, I-1)
    quads = (q1,q2,q3,q4)
    quad_con = {0:0,1:0,2:0,3:0}

    for robo in robos.values():
        j,i,_,_ = robo
        for k,(j_low,j_high,i_low,i_high) in enumerate(quads):
            if j_low <= j <= j_high and i_low <= i <= i_high:
                quad_con[k] +=1

    quad_prod = 1
    for qc in quad_con.values():
        quad_prod *= qc
    
    if par_2:
        return sum(quad_con.values())  # returns count in offset quads, track how many missing in loop

    return quad_prod
#%%
def move(robos, n=1):
    for _ in range(n):
        for r_id, (j,i,dj,di) in robos.items():
            j_dj = j+dj
            i_di = i+di
            # teleport
            j_dj = j_dj%J
            i_di = i_di%I
            robos[r_id] = (j_dj, i_di, dj, di)
    return robos
#%%
def find_egg(robos):
    grid = [['⬛' for _ in range(I)] for _ in range(J)]
    for robo in robos.values():
        j,i,_,_ = robo
        grid[j][i] = '🟩'
    # print(tabulate(grid, tablefmt="plain"))  # works but spaces 
    for g in grid:  # more compact
        print(''.join(g))
    
#%%
c = 0
# assume tree is in the middle
# assume a solid tree
min_qc = len(robos)
#%%
while True:
    c += 1
    robos = move(robos)
    qc = quad(robos, 2)
    if c == 100:
        print(f'part 1: {quad(robos)}')
    if qc < min_qc and c >= 7861:  # set after
        min_qc = qc
        find_egg(robos)
        print(c)
        break
#%%
# assumptions correct
# 🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩
# 🟩⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛🟩
# 🟩⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛🟩
# 🟩⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛🟩
# 🟩⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛🟩
# 🟩⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛🟩⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛🟩
# 🟩⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛🟩🟩🟩⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛🟩
# 🟩⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛🟩🟩🟩🟩🟩⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛🟩
# 🟩⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛🟩🟩🟩🟩🟩🟩🟩⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛🟩
# 🟩⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛🟩🟩🟩🟩🟩🟩🟩🟩🟩⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛🟩
# 🟩⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛🟩🟩🟩🟩🟩⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛🟩
# 🟩⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛🟩🟩🟩🟩🟩🟩🟩⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛🟩
# 🟩⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛🟩🟩🟩🟩🟩🟩🟩🟩🟩⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛🟩
# 🟩⬛⬛⬛⬛⬛⬛⬛⬛⬛🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩⬛⬛⬛⬛⬛⬛⬛⬛⬛🟩
# 🟩⬛⬛⬛⬛⬛⬛⬛⬛🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩⬛⬛⬛⬛⬛⬛⬛⬛🟩
# 🟩⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛🟩🟩🟩🟩🟩🟩🟩🟩🟩⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛🟩
# 🟩⬛⬛⬛⬛⬛⬛⬛⬛⬛🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩⬛⬛⬛⬛⬛⬛⬛⬛⬛🟩
# 🟩⬛⬛⬛⬛⬛⬛⬛⬛🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩⬛⬛⬛⬛⬛⬛⬛⬛🟩
# 🟩⬛⬛⬛⬛⬛⬛⬛🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩⬛⬛⬛⬛⬛⬛⬛🟩
# 🟩⬛⬛⬛⬛⬛⬛🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩⬛⬛⬛⬛⬛⬛🟩
# 🟩⬛⬛⬛⬛⬛⬛⬛⬛🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩⬛⬛⬛⬛⬛⬛⬛⬛🟩
# 🟩⬛⬛⬛⬛⬛⬛⬛🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩⬛⬛⬛⬛⬛⬛⬛🟩
# 🟩⬛⬛⬛⬛⬛⬛🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩⬛⬛⬛⬛⬛⬛🟩
# 🟩⬛⬛⬛⬛⬛🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩⬛⬛⬛⬛⬛🟩
# 🟩⬛⬛⬛⬛🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩⬛⬛⬛⬛🟩
# 🟩⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛🟩🟩🟩⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛🟩
# 🟩⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛🟩🟩🟩⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛🟩
# 🟩⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛🟩🟩🟩⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛🟩
# 🟩⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛🟩
# 🟩⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛🟩
# 🟩⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛🟩
# 🟩⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛🟩
# 🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩