#%%
import math

f = 'data/day14.txt'
f = 'data/day14_ex.txt'
f = 'data/day14_ex2.txt'
f = 'data/day14_ex3.txt'
# f = 'data/day14_ex4.txt'
# f = 'data/day14_ex5.txt'

with open(f) as input:
    read_lines = input.readlines()
data = {}

for i,l in enumerate(read_lines):
    l = l.strip()
    ins,outs = l.split(' => ')
    q_o, e_o = outs.split(' ')
    if e_o not in data:
        data[e_o] = [int(q_o)]
    else:
        print('duplicate! WARNING')
        print(data[e_o])
        raise Exception('Multiple Chemical Paths Detected!')
    i_l = []
    for i in ins.split(', '):
        q_i, e_i = i.split(' ')
        i_l.append([int(q_i),e_i])
    data[e_o].append(i_l)

#* function return the exact minimum of each element required, removed reaction constraints
def ore_miner_v3(element='FUEL', quantity=1, elements = {}):
    print(f'Element: {element} Quantity: {quantity}')
    if element not in elements:
        elements[element] = quantity
    else:
        elements[element] += quantity
    q = data[element][0]
    e = data[element][1]
    q_multiplier = math.ceil(quantity/q)
    print(f'quantity {quantity} q {q}')
    for q_i, e_i in e:
        if e_i == 'ORE': # 💎
            print(f'ORE strike!')
            print('\U0001F48E', q_multiplier * q_i, quantity, q_i, q_multiplier, q, math.ceil(quantity / q_i))
            if 'ORE' not in elements:
                elements['ORE'] = math.ceil(quantity / q_i) #! q_multiplier * q_i
            else:
                elements['ORE'] += math.ceil(quantity / q_i)
            return elements
        else:
            print('keep on digging')
            elements = ore_miner_v3(element=e_i, quantity=q_multiplier * q_i)
    return elements

elements = ore_miner_v3('FUEL',1)
print(f'elements: {elements}')

from copy import deepcopy
k2 = deepcopy(elements)
#%%
elements = deepcopy(k2)
#* function goes over the minimums in reverse order create the chemical amounts
#? before jpaulson, I was going from 'ORE' back down. But you can go from 'FUEL' up both times
def ore_optimizer_v5(elements, data, base_e = 'FUEL', processed = []):  #* expand v3 for all elements and reverse
    ctf = []
    inputs = []
    quantities = []
    for i in data[base_e][1]:
        inputs.append(i[1])
        quantities.append(elements[i[1]])
    print(f'{base_e} inputs: {inputs} and quantities {quantities} respectively')
    for i,q in zip(inputs, quantities):
        if i == 'ORE':
            print(f'\U0001F48E! ORE strike!')
        else:
            print(f'{q} {i} required for input')
            print(f'{data[i][0]} {i} made from {data[i][1]}')
            #* amount that needs to be reacted to have minimum factor
            q_required = math.ceil(elements[i] / data[i][0]) * data[i][0]
            print(f'minimum manufacturing quantity {q_required}')
            if q_required != elements[i]:
                print(f'updating input quantities of {i} to {q_required} from {elements[i]}')
                q_old = elements[i]
                elements[i] = q_required
                print(f'increasing input components')
                for q_i, e_i in data[i][1]:
                    print(f'{q_i} {e_i} required for {data[i][0]} {i}')
                    print(f'{(q_required - q_old) / data[i][0] * q_i } additional {e_i} required: now require {elements[i] + (q_required - q_old) / data[i][0] * q_i} from {elements[i]}')

                    elements[e_i] += (q_required - q_old) / q_i * data[i][0]
            elements = ore_optimizer_v5(elements, data, base_e = i)
        print()
    
    return elements




    #         base_elements = {}
    #         for e in data[i][1]:
    #             print(f'{e[0]} {e[1]} required for {data[i][0]} {i}')
    #             base_elements[i] = [data[i][0], e[0]]
    #             if e[0] not in processed:
    #                 #* amount actually needed to make is multiple of amount created each time
    #                 i_required = math.ceil(elements[i] / base_elements[i][1]) * base_elements[i][1]
    #                 print(f'minimum {i} reaction quantity is {i_required} {i}')
    #                 processed.append(i) #! AHH now I'm lost
    #                 if i_required != elements[i]:
    #                     print(f'updating input quantities of {i} to {i_required}')
    #                     elements[i] = i_required
    #                     ctf.append(i)
    #                     print(f'increasing input components')
    #         else:
    #             print(f'{i} already processed!')
    # if len(ctf) > 0:
    #     elements = ore_optimizer_v5(elements, data, base_e = i, processed = processed)
    # return elements

ores_to_mine = ore_optimizer_v5(elements, data, base_e = 'FUEL', processed = ['ORE'])
print(f'Elements: {ores_to_mine}')

