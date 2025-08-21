#%%
import hashlib

f = 'data/day05.txt'

with open(file=f) as input:
    read_lines = input.readlines()
read_lines = [li.strip() for li in read_lines]
print('🎅 🎄 🤶')
#%%
door_id = read_lines[0]
# door_id = 'abc'

password = ''
int_idx = 0
while len(password) < 8:
    idx = door_id + str(int_idx)
    md5_hash = hashlib.md5(idx.encode('utf-8'))
    hashed = md5_hash.hexdigest()
    if hashed[:5] == '00000':
        print(f'idx: {idx} \thashed: {hashed}')
        password += hashed[5]  # 6th character
        print(f'password: {password}')
    int_idx += 1

print(f'🐰 password: {password}')

#%%
#! part 2

password = ['_'] * 8
int_idx = 0
while '_' in password:
    idx = door_id + str(int_idx)
    md5_hash = hashlib.md5(idx.encode('utf-8'))
    hashed = md5_hash.hexdigest()
    if hashed[:5] == '00000':
        print(f'idx: {idx} \thashed: {hashed}')
        password_idx = hashed[5]  # 6th character
        if password_idx.isdecimal() and int(password_idx) < 8:
            password_idx = int(password_idx)
            if password[password_idx] == '_':
                password[password_idx] = hashed[6]  # 7th character
        print(f'password: {password}')
    int_idx += 1

print(f'🐰 password: {"".join(password)}')

#%%
print()
print('⭐ ⭐')
