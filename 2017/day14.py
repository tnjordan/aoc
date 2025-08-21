#%%
from day10 import hasher

f = 'data/day14.txt'

with open(file=f) as input:
    read_lines = input.readlines()
read_lines = [line.strip() for line in read_lines]
print('❄️⛄❄️')
#%%
key_string = read_lines[0]

disk = []
for i in range(128):
    hash_input = f'{key_string}-{i}'
    hash_out = hasher(hash_input)
    bits = ''
    for hex_digit in hash_out:
        bits += bin(int(hex_digit, 16))[2:].zfill(4)
    disk.append(bits)
print(f'disk used: {sum([k2.count("1") for k2 in disk])}')


#%%
#! part 2
def get_neighbors(j, i):
    neighbors = []
    for di, dj in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
        if 0 <= i + di < 128 and 0 <= j + dj < 128:
            if disk[j + dj][i + di] == '1':
                neighbors.append((j + dj, i + di))
    return neighbors


def group_of(j, i, seen):
    group = set()
    group.add((j, i))
    while group:
        j, i = group.pop()
        neighbors = get_neighbors(j, i)
        for n in neighbors:
            if n in seen:
                continue
            group.add(n)
        seen.add((j, i))
    return seen


seen = set()
groups = 0
for j, row in enumerate(disk):
    for i, v in enumerate(row):
        if v == '1':
            if (j, i) in seen:
                continue
            seen = group_of(j, i, seen)
            groups += 1
print(f'groups: {groups}')
#%%
