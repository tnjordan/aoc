#%%
from tabulate import tabulate
import copy
f = open('data\day15_input.txt', 'r')
read_lines = f.readlines()
f.close()

L_r = []
L = []
L_r_star = []
L_star = []
for line in read_lines:
    line = line.strip()
    for c in line:
        L_r.append(int(c))
        L_r_star.append(False)
    L.append(L_r)
    L_star.append(L_r_star)
    L_r = []
    L_r_star = []

headers = list(range(len(L[0])))
#print(tabulate(L,headers,showindex=True))

def print_path(L,path):
    display = copy.deepcopy(L)
    for y,x in path:
        display[y][x] = '(' + str(display[y][x]) + ')'
    headers = list(range(len(L[0])))
    #print(tabulate(display,headers,showindex=True))

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
print(tabulate(L_star,headers,showindex=True))
answer = L_star[0][0]

#%%
#! Works but is too slow :()
def next_move(L,y,x,path,score,min_score):
    #* check if at the end
    if (y,x) == (len(L)-1,len(L[0])-1):
                    min_score = score
                    path = path + [(y,x)]
                    ##print('at the end via:', path)
                    #print('new min score:', min_score)
                    #print_path(L,path)
                    return min_score
    #* check if point is valid and not already in the path. 
    elif 0<=y<len(L) and 0<=x<len(L[0]) and (y,x) not in path:
        #* add y,x to path and update score
        path = path + [(y,x)]
        #print(len(path))
        score = score + L[y][x]
        #* only continue if score is less than the min_score
        if score < min_score:
            moves = [(1,0),(0,1),(-1,0),(0,-1)]
            for move in moves:
                dy,dx = move
                new_y = y + dy
                new_x = x + dx
                min_score = next_move(L,new_y,new_x,path,score,min_score)
        return min_score
    return min_score

answer = next_move(L,0,0,[],0,1e9)

#%%
#! Does not work :( (has issues moving in all directions at new point)
'''def next_move(L,y,x,path,score,min_score):
    moves = [(0,1),(1,0),(0,-1),(-1,0)]
    for move in moves:
        ##print('move', move)
        dy,dx = move
        new_y = y + dy
        new_x = x + dx

        #if(new_y,new_x) == (2,6):
        #    #print('at the point')
        ###print(path)
        #* check move is valid and not already in the path
        if 0<=new_y<len(L) and 0<=new_x<len(L[0]) and (new_y,new_x) not in path:
            ##print('made it through')
            ##print('new_y,new_x', new_y,new_x)  
            new_score = score + L[new_y][new_x]
            ##print('new_score', new_score)
            new_path = path + [(new_y,new_x)]
            #* if score is higher than min no need to continue
            ##print('new_score',new_score, 'min_score',min_score)
            if new_score < min_score:
                #* at the end?
                if (new_y,new_x) == (len(L)-1,len(L[0])-1):
                    
                    min_score = new_score
                    #print('at the end via:', new_path)
                    #print('new min score:', min_score)
                    print_path(L,new_path)
                    return min_score
                else:
                    min_score = next_move(L,new_y,new_x,new_path,new_score,min_score)
            else:
                ##print('score > min_score')
                return min_score
        #else:
            ##print('no go')
    return min_score

answer = next_move(L,0,0,[(0,0)],0,1e9)'''