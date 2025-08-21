#%%
f = 'data/day22.txt'

with open(file=f) as puzzle_input:  # best not to use input as a variable name
    read_lines = puzzle_input.readlines()
read_lines = [li.strip() for li in read_lines]
print('🎅 🎄 🤶')
#%%
boss_hp = int(read_lines[0].split(': ')[1])
boss_damage = int(read_lines[1].split(': ')[1])

spells = {
    'magic_missile': {  'cost': 53,     'damage': 4,    'heal': 0,  'shield': 0, 'mana': 0,     'duration': 0},
    'drain': {          'cost': 73,     'damage': 2,    'heal': 2,  'shield': 0, 'mana': 0,     'duration': 0},
    'shield': {         'cost': 113,    'damage': 0,    'heal': 0,  'shield': 7, 'mana': 0,     'duration': 6},
    'poison': {         'cost': 173,    'damage': 3,    'heal': 0,  'shield': 0, 'mana': 0,     'duration': 6},
    'recharge': {       'cost': 229,    'damage': 0,    'heal': 0,  'shield': 0, 'mana': 101,   'duration': 5},
}

effects = {
    'magic_missile': 0,
    'drain': 0,
    'shield': 0,
    'poison': 0,
    'recharge': 0,
}

p1_hp = 50
p1_mana = 500
p1_shield = 0


def battle_round(p1_turn, p1_hp, p1_mana, spell, effects, boss_hp, mana_spent):
    if part_2:
        p1_hp -= 1

    # print(f'current effects pre: {effects}')
    effects = effects.copy()
    if effects['shield'] > 0:
        # print('shield active')
        p1_shield = spells['shield']['shield']
        effects['shield'] -= 1
    else:
        p1_shield = 0
    if effects['poison'] > 0:
        # print('poison damage')
        boss_hp -= spells['poison']['damage']
        effects['poison'] -= 1
    if effects['recharge'] > 0:
        # print('recharging mana')
        p1_mana += spells['recharge']['mana']
        effects['recharge'] -= 1
    # print(f'current effects post: {effects}')

    bs = battle_status(p1_hp, p1_mana, boss_hp)  # check if poison killed boss (or if player died in part 2, player dies first in battle_status)
    if bs is not None:
        # print('poison killed boss', p1_hp, p1_mana, boss_hp)
        return p1_turn, p1_hp, p1_mana, effects, boss_hp, mana_spent

    if p1_turn:
        mana_spent += spells[spell]['cost']
        p1_mana -= spells[spell]['cost']
        assert p1_mana >= 0, f'player ran out of mana! {p1_mana} {spell}'
        if spell in ['magic_missile', 'drain']:
            boss_hp -= spells[spell]['damage']
            p1_hp += spells[spell]['heal']
        else:
            effects[spell] = spells[spell]['duration']
        p1_turn = False
        # print(f'Player casts {spell}.')
        # print(f'Player has {p1_hp} hit points, {p1_mana} mana')
        # print(f'Boss has {boss_hp} hit points')
    else:
        p1_hp -= max(boss_damage - p1_shield, 1)
        p1_turn = True
        # print(f'Boss attacks for {max(boss_damage - p1_shield, 1)} damage.')
        # print(f'Player has {p1_hp} hit points, {p1_mana} mana')
        # print(f'Boss has {boss_hp} hit points')

    return p1_turn, p1_hp, p1_mana, effects, boss_hp, mana_spent


def battle_status(p1_hp, p1_mana, boss_hp):
    # print(f'Player has {p1_hp} hit points, {p1_mana} mana')
    # print(f'Boss has {boss_hp} hit points')
    if p1_hp <= 0:
        # print('Player died.')
        return False
    if boss_hp <= 0:
        # print('Boss died.')
        return True
    # print('the battle rages on')
    return None


def available_spells(effects, p1_mana):
    return [s for s in spells if spells[s]['cost'] <= ((p1_mana + 101) if (effects['recharge'] > 0) else p1_mana) and effects[s] <= 1]


part_2 = False
min_mana = 10_000


def auto_battle(p1_turn, p1_hp, p1_mana, boss_hp, effects, mana_spent):
    global min_mana
    if mana_spent >= min_mana:
        # print('too much mana spent, no need to continue')
        return None
    bs = battle_status(p1_hp, p1_mana, boss_hp)
    if bs is not None:
        if bs is True:
            # print('victory: @', mana_spent)
            min_mana = min(min_mana, mana_spent)
            # print(min_mana)
            return None
        else:
            # print('dead')
            return None
    if p1_turn:
        a_spells = available_spells(effects, p1_mana)  # trying something new
        if a_spells == []:
            # print('no spells available')
            return None
        for spell in a_spells:
            # print('spell', spell)
            p1_turn_br, p1_hp_br, p1_mana_br, effects_br, boss_hp_br, mana_spent_br = battle_round(p1_turn, p1_hp, p1_mana, spell, effects, boss_hp, mana_spent)
            auto_battle(p1_turn_br, p1_hp_br, p1_mana_br, boss_hp_br, effects_br, mana_spent_br)

    else:
        p1_turn_br, p1_hp_br, p1_mana_br, effects_br, boss_hp_br, mana_spent_br = battle_round(p1_turn, p1_hp, p1_mana, None, effects, boss_hp, mana_spent)
        auto_battle(p1_turn_br, p1_hp_br, p1_mana_br, boss_hp_br, effects_br, mana_spent_br)


auto_battle(True, p1_hp, p1_mana, boss_hp, effects, 0)
print(f'minimum mana: {min_mana}')

#%%
# fun interactive battle, made by co-pilot
# def battle(p1_hp, p1_mana, boss_hp, boss_damage, effects):
#     mana_spent = 0
#     p1_turn = True
#     while True:
#         print('---')
#         print(f'Player has {p1_hp} hit points, {spells["shield"]["shield"] if effects["shield"] > 0 else 0} shield, {p1_mana} mana')
#         print(f'Boss has {boss_hp} hit points')
#         print('\t---')
#         print('\tPlayer turn')
#         print('\t---')
#         for s in spells:
#             print(f'{s} costs {spells[s]["cost"]} mana')
#         spell = input('Which spell do you cast? ')
#         p1_turn, p1_hp, p1_mana, effects, boss_hp, boss_damage, mana_spent = battle_round(p1_turn, p1_hp, p1_mana, spell, effects, boss_hp, boss_damage, mana_spent)
#         if battle_status(p1_hp, p1_mana, boss_hp) is not None:
#             return battle_status(p1_hp, p1_mana, boss_hp)
#         print('\t---')
#         print('\tBoss turn')
#         print('\t---')
#         p1_turn, p1_hp, p1_mana, effects, boss_hp, boss_damage, mana_spent = battle_round(p1_turn, p1_hp, p1_mana, spell, effects, boss_hp, boss_damage, mana_spent)
#         if battle_status(p1_hp, p1_mana, boss_hp) is not None:
#             return battle_status(p1_hp, p1_mana, boss_hp)


# battle(p1_hp=10, p1_mana=250, boss_hp=14, boss_damage=8, effects=effects)
#%%
print()
print('⭐ ⭐')
#%%
