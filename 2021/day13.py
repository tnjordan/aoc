#%%
from tabulate import tabulate
f = open('data\day13_input.txt', 'r')
read_lines = f.readlines()
f.close()

sheet = []
fold_instructions = []
for l in read_lines:
    l = l.strip()
    try:
        x,y = map(int,l.split(','))
        sheet.append((x,y))
    except:
        fold_instructions.append(l)
#* remove blank line
fold_instructions.pop(0)

#%%
def project_sheet(sheet):
    
    x_max = 0
    y_max = 0
    for x,y in sheet:
        if x >= x_max:
            x_max = x
            #* add 1 because range in inclusive
            x_max +=1
        if y >= y_max:
            y_max = y
            #* add 1 because range in inclusive
            y_max +=1
    display = [['' for i in range(x_max)] for j in range(y_max)]
    headers = list(range(x_max))
    for x,y in sheet:
        #print(x,y,display[y][x])
        display[y][x] = '#'
        #print(tabulate(display,headers,showindex=True))
    print(tabulate(display,headers,showindex=True))
    
#project_sheet(sheet)
# %%
def fold(sheet, instruction):
    half_sheet = []
    instruction = instruction.replace('fold along ','')
    direction,fold_line = instruction.split('=')
    fold_line = int(fold_line)
    if direction == 'y':
        for x,y in sheet:
            if y < fold_line:
                half_sheet.append((x,y))
            else:
                half_sheet.append((x,fold_line-(y-fold_line)))
    else:
        for x,y in sheet:
            if x < fold_line:
                half_sheet.append((x,y))
            else:
                half_sheet.append((fold_line-(x-fold_line),y))
    return half_sheet

#%%
#project_sheet(sheet)
for instruction in fold_instructions:
    print(instruction)
    sheet = fold(sheet, instruction)
    sheet = list(set(sheet))
    #! Part 1 print statement
    #print(len(sheet))
    #project_sheet(sheet)
project_sheet(sheet)
# %%
