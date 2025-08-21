#%%
f = 'data/day13.txt'

with open(file=f) as input:
    read_lines = input.readlines()
read_lines = [line.strip() for line in read_lines]
print('❄️⛄❄️')
#%%
ready_for_departure = int(read_lines[0])
busses = [int(x) for x in read_lines[1].split(',') if x != 'x' ]
#%%
earliest_departure = 1e9
part_1 = 0
for bus in busses:
    bus_departure = ready_for_departure // bus * bus + bus
    if bus_departure < earliest_departure:
        earliest_departure = bus_departure
        part_1 = bus * (bus_departure - ready_for_departure)
print(part_1)
#%%
busses = read_lines[1].split(',')
bus_offsets = {}
for i, bus in enumerate(busses):
    if bus != 'x':
        bus_offsets[int(bus)] = i
#%%
# CRT: https://www.youtube.com/watch?v=zIFehsBHB8o
#! co-pilot algo help
from functools import reduce

def chinese_remainder_theorem(remainders, moduli):
    """
    Solve a system of simultaneous congruences using the Chinese Remainder Theorem.

    Args:
        remainders (list): List of remainders [a1, a2, ..., ak].
        moduli (list): List of moduli [n1, n2, ..., nk], must be pairwise coprime.

    Returns:
        int: The smallest solution x such that x ≡ ai (mod ni) for all i.
    """
    def modular_inverse(a, m):
        """Compute the modular inverse of a modulo m using the extended Euclidean algorithm."""
        m0, x0, x1 = m, 0, 1
        while a > 1:
            q = a // m
            a, m = m, a % m
            x0, x1 = x1 - q * x0, x0
        return x1 + m0 if x1 < 0 else x1

    # Step 1: Compute the product of all moduli
    N = reduce(lambda x, y: x * y, moduli)

    # Step 2: Compute the solution
    x = 0
    for ai, ni in zip(remainders, moduli):
        Ni = N // ni
        Mi = modular_inverse(Ni, ni)
        x += ai * Ni * Mi

    return x % N

remainders = [x-y for x,y in bus_offsets.items()]  # you can have negative remainders
moduli = list(bus_offsets.keys())
result = chinese_remainder_theorem(remainders, moduli)
print(f"The solution is x ≡ {result}")
#%%
