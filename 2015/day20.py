#%%
from functools import reduce

f = 'data/day20.txt'

with open(file=f) as input:
    read_lines = input.readlines()
read_lines = [l.strip() for l in read_lines]
print('🎅 🎄 🤶')
#%%
presents = int(read_lines[0])


def factors(n):  #* stack overflow
    return set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))


def elf_delivery(house_id):
    present_count = 0

    # find factors of house_id
    elf_visitors = factors(house_id)
    for elf in elf_visitors:
        present_count += elf * 10
    return present_count


present_count = 0
house_id = 0
while present_count < presents:
    house_id += 1
    present_count = elf_delivery(house_id=house_id)

print(f'house {house_id} will get {present_count} presents')

#%%
#! part 2


def elf_delivery_part2(house_id):
    present_count = 0

    # find factors of house_id
    elf_visitors = factors(house_id)
    for elf in elf_visitors:
        if house_id // elf <= 50:
            present_count += elf * 11
    return present_count


present_count = 0
house_id = 0
while present_count < presents:
    house_id += 1
    present_count = elf_delivery_part2(house_id=house_id)

print(f'house {house_id} will get {present_count} presents')


#%%
print()
print('⭐ ⭐')
