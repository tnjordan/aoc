#%%
from copy import deepcopy

f = 'data/day19.txt'
# f = 'data/day19.ex'

with open(file=f) as input:
    instructions, parts = input.read().strip().split('\n\n')
    instructions = instructions.split('\n')
    parts = parts.replace('=', '":')
    parts = parts.replace('{', '{"')
    parts = parts.replace(',', ',"')
    parts = parts.split('\n')
print('❄️⛄❄️')
#%%
parts = [eval(p) for p in parts]


def make_instruct(instructions, part_1=True):
    instruct = {}
    for i in instructions:
        rule, action = i.split('{')
        instruct[rule] = []
        action = action[:-1]
        action = action.split(',')

        for a in action:
            if ':' in a:
                #TODO figure out match case
                op, act = a.split(':')
                if '<' in op:
                    category, value = op.split('<')
                    if part_1:
                        category = f'part["{category}"]'
                        eval_op = category + '<' + value
                    else:
                        eval_op = (category, '<', int(value))
                elif '>' in op:
                    category, value = op.split('>')
                    if part_1:
                        category = f'part["{category}"]'
                        eval_op = category + '>' + value
                    else:
                        eval_op = (category, '>', int(value))

                instruct[rule].append((eval_op, act))
            else:
                if part_1:
                    eval_op = 'True'  # for part_1 eval, eval('True') = True. eval needs a string
                else:
                    eval_op = True
                instruct[rule].append((eval_op, a))
    return instruct


instruct = make_instruct(instructions, part_1=True)
valid_parts = 0
accepted = []
for part in parts:
    A = False
    R = False
    rule = instruct['in']
    while A is False and R is False:
        for eval_op, act in rule:
            if eval(eval_op):
                next_act = act
                break
        if next_act == 'A':
            A = True
            accepted.append(part)
            valid_parts += sum(part.values())
        elif next_act == 'R':
            R = True
        else:
            rule = instruct[next_act]

print(f'⚙️ valid parts: {valid_parts}')
#%%
#! part 2
instruct = make_instruct(instructions, part_1=False)
opposite_eq = {'<': ('>', -1), '>': ('<', +1)}  # used to get the false side of the rule

# only tracked > and < because didn't consider >= or <= for the false side of the rule
# this was my bug. This was corrected by including an offset in the opposite_eq dict
rule_rules = {
    'x': {'<': [], '>': []},
    'm': {'<': [], '>': []},
    'a': {'<': [], '>': []},
    's': {'<': [], '>': []}
}


def ruling_ruler(rule, rule_rules):
    if rule == 'A':
        return [rule_rules]
    elif rule == 'R':
        return []  # the [] added to a list is the same as adding nothing

    instructions = instruct[rule]
    master_ruler = []  # tracks all rule_rules that are 'A'cceptable
    r_r = deepcopy(rule_rules)  # deepcopy is needed so the rule_rules are not mixed, rule_rules is a dict of lists
    for op, next_rule in instructions:
        if op is True:
            master_ruler += ruling_ruler(next_rule, r_r)
        else:
            category, equality, value = op
            for bi in [True, False]:
                if bi:
                    r_r_T = deepcopy(r_r)  # a copy is needed so the True and False are not mixed
                    r_r_T[category][equality].append(value)
                    master_ruler += ruling_ruler(next_rule, r_r_T)
                else:
                    #! 🐛 False can be >= or <=, need offset to account for the = portion
                    #! could also have tracked >= and <= as part of the rule_rules
                    #! but the other logic is already written
                    opposite_equality, offset = opposite_eq[equality]
                    r_r[category][opposite_equality].append(value + offset)
    return master_ruler


master_ruler = ruling_ruler('in', rule_rules)
combos = 0
for r_r in master_ruler:
    r_r_combos = 1  # combos for this r_r
    for category, value in r_r.items():
        if r_r[category]['<']:
            category_max = min(r_r[category]['<']) - 1
        else:
            category_max = 4_000

        if r_r[category]['>']:
            category_min = max(r_r[category]['>']) + 1
        else:
            category_min = 1
        r_r_combos *= (category_max - category_min + 1)  # both inclusive +1
    combos += r_r_combos

print(f'⚙️🔩 all valid part combinations: {combos}')
#%%
