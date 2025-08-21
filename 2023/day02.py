#%%
f = 'data/day02.txt'
# f = 'data/day02.ex'

with open(file=f) as input:
    read_lines = input.readlines()
read_lines = [line.strip() for line in read_lines]
print('❄️⛄❄️')
#%%
games = {}
for line in read_lines:
    game = line.split()[1][:-1]
    games[game] = {}
    cubes = line.split(': ')[1]
    for g in cubes.split('; '):
        for i, c in [x.split() for x in g.split(', ')]:
            if c not in games[game]:
                games[game][c] = 0
            games[game][c] = max(games[game][c], int(i))

bag = {'red': 12, 'green': 13, 'blue': 14}

valid = 0
ids = 0
for k, v in games.items():
    print(f'game: {k}')
    print(f'cubes: {v}')
    for c, i in v.items():
        print(f'color: {c} - count: {i}')
        if bag[c] >= i:
            print(f'continue: {c} - {bag[c]} >= {i}')
            continue  #* keep looking
        else:
            print(f'invalid game: {k}')
            break
    else:
        valid += 1
        ids += int(k)
print(f'valid games: {valid}')
print(f'sum ids: {ids}')
#%%
#! part 2
powers = []
for k, v in games.items():
    power = 1
    for c, i in v.items():
        power *= i
    powers.append(power)
print(f'total cube power: {sum(powers)}')
#%%
print()
print('⭐⭐')
