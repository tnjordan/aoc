#%%

f = open('data/day21_input.txt', 'r')
read_lines = f.readlines()
f.close()

#! Part 1
p1_pos = int(read_lines[0][28:].strip())
p2_pos = int(read_lines[1][28:].strip())

p1_score = 0
p2_score = 0

dice_roll = 0
dice_roll_count = 0
p1_turn = True
while (p1_score < 1_000) and (p2_score < 1_000):
    roll = 0
    for i in range(3):
        if dice_roll == 100:
            # reset the dice
            dice_roll = 0
        dice_roll += 1
        dice_roll_count += 1
        roll += dice_roll
    if p1_turn is True:
        p1_pos += roll
        rem = p1_pos%10
        if rem == 0:
            p1_score += 10
        else:
            p1_score += rem
        # p1 turn over
        p1_turn = False
    else:
        p2_pos += roll
        rem = p2_pos%10
        if rem == 0:
            p2_score += 10
        else:
            p2_score += rem
        # back to p1 turn
        p1_turn = True

if p1_score < p2_score:
    losing_score = p1_score
else:
    losing_score = p2_score

print(losing_score*dice_roll_count)

# %%

#! Part 2
def quantum_roll(p1_pos, p1_score, p2_pos, p2_score, p1_turn):
    # check for winner
    if p1_score >= 21:
        return (1,0)
    if p2_score >= 21:
        return (0,1)
    # switch players turn
    p1_turn = not p1_turn

    if (p1_pos, p1_score, p2_pos, p2_score, p1_turn) in Previous_States:
        return Previous_States[(p1_pos, p1_score, p2_pos, p2_score, p1_turn)]

    ans = (0,0)
    for i in [1,2,3]:
        for j in [1,2,3]:
            for k in [1,2,3]:
                roll_score = i + j + k
                if p1_turn is True:
                    new_p1_pos = p1_pos + roll_score
                    rem = new_p1_pos%10
                    if rem == 0:
                        new_p1_score = p1_score + 10
                    else:
                        new_p1_score = p1_score + rem
                    new_p2_pos = p2_pos
                    new_p2_score = p2_score
                else:
                    new_p2_pos = p2_pos + roll_score
                    rem = new_p2_pos%10
                    if rem == 0:
                        new_p2_score = p2_score + 10
                    else:
                        new_p2_score = p2_score + rem
                    new_p1_pos = p1_pos
                    new_p1_score = p1_score
                # roll again
                p1_w, p2_w = quantum_roll(new_p1_pos, new_p1_score, new_p2_pos, new_p2_score, p1_turn)
                ans = (ans[0] + p1_w, ans[1] + p2_w)
    Previous_States[(p1_pos, p1_score, p2_pos, p2_score, p1_turn)] = ans
    return ans
p1_pos = int(read_lines[0][28:].strip())
p2_pos = int(read_lines[1][28:].strip())
#p1_pos = 4
#p2_pos = 8

p1_score = 0
p2_score = 0

p1_turn = False #start false because quantam roll flips on first call

Previous_States = {}
ans = quantum_roll(p1_pos, p1_score, p2_pos, p2_score, p1_turn)
print(ans)
print(max(ans))


#%%
#! https://github.com/jonathanpaulson/AdventOfCode/blob/master/2021/21.py
# dynamic programming!
# brute force + memoization.
# how many possible game states are there?
# 10 options for p1, 10 options for p2, 21 options for s1, 21 options for s2 -> 10*10*21*21 ~ 40,000
# total running time ~ state space * non-recursive time for one call ~ 40e3 * 27 ~ 120e4 = ~1M
p1 = 4-1
p2 = 8-1
DP = {} # game state -> answer for that game state
def count_win(p1, p2, s1, s2):
  # Given that A is at position p1 with score s1, and B is at position p2 with score s2, and A is to move,
  # return (# of universes where player A wins, # of universes where player B wins)
  if s1 >= 21:
    return (1,0)
  if s2 >= 21:
    return (0, 1)
  if (p1, p2, s1, s2) in DP:
    return DP[(p1, p2, s1, s2)]
  ans = (0,0)
  for d1 in [1,2,3]:
    for d2 in [1,2,3]:
      for d3 in [1,2,3]:
        new_p1 = (p1+d1+d2+d3)%10
        new_s1 = s1 + new_p1 + 1

        x1, y1 = count_win(p2, new_p1, s2, new_s1)
        ans = (ans[0]+y1, ans[1]+x1)
  DP[(p1, p2, s1, s2)] = ans
  return ans

