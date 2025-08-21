#%%
f = open('data\day16_input.txt', 'r')
read_lines = f.readlines()
f.close()

bin_input = ''
for l in read_lines:
    l = l.strip()
    for c in l:
        hex_value = c
        int_value = int(hex_value, base=16)
        bin_value = bin(int_value)[2:].zfill(4)
        bin_input += bin_value


def packet_ops(id,packet_values):
    if id == 0: #Sum
        packet_value = 0
        for p in packet_values:
            packet_value += p
    elif id == 1: #Product
        packet_value = 1
        for p in packet_values:
            packet_value *= p
    elif id == 2: #Min
        packet_value = min(packet_values)
    elif id == 3: #Max
        packet_value = max(packet_values)
    elif id == 5: #Greater than
        if packet_values[0]>packet_values[1]:
            packet_value = 1
        else:
            packet_value = 0
    elif id == 6: #Less than
        if packet_values[0]<packet_values[1]:
            packet_value = 1
        else:
            packet_value = 0
    elif id == 7: #Equal to
        if packet_values[0] == packet_values[1]:
            packet_value = 1
        else:
            packet_value = 0
    return packet_value

def read_packet(bin_input, v_total, p_values):
    op_v = bin_input[0:3]
    op_v_int = int(op_v,2)
    v_total += op_v_int
    bin_input = bin_input[3:]
    op_id = bin_input[0:3]
    op_id_int = int(op_id,2)
    bin_input = bin_input[3:]

    packet_num_bin = ''
    reading_bin = True
    if op_id_int == 4:
        while reading_bin:
            x = bin_input[0:5]
            bin_input = bin_input[5:]
            if x[0] == '0':
                reading_bin = False
            packet_num_bin += x[1:]
        p_values.append(int(packet_num_bin,2))
    
    else:
        op_len_id = bin_input[0]
        bin_input = bin_input[1:]
        if op_len_id == '0':
            len_subpackets_bin = bin_input[0:15]
            bin_input = bin_input[15:]
            len_subpackets = int(len_subpackets_bin,2)
            sub_packet_data = bin_input[0:len_subpackets]
            bin_input = bin_input[len_subpackets:]
            p_sub_v =[]
            while len(sub_packet_data) > 0:
                sub_packet_data, v_total, p_sub_v = read_packet(sub_packet_data, v_total, p_sub_v)
            #* evaluate substring values to single value
            p_sub_v = packet_ops(op_id_int,p_sub_v)
            #* append value for evaluation
            p_values.append(p_sub_v)

        elif op_len_id == '1':
            sub_packet_count_bin = bin_input[0:11]
            bin_input = bin_input[11:]
            sub_packet_count = int(sub_packet_count_bin,2)
            p_sub_v =[]
            for i in range(sub_packet_count):
                bin_input, v_total, p_sub_v = read_packet(bin_input, v_total, p_sub_v)
            #* evaluate substring values to single value
            p_sub_v = packet_ops(op_id_int,p_sub_v)
            #* append value for evaluation
            p_values.append(p_sub_v)

    return bin_input, v_total, p_values

print(read_packet(bin_input, 0, []))
# %%
