#%%
f = 'data/day04.txt'

with open(file=f) as input:
    read_lines = input.readlines()
read_lines = [line.strip() for line in read_lines]
print('🐟 🎄 🦈')
#%%
xmas = 'XMAS'

dj_di = [(0,1), (0,-1), (1, 1), (1, 0), (1, -1), (-1, 1), (-1, 0), (-1,-1)]
J = len(read_lines)
I = len(read_lines[0])

part_1 = 0
for j, line in enumerate(read_lines):
    for i, c in enumerate(line):
        if c == 'X':
            # look for xmas
            found = 'X'
            for dj, di in dj_di:
                found = 'X'
                for m in range(1,4):
                    j_dj = j + dj*m
                    i_di = i + di*m
                    if 0 <= j_dj < J and 0 <= i_di < I:
                        found += read_lines[j_dj][i_di]
                if found == xmas:
                    part_1 += 1

print(part_1)
#%%
mas = sorted('MAS')
dj_di = [(1,1), (1,-1), (-1,1), (-1,-1)]
part_2 = 0
for j, line in enumerate(read_lines):
    for i, c in enumerate(line):
        if c == 'A':
            # look for mas, start with A and if the diagonals are M and S you have MAS
            # then check both diagonals d1 and d2 for an X-MAS
            d1 = 'A'
            for dj,di in [(1,-1), (-1,1)]: # d1 is + slope
                j_dj = j + dj
                i_di = i + di
                if 0 <= j_dj < J and 0 <= i_di < I:
                    d1 += read_lines[j_dj][i_di]
            d2 = 'A'
            for dj,di in [(-1,-1), (1,1)]: # d1 is - slope
                j_dj = j + dj
                i_di = i + di
                if 0 <= j_dj < J and 0 <= i_di < I:
                    d2 += read_lines[j_dj][i_di]
            if sorted(d1) == mas and sorted(d2) == mas:
                part_2 += 1
print(part_2)
#%%