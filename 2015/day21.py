#%%
f = 'data/day21.txt'

with open(file=f) as input:
    read_lines = input.readlines()
read_lines = [l.strip() for l in read_lines]
print('🎅 🎄 🤶')
#%%

boss_hp = int(read_lines[0].split(': ')[1])
boss_damage = int(read_lines[1].split(': ')[1])
boss_armor = int(read_lines[2].split(': ')[1])


# Weapons:    Cost  Damage  Armor
# Dagger        8     4       0
# Shortsword   10     5       0
# Warhammer    25     6       0
# Longsword    40     7       0
# Greataxe     74     8       0
weapons = {
    'dagger': {'cost': 8, 'damage': 4, 'armor': 0},
    'shortsword': {'cost': 10, 'damage': 5, 'armor': 0},
    'warhammer': {'cost': 25, 'damage': 6, 'armor': 0},
    'longsword': {'cost': 40, 'damage': 7, 'armor': 0},
    'greataxe': {'cost': 74, 'damage': 8, 'armor': 0},
}

# Armor:      Cost  Damage  Armor
# Leather      13     0       1
# Chainmail    31     0       2
# Splintmail   53     0       3
# Bandedmail   75     0       4
# Platemail   102     0       5
armor = {
    'leather': {'cost': 13, 'damage': 0, 'armor': 1},
    'chainmail': {'cost': 31, 'damage': 0, 'armor': 2},
    'splintmail': {'cost': 53, 'damage': 0, 'armor': 3},
    'bandedmail': {'cost': 75, 'damage': 0, 'armor': 4},
    'platemail': {'cost': 102, 'damage': 0, 'armor': 5},
}

# Rings:      Cost  Damage  Armor
# Damage +1    25     1       0
# Damage +2    50     2       0
# Damage +3   100     3       0
# Defense +1   20     0       1
# Defense +2   40     0       2
# Defense +3   80     0       3
rings = {
    'damage1': {'cost': 25, 'damage': 1, 'armor': 0},
    'damage2': {'cost': 50, 'damage': 2, 'armor': 0},
    'damage3': {'cost': 100, 'damage': 3, 'armor': 0},
    'defense1': {'cost': 20, 'damage': 0, 'armor': 1},
    'defense2': {'cost': 40, 'damage': 0, 'armor': 2},
    'defense3': {'cost': 80, 'damage': 0, 'armor': 3},
}


def battle(p1_hp, p1_damage, p1_armor, boss_hp, boss_damage, boss_armor):
    p1_turn = True
    while p1_hp > 0 and boss_hp > 0:
        if p1_turn:
            boss_hp -= max(p1_damage - boss_armor, 1)
        else:
            p1_hp -= max(boss_damage - p1_armor, 1)
        p1_turn = not p1_turn
    return p1_hp > 0

money_spent = 200
for w in weapons:
    for a in [None] + list(armor.keys()):
        for r1 in [None] + list(rings.keys()):
            for r2 in [None] + list(rings.keys()):
                if r1 is not None and r2 is not None and r1 == r2:
                    continue
                gear_cost = weapons[w]['cost'] + (0 if a is None else armor[a]['cost']) + (0 if r1 is None else rings[r1]['cost']) + (0 if r2 is None else rings[r2]['cost'])
                if gear_cost >= money_spent:
                    continue
                p1_hp = 100
                p1_damage = 0
                p1_armor = 0
                p1_damage += weapons[w]['damage']
                if a is not None:
                    p1_armor += armor[a]['armor']
                if r1 is not None:
                    p1_damage += rings[r1]['damage']
                    p1_armor += rings[r1]['armor']
                if r2 is not None:
                    p1_damage += rings[r2]['damage']
                    p1_armor += rings[r2]['armor']
                if battle(p1_hp, p1_damage, p1_armor, boss_hp, boss_damage, boss_armor):
                    money_spent = gear_cost

print(f'player 1 needs ${money_spent} to win')
#%%
#! part 2
money_spent = 0
for w in weapons:
    for a in [None] + list(armor.keys()):
        for r1 in [None] + list(rings.keys()):
            for r2 in [None] + list(rings.keys()):
                if r1 is not None and r2 is not None and r1 == r2:
                    continue
                gear_cost = weapons[w]['cost'] + (0 if a is None else armor[a]['cost']) + (0 if r1 is None else rings[r1]['cost']) + (0 if r2 is None else rings[r2]['cost'])
                if gear_cost <= money_spent:
                    continue
                p1_hp = 100
                p1_damage = 0
                p1_armor = 0
                p1_damage += weapons[w]['damage']
                if a is not None:
                    p1_armor += armor[a]['armor']
                if r1 is not None:
                    p1_damage += rings[r1]['damage']
                    p1_armor += rings[r1]['armor']
                if r2 is not None:
                    p1_damage += rings[r2]['damage']
                    p1_armor += rings[r2]['armor']
                if not battle(p1_hp, p1_damage, p1_armor, boss_hp, boss_damage, boss_armor):
                    money_spent = gear_cost

print(f'player 1 can spend upto ${money_spent} and lose 🤷‍♂️')  #nice copilot emoji

print()
print('⭐ ⭐')
