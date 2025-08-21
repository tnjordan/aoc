#%%
from functools import reduce

f = 'data/day09.txt'
# f = 'data/day09.ex'

with open(file=f) as input:
    read_lines = input.readlines()
read_lines = [line.strip() for line in read_lines]
print('❄️⛄❄️')
#%%
oasis = []
for line in read_lines:
    oasis.append(list(map(int, line.split(' '))))


def delta_finder(history, part_2=False):
    deltas = []
    delta = history
    delta_0 = False
    while delta_0 is False:
        if part_2:
            deltas.append(delta[0])
        else:
            deltas.append(delta[-1])
        new_delta = []
        for i in range(len(delta) - 1):
            new_delta.append(delta[i + 1] - delta[i])
        delta = new_delta
        if all([0 == d for d in delta]):
            delta_0 = True
    if part_2:
        return reduce(lambda acc, d: d - acc, reversed(deltas), 0)
    else:
        return sum(deltas)


part_1 = 0
part_2 = 0
for o in oasis:
    part_1 += delta_finder(o)
    part_2 += delta_finder(o, part_2=True)
print(f'🏝️->🏜️: {part_1}')
print(f'🏜️<-🏝️: {part_2}')
#%%
