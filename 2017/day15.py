#%%
f = 'data/day15.txt'

with open(file=f) as input:
    read_lines = input.readlines()
read_lines = [line.strip() for line in read_lines]
print('❄️⛄❄️')
#%%
gen_a = int(read_lines[0].split(' ')[-1])
gen_b = int(read_lines[1].split(' ')[-1])


def generating_generator(gen_type, gen, factor, part_1):
    if part_1:
        return (gen * factor) % 2147483647
    else:
        while True:
            gen = (gen * factor) % 2147483647
            if gen_type == 'a' and gen % 4 == 0:
                return gen
            elif gen_type == 'b' and gen % 8 == 0:
                return gen


def judge(gen_a, gen_b, factor_a, factor_b, n, part_1=True):
    count = 0
    for _ in range(n):
        gen_a = generating_generator('a', gen_a, factor_a, part_1)
        gen_b = generating_generator('b', gen_b, factor_b, part_1)
        if bin(gen_a)[-16:] == bin(gen_b)[-16:]:
            count += 1
    return count


print(f'Judge finds {judge(gen_a, gen_b, 16807, 48271, 40_000_000)} matches')
print(f'Judge finds {judge(gen_a, gen_b, 16807, 48271, 5_000_000, part_1=False)} matches')


#%%
#! bonus gpt generator solution
def generator(seed, factor, divisor=1):
    value = seed
    while True:
        value = (value * factor) % 2147483647
        if divisor == 1 or value % divisor == 0:
            yield value & 0xFFFF  # Mask to the lowest 16 bits


def count_matching_pairs(generator_a, generator_b, iterations):
    count = 0
    for _ in range(iterations):
        value_a = next(generator_a)
        value_b = next(generator_b)
        if value_a == value_b:
            count += 1
    return count


# part 1
generator_a = generator(seed=gen_a, factor=16807)
generator_b = generator(seed=gen_b, factor=48271)

result = count_matching_pairs(generator_a, generator_b, iterations=40000000)
print("Number of matching pairs:", result)

# part 2
generator_a = generator(seed=gen_a, factor=16807, divisor=4)
generator_b = generator(seed=gen_b, factor=48271, divisor=8)
result = count_matching_pairs(generator_a, generator_b, iterations=5000000)
print("Number of matching pairs:", result)
