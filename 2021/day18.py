#%%
import json
f = open('data\day18_input copy.txt', 'r')
read_lines = f.readlines()
f.close()

def list_digger(l,address = [],depth = 0):
    
    for i,x in enumerate(l):
        if type(x) is list:
            depth += 1
            address = address + [i]
            print('i,x',i,x,'depth',depth, 'address',address)
            #* if depth is at set level exit this shit
            if depth == 4:
                print("LEVEL 4 BREACH")
                print('address, depth',address,depth)
                return address, depth
            #* else keep digging
            else:
                list_digger(x,address,depth)
    #* should only return on no answer
    #TODO FUCK THIS SHIT!
    #return address, depth

def snailfish_reduction(l):
    reduced = False
    #* check for 4 pair nesting
    list_digger(l)

    #* check for any

    #* if reduction action was performed check for chain reactions
    #if reduced is False:
    #    snailfish_reduction(l)

answer = []
for l in read_lines:
    l = l.strip()
    l = json.loads(l)
    #* add lines
    answer = answer + [l]
    
    #l = snailfish_reduction(answer)
list_digger(answer)
# %%
