#%%
# f = 'data/day3_ex3.txt'
# f = 'data/day3_ex2.txt' #TODO fix this, this example does not match
# f = 'data/day3_ex.txt'
f = 'data/day3.txt'
with open(f) as input:
    read_lines = input.readlines()
l0 = read_lines[0].strip().split(sep=',')
l1 = read_lines[1].strip().split(sep=',')

def interceptor_v3(command_list): #* v3 is just a basic v1
    x = 0
    y = 0
    corners = []
    for command in command_list:
        dir = command[0]
        mag = int(command[1:])
        if dir == 'L':
            x -= mag
        elif dir == 'R':
            x += mag
        elif dir == 'U':
            y += mag
        elif dir == 'D':
            y -= mag
        corners.append((x,y))
    return corners

l0_cor = interceptor_v3(l0)
l1_cor = interceptor_v3(l1)

#* point (x,y) is on a line if
#* if x is between x0 and x1; and y is between y0 and y1.
#* interception if x_1 is between x0_0 and x1_0 and 
#* y_0 is between y0_1 and y1_1.
#* interception is at (x_1,y_0)

#%%
intercepts = []
start_l0 = (0,0)
start_l1 = (0,0)
for cor_0 in l0_cor:
    x0_0,y0_0 = start_l0
    x1_0,y1_0 = cor_0

    if x0_0 == x1_0:
        x = x0_0
        x_set = False
        y_set = True
    else:
        y = y0_0
        x_set = True
        y_set = False

    for cor_1 in l1_cor:
        x0_1,y0_1 = start_l1
        x1_1,y1_1 = cor_1

        if y_set is True:
            if y0_1 == y1_1: #* check that other line is perpendicular
                y = y0_1
            # assert y0_1 == y1_1, 'wtf'
                if min(x0_1,x1_1) <= x <= max(x0_1,x1_1) and min(y0_0,y1_0) <= y <= max(y0_0,y1_0):
                    print(f'intercept! @ {(x,y)}')
                    intercepts.append((x,y))
        elif x_set is True and x0_1 == x1_1: #* could put on single line, could even make bigger.
    #   elif x_set is True and x0_1 == x1_1 and min(x0_0,x1_0) <= x0_1 <= max(x0_0,x1_0) and min(y0_1,y1_1) <= y0_0 <= max(y0_1,y1_1):
            x = x0_1
        # assert x0_1 == x1_1, f'wtf: {start_l0} {cor_0} {start_l1} {cor_1}'
            if min(x0_0,x1_0) <= x <= max(x0_0,x1_0) and min(y0_1,y1_1) <= y <= max(y0_1,y1_1):
                # print(f'intercept! @ {(x,y)}')
                intercepts.append((x,y))
        start_l1 = cor_1
    start_l0 = cor_0

try:
    intercepts.remove((0,0))
except:
    print('(0,0) already gone')

min_man_dist = float('inf')
for i in intercepts:
    d = abs(i[0])+abs(i[1])
    if d < min_man_dist:
        min_man_dist = d
print(min_man_dist)

#%%
def step_taker(intercept, corners):
    # print(f'intercept: {intercept}')
    x,y = intercept
    steps = 0
    x0, y0 = (0,0)
    for cor in corners:
        x1, y1 = cor
        if x0 == x and min(y0,y1) <= y <= max(y0,y1):
                # print(f'on intercept line between {(x0,y0)} and {(x1,y1)}')
                steps += abs(y-y0)
                # print(f'steps on y to intercept: {abs(y-y0)}')
                return steps
        elif y0 == y and min(x0,x1) <= x <= max(x0,x1):
                # print(f'on intercept line between {(x0,y0)} and {(x1,y1)}')
                steps += abs(x-x0)
                # print(f'steps on x to intercept: {abs(x-x0)}')
                return steps
        else:
            steps += abs(x1-x0)+abs(y1-y0)
        # print(f'moving between {(x0,y0)} and {(x1,y1)}')
        # print(f'current steps {steps}')
        x0,y0 = cor
    # print(f'total steps to intercept: {steps}')
    return steps

min_delay_dist = float('inf')
for intercept in intercepts:
    d0 = step_taker(intercept, l0_cor)
    d1 = step_taker(intercept, l1_cor)
    d = d0 + d1
    if d < min_delay_dist:
        min_delay_dist = d
print(min_delay_dist)

# %%

# (3,5) -> (8,5)

# (6,4) -> (6,12)