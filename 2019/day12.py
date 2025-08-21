#%%
import re
import numpy as np
from copy import deepcopy
import math

#%%
f = 'data/day12.txt'
# f = 'data/day12_ex.txt'
with open(f) as input:
    read_lines = input.readlines()
data_l = []

for i,l in enumerate(read_lines):
    l = l.strip()
    re_matches = re.match(r"<x=(.*), y=(.*), z=(.*)>",l)
    data_l.append([int(x) for x in re_matches.groups()])
    data_l[i].extend((0,0,0))

data = np.array(data_l)

for j in range(1000):
    if j % 100 == 0:
        print()
        print(f'After {j} steps:')
        print(data)
    for i in range(3):
        greater_than = np.where(np.repeat(np.atleast_2d(data[:,i]).T,repeats=4,axis=1)>np.repeat(np.atleast_2d(data[:,i]),repeats=4,axis=0),-1,0)
        less_than = np.where(np.repeat(np.atleast_2d(data[:,i]).T,repeats=4,axis=1)<np.repeat(np.atleast_2d(data[:,i]),repeats=4,axis=0),1,0)
        diff = greater_than + less_than
        delta_v = np.sum(diff,axis=1)
        #* update velocities
        data[:,i+3] = data[:,i+3] + delta_v
        #* update positions
        data[:,i] = data[:,i] + data[:,i+3]

potential_e = np.sum(np.abs(data[:,0:3]),axis=1)
kinetic_e = np.sum(np.abs(data[:,3:6]),axis=1)

total_energy = np.sum(potential_e * kinetic_e)
print(f'total energy: {total_energy}')
# %%
#! part 2
#? thanks to jpaulson I know to split x,y,z repeats as they are independent
#* https://www.youtube.com/watch?v=9UcnA2x5s-U


data_l = []
for i,l in enumerate(read_lines):
    l = l.strip()
    re_matches = re.match(r"<x=(.*), y=(.*), z=(.*)>",l)
    data_l.append([int(x) for x in re_matches.groups()])
    data_l[i].extend((0,0,0,0,0,0)) #* added more for the velocities
data = np.array(data_l)
print('init')
print(data)
print()

#* going to use energy this time since that was the last iteration
#! Failure didn't work, needed more information
# init
# [[ -1   0   2   0   0   0   0   0   0]
#  [  2 -10  -7   0   0   0   0   0   0]
#  [  4  -8   8   0   0   0   0   0   0]
#  [  3   5  -1   0   0   0   0   0   0]]

# 🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀
# duplicate for 0
# [[ -1   0   2   0   0   0   3   0   0]
#  [  2 -10  -7   0   0   0   1   0   0]
#  [  4  -8   8   0   0   0  -3   0   0]
#  [  3   5  -1   0   0   0  -1   0   0]]
# 🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀
# duplicate for 1 #! Issue is here :(
# [[ -1  -8   2   0   0   0   3   1   0]
#  [  2   5  -7   0   0   0   1  -3   0]
#  [  4   0   8   0   0   0  -3  -1   0]
#  [  3 -10  -1   0   0   0  -1   3   0]]
# 🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀
# duplicate for 2
# [[ -1  -8   8   0   0   0   3   1  -3]
#  [  2   5  -1   0   0   0   1  -3   1]
#  [  4   0   2   0   0   0  -3  -1  -1]
#  [  3 -10  -7   0   0   0  -1   3   3]]
# runs to repeat: 22

dups = []
for i in range(3):
    init_pos = deepcopy(data[:,i])
    init_vel = deepcopy(data[:,i+3])

    duplicate = False
    j = 0
    while duplicate is False:
        greater_than = np.where(np.repeat(np.atleast_2d(data[:,i]).T,repeats=4,axis=1)>np.repeat(np.atleast_2d(data[:,i]),repeats=4,axis=0),-1,0)
        less_than = np.where(np.repeat(np.atleast_2d(data[:,i]).T,repeats=4,axis=1)<np.repeat(np.atleast_2d(data[:,i]),repeats=4,axis=0),1,0)
        diff = greater_than + less_than
        delta_v = np.sum(diff,axis=1)
        #* record delta velocities
        data[:,i+6] = delta_v
        #* update velocities
        data[:,i+3] = data[:,i+3] + delta_v
        #* update positions
        data[:,i] = data[:,i] + data[:,i+3]

        j += 1
        pos = data[:,i]
        vel = data[:,i+3]
        
        if np.all(vel == init_vel):
            if np.all(pos == init_pos):
                print('\U0001F680'*12)
                print(f'duplicate for {i} at {j} cadence')
                print(data)
                dups.append(j)
                duplicate = True
        if j == 100_000_000: #* debug stop
            break

runs = 1
runs_2 = 1
for j in dups:
    runs = math.lcm(runs,j)
    runs_2 = runs_2 * j // math.gcd(runs_2,j)
    print(runs)
    print(runs_2)
print(f'runs to repeat: {runs}')
print(f'runs to repeat: {runs_2}')
#%% 
#? Also runs small demo
# data_l = []
# for i,l in enumerate(read_lines):
#     l = l.strip()
#     re_matches = re.match(r"<x=(.*), y=(.*), z=(.*)>",l)
#     data_l.append([int(x) for x in re_matches.groups()])
#     data_l[i].extend((0,0,0,0,0,0)) #* added more for the velocities
# data = np.array(data_l)

