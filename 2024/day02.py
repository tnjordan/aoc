#%%
f = 'data/day02.txt'

with open(file=f) as input:
    read_lines = input.readlines()
read_lines = [line.strip() for line in read_lines]
print('🐟 🎄 🦈')
#%%
def safe_nums(nums, fail=True):
    for i,n in enumerate(nums[:-1]):
        nn = nums[i+1]
        if nn-n >= 1 and nn-n <= 3:
            continue
        else:
            if fail:
                return False
            else:
                return safe_nums(nums[:i] + nums[i+1:], fail=True) or safe_nums(nums[:i+1] + nums[i+1+1:], fail=True)
    return True

safe = 0
safe_part2 = 0
for line in read_lines:
    nums = line.split()
    nums = [int(x) for x in nums]
    if safe_nums(nums) or safe_nums(nums[::-1]):
        safe += 1
    if safe_nums(nums, False) or safe_nums(nums[::-1], False):
        safe_part2 += 1

print(safe)
print(safe_part2)
#%%
