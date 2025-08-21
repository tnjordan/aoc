#%%
f = 'data/day04.txt'

with open(file=f) as input:
    read_lines = input.readlines()
read_lines = [line.strip() for line in read_lines]
print('❄️⛄❄️')
#%%
valid_passphrases = 0
for line in read_lines:
    words = line.split()
    if len(words) == len(set(words)):
        valid_passphrases += 1
print(f'{valid_passphrases} valid passphrases')

#%%
#! part 2
valid_passphrases = 0
for line in read_lines:
    valid = True
    words = line.split()
    for i, w in enumerate(words):
        for w_comp in words[i+1:]:
            if sorted(w) == sorted(w_comp):
                valid = False
                break
        if not valid:
            break
    else:
        valid_passphrases += 1
print(f'{valid_passphrases} valid passphrases')
#%%
