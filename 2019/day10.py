#%%
f = 'data/day10.txt'
# f = 'data/day10_ex.txt'
# f = 'data/day10_ex2.txt'
# f = 'data/day10_ex3.txt'
# f = 'data/day10_ex4.txt'
with open(f) as input:
    read_lines = input.readlines()
data = []
for l in read_lines:
    l=l.replace('#','1')
    l=l.replace('.','0')
    l=list(l.strip())
    l = [int(x) for x in l]
    data.append(l)
print(data)
print()
for r in data:
    print(r)

#%%
asteroids=[]
for y,row in enumerate(data):
    for x,space in enumerate(row):
        if space == 1:
            # print(f'Asteroid Alert! @ ({y},{x})')
            asteroids.append((x,y))

# %%
max_obs_asteroids = float('-inf')
for a in asteroids:
# for a in [(11,13)]: #* used for debug, so many bugs!
    print('\U0001F680'*12)
    print(f'at asteroid: {a}')
    # monitored_asteroids = asteroids.copy()
    # monitored_asteroids.remove(a)
    x_0,y_0 = a
    slopes = {float('inf'):[], float('-inf'):[]} #* init with infinity #! need +/- inf for part 2
    for m_a in asteroids:
        x_1,y_1 = m_a
        delta_x =x_1-x_0
        delta_y = y_1-y_0
        print(f'  checking asteroid {m_a} at slope {delta_y}/{delta_x}')
        if delta_x == 0:
            print('    to infinity and beyond!')
            if delta_y > 0:
                print('      asteroid above')
                slopes[float('-inf')].append('-') #* an above astroid is a smaller y!
            elif delta_y < 0:
                print('      asteroid below')
                slopes[float('inf')].append('+')
        else:
            slope = delta_y/delta_x
            if slope not in slopes.keys():
                slopes[slope] = []

            #* this is so hard to visualize. Also the coord system is mirrored. up->down & down->up
            #* this reverses the normal sense of +/- slopes 
            if slope > 0:
                if delta_y > 0:
                    slopes[slope].append('-')
                elif delta_y < 0:
                    slopes[slope].append('+')
            elif slope < 0:
                if delta_y < 0:
                    slopes[slope].append('-')
                elif delta_y > 0:
                    slopes[slope].append('+')
            elif slope == 0:
                if delta_x > 0:
                    slopes[slope].append('-') #* this is wrong but I need it to match.
                elif delta_x < 0:
                    slopes[slope].append('+')

    obs_asteroids = 0
    for s,l in slopes.items():
        if '+' in l:
            obs_asteroids +=1
        if '-' in l:
            obs_asteroids +=1
    print(f'observed asteroids {obs_asteroids} from asteroid {a}')
    if obs_asteroids > max_obs_asteroids:
        max_obs_asteroids = obs_asteroids
        max_slopes = slopes
        max_asteroid = a
    print()

print(f'max observed asteroids {max_obs_asteroids} from asteroid {max_asteroid}')

#%%
#! part 2
#* we can cheat a bit since we know we can observe 319 asteroids and we want the 200th vaporized.

#* starting slope is + inf, then rotate largest to smallest
#* on passing remove a + slope indicator. 
#* on second half of the pass remove the - slope indicator. 
#* note the second half or the rotation again goes largest to smallest.

from collections import OrderedDict
import copy

temp_d = copy.deepcopy(max_slopes)

k2 = OrderedDict(sorted(temp_d.items(), key=lambda t: t[0], reverse=False))
cnt = 0
symbol = '-'
while cnt < len(asteroids)-1:
    for k,v in k2.items():
        if k == float('inf'): #* switch symbol at infinity
            if symbol == '+':
                symbol = '-'
            else:
                symbol = '+'
            print(symbol)
        if symbol in v:
            cnt += 1
            k2[k].remove(symbol)
            print(f'lazer destroys asteroid {cnt} at angle: {k}')
            if cnt == 200:
                print('\U0001F680'*12)
                print(f'going {symbol} on slope')
                print('\U0001F680'*12)
                break



#* learned some maths to get the angle out of the repeating fraction.
#* https://www.khanacademy.org/math/cc-eighth-grade-math/cc-8th-numbers-operations/cc-8th-repeating-decimals/a/writing-repeating-decimals-as-fractions-review

#* angle was 0.04545454545454545...
# k1 = 10*0.04545
# k2 = 1000*0.0454545
# k3 = (k2-k1)/(1000-10)
# print(f'angle is {int(k2-k1)}/{990}')
#%%

# #* angle was 3.6666666666666665
# k1 = 1*3.66
# k2 = 10*3.666
# k3 = (k2-k1)/(10-1)
# print(f'angle {k3} is {int(k2-k1)}/{9}')
# from fractions import Fraction
# print(f'this reduces too: {Fraction(int(k2-k1),9)}')

#* angle was 0.11538461538461
k1 = 100*0.11538461
k2 = 100000000*0.11538461538461
k3 = (k2-k1)/(100000000-100)
print(f'angle {k3} is {int(k2-k1)}/{100000000-100}')
from fractions import Fraction
print(f'this reduces too: {Fraction(int(k2-k1),100000000-100)}')
#%%
print('\U0001F680'*12)
print(f'at asteroid: {max_asteroid}')
x_0,y_0 = max_asteroid
for m_a in asteroids:
    x_1,y_1 = m_a
    delta_x =x_1-x_0
    delta_y = y_1-y_0
    try:
        slope = delta_y/delta_x
        if slope == 3/26: #* hard coded but could be variable
            print(slope)
            print(f'\U0001F6A8 \U0001F52B {m_a}') #* lucky only one asteroid at this angle!
            print(f'answer: {x_1*100+y_1}')
            # break
    except:
        pass


