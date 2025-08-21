#%%
f = 'data/day09.txt'
# f = 'data/da09.ex'

with open(file=f) as input:
    read_lines = input.readlines()
read_lines = [line.strip() for line in read_lines]
print('🐟 🎄 🦈')
#%%
read_lines = map(int, list(read_lines[0]))

file_id = 0
file_or_emp = 1
files = []
only_file_id = []
file_len = {}
file_ids_and_len = {}
file_ids_and_len2 = {}

for _,f in enumerate(read_lines):
    if f not in file_len: file_len[f] = []
    if file_or_emp:
        fi = file_id
        file_len[f].append((len(files),fi))
        file_id += 1
        file_or_emp = 0
        file_ids_and_len[fi] = f
        file_ids_and_len2[fi] = (len(files),f)
        for _ in range(f):
            only_file_id.append(fi)
    else:
        fi = '.'
        file_or_emp = 1
    for _ in range(f):
        files.append(fi)
only_file_id_p2 = only_file_id[:]
#%%
sorted_files = []
idx = 0
while only_file_id:
    if files[idx] == '.':
        sorted_files.append(only_file_id[-1])
        del only_file_id[-1]
    else:
        sorted_files.append(only_file_id[0])
        del only_file_id[0]
    idx += 1
#%%
part_1 = sum([i*fi for i,fi in enumerate(sorted_files)])
print(part_1)
#%%
last_size = {}
for i in range(1,10):
    last_size[i] = 0

sorted_files = files[:]
for fi in sorted(file_ids_and_len, reverse=True):
    i,_ = file_ids_and_len2[fi]
    fi_len = file_ids_and_len.pop(fi)
    # print('fi:',fi,' fi_len:',fi_len)
    files = sorted_files[:]
    emp_count = 0
    ls = last_size[fi_len]

    for j,f in enumerate(files[ls:]):
        j += ls
        # print('f',f,'j',j)
        if f == '.':
            emp_count += 1
            if emp_count >= fi_len:
                # print('swich')
                if j >= i:
                    break
                # del file_len[emp_count][-1]

                for k in range(emp_count):
                    # print(j - emp_count + k, j,emp_count,k)
                    sorted_files[j - emp_count +1 + k] = fi
                    # print(sorted_files[i + k])
                    sorted_files[i + k] = '.'
                    # assert sorted_files.count('.') == files.count('.')
                    # print(sorted_files)
                last_size[fi_len] = j
                break
        else:
            emp_count = 0

part_2 = sum([i*fi for i,fi in enumerate(sorted_files) if fi != '.'])
print(part_2)
#%%
