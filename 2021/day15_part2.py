#%%
from tabulate import tabulate
import copy
f = open('data\day15_input.txt', 'r')
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


#* Code to extend L
def plus_1(L):
    new_L = copy.deepcopy(L)
    for y in range(len(new_L)):
        try:
            for x in range(len(new_L[0])):
                new_L[y][x] += 1
                if new_L[y][x] == 10:
                    new_L[y][x] = 1
        except:
            new_L[y] += 1
            if new_L[y] == 10:
                new_L[y] = 1
    return new_L

#* make large column
L_C = []
Li = copy.deepcopy(L)
for i in range(5):
    L_C += Li
    Li = plus_1(Li)

L = []
L_r = []
for l in L_C:
    Li = copy.deepcopy(l)
    for i in range(5):
        L_r.extend(Li)
        Li = plus_1(Li)
    L.append(L_r)
    L_r = []

headers = list(range(len(L[0])))
#print(tabulate(L,headers,showindex=True))

#* make a new larger L_star
L_star = []
for i in range(len(L)):
    L_star.append([False]*len(L[0]))

#%%
def get_valid_neighbors(L_star,y,x):
    valid_neighbors = []
    moves = [(1,0),(0,1),(-1,0),(0,-1)]
    for move in moves:
        dy,dx = move
        new_y = y + dy
        new_x = x + dx
        if 0<=new_y<len(L_star) and 0<=new_x<len(L_star[0]):
            valid_neighbors.append((new_y,new_x))
    return valid_neighbors

#%%

#* set initial conditions
L_star[len(L_star)-1][len(L_star[0])-1] = 0
updated = True

while updated:
    #print('run')
    updated = False
    for y in range(len(L_star)):
        for x in range(len(L_star[0])):
            #print('y,x',y,x,'L_star[y][x]',L_star[y][x])
            if L_star[y][x] is not False:
                v_n = get_valid_neighbors(L_star,y,x)
                #print(v_n)
                for y_n,x_n in v_n:
                    if L_star[y_n][x_n] is False:
                        L_star[y_n][x_n] = L_star[y][x] + L[y][x]
                        #print(tabulate(L_star,headers,showindex=True))
                        updated = True
                    elif L_star[y_n][x_n] != min(L_star[y_n][x_n], L_star[y][x] + L[y][x]):
                        L_star[y_n][x_n] = min(L_star[y_n][x_n], L_star[y][x] + L[y][x])
                        #print(tabulate(L_star,headers,showindex=True))
                        updated = True

answer = L_star[0][0]
print(answer)

#%%
#! WARNING THIS WORKS FOR PART2, but it takes 10+ min to run

def update_min(L,L_star,updated):
    #print('run')
    if updated:
        updated = False
        for y in range(len(L_star)):
            for x in range(len(L_star[0])):
                #print('y,x',y,x,'L_star[y][x]',L_star[y][x])
                if L_star[y][x] is not False:
                    v_n = get_valid_neighbors(L_star,y,x)
                    #print(v_n)
                    for y_n,x_n in v_n:
                        if L_star[y_n][x_n] is False:
                            L_star[y_n][x_n] = L_star[y][x] + L[y][x]
                            #print(tabulate(L_star,headers,showindex=True))
                            updated = True
                        elif L_star[y_n][x_n] != min(L_star[y_n][x_n], L_star[y][x] + L[y][x]):
                            L_star[y_n][x_n] = min(L_star[y_n][x_n], L_star[y][x] + L[y][x])
                            #print(tabulate(L_star,headers,showindex=True))
                            updated = True
        L_star = update_min(L,L_star,updated)
    else:
        #print('do I get here?')
        #print(tabulate(L_star,headers,showindex=True))
        return L_star
    #TODO Figure out the condition for why this is needed, something to do with recursion
    return L_star

#* set initial point to zero
L_star[len(L_star)-1][len(L_star[0])-1] = 0
updated = True

L_star = update_min(L,L_star,updated)
#print(tabulate(L_star,headers,showindex=True))
answer = L_star[0][0]
print(answer)
# %%
