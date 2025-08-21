#%%
f = 'data/day03.txt'

with open(file=f) as input:
    read_lines = input.readlines()
read_lines = [l.strip() for l in read_lines]
print('🎅 🎄 🤶')

priority = []
for pack in read_lines:
    half = int(len(pack)/2)
    c1 = pack[:half]
    c2 = pack[half:]
    letter = set(c1) & set(c2)
    letter = letter.pop()
    number = ord(letter) - 64 + 26 if letter.isupper() else ord(letter) - 96
    priority.append(number)
    # print(letter,number)

print(f'sum: {sum(priority)}')

#! Part 2
#%%
priority = []
for i in range(0,len(read_lines),3):
    print(i)
    elf1 = read_lines[i]
    elf2 = read_lines[i+1]
    elf3 = read_lines[i+2]
    letter = set(elf1) & set(elf2) & set(elf3)
    letter = letter.pop()
    number = ord(letter) - 64 + 26 if letter.isupper() else ord(letter) - 96
    priority.append(number)

print(f'sum: {sum(priority)}')
#%%
print()
print('⭐ ⭐')