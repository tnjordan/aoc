#%%
from itertools import permutations

f = 'data/day21.txt'

with open(file=f) as input:
    read_lines = input.readlines()
read_lines = [line.strip() for line in read_lines]
print('🐟 🎄 🦈')
#%%
# +---+---+---+
# | 7 | 8 | 9 |
# +---+---+---+
# | 4 | 5 | 6 |
# +---+---+---+
# | 1 | 2 | 3 |
# +---+---+---+
#     | 0 | A |
#     +---+---+

numeric_keypad_grid = [
    ['7','8','9'],
    ['4','5','6'],
    ['1','2','3'],
    ['VOID','0','A'],
]

numeric_keypad_map = {}
for j,row in enumerate(numeric_keypad_grid):
    for i,c in enumerate(row):
        numeric_keypad_map[c] = {}

        for j2,row2 in enumerate(numeric_keypad_grid):
            for i2,c2 in enumerate(row2):
                ups = max(0,j-j2)
                downs =  max(0,j2-j)
                lefts =  max(0,i-i2)
                rights =  max(0,i2-i)
                numeric_keypad_map[c][c2] = (ups,downs,lefts,rights)


#     +---+---+
#     | ^ | A |
# +---+---+---+
# | < | v | > |
# +---+---+---+

directional_keypad_grid = [
    ['VOID','^','A'],
    ['<','v','>']
]

directional_keypad_map = {}
for j,row in enumerate(directional_keypad_grid):
    for i,c in enumerate(row):
        directional_keypad_map[c] = {}

        for j2,row2 in enumerate(directional_keypad_grid):
            for i2,c2 in enumerate(row2):
                ups = max(0,j-j2)
                downs =  max(0,j2-j)
                lefts =  max(0,i-i2)
                rights =  max(0,i2-i)
                directional_keypad_map[c][c2] = (ups,downs,lefts,rights)

#%%
def press_num_key(num_key_pos,num_key_next):
    ups,downs,lefts,rights = numeric_keypad_map[num_key_pos][num_key_next]
    if downs:
        dir_press = lefts*'<' + rights*'>' + downs*'v'  # avoid VOID
    else:
        dir_press = ups*'^' + lefts*'<' + rights*'>'  # avoid VOID
    return dir_press + 'A'


def press_dir_key(dir_key_pos, dir_key_next):
    # print('\tdir_key_pos',dir_key_pos)
    # print('\tdir_key_next',dir_key_next)
    ups,downs,lefts,rights = directional_keypad_map[dir_key_pos][dir_key_next]
    # print('\t','^','v','<','>')
    # print('\t',ups,downs,lefts,rights)
    if downs:
        dir_press =  downs*'v' + lefts*'<' + rights*'>'  # avoid VOID
    else:
        dir_press =  lefts*'<' + rights*'>' + ups*'^'  # avoid VOID
    # dir_press = lefts*'<' + ups*'^' + downs*'v' + rights*'>'

    # print('\tdir_press:', dir_press+'A')
    # print()
    return dir_press + 'A'


def press_options(dir_press):
    dir_press = dir_press[:-1]  # remove ending A
    if dir_press == []:
        return set('A')
    perms = list(permutations(dir_press))
    perms = [''.join(p) for p in perms]
    perms = [p+'A' for p in perms]
    perms = set(perms)
    return perms


def avoid_the_void(keypad, dir_key_pos, next_dir_sequence_options):
    def get_keypad_position(keypad, key):  # should store the position of the keys
        for j, row in enumerate(keypad):
            for i, value in enumerate(row):
                if value == key:
                    return j, i

    valid_options = []
    d_pad_grid_map = {
        'v': (1,0),
        '^': (-1,0),
        '<': (0,-1),
        '>': (0,1),
        'A': (0,0)  # all end on A, easier than removing and adding
    }
    
    j_prime,i_prime = get_keypad_position(keypad, dir_key_pos)
    
    for ndso in next_dir_sequence_options:
        j,i = j_prime,i_prime
        for nd in ndso:
            print(f'{dir_key_pos} at: {j},{i} pressing: {nd}')
            dj,di = d_pad_grid_map[nd]
            j_dj = j+dj
            i_di = i+di
            if keypad[j_dj][i_di] == 'VOID':
                print('VOID! '*12)
                break
            j = j_dj
            i = i_di
        else:
            print(f'VALID: {ndso}')
            valid_options.append(ndso)
    return set(valid_options)


