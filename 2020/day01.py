#%%
#! Part 1
input = open('data/day1.txt')
read_lines = input.readlines()

ans = 0
total_1 = 0
for l1 in read_lines:
    l1 = int(l1.strip())
    for l2 in read_lines:
        l2 = int(l2.strip())
        sum = l1 + l2
        if sum == 2020:
            ans = l1 * l2
            break
print(f'part 1: ans: {ans}')
    
    

# %%
#! Part 2
input = open('data/day1.txt')
read_lines = input.readlines()

ans = 0
total_1 = 0
for l1 in read_lines:
    l1 = int(l1.strip())
    for l2 in read_lines:
        l2 = int(l2.strip())
        for l3 in read_lines:
            l3 = int(l3.strip())
            sum = l1 + l2 + l3
            if sum == 2020:
                ans = l1 * l2 * l3
                break
print(f'part 2: ans: {ans}')
# %%
