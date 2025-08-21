#%%
import time as thyme

f = 'data/day06.txt'

with open(file=f) as input:
    read_lines = input.readlines()
read_lines = [line.strip() for line in read_lines]
print('❄️⛄❄️')
#%%
time = list(map(int, read_lines[0].split(':')[1].split()))
dist = list(map(int, read_lines[1].split(':')[1].split()))

races = list(zip(time, dist))

all_ways = 1
for time, dist in races:
    ways = 0
    for t in range(time):
        if (time - t) * t > dist:
            ways += 1
    all_ways *= ways
print(f'ways to win product: {all_ways}')

#! part 2
time = read_lines[0].split(':')[1].split()  # 🤪 pay the price for using same name in loops
time = int(''.join(time))
dist = read_lines[1].split(':')[1].split()
dist = int(''.join(dist))

start = thyme.time()
for t in range(time):
    if (time - t) * t > dist:
        min_hold = t
        break
print(f'min hold: {min_hold}')

for t in range(time, 0, -1):
    if (time - t) * t > dist:
        max_hold = t
        break
print(f'max hold: {max_hold}')
end = thyme.time()

print(f'ways to win: {max_hold - min_hold + 1}')  # +1 inclusive of min 🙃
print(f'time: {end-start:.2f}')

#%%
#! worked with bhavini, turns out going from the ends wasn't needed
start = thyme.time()
ways = 0
for t in range(time):
    if (time - t) * t > dist:
        ways += 1
print(f'ways to win: {ways}')
end = thyme.time()
print(f'time: {end-start:.2f}')

#%%
#! bonus quad solve
import math
start = thyme.time()
# dist = (time - x)*(x)
# x**2 -time*x + dist = 0

a = 1
b = -time  # - time
c = dist  # dist

D = math.sqrt(b**2 - 4 * a * c)

sol1 = (-b - D) / (2 * a)
sol2 = (-b + D) / (2 * a)

print(f'ways to win: {int(sol2) - int(sol1)}')
end = thyme.time()
print(f'time: {end-start:.2f}')
#%%