# init_potential_e = np.sum(np.abs(data[:,0:3]),axis=1)

# duplicate = False
# j = 0
# import time
# start_time = time.time()
# elapsed_time = time.time()
# delta_v_last = np.zeros((4,3))
# while duplicate is False:
#     if j % 1 == 0:
#         end_time = time.time()
#         print()
#         # print(f'{j} steps at {end_time - start_time} split: {end_time - elapsed_time}')
#         # print(data)
#         print(f'{j} steps')
#         print(data[:,6:9])
#         elapsed_time = time.time()
#         # print(data)
#     for i in range(3):
#         greater_than = np.where(np.repeat(np.atleast_2d(data[:,i]).T,repeats=4,axis=1)>np.repeat(np.atleast_2d(data[:,i]),repeats=4,axis=0),-1,0)
#         less_than = np.where(np.repeat(np.atleast_2d(data[:,i]).T,repeats=4,axis=1)<np.repeat(np.atleast_2d(data[:,i]),repeats=4,axis=0),1,0)
#         diff = greater_than + less_than
#         delta_v = np.sum(diff,axis=1)
#         #* record delta velocities
#         data[:,i+6] = delta_v
#         #* update velocities
#         data[:,i+3] = data[:,i+3] + delta_v
#         #* update positions
#         data[:,i] = data[:,i] + data[:,i+3]
#     if np.all(delta_v_last == data[:,6:9]):
#         print('\U0001F680')
#     delta_v_last = data[:,6:9].copy()
#     j += 1
#     potential_e = np.sum(np.abs(data[:,0:3]),axis=1)
#     kinetic_e = np.sum(np.sum(np.abs(data[:,3:6]),axis=1))
#     if kinetic_e == 0:
#         if np.all(potential_e == init_potential_e):
#             print('\U0001F680'*12)
#             print(data)
#             duplicate = True
#     if j == 3333: #* debug stop
#         break

# print(f'runs to repeat: {j}')
# %%
#? works on small demo: data/day12_ex.txt
# data = np.array(data_l)
# data_set = set()

# duplicate = False
# j = 0
# while duplicate is False:
#     # if j % 100_000 == 0:
#     if j > 2770:
#         print()
#         print(f'After {j} steps:')
#         print(data)
#     for i in range(3):
#         greater_than = np.where(np.repeat(np.atleast_2d(data[:,i]).T,repeats=4,axis=1)>np.repeat(np.atleast_2d(data[:,i]),repeats=4,axis=0),-1,0)
#         less_than = np.where(np.repeat(np.atleast_2d(data[:,i]).T,repeats=4,axis=1)<np.repeat(np.atleast_2d(data[:,i]),repeats=4,axis=0),1,0)
#         diff = greater_than + less_than
#         delta_v = np.sum(diff,axis=1)
#         #* update velocities
#         data[:,i+3] = data[:,i+3] + delta_v
#         #* update positions
#         data[:,i] = data[:,i] + data[:,i+3]
#     j += 1
#     #* update the set
#     d_flat = tuple(data.flatten())
#     data_set.add(d_flat)
#     if len(data_set) != j:
#         print('\U0001F680'*12)
#         print(data)
#         duplicate = True
#         j -= 1

# potential_e = np.sum(np.abs(data[:,0:3]),axis=1)
# kinetic_e = np.sum(np.abs(data[:,3:6]),axis=1)

# total_energy = np.sum(potential_e * kinetic_e)
# print(f'runs to repeat: {j}')

#? also works on small demo.
# data = np.array(data_l)
# data_set = set()

# init_potential_e = np.sum(np.abs(data[:,0:3]),axis=1)

# duplicate = False
# j = 0
# import time
# start_time = time.time()
# elapsed_time = time.time()
# while duplicate is False:
#     if j % 100_000 == 0:
#         end_time = time.time()
#         print()
#         print(f'{j} steps at {end_time - start_time} split: {end_time - elapsed_time}')
#         elapsed_time = time.time()
#         # print(data)
#     for i in range(3):
#         greater_than = np.where(np.repeat(np.atleast_2d(data[:,i]).T,repeats=4,axis=1)>np.repeat(np.atleast_2d(data[:,i]),repeats=4,axis=0),-1,0)
#         less_than = np.where(np.repeat(np.atleast_2d(data[:,i]).T,repeats=4,axis=1)<np.repeat(np.atleast_2d(data[:,i]),repeats=4,axis=0),1,0)
#         diff = greater_than + less_than
#         delta_v = np.sum(diff,axis=1)
#         #* update velocities
#         data[:,i+3] = data[:,i+3] + delta_v
#         #* update positions
#         data[:,i] = data[:,i] + data[:,i+3]
        
#     j += 1
#     potential_e = np.sum(np.abs(data[:,0:3]),axis=1)
#     kinetic_e = np.sum(np.sum(np.abs(data[:,3:6]),axis=1))
#     if kinetic_e == 0:
#         if np.all(potential_e == init_potential_e):
#             print('\U0001F680'*12)
#             print(data)
#             duplicate = True

# print(f'runs to repeat: {j}')