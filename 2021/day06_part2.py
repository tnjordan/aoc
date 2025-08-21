#%%
import pandas as pd
import math


fish_df = pd.read_csv(r'data/day6_input.csv', header=None)
fish_df = fish_df.transpose()

# %%
#* receives a new fish on day 8 and calculated how many children in the avaliable days
def generation_generator(run_days, fish_count, new_fish):
    #print('function called with:',run_days, fish_count, new_fish)
    #* if we have a new fish delay reproducting
    if new_fish == True:
        if run_days >= 9:
            #* make new fish
            fish_count = generation_generator(run_days - 9, fish_count + 1, new_fish= True)[1]
            #* call existing fish
            fish_count = generation_generator(run_days - 9, fish_count, new_fish= False)[1]           
        else:
            return 0, fish_count, False
    elif new_fish == False:
        #* call out 
        if run_days >= 7:
            #* make new fish
            fish_count = generation_generator(run_days - 7, fish_count + 1, new_fish= True)[1]
            #* call existing fish
            fish_count = generation_generator(run_days - 7, fish_count, new_fish= False)[1]
        else:
            return 0, fish_count, False
    else:
        print('oh no!')
    return 0, fish_count, False

#%%
fish_list = fish_df[0]
total_fish = 0
run_days = 256
count = 0
for fish in fish_list:
    count += 1
    print (count, 'of', len(fish_list) )
    # count current fish
    total_fish += 1
    # offset days to start each fish at 8 on day zero
    fish_days_offset = 8 - fish
    #* calculate how many children of starting fish
    total_fish = generation_generator(run_days + fish_days_offset, total_fish, new_fish= True)[1]
print(total_fish)




# %%
#print(generation_generator(18, 1, True)[1])
# %%
