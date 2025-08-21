#%%
from tabulate import tabulate
f = open('data\day11_input.txt', 'r')
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
print('input')
print(tabulate(L))

def secondary_lit(L,r_i,c_i,lit_count,second_lit_octopus):
    D = [-1,0,+1]
    for r_d in D:
        for c_d in D:
            r = r_i + r_d
            c = c_i + c_d
            #* Check new row and col are in bounds
            if r >= 0 and r < len(L[0]) and c >= 0 and c < len(L):
                #* add 1 to neighboring octopus
                L[r][c] += 1
                if L[r][c] == 10:
                    lit_count += 1
                    second_lit_octopus.append((r,c))
                    lit_count,second_lit_octopus = secondary_lit(L,r,c,lit_count,second_lit_octopus)
    return lit_count,second_lit_octopus


lit_octopus = []
second_lit_octopus = []
lit_count = 0
#! Part 1 set to 100, for Part 2 set to 1000 (or any number greater than 360)
for step in range(1000):
    # add 1 to each octopus
    for r_i,r in enumerate(L):
        for c_i,c in enumerate(r):
            L[r_i][c_i] += 1
            #* when each octopus is 10 then it will be recorded.
            #* Note: octopuses in the code can go higher than 10, but they will only be recorded when crossing the 10 threshold. It matters not which octopus sets the chain reaction. >10 is still greater than 10.
            if L[r_i][c_i] == 10:
                lit_count += 1
                lit_octopus.append((r_i,c_i))

    for r_i,c_i in lit_octopus:
        lit_count,second_lit_octopus = secondary_lit(L,r_i,c_i,lit_count,second_lit_octopus)

    for r_i,c_i in lit_octopus + second_lit_octopus:
        L[r_i][c_i] = 0
    
    #! This is the part 2 code
    if len(lit_octopus) + len(second_lit_octopus) == 100:
        print('this is your answer!:',step+1)
        break

    lit_octopus = []
    second_lit_octopus = []
    #print('step',step+1)
    #print(tabulate(L))
print(lit_count)




# %%
