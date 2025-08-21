#%%
f = 'data/day07.txt'
# f = 'data/day07.ex' #* worked on code

with open(file=f) as input:
    read_lines = input.readlines()
read_lines = [l.strip() for l in read_lines]
print('🎅 🎄 🤶')

filesystem = {} #* improved with default dict
from collections import defaultdict
filesystem = defaultdict(int)
filepath = []
ls_seen = []
ls_pass = False
for l in read_lines:
    print(l)
    #* p1, *other = l.split()
    l = l.split()
    if l[0] == '$':
        if l[1] == 'cd':
            if l[2] == '..':
                print(f'\t{filepath} 🧨', end=' ')
                filepath.pop()
                print(filepath)
            else:
                filepath.append(l[2])
        if l[1] == 'ls': #* wasn't tracking before, so duplicates were present
            # if filepath[-1] not in ls_seen: #! duplicate dir names: wmsl
            #     ls_seen.append(filepath[-1])
            if tuple(filepath) not in ls_seen:
                ls_seen.append(tuple(filepath))
                ls_pass = False
            else:
                print('🎇🎆'*22)
                ls_pass = True #* already seen
    elif l[0] == 'dir':
        pass #* came up with solution below as thinking through the problem
    elif ls_pass is False:
        file_size = int(l[0])
        print('\t',filepath)
        # for f in filepath: #! ahh the duplicates strike again, the ls_seen didn't matter. Turns out the input was nice.
        #     filesystem.setdefault(f,0)
        #     filesystem[f] += file_size
        for i in range(1,len(filepath)+1):
            # filesystem.setdefault(tuple(filepath[:i]),0) #* not needed with default dict
            filesystem[tuple(filepath[:i])] += file_size
        print('\t',filesystem)

print(f'Part 1: {sum([x for x in filesystem.values() if x <=  100_000])}')

#%%
#! Part 2
disk_size = 70000000
disk_required = 30000000
space_available = 70000000 - filesystem[('/',)]
min_delete = disk_required - space_available
min_delta = float('inf')
for k,v in filesystem.items():
    if v >= min_delete:
        delta = v - min_delete
        if delta < min_delta:
            min_delta = delta
            delete_dir = k

print(f'Disk space required to update: {min_delete}')
print(f'Delete Directory: {delete_dir} to remove {filesystem[delete_dir]}')
print(f'{min_delta} excess bits removed')

#%%
print()
print('⭐ ⭐')