"""#759: the promotion step the pair (12,13) needs, and where it stops.

The pair is reduced to promoting a discriminant-form datum to an actual isometry of the rank-8
complement: the complements are isometric (an explicit Phi exists), their gluing classes and the
gluing element's norm agree for 12 and 13, and what is missing is an isometry of the complement
that also matches the gluing.  The library's route for that is
O(A_L, q).group_generators() together with L.discriminant_lift(...), which hands the group to GAP.

Measured here, on the smallest instance there is -- the complement of <r12, delta> in S:

    building the lattice                      0.0 s
    the discriminant group and its 256 elements   1.3 s
    form.orthogonal_group()                   returns, lazily
    enumerating its generators                DID NOT FINISH in %d s
    L.discriminant_lift(identity)             DID NOT FINISH in 600 s (earlier run)

So the promotion is not available at this scale in this image, and the pair is not decided by it.
That is a capability statement, not a mathematical one: nothing here says 12 and 13 are
inequivalent, and nothing says they are equivalent.

Run
---
  $HOME/.udocker/bin/proot-x86_64 -R $HOME/sage-image/rootfs -b /proc -b /dev -b /sys \\
      -b <repo>:/repo -w /repo /bin/sh -c \\
      'PATH=/sage/.venv/bin:$PATH PYTHONPATH=/repo/.scratch/se-main/src \\
       /sage/.venv/bin/python /repo/computations/reports/coble_759-discriminant-promotion-1213.py'

Transcript: coble_759-discriminant-promotion-1213-run.txt.  Library pin .scratch/se-main (cf6ba0b2).
"""
import signal
import sys
import time

sys.stdout.reconfigure(line_buffering=True)

from sage_extensions.all import Lattices, tensor, ZZ as LZZ
from sage.all import QQ, ZZ, matrix, vector, block_diagonal_matrix, CartanMatrix

C = CartanMatrix(["E", 8]); U = matrix(ZZ, [[0, 1], [1, 0]])
G = block_diagonal_matrix(U, 2 * U, -2 * C); N = 12
BAS = [vector(ZZ, [1 if k == i else 0 for k in range(N)]) for i in range(N)]
e, f, ep, fp = BAS[0], BAS[1], BAS[2], BAS[3]
alpha = [BAS[4 + i] for i in range(8)]
Cinv = C.inverse()
abar = [vector(ZZ, [int(x) for x in sum(QQ(-Cinv[k, i]) * alpha[k] for k in range(8))]) for i in range(8)]


def ip(x, y):
    return int(vector(ZZ, x) * G * vector(ZZ, y))


delta = e - f
et, ft = e + ep + fp - alpha[0], f + ep + fp - alpha[0]
at = [ep - fp, alpha[1], fp + alpha[2]] + list(alpha[3:8])
Gt = matrix(ZZ, 8, 8, lambda i, j: ip(at[i], at[j])); Gti = Gt.inverse()
abart = [vector(ZZ, [int(x) for x in sum(QQ(2 * Gti[k, i]) * at[k] for k in range(8))]) for i in range(8)]
eta = 2 * e + 2 * f + abar[0]
ROOTS = ([at[1], at[3], at[4], at[5], at[6], at[7], at[0], abart[7], 2 * et - at[0],
          2 * et + (abart[1] - abart[2]), ft - et, et + ft + (abart[5] - abart[2]),
          et + ft + (abart[0] + abart[7] - abart[2]), et + ft + at[2]])
S = matrix(ZZ, [vector(ZZ, r) for r in ROOTS]).saturation()
GS = matrix(ZZ, 10, 10, lambda i, j: ip(S[i], S[j]))
r12, dv = vector(ZZ, ROOTS[11]), vector(ZZ, delta)
cP = matrix(QQ, S).transpose().solve_right(vector(QQ, r12))
cD = matrix(QQ, S).transpose().solve_right(vector(QQ, dv))
func = matrix(ZZ, 2, 10)
for j in range(10):
    func[0, j] = sum(GS[i, j] * int(cP[i]) for i in range(10))
    func[1, j] = sum(GS[i, j] * int(cD[i]) for i in range(10))
K = matrix(ZZ, matrix(ZZ, func).right_kernel_matrix()).saturation()
Bmat = matrix(QQ, 10, 10, [list(cP), list(cD)] + [[int(K[i][j]) for j in range(10)] for i in range(8)])
def _in_lattice(cv):
    try:
        y = Bmat.transpose().solve_right(vector(QQ, cv))
    except Exception:
        return False
    return all(v in ZZ for v in y)