def efficient_press_key_map(keypad, keypad_map):
    efficient_map = {}
    for j, key_row in enumerate(keypad):
        for i, key in enumerate(key_row):
            efficient_map[key] = {}
            if key == 'VOID':
                continue
            for j_next, key_row_next in enumerate(keypad):
                for i_next, key_next in enumerate(key_row_next):
                    if key_next == 'VOID':
                        continue
                    print(f'at {key} going to {key_next}')
                    ups,downs,lefts,rights = keypad_map[key][key_next]
                    if lefts:  # priority with left -> left + up/down
                        dir_press = lefts*'<' + ups*'^' + downs*'v'
                        print(f'dir_press: {dir_press}')
                        # if we hit a void go other way
                        if not avoid_the_void(keypad, key, [dir_press]):
                            print('hit the void, change direction')
                            print('key',key,'key_next',key_next,'dir_press',dir_press)
                            dir_press = dir_press[::-1]
                            assert avoid_the_void(keypad, key, [dir_press])
                        
                    elif rights:  # priority with right -> up/down + right
                        dir_press = ups*'^' + downs*'v' + rights*'>'
                        print(f'dir_press: {dir_press}')
                        if not avoid_the_void(keypad, key, [dir_press]):
                            print('hit the void, change direction')
                            print('key',key,'key_next',key_next,'dir_press',dir_press)
                            dir_press = dir_press[::-1]
                            assert avoid_the_void(keypad, key, [dir_press])
                    else:
                        dir_press = ups*'^' + downs*'v'
                    efficient_map[key][key_next] = dir_press + 'A'
    return efficient_map


def efficient_press_key(keypad_map, key_pos, key_next):
    # made the function before I realized what it would be
    return keypad_map[key_pos][key_next]


# make maps of most efficient press
keypad_efficient_map = efficient_press_key_map(numeric_keypad_grid, numeric_keypad_map)
direction_efficient_map = efficient_press_key_map(directional_keypad_grid, directional_keypad_map)

#%%
def press(code, d_pads = 1, dir_key_pos = 'A', par2 = False):
    dir_sequences = []
    num_key_pos = 'A'
    # generate first dir sequence
    for num_key_next in code:
        if par2:
            next_dir_sequence_options = [efficient_press_key(keypad_efficient_map, num_key_pos, num_key_next)]
        else:
            next_dir_sequence_options = press_num_key(num_key_pos,num_key_next)
            next_dir_sequence_options = press_options(next_dir_sequence_options)
            next_dir_sequence_options = avoid_the_void(numeric_keypad_grid, num_key_pos, next_dir_sequence_options)
        
        if not dir_sequences:
            dir_sequences = list(next_dir_sequence_options)
        else:
            new_dir_sequences = []
            for ds in dir_sequences:
                for ndso in next_dir_sequence_options:
                    new_dir_sequences.append(ds+ndso)
            dir_sequences = new_dir_sequences
        num_key_pos = num_key_next
    # print('sequences for 1st pad:')
    # print(dir_sequences)

    # todo: fix loop mucho nest
    for _ in range(d_pads):
        print('pad:',_)
        all_seq_options = []
        for dir_sequence in dir_sequences:
            dir_sequences_n = []
            dir_key_pos = 'A'
            for dir_key_next in dir_sequence:
                if par2:
                    next_dir_sequence_n = [efficient_press_key(direction_efficient_map, dir_key_pos, dir_key_next)]
                else:
                    next_dir_sequence_n = press_dir_key(dir_key_pos,dir_key_next)
                    next_dir_sequence_n = press_options(next_dir_sequence_n)
                    next_dir_sequence_n = avoid_the_void(directional_keypad_grid, dir_key_pos, next_dir_sequence_n)

                if not dir_sequences_n:
                    dir_sequences_n = list(next_dir_sequence_n)
                else:
                    new_dir_sequences = []
                    for dsn in dir_sequences_n:
                        for ndsn in next_dir_sequence_n:
                            new_dir_sequences.append(dsn+ndsn)
                    dir_sequences_n = new_dir_sequences
                dir_key_pos = dir_key_next
            all_seq_options += dir_sequences_n  #! OMG this was the bug! a bad tab
        min_press = min([len(k) for k in all_seq_options])
        print('min_press',min_press)
        
        # only keep the minimum press
        all_seq_options = [k for k in all_seq_options if len(k) == min_press]
        
        dir_sequences = all_seq_options
    
    return all_seq_options, min_press

#%%
# read_lines = [  # example
#     '029A',
#     '980A',
#     '179A',
#     '456A',
#     '379A',
# ]

par1 = 0
for code in read_lines:
    print('code: ', code)
    num_code = int(code[:-1])
    all_seq_options, min_press = press(code, d_pads = 2, par2=False)
    # all_seq_options, min_press = press(code, d_pads = 2, par2=True)  # runs way faster
    print('num_code', num_code,' len', min_press, 'product', num_code * min_press)
    par1 += num_code * min_press
