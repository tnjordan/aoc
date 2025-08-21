#%%
import re
import matplotlib.pyplot as plt

f = 'data/day10.txt'
# f = 'data/day10.ex'

with open(file=f) as input:
    read_lines = input.readlines()
read_lines = [l.strip() for l in read_lines]
print('🎅 🎄 🤶')
#%%
pattern = r'position=< ?(-?\d+),  ?(-?\d+)> velocity=< ?(-?\d+),  ?(-?\d+)>'

points = []
for l in read_lines:
    match = re.search(pattern, l)
    x,y,dx,dy = map(int, match.groups())
    points.append([x,y,dx,dy])
    
def step(points):
    xs = []
    ys = []
    for i,(x,y,dx,dy) in enumerate(points):
        x += dx
        y += dy
        points[i] = [x,y,dx,dy]
        xs.append(x)
        ys.append(y)
    #* only plot when the range is within a y height. initial guess was 100, but as you can see 10 was the perfect answer
    plot = False
    if (max(ys)-min(ys)) <= 10: #! 10 hits the message perfect! which is amazing because c was then the answer to part 2
        plt.scatter(x=xs,y=[-y for y in ys]) #* invert y to match aoc coordinate system
        plt.show()
        plot = True
    return points, plot
#%%
plot = False
c = 0
while plot is False:
    c += 1
    if c % 1000 == 0:
        print(c)
    points, plot = step(points=points)
    
#%%
#? during initial attempt to find message ran while loop to get close (y height <= 100) 
#? then ran this cell until message appeared
points, plot = step(points=points)
#%%
print()
print('⭐ ⭐')