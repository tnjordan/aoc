#%%
f = 'data/day18.txt'
# f = 'data/day18.ex'

with open(file=f) as input:
    read_lines = input.readlines()
read_lines = [l.strip() for l in read_lines]
print('🎅 🎄 🤶')
#%%

part_2 = True

arr = []
for l in read_lines:
    l = l.replace('#','1')
    l = l.replace('.','0')
    l = list(l)
    l = [int(x) for x in l]
    arr.append(l)

neighbors = [(1, 1),
            (1, -1),
            (-1, 1),
            (-1, -1),
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0)]

new_arr = [row[:] for row in arr]
if part_2:  # turn corners on
    for j in [0, len(new_arr) - 1]:
        for i in [0, len(new_arr[0]) - 1]:
            new_arr[j][i] = 1

for _ in range(100):
    arr = [row[:] for row in new_arr]
    for j, r in enumerate(arr):
        for i, c in enumerate(r):
            neighbors_on = 0
            for dj, di in neighbors:
                if 0 <= j + dj < len(arr) and 0 <= i + di < len(r):
                    neighbors_on += arr[j+dj][i+di]
            if c == 1:
                if neighbors_on == 2 or neighbors_on == 3:
                    c_star = 1
                else:
                    c_star = 0
            elif c == 0:
                if neighbors_on == 3:
                    c_star = 1
                else:
                    c_star = 0
            new_arr[j][i] = c_star
    if part_2:  # turn corners on #!
        for j in [0, len(new_arr)-1]:
            for i in [0, len(new_arr[0])-1]:
                new_arr[j][i] = 1
    # print(new_arr)
    # print(sum([sum(r) for r in new_arr]))

print(sum([sum(r) for r in new_arr]), 'lights are on for 🎅!')
#%%
print()
print('⭐ ⭐')
