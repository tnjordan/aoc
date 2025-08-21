#%%
from collections import Counter

f = 'data/day06.txt'

with open(file=f) as input:
    read_lines = input.readlines()
read_lines = [li.strip() for li in read_lines]
print('🎅 🎄 🤶')
#%%

message = ''
for i in range(len(read_lines[0])):
    letters = ''
    for line in read_lines:
        letters += line[i]
    letter_counts = Counter(letters)
    message += letter_counts.most_common(1)[0][0]

print(f'message from 🎅: {message}')

#%%
#! part 2

message = ''
for i in range(len(read_lines[0])):
    letters = ''
    for line in read_lines:
        letters += line[i]
    letter_counts = Counter(letters)
    message += letter_counts.most_common()[-1][0]

print(f'message from 🎅: {message}')

#%%
print()
print('⭐ ⭐')
