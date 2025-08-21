#%%
f = 'data/day09.txt'

with open(file=f) as input:
    read_lines = input.readlines()
read_lines = [li.strip() for li in read_lines]
print('🎅 🎄 🤶')
#%%
compressed_file = read_lines[0]

position = 0
decompress_start = -1
decompress_end = -1
decompressed_string = ''
while position < len(compressed_file):
    char = compressed_file[position]
    if char == '(':  # init marker
        decompress_start = position
        position += 1
        continue
    if decompress_start >= 0:  # if in marker reading
        if char == ')':  # end of marker
            decompress_end = position
        else:  # just keep going
            position += 1
            continue
    if decompress_end > 0:  # created repeated string from marker
        marker = compressed_file[decompress_start:decompress_end + 1]
        # print(marker)
        decompress_start = -1
        decompress_end = -1
        chars, repeats = map(int, marker[1:-1].split('x'))
        char = compressed_file[position + 1: position + chars + 1] * repeats
        # print(chars, repeats, len(char), char)
        position += chars
    decompressed_string += char
    position += 1

print(f'decompressed length: {len(decompressed_string)}')

#%%
#! part 2


def decompress_version_two(char, chars=1, repeats=1):
    c_count = 0
    if '(' not in char:
        return chars * repeats
    position = 0
    decompress_start = -1
    decompress_end = -1
    while position < len(char):
        c = char[position]
        if c == '(':  # init marker
            decompress_start = position
            position += 1
            continue
        if decompress_start >= 0:  # if in marker reading
            if c == ')':  # end of marker
                decompress_end = position
            else:  # just keep going
                position += 1
                continue
        if decompress_end > 0:  # created repeated string from marker
            marker = char[decompress_start:decompress_end + 1]
            decompress_start = -1
            decompress_end = -1
            chars_star, repeats_star = map(int, marker[1:-1].split('x'))
            char_star = char[position + 1: position + chars_star + 1]
            c_count += decompress_version_two(char_star, chars_star, repeats_star)
            position += chars_star + 1  # same as before. Going deeper one at a time
            continue

        c_count += 1  # individual char not in a markers range.
        position += 1
    return c_count * repeats


print(f'decompressed length: {decompress_version_two(compressed_file)}')

#%%
print()
print('⭐ ⭐')
