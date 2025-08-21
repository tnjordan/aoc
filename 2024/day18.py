#%%
from collections import deque

f = 'data/day18.txt'

with open(file=f) as input:
    read_lines = input.readlines()
read_lines = [line.strip() for line in read_lines]
print('🐟 🎄 🦈')
#%%
pos = (0,0)
J=71
I=71
dj_di = [(0,1), (0,-1), (1, 0), (-1, 0)]

falling_b = []
for l in read_lines:
    j,i = l.split(',')
    falling_b.append((int(j),int(i)))
#%%
corrup = falling_b[:1024]

nq = deque()
nq.append(pos)
seen = set()
moves = 0
done = 0
while not done:
    moves += 1
    q = nq
    nq = deque()
    while q:
        # print(q)
        j,i = q.popleft()
        seen.add((j,i))
        for dj,di in dj_di:
            j_dj = j + dj
            i_di = i + di
            if 0 <= j_dj < J and 0 <= i_di < I:
                if (j_dj,i_di) in corrup:
                    # print('corrupted!')
                    continue
                if (j_dj,i_di) == (70,70):
                    print('done!')
                    done = 1
                    q = None
                    break
                if (j_dj,i_di) not in seen and (j_dj,i_di) not in nq:
                    nq.append((j_dj,i_di))
print(moves)
#%%
#! par2
def solveable(b):
    pos = (0,0)
    corrup = falling_b[:b]
    nq = deque()
    nq.append(pos)
    seen = set()
    moves = 0
    done = 0
    while not done:
        moves += 1
        q = nq
        nq = deque()
        while q:
            j,i = q.popleft()
            seen.add((j,i))
            for dj,di in dj_di:
                j_dj = j + dj
                i_di = i + di
                if 0 <= j_dj < J and 0 <= i_di < I:
                    if (j_dj,i_di) in corrup:
                        continue
                    if (j_dj,i_di) == (70,70):
                        print('done!')
                        done = 1
                        return 1
                    if (j_dj,i_di) not in seen and (j_dj,i_di) not in nq:
                        nq.append((j_dj,i_di))
    return False

b = 1684 #ran 1024 to 1455 in ~4min
solve = True
while solve:
    b+=1
    print(b)
    solve = solveable(b)
print(falling_b[b], '@ #',b)  # will reach in time
#%%
def solveable(b):  # made faster no care about moves in par2
    pos = (0,0)
    corrup = falling_b[:b]
    q = deque()
    q.append(pos)
    seen = set()
    while q:
        j,i = q.popleft()
        seen.add((j,i))
        for dj,di in dj_di:
            j_dj = j + dj
            i_di = i + di
            if 0 <= j_dj < J and 0 <= i_di < I:
                if (j_dj,i_di) in corrup:
                    continue
                if (j_dj,i_di) == (70,70):
                    print('done!')
                    return True
                if (j_dj,i_di) not in seen and (j_dj,i_di) not in q:
                    q.append((j_dj,i_di))
    return False

b = 0 #go back till can solve
solve = False
while not solve:
    print(b)
    b-=1
    solve = solveable(b)
print(falling_b[b], '@ #',b)
#%%
