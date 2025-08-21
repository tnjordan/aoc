#%%
f = 'data/day24.txt'

example = False
if example:
    f = 'data/day24.ex'
    x_min = 7
    x_max = 27
    y_min = 7
    y_max = 27
else:
    x_min = 200000000000000
    x_max = 400000000000000
    y_min = 200000000000000
    y_max = 400000000000000

with open(file=f) as input:
    read_lines = input.readlines()
read_lines = [line.strip() for line in read_lines]
print('❄️⛄❄️')
#%%
hails = []
for line in read_lines:
    p,v = line.split('@')
    p = [int(x) for x in p.split(',')]
    v = [int(x) for x in v.split(',')]
    hails.append((p[0:2], v[0:2]))
hails

#%%
def intersection(hail,hell):
    # https://www.cuemath.com/geometry/intersection-of-two-lines/
    p0,v0 = hail
    p1,v1 = hell

    x0,y0 = p0
    vx0,vy0 = v0

    m1 = vy0/vx0
    c1 = y0-m1*x0

    x1,y1 = p1
    vx1,vy1 = v1

    m2 = vy1/vx1
    c2 = y1-m2*x1

    b1 = -1
    b2 = -1

    a1 = m1
    a2 = m2

    # intersection
    try:
        x_int = (b1*c2-b2*c1)/(a1*b2-a2*b1)
        y_int = (c1*a2 - c2*a1)/(a1*b2 - a2*b1)
        intersection = x_int, y_int
        #TODO make better
        past = False
        # A
        if vx0 <= 0 and x_int >= x0:
            past = True
        elif vx0 > 0 and x_int <= x0:
            past = True
        if vy0 <= 0 and y_int >= y0:
            past = True
        elif vy0 > 0 and y_int <= y0:
            past = True
        # B
        if vx1 <= 0 and x_int >= x1:
            past = True
        elif vx1 > 0 and x_int <= x1:
            past = True
        if vy1 <= 0 and y_int >= y1:
            past = True
        elif vy1 > 0 and y_int <= y1:
            past = True
        
    except ZeroDivisionError:
        intersection = None
        past = None
    print(intersection, 'in past:', past)
    return intersection, past

crash_in_zone = 0
for i, a in enumerate(hails):
    for b in hails[i+1:]:
        print('a,b',a,b)
        inter, past = intersection(a,b)
        if inter is not None:
            x_i, y_i = inter
            if x_min <= x_i <= x_max and y_min <= y_i <= y_max and past is False:  # in the zone
                print(f'\tcrash')
                crash_in_zone += 1
print(crash_in_zone)

#%%
import sympy

hailstones = []
for line in read_lines:
    p,v = line.split('@')
    p = [int(x) for x in p.split(',')]
    v = [int(x) for x in v.split(',')]
    hailstones.append(p + v)
hailstones

xr, yr, zr, vxr, vyr, vzr = sympy.symbols("xr, yr, zr, vxr, vyr, vzr")

equations = []

for i, (sx, sy, sz, vx, vy, vz) in enumerate(hailstones):
    equations.append((xr - sx) * (vy - vyr) - (yr - sy) * (vx - vxr))
    equations.append((yr - sy) * (vz - vzr) - (zr - sz) * (vy - vyr))
    if i < 2:
        continue
    answers = [soln for soln in sympy.solve(equations) if all(x % 1 == 0 for x in soln.values())]
    if len(answers) == 1:
        break
    
answer = answers[0]

print(answer[xr] + answer[yr] + answer[zr])
#%%
#* solution from HyperNeutrino: https://github.com/hyper-neutrino/advent-of-code/blob/main/2023/day24p2.py
