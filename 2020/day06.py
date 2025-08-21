#%%

input = open('data/day6.txt')
read_lines = input.readlines()

#! Part 1
group_ans = ''
total = 0
for l in read_lines:
    if l == '\n': #* new group
        # print(f'total:{total}, group_ans:{group_ans}, len:{len(group_ans)}')
        total += len(group_ans)
        group_ans = ''
        # print('-'*12)
    else:
        l = l.strip()
        for c in l:
            # print(f'c:{c}, g:{group_ans}, len:{len(group_ans)}')
            if c not in group_ans:
                group_ans += c

print(total)



# %%
#! Part 2
group_ans = ''
total = 0
for l in read_lines:
    if l == '\n': #* new group
        total += len(group_ans)
        group_ans = 'reset!'
    elif group_ans == 'reset!': #* first person sets the answers 
        l = l.strip()
        group_ans = l
    elif len(group_ans) > 0:
        l = l.strip()
        new_group_ans = ''
        for c in l:
            if c in group_ans: 
                # group_ans = group_ans.replace(c, '')
                new_group_ans += c
        group_ans = new_group_ans
print(total)
# %%
