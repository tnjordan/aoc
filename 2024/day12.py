#%%
from collections import deque, defaultdict
f = 'data/day12.txt'
# f = 'data/da12.ex'

with open(file=f) as input:
    read_lines = input.readlines()
read_lines = [line.strip() for line in read_lines]
print('🐟 🎄 🦈')
#%%
farm = [list(l) for l in read_lines]
dj_di = [(0,1), (0,-1), (1, 0), (-1, 0)]
J = len(farm)
I = len(farm[0])
#%%
seen = set()
regions = {}
q = deque()

for j_prime, row in enumerate(farm):
    for i_prime, crop in enumerate(row):
        if (j_prime,i_prime) in seen:
            continue
        regions[(j_prime,i_prime)] = [(j_prime,i_prime)]
        q.append((j_prime,i_prime))
        while q:
            j,i = q.popleft()
            seen.add((j,i))
            for dj,di in dj_di:
                j_dj = j + dj
                i_di = i + di
                if 0 <= j_dj < J and 0 <= i_di < I and (j_dj,i_di) not in seen and (j_dj,i_di) not in q:
                    if farm[j_dj][i_di] == crop:
                        regions[(j_prime,i_prime)].append((j_dj,i_di))
                        q.append((j_dj,i_di))
#%%
def price_calc(region):
    area = len(region)
    perim = 0
    for j,i in region:
        neighbors = 0
        for dj,di in dj_di:
            j_dj = j + dj
            i_di = i + di
            if (j_dj,i_di) in region:
                neighbors += 1
            else:
                perim += 1
    return area * perim
#%%
def price_calc_bulk(region):
    area = len(region)
    perim_records = {}
    for dj,di in dj_di:
        perim_records[(dj,di)] = defaultdict(list)
    
    for j,i in region:
        neighbors = 0
        for dj,di in dj_di:
            j_dj = j + dj
            i_di = i + di
            if (j_dj,i_di) in region:
                neighbors += 1
            else:
                cons = j if j == j_dj else i  # whatever on the names, seems reversed
                non_cons = j if j != j_dj else i
                perim_records[(dj,di)][non_cons].append(cons)

    perim = 0
    for dir, dic in perim_records.items():
        for k,v in dic.items():
            v = sorted(v)
            perim += sum([1 if v[i]+1 != v[i+1] else 0 for i in range(len(v)-1)])+1
    return area * perim
#%%
ans = 0
ans_2 = 0
for (j,i),region in regions.items():
    ans += price_calc(region)
    ans_2 += price_calc_bulk(region)
print(ans)
print(ans_2)
#%%
