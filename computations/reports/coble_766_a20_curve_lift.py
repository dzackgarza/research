"""Hensel lift of a curve x = A(y)/B(y) over F_p with split preimage
(coble_766_a20_curve_search.py) to Z_p.  Unknowns: A = a2 y^2 + a1 y + 1,
B = b2 y^2 + b1 y + b0 and H of degree 6; equations: the 13 coefficients of
G - H^2, G the restriction of f_star.  Newton on 12 equations whose Jacobian
has rank 12 mod p, then the valuation of all 13 residuals: a residual of
valuation 1 means no curve over Z_p reduces to the given one; all residuals
at the working precision mean the 0-dimensional solution scheme over Q has a
point there, a curve over Q-bar.
Run: coble_766_a20_curve_lift.py p a2,a1,1 b2,b1,b0 precision."""
from sage.all import *
import itertools
C = {(4, 4): 8, (4, 2): 7, (4, 0): 6, (3, 3): 5, (3, 1): 4, (2, 4): 3, (2, 2): 2,
     (2, 0): 3, (1, 3): -13, (1, 1): -28, (0, 4): -10, (0, 2): 13}
names = ['a2','a1','b2','b1','b0'] + ['h%d'%i for i in range(7)]
Rv = PolynomialRing(QQ, names); V = Rv.gens()
a2,a1,b2,b1,b0 = V[:5]; H = V[5:]
Ry = PolynomialRing(Rv, 'y'); y = Ry.gen()
A = a2*y**2 + a1*y + 1; B = b2*y**2 + b1*y + b0
G = sum(v * A**i * B**(4-i) * y**j for (i,j), v in C.items())
Hy = sum(H[k]*y**k for k in range(7))
E = [(G - Hy**2)[k] for k in range(13)]
J = matrix([[e.derivative(x) for x in V] for e in E])
import sys
p = int(sys.argv[1]); cA = [int(c) for c in sys.argv[2].split(',')]; cB = [int(c) for c in sys.argv[3].split(',')]
# F_11 solution: A = 4t^2+5t+1, B = 9t^2+9t+5, G = H^2
F = GF(p); Ft = PolynomialRing(F,'t'); t = Ft.gen()
A0 = Ft(cA[::-1]); B0 = Ft(cB[::-1])
G0 = sum(F(v)*A0**i*B0**(4-i)*t**j for (i,j),v in C.items())
fa = G0.factor(); H0 = fa.unit().sqrt() * prod(f**(e//2) for f,e in fa)
assert H0**2 == G0
x0 = [cA[0],cA[1],cB[0],cB[1],cB[2]] + [ZZ(H0[k]) for k in range(7)]
Jm = J.change_ring(F)(*[F(c) for c in x0]) if False else matrix(F, [[F(J[i,j](*x0)) for j in range(12)] for i in range(13)])
print('rank of Jacobian mod p:', Jm.rank())
rows = Jm.pivot_rows(); print('rows', rows)
prec = int(sys.argv[4])
K = Qp(p, prec)
x = vector(K, x0)
for it in range(12):
    val = vector(K, [E[i](*x) for i in rows])
    Jx = matrix(K, [[J[i,j](*x) for j in range(12)] for i in rows])
    x = x - Jx.solve_right(val)
print('residual valuations', [E[i](*x).valuation() for i in range(13)])
for k, nm in enumerate(names[:5]):
    found = None
    for d in range(1, 17):
        pol = algdep(x[k], d)
        if max(abs(c) for c in pol.coefficients()).nbits() < prec * log(p, 2) / (d + 1) / 1.5:
            found = (d, pol.factor()); break
    print(nm, found)
