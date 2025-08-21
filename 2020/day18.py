#%%
import re

f = 'data/day18.txt'
# f = 'data/day18ex.txt'

with open(file=f) as input:
    read_lines = input.readlines()
read_lines = [line.strip() for line in read_lines]
print('❄️⛄❄️')
#%%
def find_closing_parenthesis(s):
    open_idx = s.find('(')
    stack = 0
    for i in range(open_idx, len(s)):
        if s[i] == '(':
            stack += 1
        elif s[i] == ')':
            stack -= 1
            if stack == 0:
                return open_idx, i  # Found the matching closing parenthesis
    assert False, "This should never happen!"

def maths_part_1(numbers, operators):
    previous_number = numbers[0]
    for operation,number in zip(operators, numbers[1:]):
        previous_number = str(eval(previous_number + operation + number))
    return previous_number

def maths_part_2(numbers, operators):
    while '+' in operators:  # add first
        add_idx = operators.index('+')
        result = str(eval(f'{numbers[add_idx]} + {numbers[add_idx+1]}'))
        numbers = numbers[:add_idx] + [result] + numbers[add_idx+2:]
        operators.remove('+')

    return maths_part_1(numbers, operators)

def maths(line, part_2=False):
    while '(' in line:
        open_idx, close_idx = find_closing_parenthesis(line)
        line = line[0:open_idx] + maths(line[open_idx+1:close_idx], part_2) + line[close_idx+1:]
    
    # extract the digits and the operations
    numbers = re.findall(r'\d+', line)
    operators = re.findall(r'[+*]', line)
    if part_2:
        return maths_part_2(numbers, operators)
    return maths_part_1(numbers, operators)


part_1 = 0
part_2 = 0
for line in read_lines:
    part_1 += int(maths(line))
    part_2 += int(maths(line,part_2=True))
print(f'part 1: {part_1}')
print(f'part 2: {part_2}')
#%%