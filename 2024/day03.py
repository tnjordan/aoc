#%%
f = 'data/day03.txt'

with open(file=f) as input:
    read_lines = input.readlines()
read_lines = [line.strip() for line in read_lines]
print('🐟 🎄 🦈')

#* was getting wrong answer because read_lines had more than one line
# read_lines = ['xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))']

corrupted_data = ''.join(read_lines)
#%%
import re

pattern = "mul\(\d{1,3},\d{1,3}\)"
pattern = re.compile(pattern=pattern)
muls = re.findall(pattern=pattern, string=corrupted_data)

part_1 = 0
for mul in muls:
    x, y = mul.split(',')
    x = int(re.search('\d+',x).group())
    y = int(re.search('\d+',y).group())
    part_1 += x*y
    # print(mul,':',x,'*',y)
print(part_1)
#%%
pattern = "mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)"
pattern = re.compile(pattern=pattern)
muls = re.findall(pattern=pattern, string=corrupted_data)

part_2 = 0
factor = 1
for mul in muls:
    if mul == 'do()':
        factor = 1
    elif mul == "don't()":
        factor = 0
    else:
        x, y = mul.split(',')
        x = int(re.search('\d+',x).group())
        y = int(re.search('\d+',y).group())
        part_2 += x*y*factor
print(part_2)
#%%
