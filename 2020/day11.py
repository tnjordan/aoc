#%%
f = 'data/day11.txt'

with open(file=f) as input:
    read_lines = input.readlines()
read_lines = [line.strip() for line in read_lines]
print('❄️⛄❄️')
#%%
J = len(read_lines)
I = len(read_lines[0])

seats = {}
for j, row in enumerate(read_lines):
    for i, value in enumerate(row):
        if value == 'L':
            seats[(j,i)] = 0


def find_adj_seat(j,i,dj,di,seats,part_2):
    j_dj = j + dj
    i_di = i + di
    if not part_2:
        return seats.get((j_dj, i_di), 0)
    else:
        while True:
            if 0 <= j_dj < J and 0 <= i_di < I:
                # loop to find seats
                if (j_dj,i_di) in seats:
                    return seats[(j_dj, i_di)]
                else:
                    j_dj = j_dj + dj
                    i_di = i_di + di
            else:
                return 0


def adjacent_seat_counter(j,i, seats, part_2):
    adj_seats = 0
    directions = [-1, 0, 1]
    for dj in directions:
        for di in directions:
            if dj == 0 and di == 0:
                continue
            adj_seats += find_adj_seat(j,i,dj,di,seats,part_2)
    return adj_seats


def seat_fill(seats, part_2):
    new_seats = {}
    for (j,i), seat_status in seats.items():
        new_seats[(j,i)] = seat_status
        if seat_status == 0:
            if adjacent_seat_counter(j,i,seats,part_2) == 0:
                new_seats[(j,i)] = 1
    return new_seats


def seat_abandon(seats, part_2):
    limit = 5 if part_2 else 4
    new_seats = {}
    for (j,i), seat_status in seats.items():
        new_seats[(j,i)] = seat_status
        if seat_status == 1:
            if adjacent_seat_counter(j,i,seats,part_2) >= limit:
                new_seats[(j,i)] = 0
    return new_seats


def seating_chart(seats):
    seat_chart = ''
    for j in range(J):
        for i in range(I):
            seat_chart += str(seats.get((j, i), ''))
    return seat_chart
#%%
part_2 = True
previous_seating_charts = set()

while True:
    seats = seat_fill(seats, part_2)
    seats = seat_abandon(seats, part_2)
    current_seating_chart =  seating_chart(seats)
    if current_seating_chart in previous_seating_charts:
        print('Part 2' if part_2 else 'Part 1')
        print(current_seating_chart.count('1'))
        break
    else:
        previous_seating_charts.add(current_seating_chart)
#%%