#%%
f = open('data\day10_input.txt', 'r')
read_lines = f.readlines()
f.close()

# %%
#! Part 1
open_chars = ['(','[','{','<']
char_pairs = {')':'(',']':'[','}':'{','>':'<'}
corruption_values = {')':3,']':57,'}':1197,'>':25137}
chunk = []
corruption_score = 0
corrupted = False
lines = []
for l in read_lines:
    l = l.strip()
    for c in l:
        if c in open_chars:
            chunk.append(c)
        else:
            if char_pairs[c] == chunk[-1]:
                chunk.pop(-1)
            else:
                print('corruption detected! expected close for', chunk[-1], 'got', c)
                corruption_score += corruption_values[c]
                corrupted = True
                break
    if not corrupted:
        lines.append(l)
    corrupted = False

print(corruption_score)

# %%
#! Part 2
#used the input so I don't have to make a new dictionary going opposite of char_pairs
auto_complete_values = {'(':1,'[':2,'{':3,'<':4}
auto_complete_score = 0
auto_complete_score_list = []
for l in lines:
    l = l.strip()
    for c in l:
        if c in open_chars:
            chunk.append(c)
        else:
            if char_pairs[c] == chunk[-1]:
                chunk.pop(-1)
    print(chunk)
    for c in reversed(chunk):
        auto_complete_score = auto_complete_score * 5 + auto_complete_values[c]
    auto_complete_score_list.append(auto_complete_score)
    auto_complete_score = 0
    chunk = []

import statistics
answer2 = statistics.median(auto_complete_score_list)
print(answer2)

# %%
