from sage.all import *
W = RootSystem(['E', 8]).weight_lattice()
roots = W.simple_roots()
# In E8, simple roots have norm 2. Orthogonal roots have scalar product 0.
set_A = [1, 4, 6, 8]
set_B = [2, 3, 5, 7]
def check_set(name, indices):
    print(f"Checking {name}: {indices}")
    for i in indices:
        for j in indices:
            if i < j:
                # Use scalar product in the weight lattice
                val = roots[i].inner_product(roots[j])
                print(f"  ({i}, {j}) pairing = {val}")
check_set("Set A", set_A)
check_set("Set B", set_B)
