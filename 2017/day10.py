#%%
f = 'data/day10.txt'

with open(file=f) as input:
    read_lines = input.readlines()
read_lines = [line.strip() for line in read_lines]
print('❄️⛄❄️')
#%%
example = False
if example:
    n = 5
    lengths = [3, 4, 1, 5]
else:
    n = 256
    lengths = [int(k2) for k2 in read_lines[0].split(',')]
numbers = list(range(n))


def knot_hash(lengths, rounds):
    pos = 0
    skip_size = 0
    numbers = list(range(256))
    start_idx = 0

    for _ in range(rounds):
        for length in lengths:
            rev, rem = numbers[0:length], numbers[length:]  # break at length
            numbers = rev[::-1] + rem  # reverse selection and combine
            start_num = numbers[start_idx]  # number at the start the list
            pos = (length + skip_size) % n
            numbers = numbers[pos:] + numbers[0:pos]  # index 0 is always the current position (no wraps here)
            start_idx = numbers.index(start_num)  # get the index of the number that was at the start
            skip_size += 1
    # realign the numbers
    numbers = numbers[start_idx:] + numbers[0:start_idx]
    return numbers


part_1 = knot_hash(lengths, 1)
print(f'product: {part_1[0] * part_1[1]}')


#! part 2
def hasher(raw):
    lengths = [ord(k2) for k2 in raw] + [17, 31, 73, 47, 23]

    sparse_hash = knot_hash(lengths, 64)
    dense_hash = []
    for i in range(0, len(sparse_hash), 16):
        hash = sparse_hash[i:i + 16]
        dh = 0
        for h in hash:
            dh ^= h
        dense_hash.append(dh)
    dense_hash = [format(k2, '02x') for k2 in dense_hash]
    hashed = ''.join(dense_hash)
    return hashed


part_2 = hasher(read_lines[0])  # best 🐞: hasher('read_lines[0]')
print(f'Knot Hash: {part_2}')
#%%
