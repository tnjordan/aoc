#%%
input = open('data/day3.txt')
read_lines = input.readlines()
data = []
for l in read_lines:
    l = l.strip()
    data.append(l)

rows = len(data)
cols = len(l)

at_bottom = False
delta_row = 1
delta_col = 3
sled_row = 0
sled_col = 0
trees = 0
while not at_bottom:
    sled_row += delta_row
    sled_col += delta_col
    print(f'sled_row:{sled_row}  sled_col:{sled_col}')
    sled_row = sled_row % rows
    sled_col = sled_col % cols
    print(f'sled_row:{sled_row}  sled_col:{sled_col}')
    char = data[sled_row][sled_col]
    print(char)
    if char == '#':
        trees += 1
    if sled_row == 0:
        at_bottom = True
print(trees)

    
    
# %%
#! PART 2
slopes = [(1,1), (1,3), (1,5), (1, 7), (2,1)]
ans = 1
for delta_row, delta_col in slopes:
    at_bottom = False
    sled_row = 0
    sled_col = 0
    trees = 0
    while not at_bottom:
        sled_row += delta_row
        sled_col += delta_col
        if sled_row > rows:
            break
        # print(f'sled_row:{sled_row}  sled_col:{sled_col}')
        sled_row = sled_row % rows
        sled_col = sled_col % cols
        # print(f'sled_row:{sled_row}  sled_col:{sled_col}')
        char = data[sled_row][sled_col]
        # print(char)
        if char == '#':
            trees += 1
        if sled_row == 0:
            at_bottom = True
    ans = ans * trees
    print(trees, ' ', ans)
print(ans)
# %%
