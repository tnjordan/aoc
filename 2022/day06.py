#%%
f = 'data/day06.txt'

with open(file=f) as input:
    read_lines = input.readlines()
read_lines = [l.strip() for l in read_lines]
print('🎅 🎄 🤶')

signal = read_lines[0]

#! part 1
for index in range(len(signal)):
    if len(set(signal[index:index+4])) == 4:
        print(f'signal start: {index+4}') #* +4 to adjust counting to start with 1
        break

#%%
# signal = 'mjqjpqmgbljsphdztnvjfqwrcgsmlb' #* test run, because too lazy to count and didn't know if I needed to offset 14 or 18 (for 4 character marker)
#! part 2
for index in range(len(signal)):
    if len(set(signal[index:index+14])) == 14:
        print(f'signal start: {index+14}') #* +14 to adjust counting to start with 1
        break

#%%
print()
print('⭐ ⭐')