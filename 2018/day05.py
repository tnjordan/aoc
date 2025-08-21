#%%
import string
f = 'data/day05.txt'

with open(file=f) as input:
    read_lines = input.readlines()
read_lines = [l.strip() for l in read_lines]
print('🎅 🎄 🤶')
#%%
poly = read_lines[0]

reacting = True
reactants = [x+y for x,y in zip(string.ascii_lowercase+string.ascii_uppercase,string.ascii_uppercase+string.ascii_lowercase)]
while reacting:
    poly_len = len(poly)
    for r in reactants:
        poly = poly.replace(r,'')
    if poly_len == len(poly):
        reacting = False

print(f'reacted polymer is {len(poly)} units')
#%%
#! part 2
def reactor(poly):
    reacting = True
    reactants = [x+y for x,y in zip(string.ascii_lowercase+string.ascii_uppercase,string.ascii_uppercase+string.ascii_lowercase)]
    while reacting:
        poly_len = len(poly)
        for r in reactants:
            poly = poly.replace(r,'')
        if poly_len == len(poly):
            reacting = False
    return len(poly)

min_poly = float('inf')
for a,A in zip(string.ascii_lowercase,string.ascii_uppercase):
    poly_reduced = poly.replace(a,'').replace(A,'')
    poly_reduced_len = reactor(poly_reduced)
    if poly_reduced_len < min_poly:
        min_poly = poly_reduced_len
    
print(f'min reduced poly length: {min_poly}')
#%%
#
print('⭐ ⭐')
#%%