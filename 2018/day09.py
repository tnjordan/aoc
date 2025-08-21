#%%
f = 'data/day09.txt'

with open(file=f) as input:
    read_lines = input.readlines()
read_lines = [l.strip() for l in read_lines]
print('🎅 🎄 🤶')
#%%
words = read_lines[0].split()
players = int(words[0])
max_points = int(words[-2])
#%%
# players = 10
# max_points = 1618
# players = 9
# max_points = 25

slow = False
if slow:
    print('own slow solution, too slow for 100x part 2')
    player_score = [0]*players
    circle = [0]
    current_marble = 0
    for p in range(1,max_points+1):
        if p % 23 == 0:
            # print(f'score! marble {p} for player {p%players}')
            player_score[p%players] += p
            current_marble -= 7
            if current_marble <= 0:
                current_marble = len(circle) + current_marble
            # print(f'marble counter-clock (left) 7: {circle[current_marble]}')
            player_score[p%players] += circle[current_marble]
            circle = circle[:current_marble] + circle[current_marble+1:]
            # print(f'score update: {player_score}')
        else:
            current_marble += 2
            if current_marble > len(circle):
                current_marble = 1 #* reset going over 0 marble
            if current_marble == len(circle):
                circle.append(p)
            else:
                circle = circle[:current_marble] + [p] + circle[current_marble:]
        # print(f'current_marble {current_marble} circle {circle}')

    print(f'winning score {max(player_score)}')

#%%
#! part 2
#* defeated! the above is too slow :( for 100x
# I did my own research! linked list are the answer.

for max_points in [max_points, max_points*100]: # confusing but works to print both parts
    marble = {  'current': 0, 
                'prev':None,
                'next':None}
    marble['prev'] = marble # linked list inception
    marble['next'] = marble

    player_score = [0]*players
    for m in range(1,max_points+1):
        if m % 23 == 0:
            player_score[m%players] += m # score 23x marble
            for _ in range(7):
                marble = marble['prev']
            player_score[m%players] += marble['current'] # score marble counter clock 7
            prev = marble['prev']
            nxt = marble['next']
            prev['next'] = nxt #* removes the marble by linking the marbles prev and next to each other
            nxt['prev'] = prev
            marble = nxt # current marble advances clockwise of remove marble
        else:
            prev = marble['next'] # new marble goes between the next marble and the next next marble (current marble) (next marble) (new_marble) (next next marble)
            nxt = prev['next']
            marble = {  'current': m, 
                        'prev':prev,
                        'next':nxt}
            prev['next'] = marble
            nxt['prev'] = marble
            
    print(f'max marble score: {max_points} wining player score: {max(player_score)}')

#%%
# bonus solution from reddit to explore deque
from collections import deque, defaultdict

max_players = players
last_marble = max_points

scores = defaultdict(int)
circle = deque([0])

for marble in range(1, last_marble + 1):
    if marble % 23 == 0:
        circle.rotate(7)
        scores[marble % max_players] += marble + circle.pop()
        circle.rotate(-1)
    else:
        circle.rotate(-1)
        circle.append(marble)

print(max(scores.values()))
#%%
print()
print('⭐ ⭐')