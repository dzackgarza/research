from sage.all import *
from sage.modules.free_module_integer import IntegerLattice

print("--- FreeModule(ZZ, 2) ---")
M = FreeModule(ZZ, 2)
basis = M.basis()
try:
    print(f"echelon_form: {M.echelon_form(basis)}")
except Exception as e:
    print(f"Error: {e}")

print("\n--- IntegerLattice([[2, 0], [0, 2]]) ---")
L = IntegerLattice([[2, 0], [0, 2]])
basis_L = L.basis()
try:
    print(f"echelon_form: {L.echelon_form(basis_L)}")
except Exception as e:
    print(f"Error: {e}")

print("\n--- Checking _vector_ signature ---")
v = basis_L[0]
import inspect
try:
    print(f"v._vector_ signature: {inspect.signature(v._vector_)}")
except Exception as e:
    print(f"Could not get signature: {e}")
    # Try calling it
    try:
        v._vector_(order=None)
        print("v._vector_(order=None) worked")
    except Exception as e:
        print(f"v._vector_(order=None) failed: {e}")

print("\n--- Checking category ---")
print(L.category())
