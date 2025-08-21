#%%
input = open('data/day9.txt')
read_lines = input.readlines()
# %%
XMAS = []
for l in read_lines:
    l = l.strip()
    XMAS.append(int(l))

for i in range(25,len(XMAS)):
    prev_25 = XMAS[i-25:i]
    value = XMAS[i]
    match = False
    for j in prev_25:
        if match is False:
            if value - j in prev_25 and value - j != j:
                match = True
                # print('found match')
    if match is False:
        print(f'{value} not valid at position {i}')
        invalid = value
        break #* only need first match

# %%
#* Next time read the instructions
for pos_i, i in enumerate(XMAS):
    range_sum = i
    # print(i)
    for pos_j, j in enumerate(XMAS[pos_i+1:]):
        if range_sum <= invalid:
            range_sum += j
        if range_sum == invalid:
            print(' v '*13)
            print(f'Part 2: i: {i} at {pos_i} j: {j} at {pos_i+1+pos_j+1}')
            print(f'Answer: {min(XMAS[pos_i:pos_i+1+pos_j+1])} + {max(XMAS[pos_i:pos_i+1+pos_j+1])} = {min(XMAS[pos_i:pos_i+1+pos_j+1]) + max(XMAS[pos_i:pos_i+1+pos_j+1])}')
            print(' ^ '*13)
            break
# %%
