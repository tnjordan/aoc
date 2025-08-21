#%%
f = 'data/day08.txt'

with open(file=f) as input:
    read_lines = input.readlines()
read_lines = [line.strip() for line in read_lines]
print('🐟 🎄 🦈')
#%%
grid = [list(line) for line in read_lines]
J = len(grid)
I = len(grid[0])

af = {}
for j,row in enumerate(grid):
    for i,f in enumerate(row):
        if f == '.':
            continue
        if f not in af:
            af[f] = [(j,i)]
        else:
            af[f].append((j,i))
#%%
antinodes = {}
antinode_count = set()
for f in af:
    antinodes[f] = []
    antennas = af[f]
    for x,a1 in enumerate(antennas):
        a1j,a1i = a1
        for a2 in antennas[x+1:]:
            a2j,a2i = a2

            # delta between 1 and its antinode
            dj1 = a1j - a2j
            di1 = a1i - a2i

            # delta between 2 and its antinote
            dj2 = a2j - a1j
            di2 = a2i - a1i

            # the antinodes of 1 and 2
            antinode1 = (a1j + dj1, a1i + di1)
            antinode2 = (a2j + dj2, a2i + di2)

            for an in (antinode1, antinode2):
                j,i = an
                if 0 <= j < J and 0 <= i < I:
                    antinodes[f].append(an)
                    antinode_count.add(an)
print(len(antinode_count))
#%%
#! part 2
antinodes = {}
antinode_count = set()
for f in af:
    antinodes[f] = []
    antennas = af[f]
    for x,a1 in enumerate(antennas):
        a1j,a1i = a1
        for a2 in antennas[x+1:]:
            a2j,a2i = a2

            # delta between 1 and its antinode
            dj1 = a1j - a2j
            di1 = a1i - a2i

            # delta between 2 and its antinote
            dj2 = a2j - a1j
            di2 = a2i - a1i

            for n in range(50): # only a 50x50 grid
                # the antinodes of 1 and 2 (including self at 0)
                antinode1 = (a1j + dj1*n, a1i + di1*n)
                antinode2 = (a2j + dj2*n, a2i + di2*n)

                for an in (antinode1, antinode2):
                    j,i = an
                    if 0 <= j < J and 0 <= i < I:
                        antinodes[f].append(an)
                        antinode_count.add(an)
print(len(antinode_count))
#%%
