#%%
f = 'data/day25.txt'

with open(file=f) as input:
    read_lines = input.readlines()
read_lines = [line.strip() for line in read_lines]
print('❄️⛄❄️')
#%%
card_public_key = int(read_lines[0])
door_public_key = int(read_lines[1])

# card_public_key = 5764801
# door_public_key = 17807724

def looper(subject_number, loop_size):
    """no need to run entire loop each time"""
    value = 1
    for _ in range(loop_size):
        value *= subject_number
        value = value % 20201227
    return value

def next_loop(value):
    value *= 7
    value %= 20201227
    return value

#%%
loop_size = 0
value = 1
while True:
    next_value = next_loop(value)
    loop_size += 1
    if next_value == card_public_key:
        print(looper(door_public_key, loop_size))
        break
    elif next_value == door_public_key:
        print(looper(card_public_key, loop_size))
        break
    value = next_value
#%%
