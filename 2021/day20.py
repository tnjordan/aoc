#%%
import pandas as pd
import numpy as np
import copy

f = open('data/day20_input.txt', 'r')
read_lines = f.readlines()
f.close()

algo = read_lines[0]
algo = algo.strip()

data = read_lines[2:]

k2 = []
for l in data:
    l = l.strip()
    l = list(l)
    l = list(map(lambda x: x.replace('.', '0'), l))
    l = list(map(lambda x: x.replace('#', '1'), l))
    #l = l.append(['0','0','0'])
    k2.append(l)
img = np.array(k2)

def padding(img, pad_char):
    ''' Pads with the infinite void '''
    # pad_char alternates
    new_c = [pad_char]*len(img)
    #img = np.c_[new_c, new_c, new_c,  new_c, new_c, img, new_c, new_c, new_c, new_c, new_c]
    img = np.c_[new_c,  new_c, new_c, img, new_c, new_c, new_c]
    #img = np.c_[new_c, new_c, img, new_c, new_c]
    new_r = [pad_char]*len(img[0])
    img = np.insert(img, 0, np.array(new_r), 0)
    img = np.insert(img, 0, np.array(new_r), 0)
    img = np.insert(img, 0, np.array(new_r), 0)
    # img = np.insert(img, 0, np.array(new_r), 0)
    # img = np.insert(img, 0, np.array(new_r), 0)
    img = np.insert(img, len(img), np.array(new_r), 0)
    img = np.insert(img, len(img), np.array(new_r), 0)
    img = np.insert(img, len(img), np.array(new_r), 0)
    # img = np.insert(img, len(img), np.array(new_r), 0)
    # img = np.insert(img, len(img), np.array(new_r), 0)
    return img

def infinite_fix(img):
    ''' removes the border, this fixes the infinite on issue of odd states '''
    #print(len(img),'x',len(img[0]))
    img = img[1:len(img)-1,1:len(img[0])-1]
    #print(len(img),'x',len(img[0]))
    return img

def enhance(img):
    new_img = copy.deepcopy(img)
    #new_img = np.full((len(img),len(img[0])), fill_value = '0')
    for r in range(1,len(img)-1):
        for c in range(1,len(img[0])-1):
            bin_string = ''
            for i in [-1,0,1]:
                for j in [-1,0,1]:
                    # print(f"r:{r} c:{c} i:{i} j:{j} [r+i]:{r+i} [c+j]:{c+j} img[r+i][c+j]:{img[r+i][c+j]}")
                    bin_string += img[r+i][c+j]
                    # print(f'bin_string: {bin_string}')
            algo_position = int(bin_string,2)
            # print(bin_string, algo_position)
            algo_character = algo[algo_position]
            if algo_character == '.':
                algo_character = '0'
            elif algo_character == '#':
                algo_character = '1'
            new_img[r][c] = algo_character
    return new_img

#! Part 1 
# in this case the padding is always zero. Algo[0] is a .
print((img=='1').sum())
img = padding(img, '0')
new_img = enhance(img)
new_img2 = infinite_fix(new_img)
print((new_img2=='1').sum())
img = padding(new_img2, '0')
new_img = enhance(img)
new_img2 = infinite_fix(new_img)
print((new_img2=='1').sum())

#%%
#! Part 2
def enhance_pad_fix(img, pad_char):
    img = padding(img, pad_char)
    new_img = enhance(img)
    new_img2 = infinite_fix(new_img)
    return new_img2

# reset img
img = np.array(k2)

if algo[0] == '#':
    pad_alternate = True
else:
    pad_alternate = False

for i in range(50):
    if pad_alternate is True:
        if i %2 == 0:
            pad_char = '0'
        else:
            pad_char = '1'
    else:
        pad_char = '0' 
    img = enhance_pad_fix(img, pad_char)
print((img=='1').sum())  
#%%
img[img == '0'] = '.'
img[img == '1'] = '#'

new_img[new_img == '0'] = '.'
new_img[new_img == '1'] = '#'
# %%




#%%
#! FUKING SHIT! THIS WORKS FOR THE DEMO BUT THE ASS BUT A # FOR POSITION 0!

# def padding(img):
#     new_c = ['0']*len(img)
#     #img = np.c_[new_c, new_c, new_c,  new_c, new_c, img, new_c, new_c, new_c, new_c, new_c]
#     #img = np.c_[new_c,  new_c, new_c, img, new_c, new_c, new_c]
#     img = np.c_[new_c, new_c, img, new_c, new_c]
#     new_r = ['0']*len(img[0])
#     img = np.insert(img, 0, np.array(new_r), 0)
#     img = np.insert(img, 0, np.array(new_r), 0)
#     # img = np.insert(img, 0, np.array(new_r), 0)
#     # img = np.insert(img, 0, np.array(new_r), 0)
#     # img = np.insert(img, 0, np.array(new_r), 0)
#     img = np.insert(img, len(img), np.array(new_r), 0)
#     img = np.insert(img, len(img), np.array(new_r), 0)
#     # img = np.insert(img, len(img), np.array(new_r), 0)
#     # img = np.insert(img, len(img), np.array(new_r), 0)
#     # img = np.insert(img, len(img), np.array(new_r), 0)
#     return img

# def enhance(img):
#     new_img = copy.deepcopy(img)
#     #new_img = np.full((len(img),len(img[0])), fill_value = '0')
#     for r in range(1,len(img)-1):
#         for c in range(1,len(img[0])-1):
#             bin_string = ''
#             for i in [-1,0,1]:
#                 for j in [-1,0,1]:
#                     # print(f"r:{r} c:{c} i:{i} j:{j} [r+i]:{r+i} [c+j]:{c+j} img[r+i][c+j]:{img[r+i][c+j]}")
#                     bin_string += img[r+i][c+j]
#                     # print(f'bin_string: {bin_string}')
#             algo_position = int(bin_string,2)
#             # print(bin_string, algo_position)
#             algo_character = algo[algo_position]
#             if algo_character == '.':
#                 algo_character = '0'
#             elif algo_character == '#':
#                 algo_character = '1'
#             new_img[r][c] = algo_character
#     return new_img

# img = padding(img)
# new_img = enhance(img)
# print((new_img=='1').sum())
# img = padding(new_img)
# new_img = enhance(img)
# print((new_img=='1').sum())
# #%%
# img[img == '0'] = '.'
# img[img == '1'] = '#'

# new_img[new_img == '0'] = '.'
# new_img[new_img == '1'] = '#'
# # %%
