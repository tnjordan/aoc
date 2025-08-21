#%%
f = 'data/day07.txt'
# f = 'data/day07.ex'

with open(file=f) as input:
    read_lines = input.readlines()
read_lines = [line.strip() for line in read_lines]
print('❄️⛄❄️')
#%%
weights = {}   # store weights
support = {}   # key is program, value is program supporting the key
compress = {}  # key is program, value is programs compressing the key

for line in read_lines:
    if '->' in line:
        base, holdings = line.split(' -> ')
    else:
        base = line
        holdings = None
    b, w = base.split()
    weights[b] = int(w[1:-1])
    compress[b] = []
    if holdings is not None:
        for holding in holdings.split(', '):
            support[holding] = b
            compress[b].append(holding)

# find the base
base = False
supporter = holding
while not base:
    if supporter not in support:
        base = True
    else:
        supporter = support[supporter]
print(f'base supporter is {supporter}')

# post submission alternative thought
base = set(compress.keys()).difference(support.keys())
print(f'base supporter is {base.pop()}')


#%%
def weight_watcher(supporter):
    compressors = compress[supporter]
    if compressors == []:
        return 0
    weight = [0] * len(compressors)
    for i, compressor in enumerate(compressors):
        weight[i] += weights[compressor]
        weight[i] += weight_watcher(supporter=compressor)
    if not all(k2 == weight[0] for k2 in weight):
        print('⚠️⚖️' * 12 + '⚠️')
        print(f'supporter: \t{supporter}')
        print(f'compressors: \t{compressors}')
        print(f'weights: \t{weight}')
        overweight_idx = weight.index(max(weight))
        overweight = compressors[overweight_idx]
        print(f'program {overweight} is FAT!')
        print(f'Reformat {- (max(weight) - min(weight))} to {weights[overweight] - (max(weight) - min(weight))} from {weights[overweight]}')
    return sum(weight)


weight_watcher(supporter)
#%%
