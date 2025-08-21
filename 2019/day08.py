#%%
f = 'data/day8.txt'
with open(f) as input:
    read_lines = input.readlines()
data = read_lines[0].strip()
# %%
width = 25
height = 6
layer_pixels = width*height
layers = [data[i:i+layer_pixels] for i in range(0, len(data), layer_pixels)]
# %%
min_zero_cont = float('inf')
ans = 0
for l in layers:
    if l.count('0') < min_zero_cont:
        min_zero_cont = l.count('0')
        ans = l.count('1') * l.count('2')

print(f'part 1: {ans}')

# %%
image = list(layers[0])
for l in layers:
    for idx, i in enumerate(image):
        if i == '2':
            image[idx] = l[idx]
# %%
for h in range(height):
    row = []
    row_s = ''
    for i in range(width):
        c = image[h*width + i]
        if c == '0':
            c = ' '
        row.append(c)
        row_s += c
    # print(row)
    print(row_s)
# %%