print(max(count_win(p1, p2, 0, 0)))

#%%
# Pure reursion, too much recursion :( crash and burn!

# def quantum_roll(p1_pos, p1_score, p2_pos, p2_score, dice_roll, dice_roll_count, roll_score, p1_turn, p1_wins, p2_wins):
#     #print(f'quant trouble: {p1_pos}, {p1_score}, {p2_pos}, {p2_score}, {dice_roll}, {dice_roll_count}, {roll_score}, {p1_turn}, {p1_wins}, {p2_wins}')
#     roll_score += dice_roll
#     if dice_roll_count < 3:
#         dice_roll_count += 1
#         # p1_w, p2_w = quantum_roll(p1_pos, p1_score, p2_pos, p2_score, 1, dice_roll_count, roll_score, p1_turn, p1_wins, p2_wins)
#         # p1_wins += p1_w
#         # p2_wins += p2_w
#         # p1_w, p2_w = quantum_roll(p1_pos, p1_score, p2_pos, p2_score, 2, dice_roll_count, roll_score, p1_turn, p1_wins, p2_wins)
#         # p1_wins += p1_w
#         # p2_wins += p2_w
#         # p1_w, p2_w = quantum_roll(p1_pos, p1_score, p2_pos, p2_score, 3, dice_roll_count, roll_score, p1_turn, p1_wins, p2_wins)
#         # p1_wins += p1_w
#         # p2_wins += p2_w
        
#         p1_wins, p2_wins = quantum_roll(p1_pos, p1_score, p2_pos, p2_score, 1, dice_roll_count, roll_score, p1_turn, p1_wins, p2_wins)
#         p1_wins, p2_wins = quantum_roll(p1_pos, p1_score, p2_pos, p2_score, 2, dice_roll_count, roll_score, p1_turn, p1_wins, p2_wins)
#         p1_wins, p2_wins = quantum_roll(p1_pos, p1_score, p2_pos, p2_score, 3, dice_roll_count, roll_score, p1_turn, p1_wins, p2_wins)



#     # score p1 and p2
#     if p1_turn is True:
#         p1_pos += roll_score
#         rem = p1_pos%10
#         if rem == 0:
#             p1_score += 10
#         else:
#             p1_score += rem
#         # p1 turn over
#         p1_turn = False
#     else:
#         p2_pos += roll_score
#         rem = p2_pos%10
#         if rem == 0:
#             p2_score += 10
#         else:
#             p2_score += rem
#         # back to p1 turn
#         p1_turn = True
#     dice_roll_count = 1 #? 0 or 1

#     if p1_score >= 21:
#         p1_wins += 1
#         print(f'p1_win: {p1_wins}')
#         return p1_wins, p2_wins
#     elif p2_score >= 21:
#         p2_wins += 1
#         print(f'p2_win: {p2_wins}')
#         return p1_wins, p2_wins
#     else:
#         # No winner kick it off again
#         quantum_roll(p1_pos, p1_score, p2_pos, p2_score, 0, 0, roll_score, p1_turn, p1_wins, p2_wins)
#         #return p1_wins, p2_wins
#     return p1_wins, p2_wins 
# # p1_pos = int(read_lines[0][28:].strip())
# # p2_pos = int(read_lines[1][28:].strip())

# p1_pos = 4
# p2_pos = 8

# p1_score = 0
# p2_score = 0

# dice_roll = 0
# p1_turn = True

# p1_wins, p2_wins = quantum_roll(p1_pos, p1_score, p2_pos, p2_score, dice_roll = 0, dice_roll_count = 0, roll_score = 0, p1_turn = True, p1_wins = 0, p2_wins = 0)

    


# %%
