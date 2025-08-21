#%%
import string
f = 'data/day11.txt'

with open(file=f) as input:
    read_lines = input.readlines()
read_lines = [l.strip() for l in read_lines]
print('🎅 🎄 🤶')
#%%
pwd = read_lines[0]

abc = string.ascii_lowercase
abc = abc.replace('i','')
abc = abc.replace('o','')
abc = abc.replace('l','')

abc_123 = [abc[i:i+3] for i in range(len(abc)-2)]
abc_doubles = [x+x for x in abc]

abc_idx = {}
idx_abc = {}
c = 0
for l in abc:
    abc_idx[l] = c
    idx_abc[c] = l
    c += 1

def pwd_validator(pwd):
    for abc_seq in abc_123:
        if abc_seq in pwd:
            break
    else:
        return False
    
    for i, abc_do in enumerate(abc_doubles):
        if abc_do in pwd:
            for abc_do2 in abc_doubles[i+1:]:
                if abc_do2 in pwd:
                    return True
    return False


def pwd_increment(pwd):
    pwd_inc = list(pwd[::-1])
    for i, c in enumerate(pwd_inc):
        v_c = abc_idx[c]
        v_c += 1
        v_c = v_c % 23  # have 23 letter alphabet
        pwd_inc[i] = idx_abc[v_c]
        if v_c != 0:
            break  #* don't continue increment
    return ''.join(pwd_inc[::-1])


valid = False
while valid is not True:
    pwd = pwd_increment(pwd)
    valid = pwd_validator(pwd)

print(f'🎅 next password is: {pwd}')

#%%
#! part 2
pwd = pwd_increment(pwd)
valid = pwd_validator(pwd)
while valid is not True:
    pwd = pwd_increment(pwd)
    valid = pwd_validator(pwd)

print(f'🎅 next password is: {pwd}')
#%%
print()
print('⭐ ⭐')
