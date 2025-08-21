#%%
import matplotlib.pyplot as plt

f = 'data/day24.txt'
f = 'data/day24.ex'
# f = 'data/day24.ex2'

with open(file=f) as input:
    read_lines = input.readlines()
read_lines = [l.strip() for l in read_lines]
print('🎅 🎄 🤶')

walls = set()
blizzard_up = []
blizzard_down = []
blizzard_left = []
blizzard_right = []
R = len(read_lines)
C = len(read_lines[0])
for r,line in enumerate(read_lines):
    r = -r #* invert for axis to match example
    for c,char in enumerate(line):
        if char == '#':
            walls.add((r,c))
        elif char == '^':
            blizzard_up.append([r,c])
        elif char == 'v':
            blizzard_down.append([r,c])
        elif char == '<':
            blizzard_left.append([r,c])
        elif char == '>':
            blizzard_right.append([r,c])

def blizzard_simulator(b_up, b_dn, b_lt, b_rt):
    for i,b in enumerate(b_up):
        br, bc = b
        br += 1
        if br == 0: #* at wall reset
            br = -R+1+1 #* one for zero index one for wall
        b_up[i] = [br,bc]
    for i,b in enumerate(b_dn):
        br, bc = b
        br -= 1
        if br == -R+1: #* at wall reset
            br = -1 #* one for wall
        b_dn[i] = [br,bc]
    for i,b in enumerate(b_lt):
        br, bc = b
        bc -= 1
        if bc == 0: #* at wall reset
            bc = C-1-1 #* one for zero index one for wallv
        b_lt[i] = [br,bc]
    for i,b in enumerate(b_rt):
        br, bc = b
        bc += 1
        if bc == C-1: #* at wall reset
            bc = 1 #* one for wall
        b_rt[i] = [br,bc]
    return b_up, b_dn, b_lt, b_rt

def map_scan(walls, b_up, b_dn, b_lt, b_rt,pos=(0,1)):
    plt.scatter(x=[c[1] for c in walls], y=[c[0] for c in walls], marker='s', color='black')
    plt.scatter(x=[c[1] for c in b_up], y=[c[0] for c in b_up], marker='^', color='purple')
    plt.scatter(x=[c[1] for c in b_dn], y=[c[0] for c in b_dn], marker='v', color='blue')
    plt.scatter(x=[c[1] for c in b_lt], y=[c[0] for c in b_lt], marker='<', color='red')
    plt.scatter(x=[c[1] for c in b_rt], y=[c[0] for c in b_rt], marker='>', color='green')
    plt.scatter(x=pos[1], y=pos[0], marker='*', color='orange')
    plt.show()
    print()


#? basic simulation
print('Ready Set GO!')
map_scan(walls,blizzard_up, blizzard_down, blizzard_left, blizzard_right)

for i in range(10):
    blizzard_up, blizzard_down, blizzard_left, blizzard_right = blizzard_simulator(blizzard_up, blizzard_down, blizzard_left, blizzard_right)
    map_scan(walls,blizzard_up, blizzard_down, blizzard_left, blizzard_right)
#%%
# print()
# print('⭐ ⭐')