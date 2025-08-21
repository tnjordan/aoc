#%%
f = 'data/day16.txt'

with open(file=f) as input:
    read_lines = input.readlines()
read_lines = [l.strip() for l in read_lines]
print('🎅 🎄 🤶')
#%%

MFCSAM = {  'children': 3,
            'cats': 7,
            'samoyeds': 2,
            'pomeranians': 3,
            'akitas': 0,
            'vizslas': 0,
            'goldfish': 5,
            'trees': 3,
            'cars': 2,
            'perfumes': 1
        }

for l in read_lines:
    l = l.replace('Sue ','')
    k,v = l.split(': ', 1)
    for fact in v.split(','):
        item, quantity = fact.split(': ')
        item = item.strip()
        quantity = int(quantity)


        if MFCSAM[item] == quantity:
            continue
        else:
            break
    else:
        print(f'Send thanks to Sue #{k}')

#%%
#! part 2
for l in read_lines:
    l = l.replace('Sue ','')
    k,v = l.split(': ', 1)
    for fact in v.split(','):
        item, quantity = fact.split(': ')
        item = item.strip()
        quantity = int(quantity)

        if item in ['cats', 'trees']:
            if MFCSAM[item] < quantity:
                continue
            else:
                break
        elif item in ['pomeranians', 'goldfish']:
            if MFCSAM[item] > quantity:
                continue
            else:
                break
        else:
            if MFCSAM[item] == quantity:
                continue
            else:
                break
    else:
        print(f'Send thanks to Sue #{k}')

#%%
print()
print('⭐ ⭐')
