#%%
f = 'data/day18.txt'
# f = 'data/day18.ex'

with open(file=f) as input:
    read_lines = input.readlines()
read_lines = [line.strip() for line in read_lines]
print('❄️⛄❄️')
#%%
points = [(0,0)]
boundary_points =0

directions = {
    'U': (-1,0),
    'D': (1,0),
    'L': (0,-1),
    'R': (0,1)
}

part2 = True
for line in read_lines:
    d, n, dn = line.split()
    if part2:
        dn = dn[2:-1]  # remove the # and parenthesis
        d = "RDLU"[int(dn[-1])]
        n = int(dn[:-1], 16)
    n = int(n)
    dr, dc = directions[d]
    boundary_points += n
    r,c = points[-1]
    points.append((r + dr*n, c + dc*n))
#%%
#* shoelace formula
A = abs(sum(points[i][0]*points[i+1][1] - points[i+1][0]*points[i][1] for i in range(len(points)-1))/2)
i = A - boundary_points // 2 + 1

print(f'Lava Lagoon: {int(i + boundary_points)} m^3')
#%%
#* solution by HyperNeutrino https://www.youtube.com/watch?v=bGWK76_e-LM
