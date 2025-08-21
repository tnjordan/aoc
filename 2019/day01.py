#%%
input = open('data/day1.txt')
read_lines = input.readlines()

modules = []
for l in read_lines:
    l = int(l.strip())
    modules.append(l)
# %%
weights = []
for m in modules:
    w = int(m/3) - 2
    weights.append(w)

fuel_weight = sum(weights)
print(fuel_weight)
# %%
import time

#! part 2
time_start = time.time()

weights = []
for m in modules:
    fuel_weight_init = int(m/3) - 2

    #* fuel for fuel
    more_fuel = True
    fuel_for_fuel = 0
    delta_fuel = 0
    fuel_weight_counter = fuel_weight_init
    while more_fuel is True:
        fuel_for_fuel += delta_fuel
        delta_fuel = int(fuel_weight_counter/3) - 2
        fuel_weight_counter = delta_fuel
        if delta_fuel <= 0:
            more_fuel = False
            print('done fueling')
        else:
            print(f'delta_fuel: {delta_fuel} fuel_for_fuel: {fuel_for_fuel}')
    weights.append(fuel_weight_init + fuel_for_fuel)
print(sum(weights))
time_end = time.time()
print(f'time: {time_end-time_start}')

#%%
#! part 2 numpy!
import numpy as np

time_start = time.time()

def find_fuel_for_fuel(fuel_weight_init):
    #* fuel for fuel
    more_fuel = True
    fuel_for_fuel = 0
    delta_fuel = 0
    # fuel_weight_counter = fuel_weight_init
    while more_fuel is True:
        fuel_for_fuel += delta_fuel
        delta_fuel = int(fuel_weight_init/3) - 2
        fuel_weight_init = delta_fuel
        if delta_fuel <= 0:
            more_fuel = False
            print('done fueling')
        else:
            print(f'delta_fuel: {delta_fuel} fuel_for_fuel: {fuel_for_fuel}')
    return fuel_for_fuel

arr = np.array(modules)
fuel = (arr/3).astype(int)-2
fuel_for_fuel_v = np.vectorize(find_fuel_for_fuel)
fuel_for_fuel = fuel_for_fuel_v(fuel)

time_end = time.time()
print(f'time: {time_end-time_start}')

# #! doesn't work, solved for all modules as one. Should read instructions
# fuel_for_fuel = 0
# delta_fuel = 0
# more_fuel = True
# fuel_weight_counter = fuel_weight
# while more_fuel is True:
#     fuel_for_fuel += delta_fuel
#     delta_fuel = int(fuel_weight_counter/3) - 2
#     fuel_weight_counter = delta_fuel
#     print(delta_fuel)
#     if delta_fuel <= 0:
#         more_fuel = False
#         print('done fueling')
# print(fuel_for_fuel)

# ans = fuel_weight + fuel_for_fuel
# # %%

# %%
