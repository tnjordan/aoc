#%%
from collections import deque
import copy

f = 'data/day22.txt'
f = 'data/day22ex.txt'

with open(file=f) as input:
    read_lines = input.readlines()
read_lines = [line.strip() for line in read_lines]
print('❄️⛄❄️')
#%%
p1 = deque()
p2 = deque()

for line in read_lines:
    if line == 'Player 1:':
        p1_load = True
        continue
    elif line == 'Player 2:':
        p1_load = False
        continue
    
    if line != '':
        if p1_load:
            p1.append(int(line))
        else:
            p2.append(int(line))
#%%
def part_1(p1,p2):
    p1 = copy.deepcopy(p1)
    p2 = copy.deepcopy(p2)
    while p1 and p2:
        p1_card = p1.popleft()
        p2_card = p2.popleft()
        
        if p1_card > p2_card:
            p1.append(p1_card)
            p1.append(p2_card)
        elif p2_card > p1_card:
            p2.append(p2_card)
            p2.append(p1_card)
        else:
            p1.append(p1_card)
            p2.append(p2_card)
    score(p1,p2)

def score(p1,p2):
    winner = p1 if p1 else p2
    # print('👑 ' + ('p1' if p1 else 'p2'))
    # print(f'p1: {p1} ')
    # print(f'p2: {p2}')
    score = 0
    for i,card in enumerate(reversed(winner)):
        score += (i+1)*card
    print(score)

part_1(p1,p2)

def recursive_combat(p1,p2):
    previous_games = set()
    p1 = copy.deepcopy(p1)
    p2 = copy.deepcopy(p2)
    
    while p1 and p2:
        p1_p2 = (tuple(p1), tuple(p2))
        if p1_p2 in previous_games:
            # print('seen this game! you win crush the 🦀')
            return 1  # 1 is player 1 win
        previous_games.add(p1_p2)
        
        # print('-'*42)
        # print(f'p1: {p1} len: {len(p1)}')
        p1_card = p1.popleft()
        # print(f'p1_card: {p1_card} status: {len(p1) >= p1_card}')
        # print()
        # print(f'p2: {p2} len: {len(p2)}')
        p2_card = p2.popleft()
        # print(f'p2_card: {p2_card} status: {len(p2) >= p2_card}')
        # print('-'*42)
        
        if len(p1) >= p1_card and len(p2) >= p2_card:
            #! recursive combat!
            # print('\t#! recursive combat!')
            p1_copy = deque(list(p1)[:p1_card])
            p2_copy = deque(list(p2)[:p2_card])
            
            if recursive_combat(p1=p1_copy,p2=p2_copy):
                p1.append(p1_card)
                p1.append(p2_card)
            else:
                p2.append(p2_card)
                p2.append(p1_card)
        else:
            if p1_card > p2_card:
                p1.append(p1_card)
                p1.append(p2_card)
            elif p2_card > p1_card:
                p2.append(p2_card)
                p2.append(p1_card)
            else:
                p1.append(p1_card)
                p2.append(p2_card)
    score(p1,p2)
    return 1 if p1 else 0
recursive_combat(p1,p2)  # the last print is the answer
#%%
#! GPT solution to match print of example (with minor human update)

# Global game counter
game_counter = 0

def recursive_combat(p1, p2, game_id=None):
    global game_counter
    
    # Assign a new game ID if this is a new game
    if game_id is None:
        game_counter += 1
        game_id = game_counter
    
    # Print game header
    print(f"=== Game {game_id} ===\n")
    
    previous_games = set()
    p1 = copy.deepcopy(p1)
    p2 = copy.deepcopy(p2)
    round_num = 1
    
    while p1 and p2:
        # Print round header
        print(f"-- Round {round_num} (Game {game_id}) --")
        print(f"Player 1's deck: {', '.join(str(card) for card in p1)}")
        print(f"Player 2's deck: {', '.join(str(card) for card in p2)}")
        
        # Check if we've seen this game state before
        game_state = (tuple(p1), tuple(p2))
        if game_state in previous_games:
            print(f"Player 1 wins game {game_id} because of the infinite game rule!")
            return 1  # Player 1 wins
        
        previous_games.add(game_state)
        
        # Draw cards
        p1_card = p1.popleft()
        p2_card = p2.popleft()
        print(f"Player 1 plays: {p1_card}")
        print(f"Player 2 plays: {p2_card}")
        
        # Determine round winner
        if len(p1) >= p1_card and len(p2) >= p2_card:
            print(f"Playing a sub-game to determine the winner...\n")
            p1_copy = deque(list(p1)[:p1_card])
            p2_copy = deque(list(p2)[:p2_card])
            
            # Recursive combat with incremented depth
            sub_winner = recursive_combat(p1_copy, p2_copy)
            
            print(f"...anyway, back to game {game_id}.")
            
            if sub_winner == 1:
                p1.append(p1_card)
                p1.append(p2_card)
                print(f"Player 1 wins round {round_num} of game {game_id}!")
            else:
                p2.append(p2_card)
                p2.append(p1_card)
                print(f"Player 2 wins round {round_num} of game {game_id}!")
        else:
            if p1_card > p2_card:
                p1.append(p1_card)
                p1.append(p2_card)
                print(f"Player 1 wins round {round_num} of game {game_id}!")
            else:
                p2.append(p2_card)
                p2.append(p1_card)
                print(f"Player 2 wins round {round_num} of game {game_id}!")
        
        print()  # Empty line between rounds
        round_num += 1
    
    # Game over
    winner = 1 if p1 else 2
    print(f"The winner of game {game_id} is player {winner}!")
    
    # Only show post-game results for the main game
    if game_id == 1:
        print("\n\n== Post-game results ==")
        print(f"Player 1's deck: {', '.join(str(card) for card in p1) if p1 else ''}")
        print(f"Player 2's deck: {', '.join(str(card) for card in p2) if p2 else ''}")
        
        # Calculate final score
        winner_deck = p1 if p1 else p2
        score = sum((i + 1) * card for i, card in enumerate(reversed(winner_deck)))
        print(f"Final score: {score}")
    
    return winner
recursive_combat(p1, p2)
#%%