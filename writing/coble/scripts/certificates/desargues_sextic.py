"""Exact node-incidence and curve-lattice arithmetic for ex:thas-desargues-sextic; run with Sage Python."""
from itertools import combinations

from sage.all import QQ, ZZ, PolynomialRing, gcd, matrix

R = PolynomialRing(QQ, "t")
t = R.gen()
X = 6*t**6 + 8*t**4 - 10*t**2 - 4
Y = -16*t**5 + 116*t**4 - 40*t**3 - 8*t
Z = 12*t**5 + 32*t**3 - 116*t**2 + 20*t
assert gcd(gcd(X, Y), Z) == 1
assert X.degree() == 6
A = PolynomialRing(QQ, names=("x", "y", "z"))
x, y, z = A.gens()
coefficients = [
    0,0,240,-696,96,0,9,0,416,-928,8,348,-24,128,-1160,3268,-464,-14,
    -464,136,-580,52,80,232,9,0,-20,4,
]
F = sum(c*x**(6-j-h)*y**j*z**h
        for c, (j,h) in zip(coefficients, [(j,h) for h in range(7) for j in range(7-h)]))
assert F != 0 and F(X,Y,Z) == 0
for degree, expected_rank in [(5,21),(6,27)]:
    columns = [(X**(degree-j-h)*Y**j*Z**h).list()
               for h in range(degree+1) for j in range(degree-h+1)]
    M = matrix(QQ, 6*degree+1, len(columns),
               lambda i,j: columns[j][i] if i<len(columns[j]) else 0)
    assert M.rank() == expected_rank

points = [
    (1,0,0),(2,1,1),(14,4,-2),(14,-1,3),(2,28,28),
    (-1,-8,4),(2,-4,12),(0,1,-1),(0,2,1),(0,1,3),
]
assert all(matrix(QQ, [p,q]).rank()==2 for p,q in combinations(points,2))
for p in points:
    assert F(*p)==0
    assert all(F.derivative(v)(*p)==0 for v in A.gens())
    assert matrix(QQ, [[F.derivative(u).derivative(v)(*p)
                       for v in A.gens()] for u in A.gens()]).rank()==2
    assert p[0]**2-p[1]*p[2] != 0
triples = [I for I in combinations(range(10),3)
           if matrix(QQ, [points[i] for i in I]).det()==0]
assert triples == [
    (0,1,4),(0,2,5),(0,3,6),(1,2,9),(1,3,8),
    (2,3,7),(4,5,9),(4,6,8),(5,6,7),(7,8,9),
]
assert X**2-Y*Z == 4*(3*t**6+12*t**4-58*t**3+15*t**2+2)**2
G = matrix(ZZ, 10, 10, lambda i,j: 1-len(set(triples[i]) & set(triples[j])))
assert G.det() == -256
T = PolynomialRing(ZZ, "q")
q = T.gen()
assert T(G.charpoly()) == (q-1)*(q+1)**5*(q+4)**4
print("Desargues sextic: all 10 nodes and 10 lines verified; determinant -256; index 16")
