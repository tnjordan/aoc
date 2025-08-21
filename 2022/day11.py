#%%
import re
from collections import deque 
from tabulate import tabulate

f = 'data/day11.txt'
# f = 'data/day11.ex'
# f = 'data/day11.ex2' #* only works with modified for d in data: used to look for pattern in repeats

with open(file=f) as input:
    i = input.read() #* modified from standard
data = i.split('\n\n') #* easier to split instructions
data = [x.split('\n') for x in data]
print('🎅 🎄 🤶')

monks = ['🙈', '🙉', '🙊']
monkey = {}

for d in data:
    for i,l in enumerate(d):
        l = re.sub('[^0-9,+*]', "", l) #* keep only # and ,+*
        l = l.split(sep=',')
        if i == 2:
            try:
                l = [l[0][0], int(l[0][1:])]
            except:
                print('out')
                l = [l[0][0], l[0][1:]]
        else:
            l = [int(x) for x in l] #* if l[0] != ''
        if i == 0:
            m = l[0] #* remember the monkey
            monkey[m] = [] #* init monkey
        elif i == 1:
            monkey[m].append(deque(l))
        elif i == 2:
            monkey[m].append(l)
        else:
            monkey[m].append(l[0])
    monkey[m].append(0) #* for the activitiy score

# for d in data:
#     for i,l in enumerate(d):
#         l = re.sub('[^0-9,+*]', "", l) #* keep only # and ,+*
#         l = l.split(sep=',')
#         if i == 2:
#             try:
#                 l = [l[0][0], int(l[0][1:])]
#             except:
#                 print('out')
#                 l = [l[0][0], l[0][1:]]
#         else:
#             try: #* needed for example 2 debug
#                 l = [int(x) for x in l] #* if l[0] != ''
#             except:
#                 l = []
#         if i == 0:
#             m = l[0] #* remember the monkey
#             monkey[m] = [] #* init monkey
#         elif i == 1:
#             monkey[m].append(deque(l))
#         elif i == 2:
#             monkey[m].append(l)
#         else:
#             monkey[m].append(l[0])
#     monkey[m].append(0) #* for the activitiy score


for i in range(20):
    print(f'round: {i+1}')
    # print(tabulate(monkey))
    for m,v in monkey.items(): #* m is the key, typicaly use k,v
        print(f'\t{monks[m%3]} {m}')
        while v[0]: #* iterate over the items in deque
            item = v[0].popleft()
            monkey[m][-1] += 1
            #* fix for Monkey 3 old**2
            if v[1][0] == '*':
                if v[1][1] == '':
                    if item * item // 3 % v[2] == 0: #! Operation: new = old * old'
                        monkey[v[3]][0].extend([item * item // 3])
                    else:
                        monkey[v[4]][0].extend([item * item // 3])
                else:
                    if item * v[1][1] // 3 % v[2] == 0:
                        monkey[v[3]][0].extend([item * v[1][1] // 3])
                    else:
                        monkey[v[4]][0].extend([item * v[1][1] // 3])
            elif v[1][0] == '+':
                if v[1][1] == '':
                    if (item + item )// 3 % v[2] == 0: #! Potential Operation: new = old + old'
                        monkey[v[3]][0].extend([(item + item )// 3])
                    else:
                        monkey[v[4]][0].extend([(item + item )// 3])
                else:
                    if (item + v[1][1]) // 3 % v[2] == 0: #! Order of Operations
                        monkey[v[3]][0].extend([(item + v[1][1]) // 3])
                    else:
                        monkey[v[4]][0].extend([(item + v[1][1]) // 3])
            # print(tabulate(monkey))

monkey_activity = []
for v in monkey.values():
    monkey_activity.append(v[-1])
monkey_activity.sort()

print(f'Monkey Madness: {monkey_activity[-1]*monkey_activity[-2]}')

#%%
#! part 2

#* can't track the actual worry level. Computer slows around at ~400 rounds.
#* took 2 min to print the monkey dictionary.

monkey = {}

for d in data:
    for i,l in enumerate(d):
        l = re.sub('[^0-9,+*]', "", l) #* keep only # and ,+*
        l = l.split(sep=',')
        if i == 2:
            try:
                l = [l[0][0], int(l[0][1:])]
            except:
                print('out')
                l = [l[0][0], l[0][1:]]
        else:
            l = [int(x) for x in l] #* if l[0] != ''
        if i == 0:
            m = l[0] #* remember the monkey
            monkey[m] = [] #* init monkey
        elif i == 1:
            monkey[m].append(deque(l))
        elif i == 2:
            monkey[m].append(l)
        else:
            monkey[m].append(l[0])
    monkey[m].append(0) #* for the activitiy score

#* thought about this but unsure how to implement. 
#* got hint. https://www.youtube.com/watch?v=W9vVJ8gDxj4
lcm = 1
for k,v in monkey.items():
    lcm *= v[2]

for i in range(10_000):
    if (i+1) % 1_000 == 0:
        print(f'round: {i+1}')
    # print(tabulate(monkey))
    for m,v in monkey.items(): #* m is the key, typicaly use k,v
        # print(f'\t{monks[m%3]} {m}')
        while v[0]: #* iterate over the items in deque
            item = v[0].popleft()
            item = item % lcm
            monkey[m][-1] += 1
            #* fix for Monkey 3 old**2
            if v[1][0] == '*':
                if v[1][1] == '':
                    if item * item % v[2] == 0: #! Operation: new = old * old'
                        monkey[v[3]][0].extend([item * item])
                    else:
                        monkey[v[4]][0].extend([item * item])
                else:
                    if item * v[1][1] % v[2] == 0:
                        monkey[v[3]][0].extend([item * v[1][1]])
                    else:
                        monkey[v[4]][0].extend([item * v[1][1]])
            elif v[1][0] == '+':
                if v[1][1] == '':
                    if (item + item ) % v[2] == 0: #! Potential Operation: new = old + old'
                        monkey[v[3]][0].extend([(item + item )])
                    else:
                        monkey[v[4]][0].extend([(item + item )])
                else:
                    if (item + v[1][1]) % v[2] == 0: #! Order of Operations
                        monkey[v[3]][0].extend([(item + v[1][1])])
                    else:
                        monkey[v[4]][0].extend([(item + v[1][1])])
            # print(tabulate(monkey))

monkey_activity = []
for v in monkey.values():
    monkey_activity.append(v[-1])
monkey_activity.sort()

print(f'Monkey Madness: {monkey_activity[-1]*monkey_activity[-2]}')
#%%
print()
print('⭐ ⭐')
# %%
