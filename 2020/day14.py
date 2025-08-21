#%%
import re

f = 'data/day14.txt'
# f = 'data/day14ex.txt'

with open(file=f) as input:
    read_lines = input.readlines()
read_lines = [line.strip() for line in read_lines]
print('❄️⛄❄️')
#%%

def int_to_bin(integer):
    # make a 36 character bin from an integer
    if integer < 0:
        raise ValueError("Only non-negative integers are supported.")
    binary = ""
    if integer == 0:
        return "0"
    while integer > 0:
        binary = str(integer % 2) + binary
        integer //= 2
    return binary.zfill(36)

def bin_to_int(binary):
    # Convert a 36-bit binary string to an integer
    if len(binary) != 36 or not all(c in '01' for c in binary):
        raise ValueError("Input must be a 36-bit binary string containing only '0' and '1'.")
    integer = 0
    for i in range(36):
        if binary[i] == '1':
            integer += 2 ** (35 - i)  # Calculate based on position from left
    return integer

def apply_mask(binary,mask, part_2 = False):
    masked_binary = ""
    for b, m in zip(binary, mask):
        if not part_2:
            masked_binary += m if m != 'X' else b
        else:
            masked_binary += b if m == '0' else m
    return masked_binary

def floating_binary_memory(masked_address, mem, value):
    if 'X' not in masked_address:
        mem[masked_address] = value
        return
    
    binary_sum = 0
    idx = masked_address.find('X')
    for replacement_bit in ['0', '1']:
        new_binary = masked_address[:idx] + replacement_bit + masked_address[idx+1:]
        floating_binary_memory(new_binary, mem, value)
    
    return binary_sum

part_2 = True
mem = {}
mask = 'X'*36
for line in read_lines:
    if 'mask' in line:
        mask = line.removeprefix('mask = ')
        continue
    address, value = [int(x) for x in re.findall(r"(\d+)", line)]
    binary_value = int_to_bin(value)
    if not part_2:
        mem[address] = apply_mask(binary_value, mask, part_2)
    else:
        floating_binary_memory(apply_mask(int_to_bin(address), mask, part_2), mem, value)

if not part_2:
    print(sum([bin_to_int(b) for b in mem.values()]))
else:
    print(sum([b for b in mem.values()]))
#%%
