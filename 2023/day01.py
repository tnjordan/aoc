#%%
import re
f = 'data/day01.txt'
# f = 'data/day1.ex'

with open(file=f) as input:
    read_lines = input.readlines()
read_lines = [line.strip() for line in read_lines]
print('❄️⛄❄️')
#%%
numbers = { 
            'one': '1',
            'two': '2',
            'three': '3',
            'four': '4',
            'five': '5',
            'six': '6',
            'seven': '7',
            'eight': '8',
            'nine': '9'
            }

rev_numbers = {}
for k, v in numbers.items():
    rev_numbers[k[::-1]] = v

numbers = numbers | rev_numbers


def number_finder(line, rev):
    if rev:
        line = line[::-1]
    for i in range(len(line)):
        if line[i] in numbers.values():
            return line[i]
        else:
            for k, v in numbers.items():
                if k in line[i: i + len(k)]:
                    return v

part_1 = 0
part_2 = 0
for line in read_lines:
    right = number_finder(line, False)
    left = number_finder(line, True)
    part_2 += int(right + left)

    line = re.sub(r'[a-z]', '', line)
    part_1 += int(line[0] + line[-1])
print(part_1)
print(part_2)
#%%
print()
print('⭐⭐')

#%%
#* the first attempt, soo close
# all right except 855
# 🐳0
# 🐛gseightwo6
# 🐛gseigh26
# 🦋26 -> 26

import re
f = 'data/day01.txt'
# f = 'data/day1.ex'

with open(file=f) as input:
    read_lines = input.readlines()
read_lines = [line.strip() for line in read_lines]
print('❄️⛄❄️')

def deb_print(l,i,n):
    print(f'🐌{n}')
    a, b, c = l[0:i], l[i:i+n], l[i + n:]
    print(f'l[0:i]:{a}  l_prime:{b}  l[i + {n}:]:{c}')
    print(l == a + b + c)
    print()


x = 0
c = 0
arr2 = []
for l in read_lines: #[855:856]:
    print()
    print(f'🐳{c}')
    c += 1
    print(f'🐛{l}')
    i = 0
    while 'one' in l or 'two' in l or 'three' in l or 'four' in l or 'five' in l or 'six' in l or 'seven' in l or 'eight' in l or 'nine' in l:
        # print(i)
        while i < len(l):
            # print('🐛',i)
            #deb_print(l,i,n=3)
            l_prime = l[i:i+3]
            l_prime =l_prime.replace('one', '1')
            l_prime =l_prime.replace('two', '2')  # ahh twone
            l_prime = l_prime.replace('six', '6')
            if len(l) != len(l[0:i] + l_prime + l[i + 3:]):
                l = l[0:i] + l_prime + l[i + 3-1:]
                #deb_print(l,i,n=3)
                i += 0
                break
            #print('reverse -1');
            l = l[::-1]
            #deb_print(l,i,n=3)
            l_prime = l[i:i+3]
            l_prime =l_prime.replace('one'[::-1], '1')
            l_prime =l_prime.replace('two'[::-1], '2')  # ahh twone
            l_prime = l_prime.replace('six'[::-1], '6')
            if len(l) != len(l[0:i] + l_prime + l[i + 3:]):
                l = l[0:i] + l_prime + l[i + 3-1:]
                #deb_print(l,i,n=3)
                #print('reverse');
                l = l[::-1]
                # print('rev rep',l)
                i += 0
                break
            
            #print('reverse');
            l = l[::-1]
            l_prime = l[i:i+4]
            #deb_print(l,i,n=4)
            l_prime = l_prime.replace('five', '5')
            l_prime = l_prime.replace('four', '4')
            l_prime = l_prime.replace('nine', '9')
            if len(l) != len(l[0:i] + l_prime + l[i + 4:]):
                l = l[0:i] + l_prime + l[i + 4-1:]
                #deb_print(l,i,n=4)
                i += 0
                break
            #print('reverse -1');
            l = l[::-1]
            #deb_print(l,i,n=4)
            l_prime = l[i:i+4]
            l_prime = l_prime.replace('five'[::-1], '5')
            l_prime = l_prime.replace('four'[::-1], '4')
            l_prime = l_prime.replace('nine'[::-1], '9')
            if len(l) != len(l[0:i] + l_prime + l[i + 4:]):
                l = l[0:i] + l_prime + l[i + 4-1:]
                #print('reverse');
                l = l[::-1]
                #deb_print(l,i,n=4)
                # print('rev rep',l)
                i += 0
                break
            
            #print('reverse');
            l = l[::-1]
            #deb_print(l,i,n=5)
            l_prime = l[i:i+5]
            l_prime = l_prime.replace('three', '3')
            l_prime = l_prime.replace('seven', '7')
            l_prime = l_prime.replace('eight', '8')
            if len(l) != len(l[0:i] + l_prime + l[i + 5:]):
                l = l[0:i] + l_prime + l[i + 5-1:]
                i += 0
                break
            #print('reverse -1')
            l = l[::-1]
            l_prime = l[i:i+5]
            #deb_print(l,i,n=5)
            l_prime = l_prime.replace('three'[::-1], '3')
            l_prime = l_prime.replace('seven'[::-1], '7')
            l_prime = l_prime.replace('eight'[::-1], '8')
            if len(l) != len(l[0:i] + l_prime + l[i + 5:]):
                l = l[0:i] + l_prime + l[i + 5-1:]
                #print('reverse');
                l = l[::-1]
                i += 0
                break
            l = l[::-1]
            i += 1
    print(f'🐛{l}')
    l = re.sub(r'[a-z]','',l)
    print(f'🦋{l} -> {int(l[0]+l[-1])}')
    x += int(l[0]+l[-1])
    arr2.append(int(l[0]+l[-1]))
x
#%%
