#%%
#%%
f = open('data\day8_input.txt', 'r')
read_lines = f.readlines()
f.close()

# %%
#! Part1
cout_1478 = 0
for line in read_lines:
    input, output = line.split(' | ')
    input = input.strip()
    output = output.strip()
    output = output.split(' ')
    for out in output:
        len_out = len(out)
        if len_out == 2:
            print('1')
            cout_1478 += 1
        elif len_out == 4:
            print('4')
            cout_1478 += 1
        elif len_out == 3:
            print('7')
            cout_1478 += 1
        elif len_out == 7:
            print('8')
            cout_1478 += 1
# %%
#! Part2
answer = 0
for line in read_lines:
    input, output = line.split(' | ')
    input = input.strip()
    output = output.strip()
    input = input.split(' ')
    output = output.split(' ')
    input_dict = {"a":"","b":"","c":"","d":"","e":"","f":"","g":""}
    seg_count_dict = {"a":0,"b":0,"c":0,"d":0,"e":0,"f":0,"g":0}

    for i in input:
        #* count occurrences of each segment
        for c in i:
            seg_count_dict[c] += 1
        len_i = len(i)
        if len_i == 2:
            seven_seg_1 = i
        elif len_i == 4:
            seven_seg_4 = i
        elif len_i == 3:
            seven_seg_7 = i
        elif len_i == 7:
            seven_seg_8 = i

    #* a is what is in 7 but not in 1
    for c in seven_seg_7:
        if c not in seven_seg_1:
            input_dict['a'] = c
    #* use counts of each segment to get e, b and f.
    #* c is the other 8 count that isn't 'a' which is known from 1 vs 7
    for d in seg_count_dict:
        if seg_count_dict[d] == 4:
            input_dict['e'] = d
        elif seg_count_dict[d] == 6:
            input_dict['b'] = d
        elif seg_count_dict[d] == 9:
            input_dict['f'] = d
        elif seg_count_dict[d] == 8:
            if d != input_dict['a']:
                input_dict['c'] = d
    
    #* figure out 'd' and 'g'
    #* of the characters we have d is not in the 4 string
    for d in input_dict:
        if input_dict[d] in seven_seg_4:
            seven_seg_4 = seven_seg_4.replace(input_dict[d],"")
    input_dict['d'] = seven_seg_4
    #* the last empty spot in the dictionary is the missing letter
    for d in input_dict:
        if input_dict[d] in seven_seg_8:
            seven_seg_8 = seven_seg_8.replace(input_dict[d],"")
    input_dict['g'] = seven_seg_8

    # make the numbers sequences
    num_sequences = {0:'abcefg', 1:'cf', 2:'acdeg', 3:'acdfg', 4:'bcdf', 5:'abdfg', 6:'abdefg', 7:'acf', 8:'abcdefg', 9:'abcdfg'}
    distorted_num_sequences = {0:'', 1:'', 2:'', 3:'', 4:'', 5:'', 6:'', 7:'', 8:'', 9:''}

    for key, value in num_sequences.items():
        print(key,value)
        for c in value:
            distorted_num_sequences[key] += input_dict[c]
    
    #GUH having issues figuring out the output sequence ordering (I think I did this wrong, but it is close enough it will work)
    def sortString(str):
        return ''.join(sorted(str))

    output_number_string = ""
    for out in output:
        output_number_string += str([k for k,v in distorted_num_sequences.items() if sortString(v) == sortString(out)][0])
    
    output_number = int(output_number_string)

    answer += output_number
print(answer)


# %%
