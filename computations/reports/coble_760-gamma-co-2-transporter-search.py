"""#760: a bounded search for a Gamma_Co,2-transporter of the class of 12 to that of 13 in K_5.

The pair (12,13) at cusp 5 is decided by whether some u in Gamma_Co,2 keeps the line ZZ eta_5 and
carries the class of r12 to the class of r13 in K_5 = eta_5^perp / ZZ eta_5.  This record decides
membership in Gamma_Co,2 exactly --- Gamma_Co,2 = rho_T^{-1}(P), P the stabilizer of the point
A_{U(2)} in A_{T_Co}, tested on the 2048 classes --- and searches for such a u among the products
g * s, where g is the raw 12<->13 witness restricted to T_Co (it keeps the line and moves the class,
but is outside Gamma_Co,2) and s ranges over words of length at most three in the 52 verified
generators of Stab_{O(T_Co)}(r12) that the provider returns (the family varies between runs: 44 here, 52 in another).

Result: of length 1, 2 and 3 pass the cheap tests (line kept, class carried), and
NONE of them lands in Gamma_Co,2.  That is a BOUND and not a decision: the stabilizer has infinite
index in O(T_Co), so a transporter may exist at longer length.  What would decide the pair is a
generating set of Gamma_Co,2 cap Stab_O(r12) cap Stab_O(Z eta_5) --- equivalently a complete
generating family at the primitive isotropic line, the certificate that ``generators_are_certified_
complete`` reports as False (the family the #370 call acts with is refuted by g_{13<->14}, which is in
G_v and joins 13 with 14 although the call separates them; coble_760-cusp5-root-orbits-run.txt).

    usage: python3 computations/reports/coble_760-gamma-co-2-transporter-search.py    (~30 s)
"""
import sys, pickle, time, itertools
sys.stdout.reconfigure(line_buffering=True)
t0 = time.time()
def say(*a): print("[%7.1fs]" % (time.time()-t0), *a, flush=True)

from sage_extensions.all import *   # noqa:F401,F403
from sage.all import ZZ, QQ, matrix, vector, identity_matrix, block_diagonal_matrix, CartanMatrix

Tco = NamedLattices.Tco; ring = Tco.base_ring()
labels = tuple(Tco.module_generating_set()); BAS = [Tco.module_generator(l) for l in labels]
NC = len(BAS)
Gc = matrix(ZZ, NC, NC, [[int(Tco.b(BAS[i], BAS[j])) for j in range(NC)] for i in range(NC)])
r12c = Tco.linear_combination({l: ring(int(x)) for l, x in zip(labels, [1,3,3,-2,1,2,2,1,0,0,0]) if int(x)})
r12lib = vector(ZZ, r12c.to_vector())
Ms = []
for s in Tco.Aut().vector_stabilizer_generators(r12c):
    m = matrix(ZZ, NC, NC, [list(s(b).to_vector()) for b in BAS]).transpose()
    if m * r12lib == r12lib and matrix(QQ, NC, NC, list(m.transpose() * Gc * m)) == matrix(QQ, Gc):
        Ms.append(m)
say("verified generators of Stab_{O(T_Co)}(r12): %d" % len(Ms))

U2 = matrix(ZZ, [[0, 2], [2, 0]]); C8 = CartanMatrix(["E", 8])
mine = block_diagonal_matrix(matrix(ZZ, [[2]]), U2, -2 * C8)
say("the library's Gram and mine agree: %s (det %s)" % (Gc == mine, Gc.det()))

co = dict(zip(labels, range(NC)))
def vec(d): return vector(ZZ, [d.get(l, 0) for l in labels])
r12 = vec({"h": 1, "ep": 3, "fp": 3, "a1": -2, "a2": 1, "a3": 2, "a4": 2, "a5": 1})
r13 = vec({"h": 1, "ep": 3, "fp": 4, "a1": -2, "a2": 2, "a3": 3, "a4": 4, "a5": 3, "a6": 2, "a7": 1})
src = open('/repo/computations/reports/coble_760-witness-13-14.py').read()
exec(src.split('Hre = matrix')[0].split('print("the cusp symmetries')[0])
ab0 = [int(x) for x in vector(ZZ, abar[0])][4:12]
eta = vec(dict({"h": 2}, **{"a%d" % (i + 1): ab0[i] for i in range(8) if ab0[i]}))
say("squares: r12 %s r13 %s eta %s" % (r12 * Gc * r12, r13 * Gc * r13, eta * Gc * eta))
assert eta * Gc * eta == 0

# ---- A_{T_Co} and the point test
S, U, V = Gc.smith_form(); d = [int(S[i, i]) for i in range(NC)]
Uq, Uinv = matrix(QQ, U), matrix(QQ, matrix(ZZ, U).inverse())
def key(a):
    b = Uq * vector(QQ, a); return tuple(0 if d[i] == 1 else int(b[i]) % d[i] for i in range(NC))
