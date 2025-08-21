#* Your puzzle input is 278384-824795
#%%
print(824795 - 278384)
# %%
#* this is a more complicated problem and its solution
# num_str = ''
# for i in range(278384,824795+1):
#     num_str += str(i)

# valid_count = 0
# doubles = ['00','11','22','33','44','55','66','77','88','99']
# for i in range(len(num_str)-6):
#     k2 = num_str[i:i+6]
#     if any(ele in k2 for ele in doubles):
#         if k2 == ''.join(sorted(k2)):
#             # print(k2)
#             valid_count += 1
# print('possible passwords: ', valid_count)
    
# %%
#! Part 1
doubles = ['00','11','22','33','44','55','66','77','88','99']
valid_count = 0
for num in range(278384,824795+1):
    k2 = str(num)
    if any(ele in k2 for ele in doubles):
        if k2 == ''.join(sorted(k2)):
            valid_count += 1
print('possible passwords: ', valid_count)
# %%
#! Part 2
doubles = ['00','11','22','33','44','55','66','77','88','99']
trips = [elm+elm[0] for elm in doubles]
valid_count = 0
for num in range(278384,824795+1):
    k2 = str(num)
    db = [ele in k2 for ele in doubles]
    tp = [ele in k2 for ele in trips]
    if sum(db)>sum(tp):
        if list(k2) == sorted(k2): #* different option here
            valid_count += 1
print('possible passwords: ', valid_count)
# %%
