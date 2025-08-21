#%%
import re
from collections import defaultdict
from collections import deque 
from itertools import permutations

f = 'data/day16.txt'
# f = 'data/day16.ex'
# f = 'data/day16.ex2' #* for forcing the example to check maths AA -> BB -> CC

with open(file=f) as input:
    read_lines = input.readlines()
read_lines = [l.strip() for l in read_lines]
#print('🎅 🎄 🤶')

regex = re.compile('Valve (\w*) has flow rate=(\d*); tunnels? leads? to valves? (.*)') #* https://regex101.com/

valves = defaultdict(list)
for l in read_lines:
    valve, rate, tunnel = regex.search(l).groups()
    valves[valve] = [int(rate), tunnel.split(sep=', ')]

#* valve map: distance in minutes from each valve to other valves
valve_map = defaultdict(dict)
#* BFS for all valves
for start_valve in valves.keys():
    start = start_valve
    seen = [start] #* start is special
    queue = deque([start])
    bfs_path = {}
    while queue:
        pos = queue.popleft()
        valid_moves = [m for m in valves[pos][1] if m not in seen]
        if valid_moves != []:
            [queue.append(x) for x in valid_moves]
            [seen.append(x) for x in valid_moves]
            for m in valid_moves:
                bfs_path[m] = pos
    for valve in valves.keys():
        #* find shortest path
        pos = valve
        path = []
        while pos != start:
            path.append(pos)
            pos = bfs_path[pos]
        valve_map[start][valve] = len(path)


# start = 'AA'
# seen = [start] #* start is special
# queue = deque([start])
# bfs_path = {}
# while queue:
#     pos = queue.popleft()
#     valid_moves = [m for m in valves[pos][1] if m not in seen]
#     if valid_moves != []:
#         [queue.append(x) for x in valid_moves]
#         [seen.append(x) for x in valid_moves]
#         for m in valid_moves:
#             bfs_path[m] = pos
# for valve in valves.keys():
#     #* find shortest path
#     pos = valve
#     path = []
#     while pos != start:
#         path.append(pos)
#         pos = bfs_path[pos]
#     valve_map[start][valve] = len(path)

non_zero_flow_valves = [k for k,v in valves.items() if v[0] != 0]
valve_options = valve_map['AA'].keys()
permutation_options = set(non_zero_flow_valves) & set(valve_options)
max_pressure_release = 0

queue_memory = defaultdict(list) #* does not work. No reduction in iterations. 15! is too big :(
for q in permutations(permutation_options):
    valve_queue = list(q)
    position = 'AA'
    pressure_release = 0
    hold = 0
    q_path = []
    # q_path.append(next_valve)
    time = 30
    #print(f'queue: {q}')
    for i in range(len(valve_queue)-1,0,-1): #* last valve not needed because they are unique
        #print(i)
        #print(valve_queue[-i:])
        #print(queue_memory)
        if tuple(valve_queue[-i:]) in queue_memory: #* go in reverse to get max time warp
            print(f'time warp, already been here')
            #print(f'at: {valve_queue[-i:]} with: {queue_memory[tuple(valve_queue[-i:])]}')
            q_path = valve_queue[-i:]
            time = queue_memory[tuple(valve_queue[-i:])][0]
            pressure_release =  queue_memory[tuple(valve_queue[-i:])][1]
            position = queue_memory[tuple(valve_queue[-i:])][2]
            valve_queue = valve_queue[:-i] #* remaining part of the queue
            #print(f'time remaining: {time} pressure released: {pressure_release}')
            #print(f'path taken: {q_path} starting at position {position}')
            #print(f'remaining queue: {valve_queue}')
            break

    for m in range(time,-1,-1): #* last action in min on has no effect. You can either open valve or move but no flow change
        #print(f'== Minute {30-m} ==') 
        #print(f'{m} minutes remaining:')
        if hold > 0:
            if hold == 1:
                position = next_valve
                #print(f'\topening valve: {next_valve}')
                #print(f'\tvalve will release: {flow}')
                #print(f'\tvalve releases {valves[next_valve][0]} per min for {(m-open_time)} minutes.')
                pressure_release += flow
                q_path.insert(0, next_valve) #* not optimal but list is reversed
                queue_memory[tuple(q_path)] = [m-open_time, pressure_release, position]
            else:
                #print(f'\twalking to {next_valve}, {hold-1} until arrival')
                pass
            hold -= 1
            #print()
            continue
        #* next valve from queue
        if not valve_queue:
            #print(f'no more valves to open')
            break #* queue is empty
        next_valve = valve_queue.pop()
        walk_time = valve_map[position][next_valve]
        open_time = 1
        flow = valves[next_valve][0] * (m - walk_time - open_time)
        #print(f'\tnext valve: {next_valve} with pressure release of {flow}')
        #print(f'\tvalve is {walk_time} minutes away from current location')
        #print(f'\twalking to {next_valve}')
        hold = walk_time -1 + open_time
        #print()
    #print(f'total pressure release: {pressure_release}')
    #print()
    if pressure_release > max_pressure_release:
        max_pressure_release = pressure_release

print(f'max pressure release: {max_pressure_release}')

#%%
#* come back to this, but provide full path from additional search
# position = 'AA'
# pressure_release = 0
# hold = 0
# open_valves = []
# for m in range(30,-1,-1): #* last action in min on has no effect. You can either open valve or move but no flow change
#     #print(f'== Minute {30-m} ==') 
#     #print(f'{m} minutes remaining:')
#     if hold > 0:
#         if hold == 1:
#             position = top_valve
#             open_valves.append(position)
#             #print(f'\topening valve: {top_valve}')
#             #print(f'\tvalve will release: {top_flow}')
#             #print(f'\tvalve releases {valves[top_valve][0]} per min for {(m-open_time)} minutes.')
#             pressure_release += top_flow
#         else:
#             #print(f'\twalking to {top_valve}, {hold-1} until arrival')
#         hold -= 1
#         #print()
#         continue
#     top_valve = None
#     top_flow = 0
#     top_walk = 0
#     for valve,distance in valve_map[position].items():
#         if valve in open_valves:
#             continue #* can't open same valve twice
#         walk_time = distance
#         open_time = 1
#         flow = valves[valve][0] * (m - walk_time - open_time) #* flow times remaining time
#         if flow > top_flow:
#             top_valve = valve
#             top_flow = flow
#             top_walk = walk_time
#     if top_flow == 0:
#         #print(f'\tno more valves to open!')
#         #print()
#         break
#     #print(f'\ttop valve: {top_valve} with pressure release of {top_flow}')
#     #print(f'\tvalve is {top_walk} minutes away from current location')
#     #print(f'\twalking to {top_valve}')
#     hold = top_walk -1 + open_time
#     #print()

# #print(f'total pressure release: {pressure_release}')
#%%
# #print()
# #print('⭐ ⭐')