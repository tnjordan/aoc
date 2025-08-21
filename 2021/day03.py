
#%% #! Part1
fh = open('data/day3_input.txt')

read_lines = fh.readlines()
on_bits = [0] * 12

line_count = 0
for line in read_lines:
    line = line.strip()
    line_count += 1
    for i, char in enumerate(line):
        on_bits[i]+= int(char)
fh.close()

off_bits = [line_count]*12
for bit in range(len(off_bits)):
    off_bits[bit] = off_bits[bit] - on_bits[bit]


#%%

gamma_bits = [0]*12
epsilon_bits = [0]*12

for bit in range(len(off_bits)):
    if off_bits[bit] > on_bits[bit]:
        gamma_bits[bit] = 1
    else:
        epsilon_bits[bit] = 1

#%%
bin_gamma = ''.join(str(i) for i in gamma_bits)
bin_epsilon = ''.join(str(i) for i in epsilon_bits)
# %%
answer = int(bin_gamma, 2) * int(bin_epsilon, 2)
print(answer)

#%% #! Part2
#TODO

import pandas as pd
df = pd.read_csv('data/day3_input.txt', header = None, dtype=str)
col_list = [*range(0,len(df[0][0]))]
for c in col_list:
    col_list[c] = "bit_" + str(c)

df[0] = df[0].apply(lambda x: list(x))
bits_df = pd.DataFrame(df[0].to_list(), columns=col_list)

for c in col_list:
    bits_df[c] = bits_df[c].astype(int)

bits_oxy_df = bits_df.copy()
bits_co2_df = bits_df.copy()
#%%

bits_oxy_col = [0,0]
while bits_oxy_df.shape[0] > 1:
    for c in col_list:
        if bits_oxy_df.shape[0] > 1:
            bits_oxy_col[0] = bits_oxy_df[c][bits_oxy_df[c] == 0].count()
            bits_oxy_col[1] = bits_oxy_df[c][bits_oxy_df[c] == 1].count()
            if bits_oxy_col[0] > bits_oxy_col[1]:
                bits_oxy_df = bits_oxy_df[bits_oxy_df[c] == 0]
            elif bits_oxy_col[0] < bits_oxy_col[1]:
                bits_oxy_df = bits_oxy_df[bits_oxy_df[c] == 1]
            else:
                bits_oxy_df = bits_oxy_df[bits_oxy_df[c] == 1]

#%%
bits_co2_col = [0,0]
while bits_co2_df.shape[0] > 1:
    for c in col_list:
        if bits_co2_df.shape[0] > 1:
            bits_co2_col[0] = bits_co2_df[c][bits_co2_df[c] == 0].count()
            bits_co2_col[1] = bits_co2_df[c][bits_co2_df[c] == 1].count()
            if bits_co2_col[0] > bits_co2_col[1]:
                bits_co2_df = bits_co2_df[bits_co2_df[c] == 1]
            elif bits_co2_col[0] < bits_co2_col[1]:
                bits_co2_df = bits_co2_df[bits_co2_df[c] == 0]
            else:
                bits_co2_df = bits_co2_df[bits_co2_df[c] == 0]


bin_oxy = bits_oxy_df.to_string(header=False, index=False).replace(' ', '')
bin_co2 = bits_co2_df.to_string(header=False, index=False).replace(' ', '')
answer2 = int(bin_oxy, 2) * int(bin_co2, 2)
print(answer2)

# %%
