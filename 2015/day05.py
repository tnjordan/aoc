#%%
f = 'data/day05.txt'

with open(file=f) as input:
    read_lines = input.readlines()
read_lines = [l.strip() for l in read_lines]
print('🎅 🎄 🤶')
#%%
nice_strings = 0
for s in read_lines:
    if 'ab' in s or 'cd' in s or 'pq' in s or 'xy' in s:
        continue
    vowels = 0
    for v in 'aeiou':
        vowels += s.count(v)
    if vowels < 3:
        continue
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            nice_strings += 1
            break

print(f'🎅 has {nice_strings} nice strings')

#%%
#! part 2
nice_strings = 0
for s in read_lines:
    jump_pair = False
    for i in range(len(s) - 2):
        if s[i] == s[i + 2]:
            jump_pair = True
            break
    if jump_pair:
        double_pair = False
        for i in range(len(s) - 3):
            for j in range(i + 2, len(s) - 1):
                if s[i:i + 2] == s[j:j + 2]:
                    double_pair = True
                    nice_strings += 1
                    break
            if double_pair:
                break


print(f'🎅 actually has {nice_strings} nice strings')

#%%
print()
print('⭐ ⭐')
