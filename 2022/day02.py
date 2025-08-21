#%%
f = 'data/day02.txt'

with open(file=f) as input:
    read_lines = input.readlines()
    read_lines = [l.strip() for l in read_lines]

def rps(elf,you):
    #* A,B,C rock, paper, scissors
    #* X,Y,Z rock, paper, scissors
    score = 0
    if you == 'X':
        score += 1
        if elf == 'A':
            score += 3
        elif elf == 'B':
            score += 0
        elif elf == 'C':
            score += 6
    elif you == 'Y':
        score += 2
        if elf == 'A':
            score += 6
        elif elf == 'B':
            score += 3
        elif elf == 'C':
            score += 0
    elif you == 'Z':
        score +=3
        if elf == 'A':
            score += 0
        elif elf == 'B':
            score += 6
        elif elf == 'C':
            score += 3
    return score
# %%
score = 0
for l in read_lines:
    elf,you = l.split()
    score += rps(elf,you)
print(f'score: {score}')

# %%
#! part 2
def rps_2(elf,wld):
    #* A,B,C rock, paper, scissors
    #* X,Y,Z loose, draw, win
    #* rock [1], paper [2], scissors [3]
    score = 0
    if wld == 'X':
        score += 0
        if elf == 'A':
            score += 3
        elif elf == 'B':
            score += 1
        elif elf == 'C':
            score += 2
    elif wld == 'Y':
        score += 3
        if elf == 'A':
            score += 1
        elif elf == 'B':
            score += 2
        elif elf == 'C':
            score += 3
    elif wld == 'Z':
        score +=6
        if elf == 'A':
            score += 2
        elif elf == 'B':
            score += 3
        elif elf == 'C':
            score += 1
    return score

score = 0
for l in read_lines:
    elf,wld = l.split()
    score += rps_2(elf,wld)
print(f'score: {score}')