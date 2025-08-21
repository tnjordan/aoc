#%%
from tabulate import tabulate

f = 'data/day20.txt'
# f = 'data/day20.ex'
# f = 'data/day20.ex2'

with open(file=f) as input:
    read_lines = input.readlines()
read_lines = [l.strip() for l in read_lines]
# print('🎅 🎄 🤶')

def print_order(pos): #* debugging function, was not return for final answer
    pl = {}
    for i in range(len(pos)):
        pl[i] = "X"
    for v in pos.values():
        pl[v[1]] = v[0]
    # print(tabulate([pl.values()]))
    return list(pl.values())

order = [int(l) for l in read_lines]
zero_order = order.index(0)
pos = {}
for idx,v in enumerate(order):
    pos[idx] = [v,idx]

# print('start')
# print_order(pos)
# print()
len_o = len(order)
for k,v in pos.items():
    # print(f'step:{k}')
    num, p = v
    num_num = num%len_o #* make all moves positive
    # print(f'num: {num} num num: {num_num}')
    # if num < 0 and num_num != 0:
    #     num_num-=1 #* idk, but this is crazy. Has todo with the circular nature
    #     # print(f'num_num modification: {num_num}')
    # if (p + num_num) < 0:
    #     new_p = (p+num_num)%len_o - 1 #* the loop offset
    if (p+num_num) >= len_o:
        new_p = (p+num_num)%len_o
    else:
        new_p = (p + num_num)
    # print(f'{num} at {p} new p {new_p}')
    # swap_ko = None
    if new_p - p < 0 and num < 0:
        swap_ko = False
    elif new_p - p > 0 and num > 0: #? I have not idea anymore
        swap_ko = False
    elif abs(new_p - p) == 1:
        swap_ko = False
    else:
        swap_ko = True
    for ko,vo in pos.items():
        if k == ko:
            continue
        no,po = vo
        # print(f'vo: {vo}')
        if swap_ko is True and po == new_p:
            # print('Swap KO')
            swap_ko = ko

        if p <= po <= new_p:
            # print('🐛')
            # print(f'{p} <= {po} <= {new_p}')
            po -= 1
            pos[ko] = [no,po]
        elif new_p <= po <= p:
            # print('🦋')
            # print(f'{new_p} <= {po} <= {p}')
            po += 1
            pos[ko] = [no,po]

    pos[k] = [num,new_p]
    #* if we approached from the negative, switch-a-roo
    if swap_ko is not False and swap_ko is not True:
        # print(swap_ko)
        # print('opposite day!')
        # print_order(pos)
        # print()
        pos[k][1], pos[swap_ko][1] = pos[swap_ko][1], pos[k][1]
        # print_order(pos)
        # print()

    # print_order(pos)
    # print()

zero_p = pos[zero_order][1]
final_order = print_order(pos)
# print(f'zero is at {zero_p}')
# c1 = final_order[(zero_p+1000)%len_o]
# c2 = final_order[(zero_p+2000)%len_o]
# c3 = final_order[(zero_p+3000)%len_o]
index_0 = final_order[zero_p:] + final_order[:zero_p]
c1 = index_0[1000]
c2 = index_0[2000]
c3 = index_0[3000]
print(f'grove coordinate 1: {c1}')
print(f'grove coordinate 2: {c2}')
print(f'grove coordinate 3: {c3}')
print()
print(f'part 1: {c1+c2+c3}')




#%%
# print()
# print('⭐ ⭐')
#%%
#* can't use dict: 3617 unique of 5000
# from collections import OrderedDict
# pos = OrderedDict()
# for idx,l in enumerate(read_lines):
#     # print(idx)
#     pos[l] = idx