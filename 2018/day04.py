#%%
f = 'data/day04.txt'

with open(file=f) as input:
    read_lines = input.readlines()
read_lines = [l.strip() for l in read_lines]
print('🎅 🎄 🤶')
#%%
#* sort
import re
guard_log = sorted(read_lines, key=lambda x: int(re.sub(r'\D', '', x[1:17])))
guard_sleep = {}

for l in guard_log:
    log_split = l.split(' ')
    if log_split[-1].endswith('ft'):
        guard = int(log_split[3][1:])
        if guard not in guard_sleep:
            guard_sleep[guard] = [0]*60
    elif log_split[-1].endswith('ep'):
        sleep_start = int(log_split[1][3:5])
    elif log_split[-1].endswith('up'):
        sleep_end = int(log_split[1][3:5])
        for m in range(sleep_start,sleep_end):
            guard_sleep[guard][m] += 1

sleepy_guard = 0
max_sleep_time = 0
sleepy_min = 0

for guard, sleep in guard_sleep.items():
    sleep_time = sum(sleep)
    if sleep_time > max_sleep_time:
        sleepy_guard = guard
        sleepy_min = sleep.index(max(sleep))
        max_sleep_time = sleep_time

print(f'Sleepy Guard is: {sleepy_guard}')
print(f'Favorite nap time is: {sleepy_min}')
print(f'Part 1: {sleepy_guard*sleepy_min}')
#%%
#! part 2
max_mins = [0]*60
max_guards = [0]*60

for guard, sleep in guard_sleep.items():
    for i, (max_min, guard_min) in enumerate(zip(max_mins,sleep)):
        if guard_min > max_min:
            max_mins[i] = guard_min
            max_guards[i] = guard

print(f'guard {max_guards[max_mins.index(max(max_mins))]} sleeps {max(max_mins)} mins on min {max_mins.index(max(max_mins))}')
print(f'Part 2: {max_guards[max_mins.index(max(max_mins))]*max_mins.index(max(max_mins))}')
#%%
#!
print('⭐ ⭐')
#%%
