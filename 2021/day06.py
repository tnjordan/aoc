#%%
import pandas as pd
import math
#%%
fish_df = pd.read_csv(r'data/day6_example_input copy.csv', header=None)
fish_df = fish_df.transpose()
#! Part 1 
days = 0
while days < 44:
    #print(days)
    # Increment fish reproduction day
    fish_df[0] = fish_df[0] - 1
    days += 1
    # check for reproducting fish that just reproduced (they were at zero now at -1)
    zero_fish = len(fish_df[fish_df[0] == -1])
    if zero_fish > 0:
        # make the baby fish 
        new_fish = [8]*zero_fish
        # add the baby fish
        fish_df = fish_df.append(new_fish)
        # reset parent fish
        fish_df[fish_df[0] == -1] = 6
    print(fish_df)
print(len(fish_df))
# %%
#! Part 2, don't run part 1 with 256 days
fish_df = pd.read_csv(r'data/day6_example_input copy.csv', header=None)
fish_df = fish_df.transpose()
#%%
fish_list = fish_df[0]
total_fish = 0
run_days = 44
for fish in fish_list:
    print(fish)
    # count current fish
    total_fish += 1
    # offset days to start each fish at 6
    fish_days_offset = 6 - fish
    #TODO multiply 6,8 fish
    #* calculate how many children of starting fish
    generations = math.floor((run_days + fish_days_offset)/7)
    print('total_fish',total_fish)
    for i in range(0,generations+1):
        print('generations', generations)
        # count child
        total_fish += 1
        #each child is going to have this many children
        children = math.floor((run_days - (7*i +2))/7)
        total_fish += children




# %%
