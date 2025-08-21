#%%
import re

f = 'data/day07.txt'

with open(file=f) as input:
    read_lines = input.readlines()
read_lines = [li.strip() for li in read_lines]
print('🎅 🎄 🤶')
#%%

hypernet_regex = r'(\[[a-z]*\])'


def abba(seq: str):
    if not len(seq) >= 4:
        return False
    for i in range(len(seq) - 3):
        xxxx = seq[i:i + 4]  # xxxx is 4 characters
        if '[' in xxxx or ']' in xxxx:
            continue
        if xxxx[0] == xxxx[3] and xxxx[1] == xxxx[2] and xxxx[0] != xxxx[1]:
            return True
    return False


tls_ip_count = 0
for line in read_lines:
    hypernet_sequences = re.findall(hypernet_regex, line)
    for hyper_seq in hypernet_sequences:
        abba_status = abba(hyper_seq)
        if abba_status:
            break
    else:
        abba_status = abba(line)
        if abba_status:
            tls_ip_count += 1

print(f'transport-layer snooping of 🐰 on {tls_ip_count} IPv7 addresses.')

#%%
#! part 2


def ssl(ipv7: str):
    hypernet_sequences = re.findall(hypernet_regex, ipv7)
    # check for aba
    in_hyper = False
    for i, c in enumerate(ipv7[:-2]):
        if c == '[':
            in_hyper = True
            continue
        elif c == ']':
            in_hyper = False
            continue
        if not in_hyper:
            xxx = ipv7[i:i + 3]
            if xxx[0] == xxx[2] and xxx[0] != xxx[1]:
                for hyper_seq in hypernet_sequences:
                    if xxx[1] + xxx[0] + xxx[1] in hyper_seq:
                        return True
    return False


ssl_ip_count = 0
for line in read_lines:
    if ssl(ipv7=line):
        ssl_ip_count += 1

print(f'super-secret listening of 🐰 on {ssl_ip_count} IPv7 addresses.')

#%%
print()
print('⭐ ⭐')