#%%
def ore_counter_9k(ores_to_mine, data, base_e = 'ORE'):
    ores = 0
    base_elements = {}
    for e in data:
        for i in data[e][1]:
            if i[1] == base_e:
                print(f'{i[0]} ores required for {data[e][0]} {e}')
                base_elements[e] = [data[e][0], i[0]]
    print(base_elements)
    for e in base_elements:
        print(f'{e} requires {math.ceil(ores_to_mine[e] / base_elements[e][0]) * base_elements[e][1]} ore to make {ores_to_mine[e]} {e}')
        ores += math.ceil(ores_to_mine[e] / base_elements[e][0]) * base_elements[e][1]
    return ores

ores_to_mine = ore_counter_9k(elements, data, base_e = 'ORE')
print(f'Ore 2 Mine: {ores_to_mine}')

#%%
#* this v4 is a generic parameterized version of v3, you can provide the base_e
# def ore_optimizer_v4(elements, data, base_e = 'ORE'):  #* expand v3 for all elements
#     ores = 0
#     base_elements = {}
#     for e in data:
#         print(e)
#         for i in data[e][1]:
#             print(f'{data[e][0]} ores required for {i[0]} {e}')
#             if i[1] == base_e:
#                 base_elements[e] = [data[e][0], i[0]]
#     print(base_elements)
#     for e in base_elements:
#         if e in elements:
#             ores += math.ceil(elements[e] / base_elements[e][0]) * base_elements[e][1]
#     return ores

# ores_to_mine = ore_optimizer_v4(elements, data)
# print(f'Ore 2 Mine: {ores_to_mine}')

#%%
# def ore_optimizer_v3(elements, data): #* this works for the smaller examples 1-3; however, I think a full optimizer is needed.
#     ores = 0
#     ore_elements = {}
#     for e in data:
#         if data[e][1][0][1] == 'ORE':
#             ore_elements[e] = [data[e][0], data[e][1][0][0]]
#     print(ore_elements)
#     for e in ore_elements:
#         if e in elements:
#             ores += math.ceil(elements[e] / ore_elements[e][0]) * ore_elements[e][1]
#     return ores

# ores_to_mine = ore_optimizer_v3(elements, data)
# print(f'Ore 2 Mine: {ores_to_mine}')
#%%
# def ore_optimizer_v2(elements, data): #* this works for the smaller examples 1-3; however, I think a full optimizer is needed.
#     ores = 0
#     ore_elements = {}
#     for e in data:
#         if data[e][1][0][1] == 'ORE':
#             ore_elements[e] = [data[e][0], data[e][1][0][0]]
#     print(ore_elements)
#     for e in ore_elements:
#         if e in elements:
#             ores += math.ceil(elements[e] / ore_elements[e][0]) * ore_elements[e][1]
#     return ores

# ores_to_mine = ore_optimizer_v2(elements, data)
# print(f'Ore 2 Mine: {ores_to_mine}')

# def ore_miner_v2(element='FUEL', quantity=1):
#     print(f'Element: {element} Quantity: {quantity}')
#     ore_q = 0
#     penultimate_elements = []
#     q = data[element][0]
#     e = data[element][1]
#     q_multiplier = math.ceil(quantity/q)
#     for q_i, e_i in e:
#         if e_i == 'ORE': # 💎\U0001F48E
#             print(f'ORE strike!')
#             print('',q_multiplier * q_i)
#             penultimate_elements.append([quantity,element])
#             return q_multiplier * q_i, penultimate_elements
#         else:
#             print('keep on digging')
#             _, __ = ore_miner_v2(element=e_i, quantity=q_multiplier * q_i)
#             ore_q += _
#             penultimate_elements.append(__)
#     return ore_q, penultimate_elements

# total_ore, penultimate_elements = ore_miner_v2('FUEL',1)
# print(f'total ore: {total_ore} penultimate_elements: {penultimate_elements}')

# #* This was not the way, list inception.
# def ore_optimizer(penultimate_elements):
#     element_dict = {}
#     for i in penultimate_elements:
#         while len(i) < 2:
#             i = i[0]
#         q,e = i[0],i[1]
#         print(q,e)
#         if e not in element_dict:
#             element_dict[e] = q
#         else:
#             element_dict[e] += q
#     return element_dict

# print(ore_optimizer(penultimate_elements))

# def ore_miner(element='FUEL', quantity=1):
#     print(f'Element: {element} Quantity: {quantity}')
#     ore_q = 0
#     q = data[element][0]
#     e = data[element][1]
#     q_multiplier = math.ceil(quantity/q)
#     for q_i, e_i in e:
#         if e_i == 'ORE': # 💎
#             print(f'ORE strike!')
#             print('\U0001F48E',q_multiplier * q_i)
#             return q_multiplier * q_i
#         else:
#             print('keep on digging')
#             ore_q += ore_miner(element=e_i, quantity=q_multiplier * q_i)
#     return ore_q

# total_ore = ore_miner('FUEL',1)
# print(f'total ore: {total_ore}')
# %%
