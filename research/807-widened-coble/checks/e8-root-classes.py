from fractions import Fraction
from itertools import combinations, product
from sympy import Matrix, Rational

roots = set()
for i, j in combinations(range(8), 2):
    for si in (-1, 1):
        for sj in (-1, 1):
            roots.add(tuple(Fraction(si if k == i else sj if k == j else 0) for k in range(8)))
for signs in product((-1, 1), repeat=8):
    if sum(s == -1 for s in signs) % 2 == 0:
        roots.add(tuple(Fraction(s, 2) for s in signs))
assert len(roots) == 240

# Standard simple roots for E8 (columns). This is a Z-basis, not the ambient coordinate basis.
simple = [
    (Fraction(1,2), *([Fraction(-1,2)]*6), Fraction(1,2)),
    (1,1,0,0,0,0,0,0),
    (-1,1,0,0,0,0,0,0),
    (0,-1,1,0,0,0,0,0),
    (0,0,-1,1,0,0,0,0),
    (0,0,0,-1,1,0,0,0),
    (0,0,0,0,-1,1,0,0),
    (0,0,0,0,0,-1,1,0),
]
B = Matrix(8, 8, lambda i,j: Rational(simple[j][i].numerator, simple[j][i].denominator))
assert B.det() in (1,-1), B.det()
Binv = B.inv()
coords = {}
for r in roots:
    v = Matrix([Rational(x.numerator, x.denominator) for x in r])
    c = Binv*v
    assert all(x.q == 1 for x in c), (r,c)
    coords[r] = tuple(int(x) for x in c)
classes = {tuple(x % 2 for x in c) for c in coords.values()}
print('E8 roots:', len(roots))
print('simple-root Gram determinant:', B.det())
print('root classes modulo 2E8:', len(classes))
assert len(classes) == 120, len(classes)
seen = {}
for r,c in coords.items():
    seen.setdefault(tuple(x % 2 for x in c), set()).add(r)
assert all(len(v) == 2 for v in seen.values())
for values in seen.values():
    a,b = tuple(values)
    assert b == tuple(-x for x in a)
print('each class has exactly one antipodal pair: PASS')
