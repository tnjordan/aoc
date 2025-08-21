#%%
f = 'data/day12.txt'

with open(file=f) as input:
    read_lines = input.readlines()
read_lines = [l.strip() for l in read_lines]
print('🎅 🎄 🤶')
#%%
import re
import json

nums = [int(x) for x in re.findall('-?\d+',read_lines[0])]
print(f'sum of numbers is: {sum(nums)}')
#%%
#! part 2
# regex was too complex for part 2 😊
k2 = json.loads(read_lines[0])


def no_red(d: dict | list):
    count = 0

    if type(d) is list:
        count += sum([x for x in d if type(x) is int])

    elif type(d) is dict:
        if "red" in d.values():
            return count  # do not count or continue
        else:
            count += sum([x for x in d.values() if type(x) is int])

    for v in d if type(d) is list else d.values():
        if type(v) is dict or type(v) is list:
            count += no_red(v)

    return count


print(f'sum of no red is: {no_red(k2)}')
#%%
print()
print('⭐ ⭐')
