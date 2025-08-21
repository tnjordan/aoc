#%%
f = 'data/day12.txt'
# f = 'data/day12.ex'

with open(file=f) as input:
    read_lines = input.readlines()
read_lines = [line.strip() for line in read_lines]
print('❄️⛄❄️')
#%%
hot_springs = {}
for i, line in enumerate(read_lines):
    springs, contiguous_damage = line.split(' ')
    contiguous_damage = tuple(int(x) for x in contiguous_damage.split(','))
    hot_springs[i] = {'springs': springs, 'contiguous_damage': contiguous_damage}
#%%
cache = {}

def spring_arrangements(springs, contiguous_damage, flag=False):
    def inner():
        "function from part 1 that calculates the number of valid arrangements"
        if springs == '':
            return 1 if sum(contiguous_damage) == 0 else 0
        
        if sum(contiguous_damage) == 0:
            return 0 if '#' in springs else 1
        
        if springs[0] == '#':
            if flag and contiguous_damage[0] == 0:
                return 0
            return spring_arrangements(springs[1:], (contiguous_damage[0] - 1, *contiguous_damage[1:]), True)
        
        if springs[0] == '.':
            if flag and contiguous_damage[0] > 0:
                return 0
            # if contiguous_damage[0] == 0:
            #     contiguous_damage = contiguous_damage[1:]
            return spring_arrangements(springs[1:], contiguous_damage[1:] if contiguous_damage[0] == 0 else contiguous_damage, False)

        if flag:
            if contiguous_damage[0] == 0:
                return spring_arrangements(springs[1:], contiguous_damage[1:], False)
            return spring_arrangements(springs[1:], (contiguous_damage[0] - 1, *contiguous_damage[1:]), True)
            
        return spring_arrangements(springs[1:], contiguous_damage, False) + spring_arrangements(springs[1:], (contiguous_damage[0] - 1, *contiguous_damage[1:]), True)

    key = (springs, contiguous_damage, flag)
    if key not in cache:
        cache[key] = inner()
    
    return cache[key]
#%%
part1 = 0
part2 = 0
for k,v in hot_springs.items():
    springs, contiguous_damage = v['springs'], v['contiguous_damage']
    part1 += spring_arrangements(springs, contiguous_damage)
    part2 += spring_arrangements('?'.join([springs]*5), contiguous_damage*5)
print(f'Part 1: {part1}')
print(f'Part 2: {part2}')
#%%
#* second video solution
cache = {}

def count(cfg, nums):
    if cfg == "":
        return 1 if nums == () else 0
    if nums == ():
        return 0 if '#' in cfg else 1
    
    key = (cfg, nums)
    if key in cache:
        return cache[key]
    
    result = 0
    if cfg[0] in '.?':
        result += count(cfg[1:], nums)
    if cfg[0] in '#?':
        if nums[0] <= len(cfg) and "." not in cfg[:nums[0]] and (nums[0] == len(cfg) or cfg[nums[0]] != "#"):
            result += count(cfg[nums[0] + 1:], nums[1:])
    
    cache[key] = result
    return result

part1 = 0
part2 = 0
for line in read_lines:
    cfg, nums = line.split()
    nums = tuple(map(int, nums.split(',')))
    part1 += count(cfg, nums)
    part2 += count('?'.join([cfg]*5), nums*5)
print(f'Part 1: {part1}')
print(f'Part 2: {part2}')
#%%
# solutions by HyperNeutrino
#* https://www.youtube.com/watch?v=G9EjRudvGY0&list=PLnNm9syGLD3zLoIGWeHfnEekEKxPKLivw
#* https://www.youtube.com/watch?v=g3Ms5e7Jdqo&list=PLnNm9syGLD3zLoIGWeHfnEekEKxPKLivw