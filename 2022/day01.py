#%%
f = 'data/day01.txt'

with open(file=f) as input:
    read_lines = input.readlines()
# %%
#! Part 1
cal = 0
max_cal = float('-inf')
for l in read_lines:
    l = l.strip()
    try:
        cal += int(l)
    except ValueError:
        if cal > max_cal:
            max_cal = cal
        cal = 0

print(f'max elf calories: {max_cal}')

# %%
#! Part 2
cal = 0
elf_calories = []
for l in read_lines:
    l = l.strip()
    if l == '':
        elf_calories.append(cal)
        cal = 0
    else:
        cal += int(l)

elf_calories.sort(reverse=True)
print(f'top 3 elves are carrying:  {elf_calories[0:3]}')
print(f'for a total caloric count of {sum(elf_calories[0:3])}')

# %%

#! Bonus Challenge: List inComprehension
idx = [-1]
k2 = sorted([sum([int(x) for x in [line.strip() for line in read_lines][idx[i]+1:idx[i+1]]]) for i in range(len([idx.append(i) for i,v in enumerate([line.strip() for line in read_lines]) if v == '']))])
print(f'top 3 elves are carrying:  {k2[-3:]}')
print(f'for a total caloric count of {sum(k2[-3:])}')


# %%
