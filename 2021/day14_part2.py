#%%
from tabulate import tabulate
f = open('data\day14_input.txt', 'r')
read_lines = f.readlines()
f.close()

split_add = {}
dc_count_dict = {}
new_dc_count_dict = {}
input = ""
for l in read_lines:
    l = l.strip()
    try:
        x,y = l.split(' -> ')
        split_add[x] = y
        dc_count_dict[x] = 0
        new_dc_count_dict[x] = 0
    except:
        input += str(l)

#%%
#NN -> NC & CN
#NC -> NB & BC
#CB -> CH & HB

# Each pair produces 2 children.
# First letter plus insertion & insertion letter plus last letter

#split input to fill dc_count_dict with initial values
for x in range(len(input)-1):
        double_char = input[x]+input[x+1]
        dc_count_dict[double_char] += 1


for x in range(40):
    print('run', x)
    for dc,dc_value in dc_count_dict.items():
        new_dc_count_dict[dc[0]+split_add[dc]] += dc_value
        new_dc_count_dict[split_add[dc]+dc[1]] += dc_value
    # have to use .copy() to not have the dict be the same in memory
    dc_count_dict = new_dc_count_dict.copy()
    # reset new_dc_count_dict
    for dc in new_dc_count_dict:
        new_dc_count_dict[dc] = 0
    print(dc_count_dict)

#* get character counts of every character except the last (only using first character)
c_count = {}
for dc, dc_value in dc_count_dict.items():
    x,y = list(dc)
    if x in c_count:
        c_count[x] += dc_value
    else:
        c_count[x] = dc_value
    '''
    if y in c_count:
        c_count[y] += dc_value
    else:
        c_count[y] = dc_value'''

#* add the last character of the input
c_count[input[-1]] += 1

max_c = 0
min_c = 1e99
for c,c_value in c_count.items():
    print(c,c_value)
    if c_value > max_c:
        max_c = c_value
    if c_value < min_c:
        min_c = c_value
answer = max_c - min_c
print(answer)
# %%
