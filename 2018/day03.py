#%%
f = 'data/day03.txt'

with open(file=f) as input:
    read_lines = input.readlines()
read_lines = [l.strip() for l in read_lines]
print('🎅 🎄 🤶')
#%%
#! Part 1
def cord_2_fab(x,y,dx,dy,i=1_000):
    c_2_f = []
    for r in range(y,y+dy):
        for c in range(x,x+dx):
            c_2_f.append(r*i+c)
    return c_2_f

fab_list = [0]*1_000*1_000

for l in read_lines:
    _,_,xy,dxdy = l.split(' ')
    x,y = xy[:-1].split(',')
    dx,dy = dxdy.split('x')
    
    c_2_f = cord_2_fab(int(x),int(y),int(dx),int(dy))
    for c2f in c_2_f:
        fab_list[c2f] += 1

print('Part 1: ', sum([1 for f in fab_list if f > 1]))
#%%
#! Part 2
for l in read_lines:
    id,_,xy,dxdy = l.split(' ')
    x,y = xy[:-1].split(',')
    dx,dy = dxdy.split('x')
    
    c_2_f = cord_2_fab(int(x),int(y),int(dx),int(dy))
    for c2f in c_2_f:
        if fab_list[c2f] > 1:
            break
    else: # if no break else prints
        print('Part 2: ', id)
#%%
print()
print('⭐ ⭐')