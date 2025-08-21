#%%
f = 'data/day04.txt'

with open(file=f) as input:
    read_lines = input.readlines()
read_lines = [l.strip() for l in read_lines]
print('🎅 🎄 🤶')

#%%
full_overlaps = 0
for l in read_lines:
    # print(l)
    elf1_zone, elf2_zone = l.split(sep=',')
    elf1_start, elf1_end = [int(x) for x in elf1_zone.split(sep='-')]
    elf2_start, elf2_end = [int(x) for x in elf2_zone.split(sep='-')]
    if elf1_start <= elf2_start and elf1_end >= elf2_end:
        full_overlaps += 1
        # print(f'elf1_start:{elf1_start}, elf1_end:{elf1_end}, elf2_start:{elf2_start}, elf2_end::{elf2_end}')
    elif elf1_start >= elf2_start and elf1_end <= elf2_end:
        # print(f'elf1_start:{elf1_start}, elf1_end:{elf1_end}, elf2_start:{elf2_start}, elf2_end:{elf2_end}')
        full_overlaps += 1

print(f'full overlapped elf work areas: {full_overlaps}')

#%%
#!
partial_overlaps = 0
for l in read_lines:
    elf1_zone, elf2_zone = l.split(sep=',')
    elf1_start, elf1_end = [int(x) for x in elf1_zone.split(sep='-')]
    elf2_start, elf2_end = [int(x) for x in elf2_zone.split(sep='-')]
    if len(set(range(elf1_start,elf1_end+1)) & set(range(elf2_start,elf2_end+1))) >= 1:
        partial_overlaps += 1

print(f'partial overlapped elf work areas: {partial_overlaps}')

#%%
print()
print('⭐ ⭐')