#%%
input = open('data/day10_ex.txt')
read_lines = input.readlines()

adapters = []
for l in read_lines:
    l = l.strip()
    adapters.append(int(l))

adapters.sort()
adapters.append(adapters[-1]+3)

delta_1 = 0
delta_3 = 0

prev_a = 0
for a in adapters:
    delta = a - prev_a
    if delta == 1:
        delta_1 += 1
    elif delta == 3:
        delta_3 += 1
    prev_a = a

print('Part 1:', delta_1 * delta_3)

# %%

# adapters_dict = {}
# adapters.insert(0,0)
# for i, a in enumerate(adapters):
#     cnt = 0
#     for a_c in adapters[i+1:i+4]:
#         if a_c - a <= 3:
#             cnt += 1
#     adapters_dict[a] = cnt

# adapters = []
# for l in read_lines:
#     l = l.strip()
#     adapters.append(int(l))

# #* reverse
# adapters.insert(0,0)
# adapters.sort()
# adapters.reverse()
# adapters_dict = {}

# cnt_total = 1
# for i, a in enumerate(adapters):
#     cnt = 0
#     for a_c in adapters[i+1:i+4]:
#         if a - a_c <= 3:
#             cnt += 1
#     print(f'a: {a} a_c: {adapters[i+1:i+4]} count: {cnt}')
#     if cnt > 1:
#         cnt_total*=2
#     adapters_dict[a] = cnt

# %%
adapters = []
for l in read_lines:
    l = l.strip()
    adapters.append(int(l))

adapters.insert(0,0)
adapters.sort()

adapters_dict = {}
for i, a in enumerate(adapters):
    cnt = 0
    if i < 3:
        d = i
    else:
        d = 3
    for a_c in adapters[i-d:i]:
        print(adapters[i-d:i])
        if a - a_c <= 3:
            cnt += 1
    adapters_dict[a] = cnt
# %%
