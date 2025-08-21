#%%
from collections import defaultdict, deque
from copy import deepcopy
from itertools import combinations
from queue import PriorityQueue


f = 'data/day25.txt'
# f = 'data/day25.ex'

with open(file=f) as input:
    read_lines = input.readlines()
read_lines = [line.strip() for line in read_lines]
print('❄️⛄❄️')
#%%
conn = defaultdict(list)
for line in read_lines:
    a,b = line.split(': ')
    b = b.split(' ')
    for c in b:
        conn[a].append(c)
        conn[c].append(a)
conn = dict(conn)
#%%
# :) return to traverse, was useless when created but perfect after splitting
def traverse(pos):
    global conn

    q = deque()
    seen = set()
    q.append(pos)
    while q: #?
        pos = q.popleft()
        if pos in seen:
            continue
        seen.add(pos)
        for connection in conn[pos]:
            q.append(connection)
    return len(seen)

#%%
def path_finder(start):
    global conn
    paths = {}
    path = []

    pq = PriorityQueue()
    pq.put((0,start,path))

    seen = set()

    # while not pq.empty():
    while not pq.empty(): # len(seen) != len(conn) and
        steps, pos, path = pq.get()
        if pos in seen:
            continue
        seen.add(pos)
        for connection in conn[pos]:
            new_path = deepcopy(path)
            new_path.append((pos,connection))
            if (start,connection) in paths:
                continue
            paths[(start,connection)] = deepcopy(new_path)
            pq.put((steps+1,connection,new_path))
    return paths

counts = defaultdict(int)

points = list(conn.keys())
for point in points[::42]:
    print(f'point:{point}')
    k2 = path_finder(point)
    for pair, path in k2.items():
        for p in path:
            counts[p] += 1
    print(sorted(counts.items(), key=lambda item: item[1], reverse=True)[:5])

removals = []
removed_connection = set()
sorted_connections = sorted(counts.items(), key=lambda item: item[1], reverse=True)

i = 0
while len(removals) < 3:
    connection, _ = sorted_connections[i:i+1][0]
    a,b = connection
    print(connection)
    if a not in removed_connection and b not in removed_connection:
        removals.append(connection)
        removed_connection.add(a)
        removed_connection.add(b)
    i += 1
print(removals)
#%%
def connect(start,end):
    pq = PriorityQueue()
    path = []
    pq.put((0,start,path))

    while not pq.empty():
        steps, pos, path = pq.get()
        if pos == end:
            return path
        for connection in conn[pos]:
            new_path = deepcopy(path)
            new_path.append((pos,connection))
            pq.put((steps+1,connection,new_path))
#%%
# for connection, steps in removals:
for connection in removals:
    start, end = connection
    conn[start].remove(end)
    conn[end].remove(start)

group_1 = traverse(start)
group_2 = traverse(end)

print(group_1, 'x', group_2)
print(group_1*group_2)
#%%