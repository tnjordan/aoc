#%%
f = 'data/day15.txt'
# f = 'data/day15.ex'

with open(file=f) as input:
    read_lines = input.readlines()
read_lines = [line.strip() for line in read_lines]
print('❄️⛄❄️')
#%%
codes = read_lines[0].split(',')


def hasher(code):
    hash = 0
    for c in code:
        ascii = ord(c)
        hash += ascii
        hash *= 17
        hash %= 256
    return hash


hash_sum = 0
for code in codes:
    hash_sum += hasher(code)
print(f'hash sum = {hash_sum}')

#%%
boxes = [[] for _ in range(256)]  # intresting learning [[]*256] is [[]]

for code in codes:
    if '=' in code:
        label, focal_length = code.split('=')
        focal_length = int(focal_length)
        box_id = hasher(label)
        for idx, b in enumerate(boxes[box_id]):
            if b[0] == label:
                # replace existing lense with new focal length
                boxes[box_id][idx] = (label, focal_length)
                break  # can only be one of each focal length
        else:
            # add to end if not found
            boxes[box_id].append((label, focal_length))
    else:
        label = code.rstrip('-')
        box_id = hasher(label)
        boxes[box_id] = [b for b in boxes[box_id] if b[0] != label]

focal_power = 0
for box_number, box in enumerate(boxes, start=1):
    for lens_number, (l,focal_length) in enumerate(box, start=1):
        focal_power+= box_number * lens_number * focal_length
print(f'focal power: {focal_power} 🔎')

#%%