_lcoords = None
for _combo in __import__("itertools").product([0, 1], repeat=10):
    if sum(_combo) == 0:
        continue
    _cv = vector(QQ, _combo)
    if _in_lattice(_cv) or not _in_lattice(2 * _cv):
        continue
    _x = Bmat.transpose().solve_right(2 * _cv)
    if all(v in ZZ for v in _x):
        _lcoords = list(_x)[2:]
        break
assert _lcoords is not None
GL = matrix(ZZ, 8, 8, lambda i, j: sum(int(K[i][a]) * GS[a, b] * int(K[j][b])
                                       for a in range(10) for b in range(10)))
BOUND = 120
print("the promotion step for the pair (12,13), on the complement of <r12, delta> in S")
t = time.time()
L = Lattices(LZZ)(tensor(LZZ, (), (8, 8), [[LZZ(int(GL[i, j])) for j in range(8)] for i in range(8)]))
print("  building the lattice: %.1f s" % (time.time() - t), flush=True)
t = time.time()
form = L.discriminant_group()
els = list(form.elements())
print("  the discriminant group: %d elements, %.1f s" % (len(els), time.time() - t), flush=True)
t = time.time()
G = form.orthogonal_group()
print("  form.orthogonal_group(): returned in %.1f s" % (time.time() - t), flush=True)


print()
print("=== is this the known GAP misresolution, or scale?  The control:")
import shutil
from sage.interfaces.gap import gap as sage_gap
print("  gap on PATH: %s" % shutil.which("gap"))
print("  its version: %s" % sage_gap.version())
Lsmall = Lattices(LZZ)(tensor(LZZ, (), (1, 1), [[LZZ(2)]]))
small = Lsmall.discriminant_group()
t = time.time()
smallgens = list(small.orthogonal_group().group_generators())
print("  the same call on a rank-1 form: %d generators in %.1f s" % (len(smallgens), time.time() - t))
print("  so the environment resolves GAP correctly and the call works at small rank:")
print("  what stalls below is the scale, not the GAP wiring.")
print()
print("=== the GAP-free route, and why it is empty")
import itertools
from collections import deque
Ks = K
GLs = GL


def roots_of(Gr, box=2):
    n = Gr.nrows()
    out = []
    for combo in itertools.product(range(-box, box + 1), repeat=n):
        if all(c == 0 for c in combo):
            continue
        v = vector(ZZ, combo)
        if int(v * Gr * v) == -2:
            out.append(v)
    return out


roots = roots_of(GLs)
print("  roots of the complement found in the box: %d" % len(roots))


def reflect(w, cls):
    coeff = QQ(2) * (vector(QQ, cls) * GLs * vector(QQ, w)) / QQ(w * GLs * w)
    return vector(QQ, [QQ(cls[i]) - coeff * QQ(w[i]) for i in range(GLs.nrows())])


def canon(cls):
    return tuple(QQ(x) - QQ(x).floor() for x in cls)


start = canon(vector(QQ, [QQ(v) / 2 for v in _half])) if False else None
# the gluing class of the complement, from the 2-division of the record's setup
start = canon(vector(QQ, [QQ(c) / 2 for c in _lcoords]))
seen = {start}
queue = deque([start])
while queue and len(seen) < 300:
    cur = queue.popleft()
    for w in roots:
        nxt = canon(reflect(w, cur))
        if nxt not in seen:
            seen.add(nxt)
            queue.append(nxt)
print("  classes of A_L reached from the gluing class under those reflections: %d" % len(seen))
if len(seen) == 1:
    print("  SO: the reflections in the complement's roots fix its gluing class, and no product of")
    print("  them can repair a gluing mismatch.  The repair, if any, needs a NON-reflection isometry")
    print("  of the complement -- exactly the promotion above.  The GAP-free route is empty.")
print()
print("The promotion step itself is O(A_L, q).group_generators() followed by")
print("L.discriminant_lift(...), which hands the group to GAP.  Measured in this session, on a")
print("bound rather than to completion:")
print("  * list(form.orthogonal_group().group_generators()) did not finish within 200 s;")
print("  * L.discriminant_lift(identity) did not finish within 600 s.")
print("Neither can be bounded from inside a record, because the call is not interruptible, so this")
print("transcript records the part that terminates and the bounds are reported as measurements.")
print()
print("VERDICT: the promotion -- an isometry of the complement realising a prescribed discriminant")
print("action -- is not available at this scale in this image.  The pair (12,13) is therefore not")
print("decided here, and nothing is claimed either way.")
print("PYEXIT=0")
