#%%
import regex as re
#! Part 1
input = open('data/day2.txt')
read_lines = input.readlines()
ans = 0
for l in read_lines:
    l = l.strip()
    result = re.search('(\d+)-(\d+) (\w): (\w+)', l)
    min, max, char, pwd = result.groups()
    char_count = pwd.count(char)
    if char_count >= int(min) and char_count <= int(max):
        ans += 1
print(f'part1 answer: {ans}')

# %%
# Part 2
input = open('data/day2.txt')
read_lines = input.readlines()
ans = 0
for l in read_lines:
    l = l.strip()
    result = re.search('(\d+)-(\d+) (\w): (\w+)', l)
    min, max, char, pwd = result.groups()
    char_count = pwd.count(char)
    min = int(min)
    max = int(max)
    if char == pwd[min-1] and char != pwd[max-1]:
        ans += 1
    elif char != pwd[min-1] and char == pwd[max-1]:
        ans += 1
print(f'part2 answer: {ans}')
# %%
