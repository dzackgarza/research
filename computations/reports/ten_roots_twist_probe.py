"""E8 witness identification: the typed Gram matrix, checked.
Verifications: negative determinant -1 is impossible; det is 1; even; the (-2) fibre
of the negative of that matrix has 240 elements, matching the E_8 root system, by which
the Gram lattice is the E_8 root lattice at pin c546077d."""
from sage.all import ZZ, matrix
E8r = matrix(ZZ, 8, 8, [
    [2,-1,0,0,0,0,0,0],[-1,2,-1,0,0,0,0,0],[0,-1,2,-1,0,0,0,0],[0,0,-1,2,-1,0,0,0],
    [0,0,0,-1,2,-1,0,-1],[0,0,0,0,-1,2,-1,0],[0,0,0,0,0,-1,2,0],[0,0,0,0,-1,0,0,2]])
print("det(E8r):", E8r.determinant())
print("even:", all(E8r[i,i] % 2 == 0 for i in range(8)))
from sage_extensions.all import Lattices
LE = Lattices(ZZ)([list(r) for r in (-E8r).rows()])
els = list(LE.elements_of_norm(-2))
print("|elements of norm -2 in (negative) E8 Gram|:", len(els))
