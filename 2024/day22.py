#%%
from itertools import product

f = 'data/day22.txt'  # 🐠

with open(file=f) as input:
    read_lines = input.readlines()
read_lines = [line.strip() for line in read_lines]
print('🐟 🎄 🦈')
#%%
initial_secrets = [int(x) for x in read_lines]
#%%
def prune(num):
    return num % 16777216

def mix(value, secret):
    return value ^ secret

def next_secret(secret):
    #*
    value = secret*64
    ns = mix(value,secret)
    ns = prune(ns)
    #*
    value = int(ns / 32)
    ns = mix(value, ns)
    ns = prune(ns)
    #*
    value = ns * 2048
    ns = mix(value, ns)
    ns = prune(ns)

    return ns
#%%
# plane verified on example
# initial_secrets = [
#     1,
#     10,
#     100,
#     2024,
# ]

secret_sum = 0
for secret in initial_secrets:
    for _ in range(2000):
        secret = next_secret(secret)
    secret_sum += secret
print(secret_sum)
#%%
# Define the range of values
values = range(-9, 10)  # has more than the possible options because you can't -9 then - any number
# Generate all sequences of length 4 with replacement
sequences = list(product(values, repeat=4))

sequence_profit = {s: 0 for s in sequences}

for secret in initial_secrets:
    secret_profit = {s: -1 for s in sequences}
    secret_sequence = []
    last_price = None
    for _ in range(2000):
        secret = next_secret(secret)
        price = int(str(secret)[-1])
        if last_price is not None:
            price_delta = price - last_price
            secret_sequence.append(price_delta)
            four_sequence = tuple(secret_sequence[-4:])
            if len(four_sequence) >= 4 and secret_profit[four_sequence] == -1:
                secret_profit[four_sequence] = price
        last_price = price
    
    for s_p in secret_profit:
        sequence_profit[s_p] += max(0,secret_profit[s_p])  # profit is not default value of -1

print(max(sequence_profit.values()))  # a bit slow, runs in ~1.5 minutes
#%%
