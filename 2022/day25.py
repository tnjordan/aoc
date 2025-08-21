#%%
f = 'data/day25.txt'
# f = 'data/day25.ex'

with open(file=f) as input:
    read_lines = input.readlines()
read_lines = [l.strip() for l in read_lines]
print('🎅 🎄 🤶')

def SNAFU_to_dec(snafu):
    dec = 0
    snafu = snafu[::-1]
    power_5 = 0
    for c in snafu:
        if c == '=':
            dec += (-2)*5**power_5
        elif c == '-':
            dec += (-1)*5**power_5
        else:
            dec += int(c)*5**power_5
        power_5 += 1
    return dec

dec_sum = 0
for l in read_lines:
    dec_sum += SNAFU_to_dec(l)

def d_to_S(snafu,i):
    prev_c = snafu[i-1]
    if prev_c == '=':
        prev_c = '-'
    elif prev_c == '-':
        prev_c = '0'
    else:
        prev_c = str(int(prev_c)+1)
    if prev_c in '-012':
        snafu[i-1] = prev_c
    else:
        if prev_c == '3':
            prev_c = '='
        elif prev_c == '4':
            prev_c = '-'
        snafu[i-1] = prev_c
        snafu = d_to_S(snafu,i-1)
        
    return snafu

def dec_to_SNAFU(dec):
    snafu = []
    power_5 = 24
    for i,pw_5 in enumerate(range(power_5,-1,-1)):
        if dec // 5**pw_5 == 0:
            snafu.append('0')
            dec -= 0*5**pw_5
        elif dec // 5**pw_5 == 1:
            snafu.append('1')
            dec -= 1*5**pw_5
        elif dec // 5**pw_5 == 2:
            snafu.append('2')
            dec -= 2*5**pw_5
        elif dec // 5**pw_5 == 3:
            snafu.append('=')
            dec -= 3*5**pw_5
            snafu = d_to_S(snafu,i)
        elif dec // 5**pw_5 == 4:
            snafu.append('-')
            dec -= 4*5**pw_5
            snafu = d_to_S(snafu,i)
    snafu = "".join(snafu)
    return snafu

print(f'{dec_sum} is a SNAFU {dec_to_SNAFU(dec_sum).lstrip("0")}')
#%%
print()
print('⭐')