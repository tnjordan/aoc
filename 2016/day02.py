#%%
f = 'data/day02.txt'

with open(file=f) as input:
    read_lines = input.readlines()
read_lines = [li.strip() for li in read_lines]
print('🎅 🎄 🤶')
#%%
button_map = {
    1: {'U': 1, 'D': 4, 'L': 1, 'R': 2},
    2: {'U': 2, 'D': 5, 'L': 1, 'R': 3},
    3: {'U': 3, 'D': 6, 'L': 2, 'R': 3},
    4: {'U': 1, 'D': 7, 'L': 4, 'R': 5},
    5: {'U': 2, 'D': 8, 'L': 4, 'R': 6},
    6: {'U': 3, 'D': 9, 'L': 5, 'R': 6},
    7: {'U': 4, 'D': 7, 'L': 7, 'R': 8},
    8: {'U': 5, 'D': 8, 'L': 7, 'R': 9},
    9: {'U': 6, 'D': 9, 'L': 8, 'R': 9}
}

button = 5
code = ''
for line in read_lines:
    for direction in line:
        button = button_map[button][direction]
    code += str(button)

print(f'Bathroom code: {code}')

#%%
#! part 2

button_map = {
    '1': {'U': '1', 'D': '3', 'L': '1', 'R': '1'},
    '2': {'U': '2', 'D': '6', 'L': '2', 'R': '3'},
    '3': {'U': '1', 'D': '7', 'L': '2', 'R': '4'},
    '4': {'U': '4', 'D': '8', 'L': '3', 'R': '4'},
    '5': {'U': '5', 'D': '5', 'L': '5', 'R': '6'},
    '6': {'U': '2', 'D': 'A', 'L': '5', 'R': '7'},
    '7': {'U': '3', 'D': 'B', 'L': '6', 'R': '8'},
    '8': {'U': '4', 'D': 'C', 'L': '7', 'R': '9'},
    '9': {'U': '9', 'D': '9', 'L': '8', 'R': '9'},
    'A': {'U': '6', 'D': 'A', 'L': 'A', 'R': 'B'},
    'B': {'U': '7', 'D': 'D', 'L': 'A', 'R': 'C'},
    'C': {'U': '8', 'D': 'C', 'L': 'B', 'R': 'C'},
    'D': {'U': 'B', 'D': 'D', 'L': 'D', 'R': 'D'},
}

button = '5'
code = ''
for line in read_lines:
    for direction in line:
        button = button_map[button][direction]
    code += button

print(f'Bathroom code: {code}')

#%%
print()
print('⭐ ⭐')
