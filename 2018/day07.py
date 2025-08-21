#%%
import re
from collections import defaultdict
f = 'data/day07.txt'

with open(file=f) as input:
    read_lines = input.readlines()
read_lines = [l.strip() for l in read_lines]
print('🎅 🎄 🤶')
#%%
pattern = r'Step (\w) must be finished before step (\w) can begin.'

steps = defaultdict(list)

available_steps = set()
for l in read_lines:
    match = re.search(pattern, l)
    steps[match.group(2)].append(match.group(1))
    available_steps.add(match.group(1))
    available_steps.add(match.group(2))

completed_steps = []

starting_options = available_steps - set(list(steps.keys()))

for s in list(starting_options):
    steps[s] = None

#%%
part1 = True
if part1:
    while available_steps:
        step_options = []
        for k,v in steps.items():
            if k in completed_steps:
                continue
            elif v is None:
                step_options.append(k)
            else:
                for prior in v:
                    if prior not in completed_steps:
                        break
                else:
                    step_options.append(k)
        step_options = sorted(step_options)
        completed_steps.append(step_options[0])
        available_steps.remove(step_options[0])

    print(f'Steps: {"".join(completed_steps)}')
#%%
#! part 2
workers = [True]*5
base_time = 60
letter_time = {}
for i,l in enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZ',start=1):
    letter_time[l] = i + base_time

#
time = 0
in_progress = set()
while available_steps:
    if True in workers: # worker available 
        step_options = []
        for k,v in steps.items():
            if k in completed_steps or k in in_progress:
                continue
            elif v is None:
                step_options.append(k)
            else:
                for prior in v:
                    if prior not in completed_steps:
                        break
                else:
                    step_options.append(k)
        step_options = sorted(step_options)
        for i,w in enumerate(workers):
            if w is True:
                if step_options != []:
                    workers[i] = [letter_time[step_options[0]],step_options[0]]
                    in_progress.add(step_options[0])
                    step_options = step_options[1:] # remove work option
    for i,w in enumerate(workers):
        if w is not True:
            work_time, work_step = w
            work_time -= 1
            if work_time == 0:
                # print(f'worker {i} completed {work_step}')
                completed_steps.append(work_step)
                available_steps.remove(work_step)
                in_progress.remove(work_step)
                workers[i] = True #back to work
            else:
                workers[i] = [work_time, work_step]
    time += 1
print(f'total work time: {time}')

#%%
print()
print('⭐ ⭐')