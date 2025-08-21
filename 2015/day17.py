#%%
f = 'data/day17.txt'

with open(file=f) as input:
    read_lines = input.readlines()
read_lines = [l.strip() for l in read_lines]
print('🎅 🎄 🤶')
#%%
containers = []
for l in read_lines:
    containers.append(int(l))
liters = 150

#* example
# containers  = [20, 15, 10, 5, 5]
# liters = 25

def cont_filler(used, size, containers, i):
    ways = 0
    # print('🎅')
    # print(f'used {used}, size {size} containers {containers}, i {i}')
    if size == liters:
        return 1
    for idx,c in enumerate(containers):
        true_idx = i + idx
        if size + c <= liters:
            new_size = c + size
            new_used = used + [true_idx]
            ways += cont_filler(new_used, new_size, containers[idx+1:], i=true_idx+1) #* +1 don't need if true_idx in used: logic
    return ways

#%%
k2 = cont_filler(used=[], size=0, containers=containers, i=0)
print(f'There are {k2} ways to fill the {liters} liter fridge.')

#%%
#! part 2
def cont_filler2(used, size, containers, i):
    ways = 0
    # print('🎅')
    # print(f'used {used}, size {size} containers {containers}, i {i}')
    if size == liters:
        # print(len(used))
        if len(used) == 4: #* found manually
            return 1
        else:
            return 0
    for idx,c in enumerate(containers):
        true_idx = i + idx
        if size + c <= liters:
            new_size = c + size
            new_used = used + [true_idx]
            ways += cont_filler2(new_used, new_size, containers[idx+1:], i=true_idx+1) #* +1 don't need if true_idx in used: logic
    return ways

k2 = cont_filler2(used=[], size=0, containers=containers, i=0)
print(f'There are {k2} ways to fill the {liters} liter fridge with 4 containers.')

#%%
print()
print('⭐ ⭐')
