#%%
f = 'data/day07.txt'

with open(file=f) as input:
    read_lines = input.readlines()
read_lines = [line.strip() for line in read_lines]
print('🐟 🎄 🦈')
#%%
problems = []
for line in read_lines:
    ans,nums = line.split(': ')
    ans = int(ans)
    nums = [int(x) for x in nums.split()]
    problems.append((ans, nums))
#%%
def add_mult(ans,nums,result,part_2=False):
    todos = []
    if len(nums) == 0:
        if result == ans:
            return True
        else:
            return False
    else:
        todos.append(add_mult(ans,nums[1:],result+nums[0],part_2))
        todos.append(add_mult(ans,nums[1:],result*nums[0],part_2))
        if part_2:
            todos.append(add_mult(ans,nums[1:],int(str(result)+str(nums[0])),part_2))
    if any(todos):
        return ans
    return 0
#%%
part_1 = 0
part_2 = 0
for problem in problems:
    ans, nums = problem
    part_1 += add_mult(ans, nums[1:], nums[0])
    part_2 += add_mult(ans, nums[1:], nums[0], part_2=True)
print(part_1)
print(part_2)
#%%