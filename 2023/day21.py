#%%
from collections import deque

f = 'data/day21.txt'
# f = 'data/day21.ex'

with open(file=f) as input:
    read_lines = input.readlines()
read_lines = [line.strip() for line in read_lines]
print('❄️⛄❄️')
#%%
grid = read_lines  # make variable match

sr, sc = next((r, c) for r, row in enumerate(grid) for c, ch in enumerate(row) if ch == 'S')

assert len(grid) == len(grid[0])  #* square
size = len(grid)
steps = 26501365

assert sr == sc == size // 2  #* center start assumption
assert steps % size == size // 2  #* end at edge of grid assumption

def fill(sr, sc, s):
    ans = set()
    seen = {(sr,sc)}

    q = deque([(sr,sc,s)])

    while q:
        r,c,s = q.popleft()
        if s % 2 == 0:
            ans.add((r,c))
        if s == 0:
            continue
        
        for nr, nc in [(r-1,c), (r+1,c), (r,c-1), (r,c+1)]:
            if nr < 0 or nr >= len(grid) or nc < 0 or nc >= len(grid[0]) or grid[nr][nc] == '#' or (nr,nc) in seen:
                continue
            seen.add((nr,nc))
            q.append((nr,nc,s-1))
    return len(ans)

print(f'Part 1: {fill(sr, sc, 64)}')
#%%

grid_width = steps // size - 1

# calculate even and odd grids (determined by steps to reach edge)
odd = (grid_width // 2 * 2 + 1) ** 2
even = ((grid_width + 1) // 2 * 2) ** 2

odd_points = fill(sr, sc, size * 2 + 1)
even_points = fill(sr, sc, size * 2)

corner_top = fill(size - 1, sc, size - 1)
corner_right = fill(sr, 0, size - 1)
corner_bottom = fill(0, sc, size - 1)
corner_left = fill(sr, size - 1, size - 1)

small_top_right = fill(size - 1, 0, size // 2 - 1)
small_top_left = fill(size - 1, size - 1, size // 2 - 1)
small_bottom_right = fill(0, 0, size // 2 - 1)
small_bottom_left = fill(0, size - 1, size // 2 - 1)

top_top_right = fill(size - 1, 0, size * 3 // 2 - 1)
top_top_left = fill(size - 1, size - 1, size * 3 // 2 - 1)
top_bottom_right = fill(0, 0, size * 3 // 2 - 1)
top_bottom_left = fill(0, size - 1, size * 3 // 2 - 1)

part_2 = odd * odd_points + even * even_points + corner_top + corner_right + corner_bottom + corner_left + (grid_width + 1) * (small_top_right + small_top_left + small_bottom_right + small_bottom_left) + grid_width * (top_top_right + top_top_left + top_bottom_right + top_bottom_left)
print(f'Part 2: {part_2}')
#%%
#* solution from HyperNeutrino: https://www.youtube.com/watch?v=9UOMZSL0JTg
