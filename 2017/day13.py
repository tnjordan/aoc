#%%
f = 'data/day13.txt'
# f = 'data/day13.ex'

with open(file=f) as input:
    read_lines = input.readlines()
read_lines = [line.strip() for line in read_lines]
print('❄️⛄❄️')
#%%
scanners = ','.join(read_lines)
scanners = eval('{' + scanners + '}')

caught = []
for p in range(max(scanners) + 1):  # position in firewall = time in firewall
    # print(f'time: {p}')
    if p in scanners:
        scanner_p = p % ((scanners[p] - 1) * 2)
        # print(f'scanner {p} at {scanner_p}')
        if scanner_p == 0:
            # print(f'alert! at {p} severity {scanners[p]}')
            caught.append(p * scanners[p])
print(f'severity: {sum(caught)}')


# code to get the movement correct:
# sc_id = 4
# for p in range(10):
#     scanner_p = p % ((scanners[sc_id] - 1) * 2)
#     print(f'scanner at {scanner_p} which is actually too {(2*(scanners[sc_id]-1) - scanner_p) if scanner_p >= scanners[sc_id] else "🤪"}')

#! part 2
def scan(p, delay):
    # print(f'wait {delay} picoseconds')
    if p in scanners:
        p_d = p + delay
        # print(f'at scanner: {p}')
        # print(f'time: {p_d}')
        scanner_p = p_d % ((scanners[p] - 1) * 2)
        # print(f'scanner position: {scanner_p}')
        if scanner_p == 0:
            # print(f'alert! at {p}')
            return True
    return False


delay = 0
walk_through_fire = False
while walk_through_fire is False:
    delay += 1
    for p in range(max(scanners) + 1):
        if scan(p, delay):
            break
    else:
        print(f'delay: {delay} picoseconds')
        walk_through_fire = True
        break

#%%
