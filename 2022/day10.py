#%%
f = 'data/day10.ex'
f = 'data/day10.txt'

with open(file=f) as input:
    read_lines = input.readlines()
read_lines = [l.strip() for l in read_lines]
print('🎅 🎄 🤶')

rules = read_lines #* rules are instructions

X = 1
cycle = 0
signal_search = [20,60,100,140,180,220]
signal_strength = []

for r in rules:
    if r == 'noop':
        cycle += 1
        # if cycle % 20 == 0:
        if cycle in signal_search:
            print(f'cycle:{cycle} X:{X} Signal: {cycle*X}')
            signal_strength.append(cycle*X)
    else:
        x = int(r.split()[1]) #* assume all other instructions are addx
        for _ in range(2):
            cycle += 1
            # if cycle % 20 == 0:
            if cycle in signal_search:
                print(f'cycle:{cycle} X:{X} Signal: {cycle*X}')
                signal_strength.append(cycle*X)
        X += x

print(f'signal_strength: {sum(signal_strength)}') #* first error not reading problem

#%%
#! part 2
from tabulate import tabulate #* makes display nice

X = 1
cycle = 0
display = []
display_row = []


def crt(X,cycle):
    c = cycle % 40
    sprite_range = range(X-1,X+2)
    if c in sprite_range:
        return '#'
    else:
        return ' '

for r in rules:
    if r == 'noop':
        display_row.append(crt(X,cycle))
        cycle += 1
        if cycle % 40 == 0:
            display.append(display_row)
            display_row = []

    else:
        x = int(r.split()[1]) #* assume all other instructions are addx
        for _ in range(2):
            display_row.append(crt(X,cycle))
            cycle += 1
            if cycle % 40 == 0:
                display.append(display_row)
                display_row = []
        X += x

print(tabulate(display))

#%%
print()
print('⭐ ⭐')