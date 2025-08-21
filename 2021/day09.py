#%%
f = open('data\day9_input.txt', 'r')
read_lines = f.readlines()
f.close()

L_r = []
L = []
for line in read_lines:
    line = line.strip()
    for c in line:
        L_r.append(int(c))
    L.append(L_r)
    L_r = []

#! Part 2 Function
#* function to calculate and return the basin size
def basin_sizer(r_i, c_i, L, count):
    #check if point is already a 9 (We are obviously sharing memory so not the best answer):
    if L[r_i][c_i] != 9:
        #set point to 9 so it doesn't get double counted
        L[r_i][c_i] = 9
        # increment the count:
        count += 1
        #check the 4 directions:
        if r_i == 0:
            # @ top
            up = 9
        else:
            up = L[r_i - 1][c_i]
        try:
            down = L[r_i + 1][c_i]
        except IndexError:
            #print('@ low boundary')
            down = 9
        if c_i == 0:
            #print('@ left boundary')
            left = 9
        else:
            left = L[r_i][c_i-1]
        try:
            right = L[r_i][c_i+1]
        except IndexError:
            #print('@ right boundary')
            right = 9
        if up != 9:
            #print('move up to', r_i-1, c_i, 'for', up)
            count = basin_sizer(r_i-1, c_i, L, count)
        if down != 9:
            #print('move down to', r_i+1, c_i, 'for', down)
            count = basin_sizer(r_i+1, c_i, L, count)
        if left != 9:
            #print('move left to', r_i, c_i-1, 'for', left)
            count = basin_sizer(r_i, c_i-1, L, count)
        if right != 9:
            #print('move right to', r_i, c_i+1, 'for', right)
            count = basin_sizer(r_i, c_i+1, L, count)
    return count

#initiate variables
up = 9
down = 9
left = 9
right = 9
answer = 0
low_count = 0
basin_size = 0
basin_list = []

for r_i,r in enumerate(L):
    for c_i,c in enumerate(r):
        if r_i == 0:
            #print('@ up boundary')
            up = 9
        else:
            up = L[r_i - 1][c_i]
        try:
            down = L[r_i + 1][c_i]
        except IndexError:
            #print('@ low boundary')
            down = 9
        if c_i == 0:
            #print('@ left boundary')
            left = 9
        else:
            left = L[r_i][c_i-1]
        try:
            right = L[r_i][c_i+1]
        except IndexError:
            #print('@ right boundary')
            right = 9
        if c < up and c < down and c < left and c < right:
            print("low_point",c, "@", r_i,c_i)
            answer += c + 1
            low_count += 1
            basin_size = basin_sizer(r_i, c_i, L, basin_size)
            basin_list.append(basin_size)
            print('basin_size',basin_size)
            basin_size = 0

print(answer)
print(low_count)
s_b = sorted(basin_list, reverse=True)
answer2 = s_b[0]*s_b[1]*s_b[2]
print(answer2)

# %%
