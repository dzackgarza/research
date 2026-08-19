
from sage.all import *
from sage.modules.free_module_integer import IntegerLattice

L = IntegerLattice([[2, 0], [0, 2]])
print("Testing empty list:")
try:
    ef = L.echelon_form([])
    print(f"Success: {ef}")
except Exception as e:
    print(f"Failed: {e}")
