#%%
from tabulate import tabulate
#%%
f = 'data/day08.txt'

with open(file=f) as input:
    read_lines = input.readlines()
read_lines = [l.strip() for l in read_lines]
print('🎅 🎄 🤶')

trees = read_lines
visible_trees_r = [[0]*99 for i in range(99)] #* From stack overflow: Don't use [[v]*n]*n, it is a trap!
visible_trees_c = [[0]*99 for j in range(99)]
visible_trees = [[0]*99 for j in range(99)]
# visible_trees_r = [[0]*99]*99 #* From stack overflow: Don't use [[v]*n]*n, it is a trap!
# visible_trees_c = [[0]*99]*99
# k2 = [[0]*3]*4 #* shared memory
# k2[2][1] = 21
# print(k2)

#* wanted to avoid and right/down and left/up but...

#* right and down
for i in range(len(trees[0])):
    for j in range(len(trees)):
        if i == 0 or i == 98:
            visible_trees_r[j][i] = trees[j][i] #* initial attempt tracked 1, but gaps caused issues
            visible_trees[j][i] = 1
        elif j == 0 or j == 98:
            visible_trees_c[j][i] = trees[j][i]
            visible_trees[j][i] = 1
        else:
            #* rows
            if trees[j][i] > visible_trees_r[j][i-1]:
                visible_trees_r[j][i] = trees[j][i]
                visible_trees[j][i] = 1
            else:
                visible_trees_r[j][i] = visible_trees_r[j][i-1]
            
            #* cols
            if trees[j][i] > visible_trees_c[j-1][i]:
                visible_trees_c[j][i] = trees[j][i]
                visible_trees[j][i] = 1
            else:
                visible_trees_c[j][i] = visible_trees_c[j-1][i]

#* left and up
for i in range(len(trees[0])-1,-1,-1):
    for j in range(len(trees)-1,-1,-1):
        if i == 0 or i == 98:
            visible_trees_r[j][i] = trees[j][i] #* initial attempt tracked 1s like visible_trees, but gaps caused issues so needed to track height
            # visible_trees[j][i] = 1
        elif j == 0 or j == 98:
            visible_trees_c[j][i] = trees[j][i]
            # visible_trees[j][i] = 1
        else:
            #* rows
            if trees[j][i] > visible_trees_r[j][i+1]:
                visible_trees_r[j][i] = trees[j][i]
                visible_trees[j][i] = 1
            else:
                visible_trees_r[j][i] = visible_trees_r[j][i+1]
            
            #* cols
            if trees[j][i] > visible_trees_c[j+1][i]:
                visible_trees_c[j][i] = trees[j][i]
                visible_trees[j][i] = 1
            else:
                visible_trees_c[j][i] = visible_trees_c[j+1][i]

# #%%
# print(tabulate(visible_trees_c))
# #%%
# print(tabulate(visible_trees_r))
# #%%
# print(tabulate(visible_trees))

tree_count = 0
for r in visible_trees:
    tree_count += sum(r)

print(f'{tree_count} trees observed') #* took time but got on first submit

#%%
scenic_score = [[0]*99 for j in range(99)]
max_scenic_score = float('-inf')
#! part 2
for i in range(len(trees[0])):
    for j in range(len(trees)):
        tree = trees[j][i]
        up = 0
        for k in range(1,j+1):
            up += 1
            if trees[j-k][i] >= tree:
                break

        down = 0
        for k in range(1,len(trees)-j):
            down += 1
            if trees[j+k][i] >= tree:
                break

        left = 0
        for k in range(1,i+1):
            left += 1
            if trees[j][i-k] >= tree:
                break

        right = 0
        for k in range(1,len(trees[0])-i):
            right += 1
            if trees[j][i+k] >= tree:
                break
        scenic_score[j][i] = up*down*left*right
        if scenic_score[j][i] > max_scenic_score:
            max_scenic_score = scenic_score[j][i]

print(f'max scenic score is {max_scenic_score}') #* great day! got both on first submit


#%%
print()
print('⭐ ⭐')