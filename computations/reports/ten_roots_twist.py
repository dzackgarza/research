"""T_En root structure for the reflection twist, at provider pin c546077d.

Checks: T_En = U + U(2) + E_8(-2) has rank 12, signature (2,10);
the displayed twist root alpha = e - f has square -2 and alpha.e = -1;
u = e + f has square 2; E_8(2) (negative part) has vectors of square -4;
hence alpha2 = u + v is a vector of square -2 NOT lying in the U summand.
"""
from sage.all import ZZ, matrix, vector

U = matrix(ZZ, 2, 2, [[0, 1], [1, 0]])
U2 = matrix(ZZ, 2, 2, [[0, 2], [2, 0]])
E8r = matrix(ZZ, 8, 8, [
    [2, -1, 0, 0, 0, 0, 0, 0],
    [-1, 2, -1, 0, 0, 0, 0, 0],
    [0, -1, 2, -1, 0, 0, 0, 0],
    [0, 0, -1, 2, -1, 0, 0, 0],
    [0, 0, 0, -1, 2, -1, 0, -1],
    [0, 0, 0, 0, -1, 2, -1, 0],
    [0, 0, 0, 0, 0, -1, 2, 0],
    [0, 0, 0, 0, -1, 0, 0, 2]])
E8n2 = -2 * E8r
T = U.block_sum(U2).block_sum(E8n2)

e = vector(ZZ, [1, 0] + [0] * 10)
f = vector(ZZ, [0, 1] + [0] * 10)
al = e - f
u = e + f

import numpy as np
ev = np.linalg.eigvalsh(T.change_ring(ZZ).numpy(dtype=float))
sig = (int((ev > 0).sum()), int((ev < 0).sum()))
print("T_En: rank 12, det", T.determinant(), "signature", sig)
print("alpha^2:", int(al * T * al), " alpha.e:", int(al * T * e))
print("u^2:", int(u * T * u))

from sage_extensions.all import Lattices
LE = Lattices(ZZ)([list(r) for r in E8n2.rows()])
els = list(LE.elements_of_norm(-4))
print("|elements of norm -4 in E8(2)|:", len(els))
v = els[0]
print("v in E8(2) has square", int(vector(ZZ, list(v)) * E8n2 * vector(ZZ, list(v))))
al2 = u + vector(ZZ, [0] * 4 + list(v))
print("alpha2^2:", int(al2 * T * al2), "with nonzero components in U and E8(2)")
