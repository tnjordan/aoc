
#%%
import pandas as pd
sonar_df = pd.read_csv(r'data/sonar_data.csv')
#%% #! Part1
"""sonar_df["Slope"] = "no_change"
last_depth = sonar_df["Depth"][0]

for i,depth in enumerate(sonar_df["Depth"]):
    print(i, depth)
    delta_depth = depth - last_depth
    if delta_depth > 0:
        sonar_df["Slope"][i] = "increased"
    elif delta_depth < 0:
        sonar_df["Slope"][i] = "decreased"
    else:
        print("for Dan")
    last_depth = depth
sonar_df_summary = sonar_df.groupby(by="Slope").count()
print(sonar_df_summary.head())"""

sonar_df["LastDepth"] = sonar_df["Depth"].shift(1)

sonar_df["DeltaDepth"] = sonar_df["Depth"] - sonar_df["LastDepth"]
sonar_df.loc[sonar_df["DeltaDepth"] > 0, "Slope"] = "increased"
sonar_df.loc[sonar_df["DeltaDepth"] < 0, "Slope"] = "decreased"
sonar_df.loc[sonar_df["DeltaDepth"] == 0, "Slope"] = "no_change"

sonar_df_summary = sonar_df.groupby(by="Slope").count()

print(sonar_df_summary["DeltaDepth"].head())

# %% #! Part2
sonar_df = pd.read_csv(r'data/sonar_data.csv')
sonar_df["LastDepth_1"] = sonar_df["Depth"].shift(1)
sonar_df["LastDepth_2"] = sonar_df["Depth"].shift(2)

sonar_df["Window"] = sonar_df["Depth"] + sonar_df["LastDepth_1"] + sonar_df["LastDepth_2"]
sonar_df["LastWindow"] = sonar_df["Window"].shift(1)

sonar_df["DeltaDepth"] = sonar_df["Window"] - sonar_df["LastWindow"]
sonar_df.loc[sonar_df["DeltaDepth"] > 0, "Slope"] = "increased"
sonar_df.loc[sonar_df["DeltaDepth"] < 0, "Slope"] = "decreased"
sonar_df.loc[sonar_df["DeltaDepth"] == 0, "Slope"] = "no_change"

sonar_df_summary = sonar_df.groupby(by="Slope").count()

print(sonar_df_summary["DeltaDepth"].head())
# %%
