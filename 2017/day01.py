#%%
f = 'data/day01.txt'

with open(file=f) as input:
    read_lines = input.readlines()
read_lines = [line.strip() for line in read_lines]
print('❄️⛄❄️')
#%%
input = read_lines[0]

part_1 = 0
for i,d in enumerate(input):
    if d == input[i-1]:
        part_1 += int(d)
print(f'captcha: {part_1}')
#%%
#! part 2
part_2 = 0
half = len(input)/2

for i,d in enumerate(input):
    if d == input[int((i+half)%len(input))]:
        part_2 += int(d)
print(f'captcha: {part_2}')
#%%
print()
print('⭐⭐')
