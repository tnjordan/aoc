#%%
f = 'data/day11.txt'

with open(file=f) as input:
    read_lines = input.readlines()
read_lines = [line.strip() for line in read_lines]
print('❄️⛄❄️')
#%%
directions = read_lines[0].split(',')
# directions = 'se,sw,se,sw,sw'.split(',')

n = directions.count('n') * 1
ne = directions.count('ne') * (.5 + .5j)
se = directions.count('se') * (-.5 + .5j)
s = directions.count('s') * -1
sw = directions.count('sw') * (-.5 - .5j)
nw = directions.count('nw') * (.5 - .5j)

steps = sum([n, s, ne, sw, nw, se])
print(f'child process is: {int(abs(steps.real)+abs(steps.imag))} steps away')

#! part 2
dir_step = {'n':1, 'ne':(.5 + .5j), 'se':(-.5 + .5j), 's':-1, 'sw':(-.5 - .5j), 'nw':(.5 - .5j)}

max_steps = 0
steps = 0 + 0j
for d in directions:
    steps += dir_step[d]
    max_steps = max(int(abs(steps.real)+abs(steps.imag)), max_steps)
print(f'the child process was a max of {max_steps} away')
#%%
