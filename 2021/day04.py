
#%%
import copy
from tabulate import tabulate
f = open('data\day4_input.txt', 'r')
read_lines = f.readlines()
f.close()

bingo_numbers = read_lines[0].strip().split(',')

read_lines = read_lines[1:]
#* don't work share memory address
#bingo_cards = [[]]*int(len(read_lines)/6)
bingo_cards = []
for i in range(int(len(read_lines)/6)):
    bingo_cards.append([])

for i,l in enumerate(read_lines):
    l = l.strip()
    if len(l) > 0:
        bingo_cards[i//6].append(l.split())

#* setup called matrix:
#* and convert strings to ints

bingo_winners = []
bingo_check = copy.deepcopy(bingo_cards)

for i,card in enumerate(bingo_cards):
    bingo_winners.append(False)
    for j,l in enumerate(card):
        for k,value in enumerate(l):
            bingo_cards[i][j][k] = int(value)
            bingo_check[i][j][k] = False

bingo_r = 0
bingo_c = 0
sum_unmarked = 0
answer = 0

for call in bingo_numbers:
    call = int(call)
    #! PART 1: remove #
    #* only print the first answer to prevent scrolling
    #if answer != 0:
    #    break
    for i,card in enumerate(bingo_cards):
        if bingo_winners[i] is False:
            for j,l in enumerate(card):
                for k,value in enumerate(l):
                    if value == call:
                        bingo_check[i][j][k] = True
                        bingo_r = sum(bingo_check[i][j])
                        bingo_c = bingo_check[i][0][k] + bingo_check[i][1][k] + bingo_check[i][2][k] + bingo_check[i][3][k] + bingo_check[i][4][k]
                        if bingo_r == 5 or bingo_c == 5:
                            print('bingo for card',i)
                            bingo_winners[i] = True
                            print(tabulate(card))
                            print(tabulate(bingo_check[i]))
                            for j2,l2 in enumerate(card):
                                for k2,value2 in enumerate(l2):
                                    if bingo_check[i][j2][k2] == False:
                                        sum_unmarked += card[j2][k2]
                            answer = call * sum_unmarked
                            print('answer',answer)
                            sum_unmarked = 0