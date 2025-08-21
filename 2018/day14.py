#%%
f = 'data/day14.txt'

with open(file=f) as input:
    read_lines = input.readlines()
read_lines = [li.strip() for li in read_lines]
print('🎅 🎄 🤶')
#%%
recipes = [int(x) for x in list(read_lines[0])]
recipes = [3, 7]

elf_1 = 0
elf_2 = 1
# after = 2018
after = int(read_lines[0])

# for i in range(10):
while len(recipes) < after + 10:
    new_recipe = recipes[elf_1] + recipes[elf_2]
    recipes.extend([int(x) for x in list(str(new_recipe))])
    elf_1 = (elf_1 + 1 + recipes[elf_1]) % len(recipes)
    elf_2 = (elf_2 + 1 + recipes[elf_2]) % len(recipes)

print(''.join([str(x) for x in recipes[after:after + 10]]))

#? this more complicated thing I tried, because I can't read instructions
#! which i can use for part 2
digits = [int(x) for x in list(read_lines[0])]
recipes = [3, 7]
elf_1 = 0
elf_2 = 1

while recipes[-len(digits) - 10: -10] != digits:
    new_recipe = recipes[elf_1] + recipes[elf_2]
    recipes.extend([int(x) for x in list(str(new_recipe))])
    elf_1 = (elf_1 + 1 + recipes[elf_1]) % len(recipes)
    elf_2 = (elf_2 + 1 + recipes[elf_2]) % len(recipes)

# print(''.join([str(x) for x in recipes[-10]])) #? from the failed attempt
print(len(recipes) - len(digits) - 10) #* the -10 is because that loop goes 10 too far
#%%
print()
print('⭐ ⭐')
