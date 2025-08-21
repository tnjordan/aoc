#%%
import numpy as np
#%%
f = open('data\day7_input.csv', 'r', encoding='utf-8-sig')
crab_pos = list(map(int,f.read().split(',')))
f.close()
# %%
#! Part1
fuel_cost = [0]*(max(crab_pos)+1)
pos_list = list(range(0,max(crab_pos)+1))

#To Numpy! For array maths!
fuel_cost = np.asarray(fuel_cost)
pos_list = np.asarray(pos_list)

for pos in crab_pos:
    fuel_cost += abs(pos_list - pos)

answer = np.amin(fuel_cost)
print(answer)

#%%
#! Part2
#Reset the fuel
fuel_cost = [0]*(max(crab_pos)+1)
fuel_cost = np.asarray(fuel_cost)

for pos in crab_pos:
    y = abs(pos_list - pos)*(abs(pos_list - pos)+1)/2
    #* had to cast to integer since np made float due to division
    #* numpy would not += otherwise
    fuel_cost += np.int_(y)

answer = np.amin(fuel_cost)
print(answer)
# %%
