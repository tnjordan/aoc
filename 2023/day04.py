#%%
f = 'data/day04.txt'
# f = 'data/day04.ex'

with open(file=f) as input:
    read_lines = input.readlines()
read_lines = [line.strip() for line in read_lines]
print('❄️⛄❄️')
#%%
points = 0
for line in read_lines:
    card_data, number_data = line.split(' | ')
    winners = [int(x) for x in card_data.split(': ')[1].split()]
    numbers = [int(x) for x in number_data.split()]
    winning_numbers = set(winners).intersection(set(numbers))
    if winning_numbers:
        points += 2 ** (len(winning_numbers) - 1)

print(f'🧝 cards are worth: {points} points🎄')
#%%
#! part 2
cards = {}
card_counts = {}
for line in read_lines:
    card_data, number_data = line.split(' | ')
    card = int(card_data.split(': ')[0][5:])
    winners = [int(x) for x in card_data.split(': ')[1].split()]
    numbers = [int(x) for x in number_data.split()]
    cards[card] = (winners, numbers)
    card_counts[card] = 1

for current_card in cards:  # 🐛 while -> for loop update
    winners, numbers = cards[current_card]
    winning_numbers = set(winners).intersection(set(numbers))
    for c in range(1, len(winning_numbers) + 1):
        card_counts[current_card + c] += 1 * card_counts[current_card]

print(f'🧝 has {sum(card_counts.values())} cards🎄')
#%%
