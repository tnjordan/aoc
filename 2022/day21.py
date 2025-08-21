#%%
import re
f = 'data/day21.txt'
f = 'data/day21.ex'

with open(file=f) as input:
    read_lines = input.readlines()
read_lines = [l.strip() for l in read_lines]
print('🎅 🎄 🤶')

#* how I started
# monkey_screams = {}
# monkeys_int_screams = {}
# monkey_eq_screams = {}
# for l in read_lines:
#     m, e = l.split(sep=': ')
#     monkey_screams[m] = e #* can't eval(e) yet as variables not defined :(
#     try:
#         e = int(e)
#         monkeys_int_screams[m] = e
#     except ValueError:
#         monkey_eq_screams[m] = [re.split(' \* | \/ | \+ | \- ',e), e] #* monkeys queue and the equation.

#%%
#! super lazy way!
#* hoho it worked first try! I was trying to run it on the example input to see how long it ran
root = False
ints = []
monkey_screams = {}
while root is False:
    for l in read_lines:
        m, e = l.split(sep=': ')
        if m in ints:
            continue
        try:
            monkey_screams[m] = eval(re.sub(r'([a-z]{4})', r'monkey_screams["\1"]',e))
            if type(monkey_screams[m]) is int:
                ints.append(m)
            if m == 'root':
                root = monkey_screams[m]
                print(f'root is {root}')
                break
        except KeyError:
            pass

#%%
#! part 2
#* update dictionary of rules
monkey_screams_in = {}
for l in read_lines:
    m, e = l.split(sep=': ')
    if m == 'root':
        e = re.sub(r' \* | \/ | \+ | \- ', ' == ', e)
    monkey_screams_in[m] = e

root = False
ints = ['humn']
monkey_screams = {}
monkey_screams['humn'] = monkey_screams_in['humn'] = 0

# while root is False:
#     print('.',end='')
#     for m,e in monkey_screams_in.items():
#         if m in ints:
#             continue
#         try:
#             monkey_screams[m] = eval(re.sub(r'([a-z]{4})', r'monkey_screams["\1"]',e))
#             if type(monkey_screams[m]) is int:
#                 ints.append(m)
#             if m == 'root':
#                 root = monkey_screams[m]
#                 print(f'root is {root}')
#                 if root is True:
#                     print(f"you scream {monkey_screams_in['humn']}")
#                     break
#                 else:
#                     #* try again
#                     ints = ['humn']
#                     monkey_screams = {}
#                     #TODO do some split searching. Start at say 1000. based on x < y double/half guess and check again
#                     monkey_screams_in['humn'] += 1 #* += 1 works for example but it too slow on full input
#                     monkey_screams['humn'] = monkey_screams_in['humn']
#                     print(f"human screams {monkey_screams_in['humn']}")
#         except KeyError:
#             pass


#! get the root equation in terms of humn
root = False
ints = []
humans = ['humn']
monkey_screams = {}
monkey_screams['humn'] = monkey_screams_in['humn'] = 'humn'

while root is False:
    print('.',sep='')
    for m, e in monkey_screams_in.items():
        if m in ints or m in humans: #* solved to int or human lvl
            continue
        m_s = re.sub(r'([a-z]{4})', r'monkey_screams["\1"]',e)
        m_s = m_s.split(sep=' ')
        no_exc = True
        new_m_s = '( '
        for k in m_s:
            if 'monkey_screams' in k:
                try:
                    k = eval(k)
                except KeyError:
                    no_exc = False
                    k = re.search(r'\"([a-z]{4})\"',k).groups(0)[0]
                    pass
            new_m_s += f' {k} '
        new_m_s += ' )'
        if no_exc:
            if 'humn' in new_m_s:
                # print('a human has been detected in the loop!')
                # print(new_m_s)
                humans.append(m)
                monkey_screams[m] = new_m_s
                monkey_screams_in[m] = new_m_s
                if m == 'root':
                    print(f'devised the root monkey problem')
                    root = monkey_screams[m]
                    root = root.replace(' ', '') #* don't need the extra space now
                    print(f'root is {root}')
            else:
                monkey_screams[m] = eval(new_m_s)
                if type(monkey_screams[m]) is int:
                    ints.append(m)
                    monkey_screams_in[m] = monkey_screams[m]

#%%
solved = False
left_side, right_side = root.split(sep='==')
left_side = left_side[1:].strip()
right_side = eval(right_side[:-1].strip())

print(f'🤯 Sanity Check! 🤯')
print(not eval(left_side.replace('humn',str(0))) > eval(left_side.replace('humn',str(100))))
print()

#? That was it, it was a reversed search for my equation vs the example
my_sanity = not eval(left_side.replace('humn',str(0))) > eval(left_side.replace('humn',str(100)))

# humn = -1 #* part of the still too slow
min_scream = -1e24
max_scream = 1e24
humn = (min_scream + max_scream)//2
# while not solved:
for i in range(100):
    # humn += 1 #* still too slow
    left_side_eval = eval(left_side.replace('humn',str(humn)))
    print(f'left_side({humn:,}) = {left_side_eval:,}')
    if left_side_eval == right_side:
        print(f"you scream {humn}")
        solved = True
        break
    elif left_side_eval < right_side:
        print(f'\t🐁 too small')
        print(f'\tprevious search range: {min_scream} to {max_scream}')
        if my_sanity is True:
            min_scream = humn
        else:
            max_scream = humn
    elif left_side_eval > right_side:
        print(f'\t🐘 too large')
        print(f'\tprevious search range: {min_scream} to {max_scream}')
        if my_sanity is True:
            max_scream = humn
        else:
            min_scream = humn
    
    print(f'\tnew search range: {min_scream} to {max_scream}')
    humn = (min_scream + max_scream)//2

#%%
print()
print('⭐ ⭐')