#%%
f = 'data/day08.txt'
# f = 'data/day08.ex'

with open(file=f) as input:
    read_lines = input.readlines()
read_lines = [l.strip() for l in read_lines]
print('🎅 🎄 🤶')
#%%
code_character = 0
memory_character = 0
# x_count = 0
for l in read_lines:
    code_character += len(l)
    l = l.replace('\\\\','$') #? changed symbol to prevent issues
    l = l.replace('\\"','*')
    len_l = len(l)
    l = l.replace('\\x','')
    len_lrx = len(l)
    x_replace = (len_l - len_lrx)/2
    memory_character += len(l) - x_replace - 2 #* -2 for quotes on the ends
    # x_count += x_replace #* verfied count in the input file was the same

print(f'code_character: {code_character}')
print(f'memory_character: {memory_character}')
print(f'delta: {code_character - memory_character}')

#%%
#! part 2
code_character = 0
encode_character = 0
# x_count = 0
for l in read_lines:
    code_character += len(l)
    l = l.replace('"','**')
    l = l.replace('\\','**')
    encode_character += len(l) + 2 #* 2 for the  new end ""


print(f'code_character: {code_character}')
print(f'encode_character: {encode_character}')
print(f'delta: {-code_character + encode_character}')


#%%
print()
print('⭐ ⭐')