def lift(k): return vector(ZZ, Uinv * vector(QQ, k))
zero = tuple(0 for _ in range(NC))
def cls(l): return key(vector(ZZ, [1 if x == l else 0 for x in labels]))
point = {zero, cls("ep"), cls("fp")}
point = point | {key(vector(ZZ, lift(x)) + vector(ZZ, lift(y))) for x in list(point) for y in list(point)}
say("the point A_{U(2)}: %d classes" % len(point))
def in_GammaCo2(m):
    rho = matrix(QQ, matrix(ZZ, m.inverse()).transpose())
    return frozenset(key(rho * vector(ZZ, lift(k))) for k in point) == frozenset(point)
for name, m in (("identity", identity_matrix(ZZ, NC)), ("-identity", -identity_matrix(ZZ, NC))):
    say("  calibration %-9s in Gamma_Co,2: %s" % (name, in_GammaCo2(m)))

# ---- the raw transporter, restricted to T_Co (built from the T_En model)
h12 = vector(ZZ, [1 if k == 0 else 0 for k in range(12)]) + vector(ZZ, [1 if k == 1 else 0 for k in range(12)])
E2C = matrix(ZZ, NC, 12, [list(h12)] + [list(vector(ZZ, [1 if k == i else 0 for k in range(12)])) for i in range(2, 12)]).transpose()
rows = [list(G * vector(ZZ, v)) for v in (vector(ZZ, delta), R5[11], R5[12])]
Sv, _, Vv = matrix(ZZ, 3, 12, rows).smith_form()
K3 = [vector(ZZ, [Vv[i, j] for i in range(12)]) for j in range(12) if all(Sv[k, j] == 0 for k in range(3))]
Sb, _, Vb = matrix(ZZ, len(K3), 12, [list(G * vector(ZZ, k)) for k in K3]).smith_form()
P = [vector(ZZ, [Vb[i, j] for i in range(12)]) for j in range(12) if all(Sb[k, j] == 0 for k in range(len(K3)))]
T = matrix(QQ, [list(vector(ZZ, delta)), list(R5[11]), list(R5[12])]).transpose()
sw = []
for b in P:
    c = T.solve_right(vector(QQ, b))
    sw.append(int(c[0]) * vector(ZZ, delta) + int(c[2]) * vector(ZZ, R5[11]) + int(c[1]) * vector(ZZ, R5[12]))
PP = matrix(ZZ, 12, 12, [list(v) for v in P] + [list(v) for v in K3]).transpose()
im = matrix(ZZ, 12, 12, [list(v) for v in sw] + [list(v) for v in K3]).transpose()
g12 = matrix(ZZ, matrix(QQ, im) * matrix(QQ, PP).inverse())
cols = []
for j in range(NC):
    w = g12 * vector(ZZ, E2C.column(j))
    x = matrix(QQ, Gc).solve_right(vector(QQ, matrix(ZZ, E2C).transpose() * G * w))
    assert all(y in ZZ for y in x), "g does not restrict integrally"
    cols.append(vector(ZZ, [int(y) for y in x]))
g = matrix(ZZ, NC, NC, cols).transpose()
def mult(w):  # w a multiple of eta?
    k = None
    for i in range(NC):
        if eta[i] != 0:
            if w[i] % eta[i] != 0: return False
            cand = w[i] // eta[i]
            if all(w[j] == cand * eta[j] for j in range(NC)): return True
            return False
    return w.is_zero()
def cheap(m): return m * eta in (eta, -eta) and mult(m * r12 - r13)
say("g|T_Co: keeps the line %s, moves [12]->[13] %s, in Gamma_Co,2 %s"
    % (g * eta in (eta, -eta), mult(g * r12 - r13), in_GammaCo2(g)))

found = None
for depth in (1, 2, 3):
    hits = 0
    for word in itertools.product(range(len(Ms)), repeat=depth):
        s = matrix(ZZ, identity_matrix(ZZ, NC))
        for idx in word: s = s * Ms[idx]
        u = g * s
        if not cheap(u): continue
        hits += 1
        if in_GammaCo2(u):
            found = (word, u); break
    say("depth %d: %d words, %d pass the cheap tests, found %s" % (depth, len(Ms) ** depth, hits, found is not None))
    if found: break
print()
if found:
    word, u = found
    say("TRANSPORTER FOUND, word length %d: %s" % (len(word), word))
    say("   u is integral, form-preserving %s; in Gamma_Co,2 %s; keeps the eta_5 line %s; u[r12] = [r13] %s"
        % (matrix(QQ, NC, NC, list(u.transpose() * Gc * u)) == matrix(QQ, Gc), in_GammaCo2(u),
           u * eta in (eta, -eta), mult(u * r12 - r13)))
else:
    say("no transporter of word length <= 3 in the %d stabilizer generators" % len(Ms))
    say("(the family the provider returns varies between runs -- 44, 48, 52 in three runs -- and the")
print("PYEXIT=0")
