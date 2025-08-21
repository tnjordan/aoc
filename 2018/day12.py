#%%
f = 'data/day12.txt'

with open(file=f) as input:
    read_lines = input.readlines()
read_lines = [l.strip() for l in read_lines]
print('🎅 🎄 🤶')
#%%
state = read_lines[0].split(' ')[2]
spreads = read_lines[2:]

spreads = [s.split(' => ') for s in spreads]
spreads = {s[0]: s[1] for s in spreads}

part1 = False
if part1:
    zero_pot = 0
    for i in range(20):
        state = '....' + state + '....'
        new_state = ''
        zero_pot += 2 # zero pot shifts 2 each run
        for j in range(0,len(state)-4): # added 4 dots
            pot_state = state[j:j+5]
            new_state += spreads[pot_state]
        state = new_state
        
    score = 0
    for i,p in enumerate(state):
        if p == '#':
            score += i-zero_pot
    print(f'pot score: {score}')

#! part 2
zero_pot = 0
pot_history = set()
for i in range(500): #? i don't know what this problem is. I printed 50k and 500k and noticed they were 1700011, 17000011 so I tried 5k and got 170011 and decided they number was 17...11 where the ... is the number of 0's in the number minus 1
    state = '....' + state + '....'
    new_state = ''
    zero_pot += 2 # zero pot shifts 2 each run with added 4 .
    for j in range(0,len(state)-4): # added 4 dots
        pot_state = state[j:j+5]
        new_state += spreads[pot_state]
    state = new_state
    zero_pot -= len(state) - len(state.lstrip('.'))
    state = state.strip('.')
    # if (zero_pot,state) in pot_history:
    if state in pot_history: # issue was zero is always moving. The shape stabilizes into a 'glider' and stays the same for each further iteration. 
        print(f'found duplicate! {zero_pot} {state}')
    else:
        # pot_history.add((zero_pot,state))
        pot_history.add(state) # works to show glider pattern

#* based on reddit solutions could make formula to calc
#* the final zero_pot and score for the pattern. (need to adjust for the pre-glider stabilization)

score = 0
for i,p in enumerate(state):
    if p == '#':
        score += i-zero_pot
print(f'pot score: {score}')
#%%
print()
print('⭐ ⭐')