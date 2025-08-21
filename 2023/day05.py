#%%
f = 'data/day05.txt'
# f = 'data/day05.ex'

with open(file=f) as input:
    read_lines = input.readlines()
read_lines = [line.strip() for line in read_lines]
print('❄️⛄❄️')
#%%
seeds = [int(x) for x in read_lines[0].split(': ')[1].split()]
# seeds = [79]
maps = {}

for line in read_lines[1:]:
    if line == '':
        continue
    if 'map' in line:
        map = line.split()[0]
        maps[map] = {}
        continue
    destination, source, delta = [int(x) for x in line.split()]
    maps[map][(destination, source)] = delta

locations = []
for s in seeds:
    state = 'seed'
    while state != 'location':
        print(f'state {state} s {s}')
        for map_name, map in maps.items():
            if map_name.startswith(state):
                print(f'  map {map_name}')
                state = map_name.split('-')[-1]
                for (destination, source), delta in map.items():
                    if source <= s < source + delta:
                        s = destination + (s - source)
                        print(f'  state {state} s {s}')
                        break
                # else:
                #     s = s  # not needed but for clarity
    locations.append(s)
print(min(locations))

#%%
#! part 2
#?
print(f'there are {sum(seeds[1::2])} seeds that need to be processed')


# just for fun solve the example
def seed_map(s):
    state = 'seed'
    while state != 'location':
        for map_name, map in maps.items():
            if map_name.startswith(state):
                state = map_name.split('-')[-1]
                for (destination, source), delta in map.items():
                    if source <= s < source + delta:
                        s = destination + (s - source)
                        break
    return s


# min_location = float('inf')
# for i, s in enumerate(seeds[::2]):
#     print(f'init seed {s}')
#     for j in range(seeds[1::2][i]):
#         n_s = seed_map(s + j)
#         min_location = min(min_location, n_s)
# print(min_location)

#%%

#? reverse the map

def location_map(m):
    state = 'location'
    while state != 'seed':
        for map_name, map in maps.items():
            if map_name.endswith(state):
                state = map_name.split('-')[0]
                for (destination, source), delta in map.items():
                    if destination <= m < destination + delta:
                        m = source + (m - destination)
                        break
    return m


seed_ranges = []
for i, s in enumerate(seeds[::2]):
    seed_ranges.append((s, s + seeds[1::2][i] - 1))

# min_location = 0
# found_seed = False
# while not found_seed:
#     seed = location_map(min_location)
#     for s, e in seed_ranges:
#         if s <= seed <= e:
#             found_seed = True
#             break
#     else:
#         min_location += 1
# print(min_location)
#%%
# at 10,061,042 in 83 seconds
# get to 324,724,204 in?
print(f'{10061042/83*324724204} seconds')
print(f'{10061042/83*324724204/60} minutes')
print(f'{10061042/83*324724204/60/60} hours')
print(f'{10061042/83*324724204/60/60/24} days')
print(f'{10061042/83*324724204/60/60/24/365} years')
print(f'{10061042/83*324724204/60/60/24/365/100} centuries')
print(f'{10061042/83*324724204/60/60/24/365/1000} millennia')


#%%

def seed_locator(m):
    "given a location return if a seed is there"
    seed = location_map(m)
    for s, e in seed_ranges:
        if s <= seed <= e:
            return True
    return False


min_location = 0
last_invalid_min_location = 0
max_location = 324724204
last_valid_max_location = 324724204
found_seed = False
min_found = False
c = 0
while min_location <= max_location:
    c += 1
    if c > 100000:
        break
    # print(f'min {min_location} \tmax {max_location}')
    # print(f'min {seed_locator(min_location)} \tmax {seed_locator(max_location)}')
    mid = (min_location + max_location) // 2
    if seed_locator(max_location):
        last_valid_max_location = max_location
        max_location = mid - 1
    elif seed_locator(min_location):
        min_location = last_invalid_min_location
    else:
        last_invalid_min_location = min_location
        max_location = max_location + (max_location + last_valid_max_location) // 4
print(min_location)


#%%
# other option just go up the min seed[1::2] till you find a match
# then back down till you don't

min_step = min(seeds[1::2])

min_location = 0
found_seed = False
while not found_seed:
    if seed_locator(min_location):
        found_seed = True
        break
    else:
        min_location += int(min_step / 234)
print(min_location)

#%%

super_min_location = min_location
for i in range(int(min_step/234)):
    if seed_locator(min_location - i):
        super_min_location = min_location - i
    else:
        break
print(super_min_location)
#%%

#* the 234 comes from:
import math

number = min_step
factors = []

for i in range(1, int(math.sqrt(number)) + 1):
    if number % i == 0:
        factors.append(i)
        factors.append(number // i)

# Sort the factors in ascending order
factors.sort()

print(factors)

print(f'selected to be a "reasonable" number of steps: {factors[int(len(factors)/2)-1]}')
#%%
