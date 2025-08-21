#%%
from collections import Counter
from collections import defaultdict

f = 'data/day07.txt'
f = 'data/day07.ex'

with open(file=f) as input:
    read_lines = input.readlines()
read_lines = [line.strip() for line in read_lines]
print('❄️⛄❄️')
#%%

verbose = True

cards = 'A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, 2'
cards = cards.split(', ')
card_rank = {}
for i, c in enumerate(reversed(cards), start=11):  # starting at 11 to have double digits and make room for wild J in part 2
    card_rank[c] = i

card_rank_wild = card_rank.copy()
card_rank_wild['J'] = 10  #  J is the weakest

hand_type_map = {7: 'five of a kind', 6: 'four of a kind', 5: 'full house', 4: 'three of a kind', 3: 'two pair', 2: 'one pair', 1: 'high card'}


def hand_type(hand):
    counts = Counter(hand).most_common()
    card, count = counts[0]
    if count == 5:
        return 7
    elif count == 4:
        return 6
    elif count == 3:
        if len(counts) == 2:
            return 5
        else:
            return 4
    elif count == 2:
        if len(counts) == 3:
            return 3
        else:
            return 2
    return 1


def wild_hand_type(hand):
    if 'J' not in hand:
        return hand_type(hand)
    counts = Counter(hand)
    wildies = counts['J']
    if wildies == 5:
        return 7  # all wildies
    counts = Counter(hand.replace('J', ''))
    card, count = counts.most_common()[0]
    if count == (5 - wildies):
        return 7
    elif count == (4 - wildies):
        return 6
    elif count == (3 - wildies):
        if len(counts) == 2:
            return 5
        else:
            return 4
    elif count == (2 - wildies):
        if len(counts) == 3:
            return 3
        else:
            return 2


def hand_scorer(hand, card_rank):
    score = ''
    for card in hand:
        score += str(card_rank[card])  # ord didn't work
    return int(score)


if verbose:
    print('grouping hands by type')
hands = defaultdict(list)
hands_wildies = defaultdict(list)
for line in read_lines:
    hand, bid = line.split()
    bid = int(bid)
    hand_t = hand_type(hand)
    hands[hand_t].append((hand, bid))
    # wild
    hand_t_w = wild_hand_type(hand)
    hands_wildies[hand_t_w].append((hand, bid))
    if verbose:
        print(f'\thand: {hand} is a: {hand_type_map[hand_t]}, and a wild: {hand_type_map[hand_t_w]}')

for part in [1, 2]:
    print(f'♠️ part_{part}')
    total_winnings = 0
    rank = 1
    for h_t in range(1, 8):
        if verbose:
            print(f'ranking hand type: {hand_type_map[h_t]}')
        if part == 1:
            type_hands = hands[h_t]
            type_hands = sorted(type_hands, key=lambda x: hand_scorer(x[0], card_rank))
        else:
            type_hands = hands_wildies[h_t]
            type_hands = sorted(type_hands, key=lambda x: hand_scorer(x[0], card_rank_wild))
        for hand, bid in type_hands:
            if verbose:
                print(f'\thand: {hand} bids {bid} and is rank {rank} to win {rank * bid}')
            total_winnings += rank * bid
            rank += 1
    print(f'💰 total winnings: {total_winnings} 💰')
    print('💰 ' * 11, '\n')
#%%
