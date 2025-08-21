#%%
f = 'data/day19.txt'  # 🐠
# f = 'data/da19.ex'  # on plane no internet for submit

with open(file=f) as input:
    read_lines = input.readlines()
read_lines = [line.strip() for line in read_lines]
print('🐟 🎄 🦈')
#%%
towels = read_lines[0].split(', ')
designs = read_lines[2:]
#%%
# all_possible = set()  # no need
no_possible = set()  # very much need
def design_possible(design, towels):
    # global all_possible
    global no_possible
    # print('\t',design)
    possible = 0
    if design == '':
        return 1
    # if design in all_possible:
    #     return 1
    if design in no_possible:
        return 0  # no solve same problem
    if design in towels:
        # all_possible.add(design)
        return 1
    for towel in towels:
        if design.startswith(towel):
            remaining_design = design[len(towel):]
            possible += design_possible(remaining_design, towels)
            if possible:
                return 1  # no need to continue
    no_possible.add(design)
    return possible

possible = 0
for design in designs:
    print('design:', design)
    if design_possible(design, towels):
        possible += 1
        print('\tpossible!')
possible
#%%
no_possible = set()  # very much need
designs_solved = {}
def design_possible_par2(design):
    global no_possible
    global designs_solved
    possible = 0
    
    if design in designs_solved:  # this is what I was missing to solve par2
        #! solved this before
        return designs_solved[design]
    
    if design == '':
        return 1
    if design in no_possible:
        return 0
    used_a_towel = False
    for towel in towels:
        if design.startswith(towel):
            used_a_towel = True
            remaining_design = design[len(towel):]
            more_possible = design_possible_par2(remaining_design)
            if more_possible:
                possible += more_possible
            else:
                no_possible.add(remaining_design)
    if not used_a_towel:
        no_possible.add(design)
    designs_solved[design] = possible  # save the ways to solve this design
    return possible

possible = 0
par2 = 0
for design in designs:
    print('design:', design)
    dp = design_possible_par2(design)
    if dp:
        possible += 1
        print('\t possible!')
        print('\t',dp,'ways.')
        par2 += dp
print('par1', possible)
print('par2', par2)  # needed dynamic programming with memoization
#%%