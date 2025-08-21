#%%
import numpy as np
from copy import deepcopy
from tabulate import tabulate

f = 'data/day17.txt'
# f = 'data/day17.ex'

with open(file=f) as input:
    read_lines = input.readlines()
jets = [l.strip() for l in read_lines][0]
##print('🎅 🎄 🤶')

"""
####

.#.
###
.#.

..#
..#
###

#
#
#
#

##
##
"""

#* make all rocks the same shape
k2 = """
[..####.]

[...#...],
[..###..],
[...#...]

[....#..],
[....#..],
[..###..]

[..#....],
[..#....],
[..#....],
[..#....]

[..##...],
[..##...]
"""

# The tall, vertical chamber is exactly seven units wide. Each rock appears 
# so that its left edge is two units away from the left wall and its bottom 
# edge is three units above the highest rock in the room (or the floor, if 
# there isn't one)

rocks = [np.atleast_2d(c) for c in [np.array(b) for b in [eval(a) for a in [z.replace('#','1,') for z in [y.replace('.','0,') for y in [x.replace('\n','') for x in k2.split(sep= '\n\n')]]]]]]

wall = np.array([[1,0,0,0,0,0,0,0,1]])

stack = np.array([[1,1,1,1,1,1,1,1,1]])
answer = -1
max_height = 0
jet_position = 0
jet_count = len(jets)
jet = jets[jet_position%jet_count]
#! Return to this! Part 1 no longer works :(
runs = 2022 #* part 1
runs = 1000000000000 #* part 2
r = -1 #* lazy fix
skipper = True
stack_conditions = {}

# for r in range(runs): #! part 1 range(2022) #! part 2 Brute Force: range(1_000_000_000_000)
while r < runs: #* converted to while loop for time warping on repeats
    r += 1
    if r % (runs//10) == 0:
        print(f'{r/runs*100:.2f}%')
    # if r % 10_000_000_000 == 0: #* seeing if I could do a single %
    #     print(f'{r/1000000000000*100}%')
    ##print()
    ##print('rock #: ',r)
    rock = rocks[r%5] #* iterate through the rocks
    rock_height = len(rock)
    # ##print('rock')
    # ##print(rock)

    #* build the stack
    for s in range((3+rock_height)):
        stack = np.vstack((wall,stack))
    stack_height = len(stack)
    # ##print('stack')
    # ##print(stack)

    #* 
    temp_stack = deepcopy(stack)
    ##print('rocking stack')
    temp_stack[0:0+rock_height,1:8] += rock
    # ##print(tabulate(temp_stack).replace('0', ' '))

    #! part 2
    #* check for repeat: rock is at start and jet is at start, 
    if skipper is True:
        #* taking only the top 42 rows was just because that is the answer. (and trial and error)
        conditions = (tuple(rock.flatten()), jet_position%jet_count, tuple(stack[:42,:].flatten()))
        if conditions in stack_conditions:
            skipper = False #* only skip once
            print('found a repeater!')
            print(f'previous height {stack_conditions[conditions][0]} at rock {stack_conditions[conditions][1]}')
            print(f'current height: {answer + max_height} at rock {r}')
            delta_rocks = r - stack_conditions[conditions][1]
            delta_height = (answer + max_height) - stack_conditions[conditions][0]
            print(f'{delta_rocks} rocks yield {delta_height} height')
            skips = (runs - r) // delta_rocks
            print(f'skipping {skips} times: {skips*delta_rocks} rocks for a height of {skips*delta_height}')
            print(f'was at rock {r} now at rock {r + skips*delta_rocks}')
            r += skips*delta_rocks
            answer += skips*delta_height
            if skips > 0: #* omg this is nasty
                answer += -1 #* maths? Just noticed that the example was off by 1
            print(f'height was {answer + max_height} new height {(answer + max_height) + skips*delta_height}')
        else:
            stack_conditions[conditions] = [answer + max_height, r]

    lvl = 0
    stuck = False
    while stuck is False:
        # for jet in jets:
        jet = jets[jet_position%jet_count]
        # if jet_position%jet_count == 0: print('they do here!') 
        jet_position += 1
        #* check jet
        if jet == '<': #* left move
            ##print('< ', end='')
            jet_check = stack[lvl:lvl+rock_height,0:7] + rock
            if np.all(jet_check != 2):
                ##print('Jet of gas pushes rock left:')
                zeros = np.zeros((rock_height,1),dtype=int)
                rock = np.hstack((rock[:,1:],zeros))
            else:
                ##print('but nothing happens.')
                pass

        elif jet == '>': #* right move
            ##print('> ', end='')
            jet_check = stack[lvl:lvl+rock_height,2:9] + rock
            if np.all(jet_check != 2):
                ##print('Jet of gas pushes rock right:')
                zeros = np.zeros((rock_height,1),dtype=int)
                rock = np.hstack((zeros,rock[:,:-1]))
            else:
                ##print('but nothing happens.')
                pass
        
        #* check down
        down_check = stack[lvl+1:lvl+1+rock_height,1:8] + rock
        if np.all(down_check != 2):
            ##print('rock falls')
            lvl += 1
        else:
            # ##print('stuck')
            stuck = True
            stack[lvl:lvl+rock_height,1:8] += rock
            height = stack_height - lvl
            max_height = max(max_height,height)
            stack = stack[stack_height-max_height:,:] #* reset stack
            lvl -= stack_height-max_height

            #* check if we can dump stack
            # [1,1,1,1,1,1,1,1,1]
            dump_check = stack[lvl:lvl+rock_height,1:8].sum(axis=1) == 7
            if np.any(dump_check):
                # print('dump it')
                #print(stack[lvl:lvl+rock_height,1:8])
                #print('stack')
                #print(tabulate(stack).replace('0', ' ').replace('1', '#'))
                full_line = np.argmax(dump_check)
                dump_rows = len(stack[lvl+full_line+1:,:]) #* there is a math way to do this but ...
                #print('dump rows')
                #print(tabulate(stack[lvl+full_line+1:,:]).replace('0', ' ').replace('1', '#'))
                answer += dump_rows
                stack = stack[:lvl+full_line+1,:] #* keep new full line
                max_height = max_height - dump_rows
                #print('answer',answer)
                #print(f'max_h: {max_height}')
                #print(f'total height: {answer + max_height}')
                #print('stack after')
                #print(tabulate(stack).replace('0', ' ').replace('1', '#'))

print(f'tower is {answer + max_height}') #* answer init as -1 for the floor

#%%
print()
print('⭐ ⭐')