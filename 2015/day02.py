#%%
f = 'data/day02.txt'

with open(file=f) as input:
    read_lines = input.readlines()
read_lines = [l.strip() for l in read_lines]
print('🎅 🎄 🤶')
#%%
dims = [l.split('x') for l in read_lines]
dims = [[int(d) for d in l] for l in dims]

wrapping_paper = 0
for (l, w, h) in dims:
    sides = [l * w, w * h, h * l]
    wrapping_paper += 2 * sum(sides) + min(sides)

print(f'🎅 should order {wrapping_paper} square feet of wrapping paper')
#%%
#! part 2
ribbon = 0
for (l, w, h) in dims:
    sides = [l, w, h]
    sides.remove(max(sides))
    ribbon += 2 * sum(sides) + l * w * h

print(f'🎅 should order {ribbon} feet of ribbon')
#%%
print()
print('⭐ ⭐')
