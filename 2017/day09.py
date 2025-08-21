#%%
f = 'data/day09.txt'

with open(file=f) as input:
    read_lines = input.readlines()
read_lines = [line.strip() for line in read_lines]
print('❄️⛄❄️')
#%%
stream = read_lines[0]
score = 0
depth = 0
prev_c = None
in_garbage = False
garbage_chars = 0
for c in stream:
    if in_garbage:
        if prev_c == '!':
            prev_c = None  # ! negates !
        elif c == '!':  # don't score !
            prev_c = c
        elif c == '>':
            in_garbage = False
            prev_c = c
        else:
            garbage_chars += 1
            prev_c = c
        continue
    if c == '{':
        depth += 1
    elif c == '}':
        score += depth
        depth -= 1
    elif c == '<':
        in_garbage = True
    prev_c = c
print(f'score: {score}')
print(f'garbage: {garbage_chars}')
#%%
