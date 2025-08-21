#%%
import re
from collections import defaultdict
import random

f = 'data/day19.txt'
f = 'data/day19.ex'

with open(file=f) as input:
    read_lines = input.readlines()
read_lines = [l.strip() for l in read_lines]
#print('🎅 🎄 🤶')

regex = re.compile('(\d+)')

blueprints = {}
for l in read_lines:
    in_numbers = [int(x) for x in regex.findall(l)]
    #TODO decide on naming, if need _robot or not
    # blueprints[in_numbers[0]]= {'ore_robot':        {'ore':in_numbers[1]},
    #                             'clay_robot':       {'ore':in_numbers[2]},
    #                             'obsidian_robot':   {'ore':in_numbers[3],'clay':in_numbers[4]},
    #                             'geode_robot':      {'ore':in_numbers[5],'obsidian':in_numbers[6]}}
    blueprints[in_numbers[0]]= {'ore':        {'ore':in_numbers[1]},
                                'clay':       {'ore':in_numbers[2]},
                                'obsidian':   {'ore':in_numbers[3],'clay':in_numbers[4]},
                                'geode':      {'ore':in_numbers[5],'obsidian':in_numbers[6]}}



max_g = 0
g_list = []
for i in range(1_000_000):
    robot_army = defaultdict(int)
    elements = defaultdict(int)

    #* start with ore robot from backpack
    robot_army['ore'] += 1
    bp = blueprints[2] #* developing with first blue_print
    for m in range(1,24+1):
        #print(f'== Minute {m} ==')
        robot_options = []
        for robot,cost in bp.items():
            for element, quantity in cost.items():
                if elements[element] < quantity:
                    break #* not enough elements!
            else:
                robot_options.append(robot)
        
        #TODO figure out algo way to implement
        new_robot = None
        if robot_options:
            robot_options.append(None)
            # new_robot = robot_options[-1] #* always build the most expensive thing you can #? this did spectacularly bad and only made clay robots
            new_robot = random.choice(robot_options) #* this is able to build geodes, but rarely
            if new_robot is not None:
                cost = bp[new_robot]
                for element, quantity in cost.items():
                    elements[element] -= quantity
                #print(f'Spend {cost} to start building a {new_robot}-collecting robot.')
            else:
                #print('Spend {Nothing} and wait.')
                pass

        for robot,quantity in robot_army.items(): #* harvest resources
            elements[robot] += quantity
            #print(f'{quantity} {robot}-collecting robot collects {quantity} {robot}; you now have {elements[robot]} {robot}.')
        
        if new_robot is not None:
            robot_army[new_robot] += 1 #* end of turn new robot is ready for next turn
            #print(f'The new {new_robot}-collecting robot is ready; you now have {robot_army[new_robot]} of them.')

    #print(f'geodes mined {elements["geode"]}')
    max_g = max(max_g, elements["geode"])
    g_list.append(elements["geode"])

print(f'max geodes: {max_g}')
#%%
# #print()
# #print('⭐ ⭐')