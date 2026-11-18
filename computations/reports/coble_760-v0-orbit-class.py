"""#760: the O(q)-orbit of V0 = A_{U(2)} in A_{T_Co} has 67,456 elements; the supplied family covers 18,360.

The deciding record coble_759-gamma-co-2-orbit-1213-run.txt states its negative modulo the provider's
family generating Stab_O(T_Co)(r12): the orbit of V0 under that family's images is 18,360 subspaces and
does not contain the target.  This record measures the class the question lives in, so the residue is a
number rather than a phrase.

All 698,027 two-dimensional subspaces of A_{T_Co} (2,048 classes) are enumerated by canonical basis, and
their isometry type is read off the multiset of q-values on the three nonzero elements together with the
pairing.  V0 has q = 0, 0, 1/2 and b = 1/2, and by Witt's theorem the subspaces of that type are exactly
one O(q)-orbit:

    2-dimensional subspaces of A_{T_Co}:                 698,027
    isometric to V0 (q = 0,0,1/2 with b = 1/2):           67,456

So the orbit the deciding record exhausts is 18,360 of the 67,456 subspaces of the class.  That is what
the caveat means and it does not dissolve it: rho(Stab_O(T_Co)(r12)) is a proper subgroup of O(q), so
its orbit is properly smaller than the class, and the negative conclusion holds once -- and only once --
the family the record used generates that stabilizer.  Nothing here bears on whether it does.

Two arithmetic points are worth pinning, both of which cost runs to find: q on A_{T_Co} takes values in
(1/4)Z/Z, and a representative's v^2/2 is unbounded, so q must be reduced to a rational representative
in [0,1) before comparing -- reducing in the quotient Q/Z and then scaling by 4 gives 0 for every class.

    usage: python3 computations/reports/coble_760-v0-orbit-class.py    (~2.5 min)
"""
"""#760: the O(q)-orbit of V0 = A_{U(2)} among the 2-dim subspaces of A_{T_Co}."""
import sys, time
sys.stdout.reconfigure(line_buffering=True)
t0=time.time()
def say(*a): print("[%7.1fs]" % (time.time()-t0), *a, flush=True)
from sage_extensions.all import *   # noqa
from sage.all import ZZ, QQ, matrix, vector
lattice = NamedLattices.Tco
labels = tuple(lattice.module_generating_set()); NC = len(labels)
Gc = matrix(ZZ, NC, NC, [[int(lattice.b(lattice.module_generator(labels[i]), lattice.module_generator(labels[j]))) for j in range(NC)] for i in range(NC)])
S, U, V = Gc.smith_form(); d = [int(S[i,i]) for i in range(NC)]
Uq, Uinv = matrix(QQ, U), matrix(QQ, matrix(ZZ, U).inverse()); Gin = matrix(QQ, Gc.inverse())
def key(a):
    b = Uq*vector(QQ, a); return tuple(0 if d[i]==1 else int(b[i]) % d[i] for i in range(NC))
def lift(k): return vector(ZZ, Uinv*vector(QQ, k))
def qv(k):
    a = lift(k); q = QQ(a*Gin*a)/2                 # q([v]) = v^2/2 with v = G^{-1}a
    return q - q.floor()                           # its representative in [0,1), not an element of Q/Z
def bv(x, y):
    b = QQ(lift(x)*Gin*lift(y)); return b - b.floor()
zero = tuple(0 for _ in range(NC))
# enumerate the classes as keys of the basis vectors' classes and their sums
keys = {zero}
basis = [key(vector(ZZ, [1 if i == j else 0 for j in range(NC)])) for i in range(NC)]
frontier = [zero]
while len(keys) < 2048:
    nxt = []
    for k in list(keys):
        for b in basis:
            s = tuple((a + c) % 2 for a, c in zip(k, b))
            if s not in keys:
                keys.add(s); nxt.append(s)
    if not nxt: break
keys = sorted(keys)
say("|A| = %d" % len(keys))
vals = sorted(set((4*qv(k)) for k in keys))
say("q takes values (in quarters): %s" % [str(v) for v in vals])
def add(x, y): return tuple((a+b) % 2 for a, b in zip(x, y))
nz = [k for k in keys if k != zero]
order = {k: i for i, k in enumerate(nz)}
total = h2 = 0
for i, x in enumerate(nz):
    for y in nz[i+1:]:
        z = add(x, y)
        if z == zero: continue
        if order[x] > min(order[y], order[z]) or order[y] > order[z]: continue
        total += 1
        qs = sorted(int(4*qv(m)) for m in (x, y, z))
        if qs == [0, 0, 2] and 2*bv(x, y) == 1: h2 += 1
say("2-dim subspaces of A_{T_Co}: %d" % total)
say("isometric to V0 (q = 0,0,1/2 with b = 1/2): %d" % h2)
print("PYEXIT=0")
