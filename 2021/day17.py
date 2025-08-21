#%%
f = open('data\day17_input.txt', 'r')
read_line = f.readlines()
f.close()

for l in read_line:
    l = l.strip()
    l = l.replace('target area: x=','')
    l = l.replace(' y=','')
    l = l.replace('..',',')

x0,x1,y0,y1 = [int(i) for i in l.split(',')]

# %%
def time_advance(x,y,v_x, v_y):
    x += v_x
    y += v_y
    if v_x != 0:
        v_x -= 1
    v_y -=1
    return(x,y,v_x, v_y)

y_max_dict = {}
for v_x in range(x1 + 1): #* max move to hit target in the x direction is x1 (+1 because range not inclusive)
    v_x0 = v_x
    for v_y in range(y0,1010): #* lower bound is y0, top is just a big number
        v_x = v_x0
        v_y0 = v_y
        x = 0
        y = 0
        y_max = 0
        #* while have chance to hit target
        while x < x1 and y > y0:
            x,y,v_x,v_y = time_advance(x,y,v_x,v_y)
            if y > y_max:
                y_max = y
            #* check target hit
            if x0 <= x <= x1 and y0 <= y <= y1:
                print('hit!')
                y_max_dict[(v_x0,v_y0)] = y_max
                break
print(max(y_max_dict.values()))
print(len(y_max_dict.keys()))


