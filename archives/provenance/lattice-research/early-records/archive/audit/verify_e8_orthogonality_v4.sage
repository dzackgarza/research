from sage.all import *
A = CartanMatrix(['E', 8])
set_A = [0, 3, 5, 7] # 0-indexed for CartanMatrix
set_B = [1, 2, 4, 6]
def check_set(name, indices):
    print(f"Checking {name}: {indices}")
    for i in indices:
        for j in indices:
            if i < j:
                val = A[i, j]
                print(f"  ({i+1}, {j+1}) pairing = {val}")
check_set("Set A", [i+1 for i in set_A])
check_set("Set B", [i+1 for i in set_B])
