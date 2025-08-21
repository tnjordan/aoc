#%%
f = 'data/day17.txt'

with open(file=f) as input:
    read_lines = input.readlines()
read_lines = [line.strip() for line in read_lines]
print('❄️⛄❄️')
#%%
spins = int(read_lines[0])

spinlock = [0]
position = 0
for i in range(1, 2018):
    position = (position + spins) % len(spinlock) + 1
    spinlock.insert(position, i)

idx_2017 = spinlock.index(2017)
print(spinlock[idx_2017 + 1])

#%%
#! part 2

#! spinlock has locked my computer!
# for i in range(2018, 50000001):
#     position = (position + spins) % i + 1
#     spinlock.insert(position, i)

# idx_0 = spinlock.index(0)
# print(spinlock[idx_0 + 1])

for i in range(2018, 50000001):
    position = (position + spins) % i + 1
    if position == 1:  # zero is always at position 0
        value_after_zero = i
print(value_after_zero)
#%%
