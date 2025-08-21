#%%
f = 'data/day6.txt'
# f = 'data/day6_ex.txt'
with open(f) as input:
    read_lines = input.readlines()

orb_map = {}
orb_map_r = {}
for l in read_lines:
    planet_c, planet_o = l.strip().split(sep=')')
    # orb_map[planet_c] = planet_o #* not unique keys :(
    orb_map_r[planet_o] = planet_c


orb_count = {'COM':0} #* set the center
direct_orbits = 0
indirect_orbits = 0
indirect_orbs = 0
for planet_o, planet_c  in orb_map_r.items():
    direct_orbits += 1

    if planet_c in orb_count:
        indirect_orbits += orb_count[planet_c]
    else:
        indirect_orbs = 0
        planet_c_i = planet_c
        while planet_c_i != 'COM':
            indirect_orbs += 1
            planet_c_i = orb_map_r[planet_c_i]
        orb_count[planet_c] = indirect_orbs
        orb_count[planet_o] = indirect_orbs + 1 #* because everything only orbits 1
        indirect_orbits += indirect_orbs
    print(f'planet: {planet_o} direct: {1} indirect: {indirect_orbs}')

print(f'direct: {direct_orbits} indirect: {indirect_orbits}')
print(f'part 1: {direct_orbits + indirect_orbits}')
# %%
#! part 2
#* get distance from YOU to COM and SAN to COM
#* then find the intersection point and subtract
#* the distance from the intercept to COM

YOU_path = []
planet_c_i = 'YOU'
while planet_c_i != 'COM':
    planet_c_i = orb_map_r[planet_c_i]
    YOU_path.append(planet_c_i)

SAN_path = []
planet_c_i = 'SAN'
while planet_c_i != 'COM':
    planet_c_i = orb_map_r[planet_c_i]
    SAN_path.append(planet_c_i)
    if planet_c_i in YOU_path:
        #* path intersection planet
        planet_int = planet_c_i
        print(f'planet_int {planet_int}')
        break

SAN_count = orb_count[orb_map_r['SAN']]
YOU_count = orb_count[orb_map_r['YOU']]
INT_count = orb_count[orb_map_r[planet_int]]

part_2 = (YOU_count - INT_count) + (SAN_count - INT_count) -2 #* the minus 2 is because we are not going from SAN to YOU
print(part_2)
# %%
