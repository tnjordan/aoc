#%%
input = open('data/day2.txt')
read_lines = input.readlines()

data = read_lines[0].strip().split(sep=',')
data = [int(x) for x in data]
memory_init = data.copy()


# %%
#* setup 
data[1] = 12
data[2] = 2

# #* testing
# data = [1,9,10,3,2,3,11,0,99,30,40,50]

pos = 0
while data[pos] != 99:
    #*
    op_pos = pos
    v1_pos = pos + 1
    v2_pos = pos + 2
    ans_pos = pos + 3
    # print(op_pos, v1_pos, v2_pos, ans_pos)
    # print(data[op_pos] ,data[v1_pos] ,data[v2_pos] , data[ans_pos])
    if data[op_pos] == 1:
        data[data[ans_pos]] = data[data[v1_pos]] + data[data[v2_pos]]
    elif data[op_pos] == 2:
        data[data[ans_pos]] = data[data[v1_pos]] * data[data[v2_pos]]
    pos += 4
print(f'part 1: {data[0]}')
# %%

#! Part 2

#* intcode computer
def intcode_computer(memory, address = 0):
    while memory[address] != 99:
        #*
        op_address = address
        noun_address = address + 1
        verb_address = address + 2
        result_address = address + 3

        instruction = memory[op_address]
        noun_parameter = memory[noun_address]
        verb_parameter = memory[verb_address]
        result_pointer = memory[result_address]

        noun = memory[noun_parameter]
        verb = memory[verb_parameter]
        
        if instruction == 1:
            memory[result_pointer] = noun + verb
        elif instruction == 2:
            memory[result_pointer] = noun * verb
        address += 4
    return memory[0]


input_options = list(range(0,100))
for i in input_options:
    for j in input_options:
        memory = memory_init.copy()
        memory[1] = i
        memory[2] = j
        output = intcode_computer(memory)
        if output == 19690720:
            print('\U0001F973')
            print(f'100*noun + verb = {100*i + j}')
            break


# %%
