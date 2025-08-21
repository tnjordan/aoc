# %%
f = 'data/day24.txt'

with open(file=f) as input:
    read_lines = input.readlines()
read_lines = [line.strip() for line in read_lines]
print('🎅 🎄 🤶')
#%%

part_2 = False

packages = [int(x) for x in read_lines]

weight = sum(packages)

if part_2 is True:
    compartment_weight = weight / 4
else:
    compartment_weight = weight / 3

print(f'The {len(packages)} packages weigh {weight} kg.')
print(f'Each compartment needs {compartment_weight} kg for equal split.')

compartment_weight_arrangements = set()
def weight_watcher(used_packages, available_packages, target_weight=compartment_weight):
    # print(f'used_packages: {used_packages} weight: {sum(used_packages)}')
    # print(f'available_packages: {available_packages}')
    global compartment_weight_arrangements
    current_weight = sum(used_packages)
    if current_weight == target_weight:
        compartment_weight_arrangements.add(tuple(used_packages))
        return None
    if used_packages != []:
        max_used = max(used_packages)
        available_packages = [p for p in available_packages if p > max_used]
    
    for p in available_packages:
        if p + current_weight > target_weight:
            break
        ap = [ap for ap in available_packages if ap != p]
        up = [up for up in used_packages] + [p]
        weight_watcher(up, ap)
    return None

weight_watcher(used_packages=[], available_packages=packages, target_weight=compartment_weight)

#%%
min_package_count = float('inf')
min_packages = []
for package_config in compartment_weight_arrangements:
    if len(package_config) < min_package_count:
        min_package_count = len(package_config)
        min_packages = [package_config]
    elif len(package_config) == min_package_count:
        min_packages.append(package_config)

#%%
from functools import reduce

min_quantum_entanglement = float('inf')
min_q_pack = []
for mp in min_packages:
    qe = reduce(lambda x, y: x * y, mp)
    if qe < min_quantum_entanglement:
        min_quantum_entanglement = qe
        min_q_pack = [mp]
    elif qe == min_quantum_entanglement:
        min_q_pack.append(mp)

print(f'minimum quantum entanglement: {min_quantum_entanglement}')
print(f'packages: {min_q_pack}')

# Note: I ignored the check for the other compartments being viable.
# the answers produced with my input worked without that edge case.

# %%
print()
print('⭐ ⭐')
