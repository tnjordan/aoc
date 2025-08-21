#%%
import pandas as pd
directions_df = pd.read_csv(r'data/day2_input.csv', header=None)

# %% #! Part 1
direction_sums_df = directions_df.groupby([0])[1].sum()
depth = direction_sums_df["down"] -  direction_sums_df["up"]
horizontal = direction_sums_df["forward"]

answer1 = depth * horizontal
# %% #! Part 2
directions_df = pd.read_csv(r'data/day2_input.csv', header=None)

depth = 0
horizontal = 0
aim = 0

for index, row in directions_df.iterrows():
    if row[0] == "down":
        aim += row[1]
    elif row[0] == "up":
        aim -= row[1]
    elif row[0] == "forward":
        horizontal += row[1]
        depth += row[1] * aim

answer2 = depth * horizontal

# %%
