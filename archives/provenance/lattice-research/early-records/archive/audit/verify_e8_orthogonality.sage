from sage.all import *
L = RootSystem(['E', 8]).root_lattice()
roots = L.simple_roots()
# Bourbaki diagram: 1-2-3-4-5-6-7, 5-8
# We want independent sets (orthogonal roots)
# Set A: {1, 3, 6, 8}
# Set B: {2, 4, 7}
# Let's check my sets from task5_1: {1, 4, 6, 8} and {2, 3, 5, 7}?
set_A = [1, 4, 6, 8]
set_B = [2, 3, 5, 7]
print(f"Checking Set A: {set_A}")
for i in set_A:
    for j in set_A:
        if i < j:
            pair = roots[i].inner_product(roots[j])
            print(f"  ({i}, {j}) pairing = {pair}")
print(f"Checking Set B: {set_B}")
for i in set_B:
    for j in set_B:
        if i < j:
            pair = roots[i].inner_product(roots[j])
            print(f"  ({i}, {j}) pairing = {pair}")
