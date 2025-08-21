#%%
f = 'data/day5.txt'
with open(f) as input:
    read_lines = input.readlines()
data = read_lines[0].strip().split(sep=',')
data = [int(x) for x in data]
memory_init = data.copy()

#* intcode computer
def intcode_computer(input, memory, address = 0):
    while memory[address] != 99:
        #* get instructions
        op_address = address
        instruction = memory[op_address]
        instruction = list(str(instruction))
        while len(instruction)<5: #* get all values
            instruction.insert(0,'0')
            #TODO zfill()
        op_code = int(instruction[-2]+instruction[-1])
        mode_param_1 = int(instruction[-3])
        mode_param_2 = int(instruction[-4])
        mode_param_3 = int(instruction[-5])

        #* all op_codes so far use first parameter
        address_param_1 = address + 1
        if mode_param_1 == 0: #* position mode
            param_1 = memory[address_param_1]
        elif mode_param_1 == 1: #* immediate mode
            param_1 = address_param_1
        
        #* only set parameters if used by operation
        if op_code in [1,2,5,6,7,8]:
            address_param_2 = address + 2
            if mode_param_2 == 0:
                param_2 = memory[address_param_2]
            elif mode_param_2 == 1:
                param_2 = address_param_2
        if op_code in [1,2,7,8]:
            address_param_3 = address + 3
            if mode_param_3 == 0:
                param_3 = memory[address_param_3]
            elif mode_param_3 == 1:
                param_3 = address_param_3
        
        #* perform operations
        assert op_code in [1,2,3,4,5,6,7,8], op_code
        if op_code == 1:
            memory[param_3] = memory[param_1] + memory[param_2]
            address += 4
        elif op_code == 2:
            memory[param_3] = memory[param_1] * memory[param_2]
            address += 4
        elif op_code == 3:
            memory[param_1] = input
            address += 2
        elif op_code == 4:
            output = memory[param_1]
            address += 2
            input = output #* output of 4 will be input to 3; and returned output
        elif op_code == 5:
            if memory[param_1] != 0:
                address = memory[param_2] #! Ugh, had memory[address] = ...
            else:
                # pass #? is said do nothing.
                address += 3 #* obviously nothing was wrong
        elif op_code == 6:
            if memory[param_1] == 0:
                address = memory[param_2]
            else:
                # pass #? is said do nothing.
                address += 3 #* obviously nothing was wrong
        elif op_code == 7:
            if memory[param_1] < memory[param_2]:
                memory[param_3] = 1
            else:
                memory[param_3] = 0
            address += 4
        elif op_code == 8:
            if memory[param_1] == memory[param_2]:
                memory[param_3] = 1
            else:
                memory[param_3] = 0
            address += 4
        # print(f'address:{address} instruction: {instruction}') #* used to debug my inf loop. ops 7 and 8 didn't have the += 4
    return output

part_1 = intcode_computer(input=1, memory=memory_init)
print(f'part 1: {part_1}')

part_2 = intcode_computer(input=5, memory=memory_init)
print(f'part 2: {part_2}')