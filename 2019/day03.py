#%%
input = open('data/day3_ex3.txt')
# input = open('data/day3_ex2.txt')
# input = open('data/day3_ex.txt')
# input = open('data/day3.txt')
read_lines = input.readlines()
l0 = read_lines[0].strip().split(sep=',')
l1 = read_lines[1].strip().split(sep=',')

def interceptor(command_list):
    x = 0
    y = 0
    pos = (x,y)
    l0_pos = []
    l0_cor = []
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
        new_pos = (x,y)
        l0_cor.append(new_pos)
        for x_i in range(min(pos[0],new_pos[0])+1,max(pos[0],new_pos[0])):
            l0_pos.append((x_i,y))
        for y_i in range(min(pos[1],new_pos[1])+1,max(pos[1],new_pos[1])):
            l0_pos.append((x,y_i))
        l0_pos.append(new_pos)
        pos = new_pos
    return l0_cor, l0_pos

l0_cor, l0_pos = interceptor(l0)
l1_cor, l1_pos = interceptor(l1)

intercepts = set(l0_pos) & set(l1_pos)
#%%
#! part 1
min_man_dist = 1e99 #TODO look up better way to do this.
for i in intercepts:
    if abs(i[0])+abs(i[1]) < min_man_dist:
        min_man_dist = abs(i[0])+abs(i[1])
print(min_man_dist)

#%%
#! part 2

#* interceptor does not have the points in the right order. need interceptor v2
def interceptor_v2(command_list):
    x = 0
    y = 0
    l0_pos = []
    l0_cor = []
    for command in command_list:
        dir = command[0]
        mag = int(command[1:])
        for _ in range(mag):
            if dir == 'L':
                x -= 1
            elif dir == 'R':
                x += 1
            elif dir == 'U':
                y += 1
            elif dir == 'D':
                y -= 1
            l0_pos.append((x,y))
        l0_cor.append((x,y))
    return l0_cor, l0_pos

l0_cor, l0_pos = interceptor_v2(l0)
l1_cor, l1_pos = interceptor_v2(l1)

intercepts = set(l0_pos) & set(l1_pos) #* verified they are the same

min_delay_dist = 1e99
for i in intercepts:
    d0 = l0_pos.index(i) +1 #* first step is missing with index 0
    d1 = l1_pos.index(i) +1
    d = d0 + d1
    # print(f'int: {i} @ d: {d} via d0: {d0} d1: {d1}') #* had to debug. turns out everything was right. I was just printing d and not min_delay_dist at the end :(
    if d < min_delay_dist:
        min_delay_dist = d
print(min_delay_dist)


#? wrote the logic first, then put it into a function.
# x = 0
# y = 0
# pos = (x,y)
# l0_pos = [pos,]
# l0_cor = [pos,]
# for command in l0:
#     dir = command[0]
#     mag = int(command[1:])
#     if dir == 'L':
#         x -= mag
#     elif dir == 'R':
#         x += mag
#     elif dir == 'U':
#         y += mag
#     elif dir == 'D':
#         y -= mag
#     new_pos = (x,y)
#     l0_cor.append(new_pos)
#     for x_i in range(min(pos[0],new_pos[0])+1,max(pos[0],new_pos[0])):
#         l0_pos.append((x_i,y))
#     for y_i in range(min(pos[1],new_pos[1])+1,max(pos[1],new_pos[1])):
#         l0_pos.append((x,y_i))
#     l0_pos.append(new_pos)
#     pos = new_pos


# %%
