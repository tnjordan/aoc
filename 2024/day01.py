#%%
f = 'data/day01.txt'

with open(file=f) as input:
    read_lines = input.readlines()
read_lines = [line.strip() for line in read_lines]
print('🐟 🎄 🦈')
#%%
left = []
right = []
for line in read_lines:
    l,r = line.split()
    left.append(int(l))
    right.append(int(r))

left = sorted(left)
right = sorted(right)

total_distance = 0
for l,r in zip(left,right):
    total_distance += abs(l - r)

print(total_distance)
#%%
similarity_score = 0
for n in left:
    similarity_score += n * right.count(n)

print(similarity_score)
#%%
