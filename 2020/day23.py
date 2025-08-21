#%%
f = 'data/day23.txt'
# f = 'data/day23ex.txt'

with open(file=f) as input:
    read_lines = input.readlines()
read_lines = [line.strip() for line in read_lines]
print('❄️⛄❄️')
#%%
part_2 = True

all_cups = list(map(int, (list(read_lines[0]))))
if part_2:
    all_cups += list(map(int, range(10, 1_000_001)))

cups = {}
prev_c = all_cups[-1]
for c in all_cups:
    cups[prev_c] = c
    prev_c = c
#%%
current_cup = int(read_lines[0][0])

def get_removed_cups(current_cup, cups):
    removed_cups = []
    for _ in range(3):
        next_cup = cups[current_cup]
        removed_cups.append(next_cup)
        current_cup = next_cup
    return removed_cups

def find_destination_cup(current_cup, removed_cups):
    potential_destination_cup = current_cup - 1
    while True:
        if potential_destination_cup < 1:
            potential_destination_cup = 1e6 if part_2 else 9
        if potential_destination_cup not in removed_cups:
            return potential_destination_cup
        potential_destination_cup -= 1
        

def place_removed_cups(cups, current_cup, destination_cup, removed_cups):
    cups[current_cup] = cups[removed_cups[-1]]  # current cup points to the destination of last removed cup
    destination_cups_next = cups[destination_cup]
    cups[destination_cup] = removed_cups[0]  # destination cup points to first inserted cup
    cups[removed_cups[-1]] = destination_cups_next  # last inserted cup points to where destination cup was going
    return cups

rounds = 10_000_000 if part_2 else 100

for _ in range(rounds):
    removed_cups = get_removed_cups(current_cup, cups)
    destination_cup = find_destination_cup(current_cup, removed_cups)
    cups = place_removed_cups(cups, current_cup, destination_cup, removed_cups)
    current_cup = cups[current_cup]

if part_2:
    c1 = cups[1]
    c2 = cups[c1]
    print(f'c1:{c1} c2:{c2} c1*c2:{c1*c2}')
else:
    score_cup = 1
    cup_labels = ''
    for _ in range(len(cups)-1):
        score_cup = cups[score_cup]
        cup_labels += str(score_cup)
    print(cup_labels)
#%%
