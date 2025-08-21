#%%
f = 'data/day03.txt'

with open(file=f) as input:
    read_lines = input.readlines()
read_lines = [line.strip() for line in read_lines]
print('🎅 🎄 🤶')
#%%
valid = 0
for line in read_lines:
    sides = [int(x) for x in line.split()]
    a, b, c = sorted(sides)
    if a + b > c:
        valid += 1

print(f'{valid} triangles')

#%%
#! part 2
valid = 0

for i in range(0, len(read_lines), 3):
    for j in range(3):
        sides = []
        for k in range(3):
            row = read_lines[i + k].split()
            sides.append(int(row[j]))
        a, b, c = sorted(sides)
        if a + b > c:
            valid += 1

print(f'{valid} triangles')

#%%
print()
print('⭐ ⭐')
