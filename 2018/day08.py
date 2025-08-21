#%%
f = 'data/day08.txt'
# f = 'data/day08.ex'

with open(file=f) as input:
    read_lines = input.readlines()
read_lines = [l.strip() for l in read_lines]
print('🎅 🎄 🤶')
#%%
nodes = [int(x) for x in read_lines[0].split()]

def meta_master(i,nodes,meta_sum):
    c = nodes[i]
    i += 1
    m = nodes[i]
    if c == 0:
        # meta_sum = 0 #? pass meta_sum into meta_master, yup that worked
        for _ in range(m):
            i += 1
            # print(f'metadata {nodes[i]} at {i}')
            meta_sum += nodes[i]
        return meta_sum, i
    else:
        for _ in range(c):
            i += 1
            meta_sum, i = meta_master(i, nodes, meta_sum)
        for _ in range(m):
            i += 1
            # print(f'metadata {nodes[i]} at {i}')
            meta_sum += nodes[i]
    return meta_sum, i

meta_master(i=0,nodes=nodes, meta_sum=0)
#%%
#! part 2
def meta_master_2(i,nodes):
    c = nodes[i]
    i += 1
    m = nodes[i]
    if c == 0:
        node_value = 0
        for _ in range(m):
            i += 1
            node_value += nodes[i]
        # print(f'base node_value {node_value} at {i}')
        return node_value, i
    else:
        child_node_values = [0] #* zero because child count starts at 1
        for _ in range(c):
            i += 1
            node_value, i = meta_master_2(i, nodes)
            child_node_values.append(node_value)
        # print(f'child_node_values {child_node_values}')
        node_value = 0
        for _ in range(m):
            i += 1
            # print(f'metadata {nodes[i]} at {i}')
            if nodes[i] < len(child_node_values):
                # print(f'node adder child # {nodes[i]}')
                # print(f'adding {child_node_values[nodes[i]]}')
                node_value += child_node_values[nodes[i]]
                # print(f'node_value {node_value}')
            else:
                node_value += 0
    return node_value, i

#%%
meta_master_2(i=0,nodes=nodes)
#%%
print()
print('⭐ ⭐')