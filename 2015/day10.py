#%%
f = 'data/day10.txt'

with open(file=f) as input:
    read_lines = input.readlines()
read_lines = [l.strip() for l in read_lines]
print('🎅 🎄 🤶')
#%%
seq = read_lines[0]  #* 3113322113

for i in range(50):
    new_seq = []
    last_c = seq[0]
    c_cnt = 0
    for c in seq:
        # if last_c is None:
        #     last_c = c
        #     c_cnt = 0
        if c == last_c:
            c_cnt += 1
        else:
            new_seq.append(str(c_cnt))
            new_seq.append(last_c)
            last_c = c
            c_cnt = 1
    new_seq.append(str(c_cnt))
    new_seq.append(last_c)
    seq = ''.join(new_seq)
    # print(seq)
    if i == 39:
        print('part 1')
        print(f'look see is: {len(seq)} characters')
        print()
    if i == 49:
        print('part 2')
        print(f'look see is: {len(seq)} characters')

#%%
print()
print('⭐ ⭐')

#%%
