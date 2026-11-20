"""The class w = C+ - iota C+ of the curve C: x = A(y)/B(y), A = 2y^2+6y+1,
B = 7y^2+14y+16 over F_17, which lifts to characteristic 0
(coble_766_a20_curve_lift.py).  C+ is the component z = H(y)/B(y)^2 of its
preimage; intersections with D_{+-1,+-} and with iota C+ are read off over
F_17-bar (all intersection points are off the branch curve), and
w^2 = -4 - 2 C+.iotaC+, w.v = 2 (C+.D_{1,+} - C+.D_{-1,+})."""
from sage.all import *
import sys
C = {(4, 4): 8, (4, 2): 7, (4, 0): 6, (3, 3): 5, (3, 1): 4, (2, 4): 3, (2, 2): 2,
     (2, 0): 3, (1, 3): -13, (1, 1): -28, (0, 4): -10, (0, 2): 13}
p = 17
F = GF(p); R = PolynomialRing(F, 'y'); y = R.gen()
A = 2*y**2 + 6*y + 1; B = 7*y**2 + 14*y + 16
G = sum(F(v) * A**i * B**(4-i) * y**j for (i, j), v in C.items())
fa = G.factor(); print('restriction', fa)
c = fa.unit(); s = c.sqrt(); assert s in F
H = s * prod(f**(e//2) for f, e in fa); assert H**2 == G
fxy = lambda X, Y: sum(v * X**i * Y**j for (i, j), v in C.items())
# all roots over a common extension
P1 = A - B; P2 = A + B; P3 = A*B(-y) + A(-y)*B
L = lcm([f.degree() for P in (P1, P2, P3) for f, _ in P.factor()] + [1])
K = GF(p**L, 'g'); 
def pts(P):
    return [(r, P.change_ring(K).roots(multiplicities=True)) for r in [0]][0][1]
def zC(r): return K(H(r)) / K(B(r))**2
print('C at y = infinity: x =', A[2]/B[2], ' (x = 1 or -1 would add points)')
def count(P, zD, label):
    tot = 0
    for r, m in P.change_ring(K).roots(multiplicities=True):
        assert B(r) != 0
        zc = zC(r); zd = zD(r)
        if zc == 0: print('  ', label, 'branch point at y =', r); 
        if zc == zd: tot += m; print('  ', label, 'y =', r, 'mult', m)
    return tot
c1p = count(P1, lambda r: (r - 1)*(r - 3), 'C+.D_{1,+}')
c1m = count(P1, lambda r: -(r - 1)*(r - 3), 'C+.D_{1,-}')
cmp_ = count(P2, lambda r: -(r + 1)*(r + 3), 'C+.D_{-1,+}')
cmm = count(P2, lambda r: (r + 1)*(r + 3), 'C+.D_{-1,-}')
# C+ . iota C+: iota C+ over tau C has z = -H(-y)/B(-y)^2 at the point with coordinate y
cii = count(P3, lambda r: -K(H(-r)) / K(B(-r))**2, 'C+.iotaC+')
print('degrees: deg P3 =', P3.degree(), ' (y = infinity on C and tau C: x =', A[2]/B[2], -A[2]/B[2], ')')
print('C+.D1+ =', c1p, ' C+.D1- =', c1m, ' C+.D-1+ =', cmp_, ' C+.D-1- =', cmm, ' C+.iotaC+ =', cii)
w2 = -4 - 2*cii; wv = 2*(c1p - cmp_)
print('w^2 =', w2, ' w.v =', wv, ' (w.v)^2 + 4 w^2 =', wv**2 + 4*w2)