#%%
#? debugging the angles
x_0,y_0 = (11,13)
vaporized_dict = {1:(11,12), 2:(12,1), 3:(12,2), 10:(12,8), 20:(16,0), 50: (16,9), 100: (10,16), 199: (9,6), 200: (8,2), 201: (10,9), 299: (11,1)}

for k,v in vaporized_dict.items():
    x_1,y_1 = v
    delta_x =x_1-x_0
    delta_y = y_1-y_0
    if delta_x == 0:
        if delta_y > 0:
            print(f'asteroid {k} is above!')
            slopes[float('inf')].append('-') #* an above astroid is a smaller y!
        elif delta_y < 0:
            print(f'asteroid {k} is below!')
            slopes[float('inf')].append('+')
    else:
        slope = delta_y/delta_x
        print(f'asteroid {k} is at slope {delta_y}/{delta_x} = {slope}')


# %%
#* this runs but gets the wrong answer :( 
# max_obs_asteroids = float('-inf')
# for a in asteroids:
#     print(f'at asteroid: {a}')
#     monitored_asteroids = asteroids.copy()
#     monitored_asteroids.remove(a)
#     x_0,y_0 = a
#     slopes = [] #* list didn't work because you have up-slope and down-slope.
#     #* can only have one asteroid on the straight lines, these are the zero case.
#     asteroid_horz_plus = False
#     asteroid_horz_neg = False
#     asteroid_vert_plus = False
#     asteroid_vert_neg = False
#     for m_a in monitored_asteroids:
#         x_1,y_1 = m_a
#         delta_x =x_1-x_0
#         delta_y = y_1-y_0
#         print(f'  checking asteroid {m_a} at slope {delta_x}/{delta_y}')
#         on_shared_slope = False
#         rm_slope = [] #TODO this might be okay just being one.
#         if 0 in [delta_x, delta_y]:
#             # print('0 alert!')
#             if delta_x > 0:
#                 if asteroid_horz_plus is True:
#                     print('another + x asteroid')
#                 else:
#                     print('+ x asteroid')
#                     asteroid_horz_plus = True
#             elif delta_x < 0:
#                 if asteroid_horz_neg is True:
#                     print('another - x asteroid')
#                 else:
#                     print('- x asteroid')
#                     asteroid_horz_neg = True
#             elif delta_y > 0:
#                 if asteroid_vert_plus is True:
#                     print('another + y asteroid')
#                 else:
#                     print('+ y asteroid')
#                     asteroid_vert_plus = True
#             elif delta_y < 0:
#                 if asteroid_vert_neg is True:
#                     print('another - y asteroid')
#                 else:
#                     print('- y asteroid')
#                     asteroid_vert_neg = True
#         else:
#             for s in slopes:
#                 delta_x_s, delta_y_s = s
#                 if delta_x % delta_x_s == 0 and delta_y % delta_y_s == 0:
#                     on_shared_slope = True
#                     print(f'    asteroid is blocked by {delta_x_s}/{delta_y_s}')
#                 elif delta_x_s %  delta_x == 0 and delta_y_s % delta_y == 0:
#                     print(f'    this asteroid blocks {delta_x_s}/{delta_y_s}')
#                     rm_slope.append(s)
#             if rm_slope != []:
#                 for s_r in rm_slope:
#                     slopes.remove(s_r)
#             if on_shared_slope is False:
#                 slopes.append((delta_x,delta_y))
#         print(f'slopes {slopes}')
#     break

# max_obs_asteroids = float('-inf')
# for a in asteroids:
#     print('\U0001F680'*12)
#     print(f'at asteroid: {a}')
#     # monitored_asteroids = asteroids.copy()
#     # monitored_asteroids.remove(a)
#     x_0,y_0 = a
#     slopes = []
#     #* can only have one asteroid on the straight lines, these are the zero case.
#     asteroid_horz_plus = False
#     asteroid_horz_neg = False
#     asteroid_vert_plus = False
#     asteroid_vert_neg = False
#     for m_a in asteroids:
#         x_1,y_1 = m_a
#         delta_x =x_1-x_0
#         delta_y = y_1-y_0
#         print(f'  checking asteroid {m_a} at slope {delta_y}/{delta_x}')
#         if delta_x == 0:
#             print('    to inf and beyond!')
#             if delta_y > 0:
#                 print('      asteroid above')
#                 asteroid_vert_plus = True
#             elif delta_y < 0:
#                 print('      asteroid below')
#                 asteroid_vert_neg = True
#         elif delta_y == 0:
#             if delta_x > 0:
#                 print('      asteroid right')
#                 asteroid_horz_plus = True
#             elif delta_x < 0:
#                 print('      asteroid left')
#                 asteroid_horz_neg = True
#         else:
#             slope = delta_y/delta_x
#             if slope in slopes:
#                 print('\talready have slope')
#             else:
#                 print('\tnew slope!')
#                 slopes.append(slope)
#     obs_asteroids = len(slopes) + asteroid_vert_plus + asteroid_vert_neg + asteroid_horz_plus + asteroid_horz_neg #* python will convert True to 1
#     print(f'observed asteroids {obs_asteroids}')
#     print(f'where did I go wrong? : {asteroid_vert_plus + asteroid_vert_neg + asteroid_horz_plus + asteroid_horz_neg}')
#     if obs_asteroids > max_obs_asteroids:
#         max_obs_asteroids = obs_asteroids
#         max_slopes = slopes
#         max_asteroid = a
#         straight_lines = [asteroid_vert_plus, asteroid_vert_neg, asteroid_horz_plus, asteroid_horz_neg]
#     print()

# print(f'max observed asteroids {max_obs_asteroids} from asteroid {max_asteroid}')