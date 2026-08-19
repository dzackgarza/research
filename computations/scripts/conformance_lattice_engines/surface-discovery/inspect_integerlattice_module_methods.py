from sage.all import *
from sage.modules.free_module_integer import IntegerLattice

lat = IntegerLattice([[1, 0], [0, 1]])
methods = [
    'coordinate_vector', 'coordinates', 'linear_combination_of_basis', 
    'relations', 'zero', 'random_element', 'span_of_basis', 'gen', 'gens'
]

for m in methods:
    method = getattr(lat, m, None)
    if method:
        print(f"\n[{m}]")
        print(method.__doc__)
    else:
        print(f"\n[{m}] NOT FOUND")
