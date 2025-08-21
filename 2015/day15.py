#%%
import re
f = 'data/day15.txt'

with open(file=f) as input:
    read_lines = input.readlines()
read_lines = [l.strip() for l in read_lines]
print('🎅 🎄 🤶')
#%%
ingredents = {}
for l in read_lines:
    stats = re.findall('-?\d+',l)
    l = l.split()
    ingredents[l[0]] = [int(x) for x in stats]

ingreds = list(ingredents.values())

#%%
max_cookie = 0
max_ingredents = []
for i in range(100):
    print(i)
    for j in range(100 - i):
        for k in range(100 - i - j):
            z = 100 - i - j - k
            # print(sum([i,j,k,z]),': ',i,j,k,z)
            capacity = 0
            durability = 0
            flavor = 0
            texture = 0
            ingredents_q = [i,j,k,z]
            for x in range(4):
                capacity += ingreds[x][0] * ingredents_q[x]
                durability += ingreds[x][1] * ingredents_q[x]
                flavor += ingreds[x][2] * ingredents_q[x]
                texture += ingreds[x][3] * ingredents_q[x]
            capacity = max(0,capacity)
            durability = max(0,durability)
            flavor = max(0,flavor)
            texture = max(0,texture)
            score = capacity * durability * flavor * texture
            if score > max_cookie:
                max_cookie = score
                max_ingredents = ingredents_q

print(f'best cookie:')
for i,q in zip(ingredents.keys(),max_ingredents):
    print(f'\t{q} teaspoons {i}')
print(f'score: {max_cookie}')

#%%
#! part 2
max_cookie = 0
max_ingredents = []
for i in range(100):
    print(i)
    for j in range(100 - i):
        for k in range(100 - i - j):
            z = 100 - i - j - k
            capacity = 0
            durability = 0
            flavor = 0
            texture = 0
            calories = 0
            ingredents_q = [i,j,k,z]
            for x in range(4):
                capacity += ingreds[x][0] * ingredents_q[x]
                durability += ingreds[x][1] * ingredents_q[x]
                flavor += ingreds[x][2] * ingredents_q[x]
                texture += ingreds[x][3] * ingredents_q[x]
                calories += ingreds[x][4] * ingredents_q[x]
            if calories != 500:
                continue
            capacity = max(0,capacity)
            durability = max(0,durability)
            flavor = max(0,flavor)
            texture = max(0,texture)
            score = capacity * durability * flavor * texture
            if score > max_cookie:
                max_cookie = score
                max_ingredents = ingredents_q

print(f'best cookie at 500 calories:')
for i,q in zip(ingredents.keys(),max_ingredents):
    print(f'\t{q} teaspoons {i}')
print(f'score: {max_cookie}')

#%%
print()
print('⭐ ⭐')
