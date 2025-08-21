#%%
from tabulate import tabulate
f = open('data\day14_input.txt', 'r')
read_lines = f.readlines()
f.close()

#%%
split_add = {}
input = ""
for l in read_lines:
    l = l.strip()
    try:
        x,y = l.split(' -> ')
        split_add[x] = y
    except:
        input += str(l)


# %%
new_input = ''
for x in range(10):
    print('run', x)
    for x in range(len(input)-1):
        double_char = input[x]+input[x+1]
        #* add character and inserted character
        new_input += input[x] + split_add[double_char]
    #* add last character
    new_input += input[-1]
    input = new_input
    new_input = ''
print(len(input))

input_list  = list(input)
input_set = set(input_list)

max_c = 0
min_c = len(input)
for c in input_set:
    x = input_list.count(c)
    if x > max_c:
        max_c = x
    if x < min_c:
        min_c = x
answer = max_c - min_c
print(answer)







# %%