par1
#%%
# par2 = 0
# for code in read_lines:
#     print('code: ', code)
#     num_code = int(code[:-1])
#     all_seq_options, min_press = press(code, d_pads = 25, par2=True)  #! kernel crash and burn
#     print('num_code', num_code,' len', min_press, 'product', num_code * min_press)
#     par2 += num_code * min_press
# par2
#%%
#* got so stuck on part one I wrote a decoder to verify my results and sanity check
#* the decoder worked perfectly but I still didn't find my indent bug in Honduras

outcode = []
def decode(dir_sequence, d_pads = 1):
    global outcode
    global num_key_grid
    global d_pad_grid
    
    d_pad_A = (0,2)
    num_key_A = (3,2)
    
    d_pad_grid = [d_pad_A]*d_pads
    num_key_grid = num_key_A

    d_pad_grid_map = {
        'v': (1,0),
        '^': (-1,0),
        '<': (0,-1),
        '>': (0,1)
    }

    def pos_update(num_key_grid, d_pads):
        j,i = num_key_grid
        print('num key grid', num_key_grid, '@', numeric_keypad_grid[j][i])
        for dp in range(d_pads):
            j,i = d_pad_grid[dp]
            print('dpad',dp, 'grid', d_pad_grid[dp], '@', directional_keypad_grid[j][i])
        print()
    pos_update(num_key_grid, d_pads)


    # update down the pads
    def update(dpad_id, ds):
        print('🐛 update dpad', dpad_id,'press',ds)
        global num_key_grid
        global d_pad_grid

        dj,di = d_pad_grid_map[ds]
        if dpad_id == 0:
            # update keypad
            j,i = num_key_grid
            num_key_grid = (j+dj, i+di)
            print('🐛  keypad now at:', numeric_keypad_grid[j+dj][i+di])
        else:
            dpad_id -= 1
            j,i = d_pad_grid[dpad_id]
            d_pad_grid[dpad_id] = (j+dj, i+di)
            print('🐛  dpad', dpad_id, ' now at:', directional_keypad_grid[j+dj][i+di])
    
    def press_update(dpad_id):
        print('🦋​ press_update dpad_id',dpad_id)
        global outcode
        global num_key_grid
        global d_pad_grid

        if dpad_id == -1: # we are on the keypad
            j,i = num_key_grid
            print('🔢 pressing key', numeric_keypad_grid[j][i])
            outcode.append(numeric_keypad_grid[j][i])
            return

        j,i = d_pad_grid[dpad_id]
        ds = directional_keypad_grid[j][i]

        if ds == 'A':
            # prop down
            press_update(dpad_id-1)
        else:
            update(dpad_id, ds)

    for dir_seq in dir_sequence.split('A')[:-1]:  # final A is assumed
        print('\tdir_seq',dir_seq)
        for ds in dir_seq:
            print('\t\tpressing:',ds)
            update(dpad_id=d_pads-1, ds=ds)  # press of your pad is direct
            pos_update(num_key_grid, d_pads)

        # split on 'A' means now we press 'A'
        print('\t\tpress_update')
        press_update(dpad_id=d_pads-1)
        pos_update(num_key_grid, d_pads)
    return outcode
#%%
outcode = []
decode(all_seq_options[-1], d_pads = 3)
#%%
solved = {}
def get_press(current, target, level=1) -> int:
    # minimum of 1 level, otherwise we just press the buttons
    global max_level
    print(' '*level, 'current',current,'target',target,'level',level)
    
    if (current, target, level) in solved:
        return solved[(current, target, level)]

    if target in '0123456789' or current in '0123456789':
        keypad_map = keypad_efficient_map  # oh the trouble with similar variable names
    else:
        keypad_map = direction_efficient_map
    
    cheat_code = efficient_press_key(keypad_map, current, target)
    print(f'{" "*(level+4)} cheat_code: {cheat_code}')  # optimal path from par1
    
    if level == max_level:
        print(f'{" "*(level+4*2)} max level reached! mash the {len(cheat_code)} buttons: {cheat_code}')
        return len(cheat_code)  # you are typing the on the final dpad
    
    button_mash = 0
    new_current = 'A'  # always start at A
    new_level = level + 1
    for new_target in cheat_code:
        button_mashes = get_press(new_current, new_target, new_level)
        solved[(new_current, new_target, new_level)] = button_mashes
        button_mash += button_mashes
        new_current = new_target
    solved[(current, target, level)] = button_mash
    return button_mash

# max_level = 3
# button_mash = get_press(current='A', target='0')
# print('buttons mashed:', button_mash)
# solved
#%%
max_level = 26
par2 = 0
for code in read_lines:
    print('code:',code)
    num_code = int(code[:-1])
    current = 'A'
    button_mashes = 0
    for target in code:
        button_mash = get_press(current, target)  # recursion help from u/nivlark excellent explanation
        button_mashes += button_mash
        current = target
    print('num_code', num_code,' len', button_mashes, 'product', num_code * button_mashes)
    par2 += num_code * button_mashes
par2
#%%
