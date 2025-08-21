
#%%
input = open('data/day5.txt')
read_lines = input.readlines()

max_seat_id = -1
seat_id_list = []
for l in read_lines:
    l = l.strip()
    #* rows 0-127
    row_dir = l[0:7]
    row = 0
    update = 128/2
    for d in row_dir:
        if d == 'B':
            row += update
        update /= 2

    #* cols 0-7
    col_dir = l[7:10]
    col = 0
    update = 8/2
    for d in col_dir:
        if d == 'R':
            col += update
        update /= 2

    #* calc seat number
    seat_id = row * 8 + col
    if seat_id > max_seat_id:
        max_seat_id = seat_id
    seat_id_list.append(seat_id)
print('Max seat id: ', max_seat_id)
# %%

min_seat_id = min(seat_id_list)

for i in range(int(min_seat_id), int(max_seat_id)+1):
    if i not in seat_id_list:
        print('Your seat is :', i)

# %%
