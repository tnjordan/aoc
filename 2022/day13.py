#%%
from copy import deepcopy
f = 'data/day13.txt'
# f = 'data/day13.ex' #* wanted to debug, but my first left is []

with open(file=f) as input:
    i = input.read() #* modified from standard
signal = i.split('\n\n') #* easier to split instructions
signal = [x.split('\n') for x in signal]

# def check_empty(l):
#     count = 0
#     while type(l) is list:
#         try:
#             count += 1
#             l=l[0]
#         except IndexError:
#             return count
#     return False

# def double_empty_check(left,right):
#     left_empty = check_empty(left)
#     right_empty = check_empty(right)
#     if left_empty and right_empty:
#         if left_empty <= right_empty:
#             return True #* pass. Right has more or equal empty brackets
#         else:
#             return False #* fail. Left has more empty brackets
#     elif left_empty:
#         return True #* left is empty, right is not
#     elif right_empty:
#         return False #* right is empty, left if not
#     else:
#         return 'full' #* no empty

def the_decider(left, right): #* turned to function because of nested loops.
    left = deepcopy(left) #* deep copy needed for part 2
    right = deepcopy(right)
    print(f'left: {left}')
    print(f'right: {right}')
    for i in range(max(len(left),len(right))):
        if i == len(left):
            print('🐛')
            return 1 #* left has run out of items
        if i == len(right):
            print('🐝')
            return 0 #* right has run out of items
        
        # #* empty check prevents index out of bounds errors
        # if double_empty_check(left[i],right[i]) is True: #! ahh my first love betrayed me, she was not meant for the recursion
        #     print('🐞')
        #     return 1 #* right wins
        # elif double_empty_check(left[i],right[i]) is False:
        #     print('🐜')
        #     return 0 #* left wins
        
        #* integer check, round ends here (it used too)
        l_type = type(left[i])
        r_type = type(right[i])
        if l_type is int and r_type is int:
            print(f'{left[i]} v {right[i]}')
            if left[i] > right[i]:
                print('🕷')
                return 0
            elif left[i] < right[i]: #* missing logic
                print('🦋')
                return 1
        elif l_type is int:
            # if left[i] > right[i][0]: #* only compare first element
            #     return 0
            # else:
            #     return 1 #* right is >= left, left is out of elements
            left[i] = [left[i]]
            l_type = type(left[i]) #* was using a flag; however this required double calls to the_decider
        elif r_type is int:
            # if left[i][0] >= right[i]: #* note greater or equal as right has only one value
            #     return 0
            # else:
            #     return 1
            right[i] = [right[i]]
            r_type = type(right[i])
        if l_type is list and r_type is list:
            print('🦟')
            decision = the_decider(left[i], right[i])
            if decision != -1: #* -1 keep looking
                return decision
        # else: #* both lists, these could be nested per Pair 8 or example
        #     return the_decider(left[i], right[i])
    print('🦗')
    return -1 #* applies if all integers are equal, keep searching

index_sum = 0
for index, signal_pair in enumerate(signal, start=1):
    print()
    left = eval(signal_pair[0])
    right = eval(signal_pair[1])
    print('🤯 '*13)
    print(f'== Pair {index} ==')
    index_sum += the_decider(left, right) * index
    print(f'index_sum: {index_sum}')
    print()
print(f'index_sum: {index_sum}')

#%%
#! part 2
#* sort all lines but add [[2]] and [[6]]

#* step 1 remove all lines that are greater than [[6]] these are not needed
signals = []
for index, signal_pair in enumerate(signal, start=1):
    print()
    left = eval(signal_pair[0])
    right = eval(signal_pair[1])
    print('🤯 '*13)
    print(f'== Pair {index} ==')
    for s in [left, right]:
        if the_decider(s, [[6]]) == 1:
            print('+1')
            signals.append(s)
signals.append([[2]])
signals.append([[6]])

#* code the sort
#* try bubble sort bc ... the internet says it is an easy sorting algo
def bubble_sorter_9000(signals):
    for i in range(len(signals)):
        for j in range(len(signals)-i-1):
            if the_decider(signals[j], signals[j+1]) == 0:
                signals[j], signals[j+1] = signals[j+1], signals[j]
    return signals

sorted_signals = bubble_sorter_9000(signals.copy())
print(f'decoder key: {(sorted_signals.index([[2]])+1) * (sorted_signals.index([[6]])+1)}')
#%%
print()
print('⭐ ⭐')