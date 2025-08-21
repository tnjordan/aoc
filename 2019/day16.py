#%%
import numpy as np
#%%
f = 'data/day16.txt'
# f = 'data/day16_ex.txt'

with open(f) as input:
    read_lines = input.readlines()

data = read_lines[0].strip()
offset = int(data[0:7])
data = [int(x) for x in [*data]]
# %%
#! part 2
data2 = data*10_000 
#TODO https://imgur.com/wAJ1zEj hint for part 2
#* also studied the master: https://github.com/kresimir-lukin/AdventOfCode2019/blob/master/day16.py
in_signal = data2[offset:]

#* only going to be ones, so can ignore the filter
for i in range(100):
    suffix_sum = 0
    for j in range(len(in_signal)-1,-1,-1):
        in_signal[j] = (suffix_sum + in_signal[j]) % 10 #* only positive numbers
        suffix_sum = in_signal[j]

print(f'Part 2: {"".join([str(x) for x in list(in_signal[0:8])])}')
#%%
base_pattern = [0, 1, 0, -1]

phase_out = []
pattern = []
for i in range(1,len(data)+1):
    if i % 1000 == 0:
        print(i)
    b_p = []
    for j in base_pattern:
        for k in range(i):
            b_p.append(j)
    #* inverse floor is the ceiling: https://stackoverflow.com/questions/14822184/is-there-a-ceiling-equivalent-of-operator-in-python
    #* add 1 for lazy handling of boundary condition as b_p is decrease by 1
    b_p_repeats = -(len(data) // -len(b_p)) + 1 
    pattern_i = b_p * b_p_repeats
    pattern_i = pattern_i[1:len(data)+1] #* shift by 1
    pattern.append(pattern_i)
    # print(pattern_i)

#%%
#! maths
in_signal = np.array(data)
pattern = np.array(pattern).T
#* %10 keep only the ones digit, but the negatives throw it off because maths
#* so absolute value to preserve the ones digit
for i in range(100):
    print(i)
    out_signal = abs(in_signal @ pattern) % 10
    in_signal = out_signal

print(''.join([str(x) for x in list(out_signal[0:8])]))


#%%
#! part 1
base_pattern = [0, 1, 0, -1]

phase_out = []
pattern = []
for i in range(1,len(data)+1):
    if i % 1000 == 0:
        print(i)
    b_p = []
    for j in base_pattern:
        for k in range(i):
            b_p.append(j)
    #* inverse floor is the ceiling: https://stackoverflow.com/questions/14822184/is-there-a-ceiling-equivalent-of-operator-in-python
    #* add 1 for lazy handling of boundary condition as b_p is decrease by 1
    b_p_repeats = -(len(data) // -len(b_p)) + 1 
    pattern_i = b_p * b_p_repeats
    pattern_i = pattern_i[1:len(data)+1] #* shift by 1
    pattern.append(pattern_i)
    # print(pattern_i)

#! maths
in_signal = np.array(data)
pattern = np.array(pattern).T
#* %10 keep only the ones digit, but the negatives throw it off because maths
#* so absolute value to preserve the ones digit
for i in range(100):
    print(i)
    out_signal = abs(in_signal @ pattern) % 10
    in_signal = out_signal

print(''.join([str(x) for x in list(out_signal[0:8])]))