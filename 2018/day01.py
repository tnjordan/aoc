#%%
f = 'data/day01.txt'

with open(file=f) as input:
    read_lines = input.readlines()
read_lines = [l.strip() for l in read_lines]
print('🎅 🎄 🤶')
#%%
ans_part1 = sum([int(x) for x in read_lines])
print(f'frequency sum: {ans_part1}')
#%%
freq = 0
freq_seen = set()
freq_seen.add(freq)

duplicate_found = False
while duplicate_found is not True:
    for x in read_lines:
        freq += int(x)
        if freq in freq_seen:
            duplicate_found = True
            print(f'duplicate found: {freq}')
            break
        else:
            freq_seen.add(freq)
#%%
print()
print('⭐ ⭐')
#%%
