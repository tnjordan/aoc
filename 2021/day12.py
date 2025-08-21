#%%
f = open('data\day12_input.txt', 'r')
read_lines = f.readlines()
f.close()

#%%
connection_list = []
connection_dict = {}
for line in read_lines:
    line = line.strip()
    start_point, end_point = line.split('-')
    connection_list.append((start_point,end_point))
    if start_point not in connection_dict:
        connection_dict[start_point] = [end_point]
    else:
        connection_dict[start_point].append(end_point)
    if end_point not in connection_dict:
        connection_dict[end_point] = [start_point]
    else:
        connection_dict[end_point].append(start_point)


#* Drop 'end' from connection dict, can't go back once you end
connection_dict.pop('end')

#* Later Todd says add back in 'end' with no values to help the flow later
connection_dict['end'] = []

#* drop 'start' from key values, can't go back to start.
for key in connection_dict:
    if 'start' in connection_dict[key]:
        connection_dict[key].remove('start')


# %%
#! Part 1
path_list = []
path = ['start',]

def avaliable_positions(connection_dict,position,path):
    path_options = []
    for connection in connection_dict[position]:
        if connection.isupper():
            path_options.append(connection)
        elif connection not in path:
            path_options.append(connection)
    return path_options


counter = 0
def path_finder(connection_dict,position,path,counter):
    next_move_options = avaliable_positions(connection_dict,position,path)
    #print('At',position,'avaliable',next_move_options,'current path',path)
    if len(next_move_options) == 0:
        if position == 'end':
            print('end of the line! path to end',path)
            counter += 1
            return counter
        else:
            #print('IT\'S A TRAP',path,'is a dead end')
            #path_list.append(path)
            #print(path_list)
            return counter
    for move in next_move_options:
        pathy_path = path + [move]
        counter = path_finder(connection_dict,move,pathy_path,counter)
    return counter


answer = path_finder(connection_dict,'start',path,counter)
print(answer)

#%%
#! Part 2
path_list = []
path = ['start',]

#* Function for part 2
def double_visit(path):
    double_trouble = False
    for pos in path:
        if pos.islower():
            if path.count(pos) > 1:
                double_trouble = True
    return double_trouble


def avaliable_positions2(connection_dict,position,path):
    path_options = []
    for connection in connection_dict[position]:
        if connection.isupper():
            path_options.append(connection)
        elif connection not in path:
            path_options.append(connection)
        #* change for part 2
        elif not double_visit(path):
            path_options.append(connection)
    return path_options


counter = 0
def path_finder2(connection_dict,position,path,counter):
    next_move_options = avaliable_positions2(connection_dict,position,path)
    #print('At',position,'avaliable',next_move_options,'current path',path)
    if len(next_move_options) == 0:
        if position == 'end':
            print('end of the line! path to end',path)
            counter += 1
            return counter
        else:
            #print('IT\'S A TRAP',path,'is a dead end')
            #path_list.append(path)
            #print(path_list)
            return counter
    
    for move in next_move_options:
        pathy_path = path + [move]
        counter = path_finder2(connection_dict,move,pathy_path,counter)
    
    return counter


answer = path_finder2(connection_dict,'start',path,counter)
print(answer)


# %%
#This code works but is too slow, passing the path_list is too cumbersome
'''path_list = []
path = ['start',]

def avaliable_positions(connection_dict,position,path):
    path_options = []
    for connection in connection_dict[position]:
        if connection.isupper():
            path_options.append(connection)
        elif connection not in path:
            path_options.append(connection)
    return path_options

def path_finder(connection_dict,position,path,path_list):
    next_move_options = avaliable_positions(connection_dict,position,path)
    print('At',position,'avaliable',next_move_options,'current path',path)
    if len(next_move_options) == 0:
        if position == 'end':
            print('end of the line! path to end',path)
            path_list.append(path)
            return path_list
        else:
            print('IT\'S A TRAP',path,'is a dead end')
            #path_list.append(path)
            #print(path_list)
            return path_list
    for move in next_move_options:
        pathy_path = path + [move]
        path_finder(connection_dict,move,pathy_path,path_list)
    return path_list


listy_list = path_finder(connection_dict,'start',path,path_list)
print(listy_list)
print(len(listy_list))'''