"""Referee check for S_dP candidates: discriminant form of M = U(2)+<-2> and its even overlattices.
At pin c546077d. Answers: |A_M|, the integral-valued order-2 classes, and the even overlattices."""
from sage.all import ZZ, matrix, vector
U2 = matrix(ZZ, 2, 2, [[0, 2], [2, 0]])
minus2 = matrix(ZZ, 1, 1, [[-2]])
G = U2.block_sum(minus2)
print("det M:", G.determinant())
# overlattice search: y = (a)(e/2) + (b)(f/2) + (c)(d/2), a,b,c in {0,1}, even square, not all zero
e, f, d = vector(ZZ, [1,0,0]), vector(ZZ, [0,1,0]), vector(ZZ, [0,0,1])
cands = []
from itertools import product
for a, b, c in product([0,1],[0,1],[0,1]):
    if (a, b, c) == (0,0,0): continue
    y = a*e/2 + b*f/2 + c*d/2
    q = (y*G*y)
    num = q.numerator() if q.denominator() == 1 else None
    if num is not None and num % 2 == 0:
        cands.append((a, b, c, num))
print("integral-valued nonzero half-classes (a,b,c,q):", cands)
# overlap: index-2 overlattice; determinants
for a, b, c, q in cands:
    print("  generated overlattice det would be", G.determinant()//4)
