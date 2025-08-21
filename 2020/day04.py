#%%
input = open('data/day4.txt')
read_lines = input.readlines()

byr = False
iyr = False
eyr = False
hgt = False
hcl = False
ecl = False
pid = False
cid = False

valid = 0
passport = ''
for l in read_lines:
    if l == '\n':
        if 'byr:' in passport:
            byr = True
        if 'iyr:' in passport:
            iyr = True
        if 'eyr:' in passport:
            eyr = True
        if 'hgt:' in passport:
            hgt = True
        if 'hcl:' in passport:
            hcl = True
        if 'ecl:' in passport:
            ecl = True
        if 'pid:' in passport:
            pid = True
        if 'cid:' in passport:
            cid = True
        if byr and iyr and eyr and hgt and hcl and ecl and pid:
            valid += 1
            # print('valid, passport',passport)
        byr = False
        iyr = False
        eyr = False
        hgt = False
        hcl = False
        ecl = False
        pid = False
        cid = False
        passport = ''
    l = l.strip()
    l += ' '
    passport += l

print('part 1: ', valid)
# %%
#! Part 2

byr = False
iyr = False
eyr = False
hgt = False
hcl = False
ecl = False
pid = False
cid = False

valid_1 = 0
valid = 0
passport = ''
for l in read_lines:
    if l == '\n':
        if 'byr:' in passport:
            byr = True
        if 'iyr:' in passport:
            iyr = True
        if 'eyr:' in passport:
            eyr = True
        if 'hgt:' in passport:
            hgt = True
        if 'hcl:' in passport:
            hcl = True
        if 'ecl:' in passport:
            ecl = True
        if 'pid:' in passport:
            pid = True
        if 'cid:' in passport:
            cid = True
        if byr and iyr and eyr and hgt and hcl and ecl and pid:
            valid_1 += 1
            # make a dictionary
            passport = passport.strip()
            passport_d = passport.replace(' ','\',\'')
            passport_d = passport_d.replace(':', '\':\'')
            passport_d = "{\'" + passport_d + "\'}"
            passport_d = eval(passport_d)
            if int(passport_d['byr']) >= 1920 and int(passport_d['byr']) <= 2002:
                if int(passport_d['iyr']) >= 2010 and int(passport_d['iyr']) <= 2020:
                    if int(passport_d['eyr']) >= 2020 and int(passport_d['eyr']) <= 2030:
                        if passport_d['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                            if len(passport_d['pid']) == 9:
                                if all([True if i in ['0','1','2','3','4','5','6','7','8','9'] else False for i in passport_d['pid']]):
                                    if passport_d['hcl'][0] == '#':
                                        if all([True if i in ['0','1','2','3','4','5','6','7','8','9', 'a', 'b', 'c', 'd', 'e', 'f'] else False for i in passport_d['hcl'][1:]]):
                                            if passport_d['hgt'][-2:] == 'cm':
                                                if int(passport_d['hgt'][:-2]) >= 150 and int(passport_d['hgt'][:-2]) <= 193:
                                                    valid += 1
                                            elif passport_d['hgt'][-2:] == 'in':
                                                if int(passport_d['hgt'][:-2]) >= 59 and int(passport_d['hgt'][:-2]) <= 76:
                                                    valid += 1
        byr = False
        iyr = False
        eyr = False
        hgt = False
        hcl = False
        ecl = False
        pid = False
        cid = False
        passport = ''
    l = l.strip()
    l += ' '
    passport += l

print('part 1: ', valid_1)
print('part 2: ', valid)
# %%
