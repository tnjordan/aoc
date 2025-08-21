#%%
f = 'data/day02.txt'

with open(file=f) as input:
    read_lines = input.readlines()
read_lines = [line.strip() for line in read_lines]
print('❄️⛄❄️')
#%%
checksum = 0
for line in read_lines:
    line = line.split('\t')
    line = [int(k2) for k2 in line]
    checksum += (max(line) - min(line))
print(f'checksum: {checksum}')
#%%
#! part 2
checksum = 0
for line in read_lines:
    line = line.split('\t')
    line = [int(k2) for k2 in line]
    for i, x in enumerate(line):
        for y in line[i+1:]:
            big,small = (max(x,y), min(x,y))
            if big%small == 0:
                checksum += big/small
print(f'checksum: {int(checksum)}')
#%%
print()
print('⭐⭐')
