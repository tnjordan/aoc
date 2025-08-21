#%%
import re
from collections import Counter

f = 'data/day04.txt'

with open(file=f) as input:
    read_lines = input.readlines()
read_lines = [li.strip() for li in read_lines]
print('🎅 🎄 🤶')
#%%
sector_sum = 0
real_rooms = []
for line in read_lines:
    name, check_sum_check = line.split('[')
    check_sum_check = check_sum_check[:-1]

    letters = re.findall(r'[a-z]', name)
    letters = ''.join(letters)

    digits = re.findall(r'\d+', name)
    digits = int(digits[0])

    letter_counts = Counter(letters)
    sorted_letters = sorted(letter_counts.items(), key=lambda item: (-item[1], item[0]))

    check_sum = [sl[0] for sl in sorted_letters[:5]]

    if check_sum == list(check_sum_check):
        sector_sum += digits
        real_rooms.append((name, digits))

print(f'Sector ID Sum: {sector_sum}')

#%%
#! part 2


def decrypt(letter, shift):
    a_ord = ord('a')
    letter_digit = ord(letter) - a_ord
    shift_digit = (letter_digit + shift) % 26 + a_ord
    return chr(shift_digit)


for room in real_rooms:
    name, shift = room
    decrypt_name = ''
    for character in name:
        if character == '-':
            new_character = ' '
        elif character.isalpha():
            new_character = decrypt(character, shift)
        else:
            new_character = character
        decrypt_name += new_character

    if 'north' in decrypt_name:
        print(f'{decrypt_name}')


#%%
print()
print('⭐ ⭐')
