#%%
import re

f = 'data/day16.txt'
# f = 'data/day16ex.txt'

with open(file=f) as input:
    read_lines = input.readlines()
read_lines = [line.strip() for line in read_lines]
print('❄️⛄❄️')
#%%
fields = {}
your_ticket = []
nearby_tickets = []

f = True
yt = False
nt = False
for l in read_lines:
    if f and l == '':
        f = False
    elif f:
        v,r = l.split(': ')
        r0,r1,r2,r3 = [int(x) for x in re.findall(r"(\d+)", r)]
        fields[v] = ((r0,r1),(r2,r3))
        continue
    
    if 'your ticket:' in l:
        yt = True
        continue
    elif yt:
        your_ticket = [int(x) for x in l.split(',')]
        yt = False
        continue
    
    if 'nearby tickets:' in l:
        nt = True
    elif nt:
        nearby_tickets.append([int(x) for x in l.split(',')])
#%%
part_1 = 0
valid_tickets = []
for n_t in nearby_tickets:
    valid_ticket = True
    for value in n_t:
        valid = False
        for k,v in fields.items():
            for a,b in v:
                if a <= value <= b:
                    valid = True
        if not valid:
            part_1 += value
            valid_ticket = False
    if valid_ticket:
        valid_tickets.append(n_t)

print(f'scanning error rate: {part_1}')
#%%
pos_map = {}
for field, valid_range in fields.items():
    (a,b),(c,d) = valid_range
    for pos in range(len(valid_tickets[0])):
        field_accepted = True
        for v_t in valid_tickets:
            valid_field = a <= v_t[pos] <= b or c <= v_t[pos] <= d
            if not valid_field:
                field_accepted = False
                break
        if field_accepted:
            if pos in pos_map:
                pos_map[pos].append(field)
            else:
                pos_map[pos] = [field]
#%%
confirmed_positions = {}
while any(len(value) >= 1 for value in pos_map.values()):
    for position, fields in pos_map.items():
        if len(fields) == 1:
            confirmed_positions[position] = fields[0]
    # then remove the confirmed!
    for confirmed_position, confirmed_field in confirmed_positions.items():
        for position, fields in pos_map.items():
            if confirmed_field in fields: 
                fields.remove(confirmed_field)  # python list in loops shares memory
#%%
part_2 = 1
for k,v in confirmed_positions.items():
    if v.startswith('departure'):
        print(f'{v} is {your_ticket[k]}')
        part_2 *= your_ticket[k]
print(f'departure product: {part_2}')
#%%
