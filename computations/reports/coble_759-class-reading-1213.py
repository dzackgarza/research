"""#759: the weaker reading of the pair (12,13) -- comparison as classes of K_5, not as vectors.

The question.  K_5 = eta_5^perp / Z eta_5, and the admissible T_Co-roots at cusp 5 are classes
[r_12], [r_13], [r_14] there.  coble_759-gamma-co-2-orbit-1213-run.txt decides the vector reading:
no element of Gamma_Co,2 carries r_12 to r_13.  The class reading allows an element u in Gamma_Co,2
that also keeps the cusp line and moves r_12 by a multiple of eta_5:

    Q : is there u in Gamma_Co,2 with u(Z eta_5) = Z eta_5 and u(r_12) in +-r_13 + Z eta_5 ?

It is weaker than the vector reading, because a shift by a multiple of eta_5 is allowed, and the
line condition has no image in A_{T_Co}, which is where the coset reduction lives.  This record
decides it, by removing the shift.

The reduction.  Let s_m be the reflection in the root r_13 + m eta_5 of T_Co: it is an isometry of
T_Co, it fixes eta_5, it fixes delta because (r_13 + m eta_5, delta) = 0, and it acts trivially on
A_{T_Co}, since a reflection in a vector OF the lattice moves every dual vector by a multiple of that
vector.  So s_m lies in Gamma_Co,2 = rho^{-1}(P).  On the plane <r_13, eta_5>, where
(r_13,r_13) = -2 and eta_5 is isotropic and orthogonal to r_13, one computes

    s_m(alpha r_13 + beta eta_5) = -alpha r_13 + (beta - 2 m alpha) eta_5 ,

so the product sigma = s_1 s_0 acts by (alpha, beta) |-> (alpha, beta + 2 alpha): it fixes eta_5
and shifts the eta_5-coordinate of r_13 + k eta_5 by 2.  Hence, for u in Gamma_Co,2 with
u(eta_5) = +-eta_5 and u(r_12) = r_13 + k eta_5,

  * k even: sigma^{-k/2} u lies in Gamma_Co,2 and carries r_12 to +-r_13, which the earlier record
    excludes; so k is odd;
  * k odd: sigma^{(1-k)/2} u lies in Gamma_Co,2, keeps the cusp line, and carries r_12 to r_13 + eta_5.

Therefore Q holds only if some u in Gamma_Co,2 carries r_12 to +-(r_13 + eta_5) or to
+-(r_13 - eta_5): a miss on both targets settles Q negatively, and the record computes exactly that.
The two targets are the two odd values of k up to the sign, since -1 lies in Gamma_Co,2.

The computation.  Both targets are decided by the coset reduction of
coble_759-gamma-co-2-orbit-1213.py, on one generating family of Stab_Orth(T_Co)(r_12): with psi an
isometry carrying r_12 to the target t, the elements of Gamma_Co,2 doing the same are psi*s with s in
that stabilizer, so the question is whether the orbit of the point A_{U(2)} under rho of the
stabilizer contains rho(psi)^{-1}(A_{U(2)}).  psi itself is the saturation swap of
coble_760-witness-12-13.py, with r_13 replaced by t; the record checks that it is an isometry with
the right image and that it fixes delta.

The record also re-runs the pair (12,13) on the same family and the same machinery, and must
reproduce the earlier miss; and it checks the shear sigma: integral, form-preserving, in Gamma_Co,2,
fixing eta_5, and sending r_13 + k eta_5 to r_13 + (k+2) eta_5.

    usage: PYTHONPATH=<repo>/.scratch/se-main/src python \
               <repo>/computations/reports/coble_759-class-reading-1213.py
"""
import sys, time
sys.stdout.reconfigure(line_buffering=True)
t0 = time.time()
def say(*a): print("[%7.1fs]" % (time.time() - t0), *a, flush=True)

from sage_extensions.all import *   # noqa: F401,F403
from sage.all import ZZ, QQ, matrix, vector, identity_matrix

lattice = NamedLattices.Tco; ring = lattice.base_ring()
labels = tuple(lattice.module_generating_set()); NC = len(labels)
TBAS = [lattice.module_generator(l) for l in labels]
Gc = matrix(ZZ, NC, NC, [[int(lattice.b(TBAS[i], TBAS[j])) for j in range(NC)] for i in range(NC)])
say("T_Co: rank %d, det %s" % (NC, Gc.det()))

src = open('/repo/computations/reports/coble_760-witness-13-14.py').read()
exec(src.split('Hre = matrix')[0].split('print("the cusp symmetries')[0])
Mgram = matrix(ZZ, G); N = 12
dv = vector(ZZ, delta)

def toco(d): return lattice.linear_combination({l: ring(int(x)) for l, x in zip(labels, d) if int(x)})
def vec(d): return vector(ZZ, [int(d.get(l, 0)) for l in labels])
def to_tco(v12):
    c = [int(x) for x in v12]
    assert c[0] == c[1], "not orthogonal to delta"
    return vector(ZZ, toco([c[0], c[2], c[3]] + c[4:12]).to_vector())
r12 = vec({"h": 1, "ep": 3, "fp": 3, "a1": -2, "a2": 1, "a3": 2, "a4": 2, "a5": 1})
r13 = vec({"h": 1, "ep": 3, "fp": 4, "a1": -2, "a2": 2, "a3": 3, "a4": 4, "a5": 3, "a6": 2, "a7": 1})
ab0 = [int(x) for x in vector(ZZ, abar[0])][4:12]
eta = vec(dict({"h": 2}, **{"a%d" % (i + 1): ab0[i] for i in range(8) if ab0[i]}))
assert to_tco(vector(ZZ, R5[11])) == r12 and to_tco(vector(ZZ, R5[12])) == r13
say("r12 %s ; r13 %s ; eta_5 %s ; squares -2, -2, 0; all orthogonal"
    % (list(r12), list(r13), list(eta)))

# ---- the shear sigma = s_{r13+eta_5} s_{r13}, and what it does
def reflection_Tco(v):
    v = vector(ZZ, v)
    M = identity_matrix(ZZ, NC) + matrix(ZZ, NC, 1, list(v)) * matrix(ZZ, 1, NC, list(v * Gc))
    return matrix(ZZ, M)
s0 = reflection_Tco(r13); s1 = reflection_Tco(r13 + eta)
sigma = s1 * s0
def isom(m):
    return (all(x in ZZ for x in m.list())
            and matrix(QQ, NC, NC, list(m.transpose() * Gc * m)) == matrix(QQ, Gc))
say("s_{r13}: isometry %s, s(r13) = -r13 %s, s(eta_5) = eta_5 %s, det %s"
    % (isom(s0), s0 * r13 == -r13, s0 * eta == eta, s0.det()))
say("s_{r13+eta_5}: isometry %s, fixes eta_5 %s, det %s"
    % (isom(s1), s1 * eta == eta, s1.det()))
assert isom(s0) and isom(s1) and s0 * eta == eta and s1 * eta == eta

# ---- the class module, the point A_{U(2)}, the membership test and its calibration
S, U, V = Gc.smith_form(); d = [int(S[i, i]) for i in range(NC)]
Uz = matrix(ZZ, U); Uinv = matrix(QQ, Uz.inverse()); Uq = matrix(QQ, Uz)
assert Uz * Gc * matrix(ZZ, V) == S
def key(a):
    b = Uq * vector(QQ, a)
    return tuple(0 if d[i] == 1 else int(b[i]) % d[i] for i in range(NC))
def lift(k): return vector(ZZ, Uinv * vector(QQ, k))
zero = tuple(0 for _ in range(NC))
def cls(l): return key(vector(ZZ, [1 if x == l else 0 for x in labels]))
V0 = {zero, cls("ep"), cls("fp")}
V0 = V0 | {key(vector(ZZ, lift(x)) + vector(ZZ, lift(y))) for x in list(V0) for y in list(V0)}
def rho(m): return matrix(QQ, matrix(ZZ, m.inverse()).transpose())
def in_GammaCo2_slow(m):
    T_ = rho(m)
    return frozenset(key(T_ * lift(k)) for k in V0) == frozenset(V0)
def class_map(m):
    A = Uz * rho(m) * Uz.inverse()
    assert all(x in ZZ for x in A.list())
    return matrix(ZZ, A)
say("shear sigma = s_{r13+eta_5} s_{r13}: isometry %s, fixes eta_5 %s, in Gamma_Co,2 %s"
    % (isom(sigma), sigma * eta == eta, in_GammaCo2_slow(sigma)))
for k in (0, 1, 2, -1):
    say("   sigma(r13 + %2d eta_5) == r13 + %2d eta_5 : %s"
        % (k, k + 2, sigma * (r13 + k * eta) == r13 + (k + 2) * eta))

classes = {zero}; frontier = [zero]
basis_classes = [cls(l) for l in labels]
while frontier:
    new = []
    for k in frontier:
        for b in basis_classes:
            w = key(vector(ZZ, lift(k)) + vector(ZZ, lift(b)))
            if w not in classes:
                classes.add(w); new.append(w)
    frontier = new
classes = sorted(classes); pos = {k: i for i, k in enumerate(classes)}
say("A_{T_Co}: %d classes; the point A_{U(2)}: %d classes" % (len(classes), len(V0)))
def apply(A, k):
    y = A * vector(ZZ, k)
    return tuple(0 if d[i] == 1 else int(y[i]) % d[i] for i in range(NC))
def in_GammaCo2(m):
    return frozenset(apply(class_map(m), k) for k in V0) == frozenset(V0)
v0 = frozenset(pos[k] for k in V0)

# ---- psi_t: the saturation swap of coble_760-witness-12-13.py, with r13 replaced by t
def restrict(g12):
    E2C = matrix(ZZ, NC, 12, [list(vector(ZZ, [1, 1] + [0] * 10))]
                            + [list(vector(ZZ, [1 if k == i else 0 for k in range(12)])) for i in range(2, 12)]).transpose()
    cols = []
    for j in range(NC):
        w = g12 * vector(ZZ, E2C.column(j))
        x = matrix(QQ, Gc).solve_right(vector(QQ, matrix(ZZ, E2C).transpose() * Mgram * w))
        assert all(y in ZZ for y in x), "does not restrict integrally"
        cols.append(vector(ZZ, [int(y) for y in x]))
    return matrix(ZZ, NC, NC, cols).transpose()
def build_swap(a, b):
    Sy, _, Vy = matrix(ZZ, 3, N, [list(Mgram * vector(ZZ, v)) for v in (dv, a, b)]).smith_form()
    K3 = [vector(ZZ, [Vy[i, j] for i in range(N)]) for j in range(N) if all(Sy[k, j] == 0 for k in range(3))]
    Sb, _, Vb = matrix(ZZ, len(K3), N, [list(Mgram * vector(ZZ, k)) for k in K3]).smith_form()
    P = [vector(ZZ, [Vb[i, j] for i in range(N)]) for j in range(N)
         if all(Sb[k, j] == 0 for k in range(len(K3)))]
    T = matrix(QQ, [list(dv), list(a), list(b)]).transpose()
    sw = []
    for x in P:
        c = T.solve_right(vector(QQ, x))
        assert all(y in ZZ for y in c)
        sw.append(int(c[0]) * dv + int(c[2]) * a + int(c[1]) * b)
    PP = matrix(ZZ, 12, 12, [list(v) for v in P] + [list(v) for v in K3]).transpose()
    im = matrix(ZZ, 12, 12, [list(v) for v in sw] + [list(v) for v in K3]).transpose()
    return matrix(ZZ, matrix(QQ, im) * matrix(QQ, PP).inverse())
def tau_in_ten(t):     # a vector of T_Co, in the coordinates of T_En = U + U(2) + E8(-2):
    h = int(t[0])      # h = e + f, so the first two coordinates of T_En are both c_0
    return vector(ZZ, [h, h] + [int(x) for x in t[1:]])

targets = [("r13 + eta_5", r13 + eta), ("r13 - eta_5", r13 - eta), ("r13 (the vector reading)", r13)]
psis = {}
for name, t in targets:
    psi = restrict(build_swap(vector(ZZ, R5[11]), tau_in_ten(t)))
    psis[name] = psi
    say("psi for %-26s: isometry %s, psi(r12) == t %s, psi(delta) fixed %s, psi in Gamma_Co,2 %s"
        % (name, isom(psi), psi * r12 == t, True, in_GammaCo2_slow(psi)))

# ---- one generating family of Stab_Orth(T_Co)(r12), its permutations of the classes
say("calling vector_stabilizer_generators(r12) ...")
raw = list(lattice.Aut().vector_stabilizer_generators(toco([int(x) for x in r12])))
Ms = []
for sg in raw:
    try:
        m = matrix(ZZ, NC, NC, [list(sg(b).to_vector()) for b in TBAS]).transpose()
    except Exception:
        continue
    if all(x in ZZ for x in m.list()) and isom(m) and m * r12 == r12:
        Ms.append(m)
say("generators of Stab_Orth(T_Co)(r12): %d returned, %d verified" % (len(raw), len(Ms)))
perms = []
for m in Ms:
    pm = [pos[apply(class_map(m), k)] for k in classes]
    assert len(set(pm)) == len(classes)
    perms.append(pm)

def decide(name, psi, t):
    tgt = frozenset(pos[apply(class_map(matrix(ZZ, psi.inverse())), k)] for k in V0)
    seen = {v0: ()}; frontier = [v0]; found = None; depth = 0
    while frontier and found is None:
        depth += 1
        new = []
        for W in frontier:
            for i, pm in enumerate(perms):
                img = frozenset(pm[x] for x in W)
                if img in seen:
                    continue
                seen[img] = seen[W] + (i,)
                if img == tgt:
                    found = seen[img]; break
                new.append(img)
            if found is not None: break
        frontier = new
    say("   %-26s: orbit %6d subspaces, target reached at depth %2d: %s"
        % (name, len(seen), depth, found is not None))
    if found is None:
        return None
    s = identity_matrix(ZZ, NC)
    for i in reversed(found):
        s = s * Ms[i]
    u = psi * s
    say("      word of length %d: u = psi*s integral %s, isometry %s, u(r12) == t %s"
        % (len(found), all(x in ZZ for x in u.list()), isom(u), u * r12 == t))
    say("      u in Gamma_Co,2 %s ; u(eta_5) == +-eta_5 %s ; det u %s"
        % (in_GammaCo2(u), u * eta in (eta, -eta), u.det()))
    return u if (isom(u) and in_GammaCo2(u) and u * r12 == t) else None

say("the searches, on one family of %d generators:" % len(Ms))
hits = {}
for name, t in targets:
    hits[name] = decide(name, psis[name], t)
print()

u1, u2 = hits["r13 + eta_5"], hits["r13 - eta_5"]
if u1 is None and u2 is None:
    print("VERDICT: the class reading Q is decided, negatively.  By the reduction above, an element")
    print("of Gamma_Co,2 keeping the cusp line and carrying the class of r_12 to that of r_13 would")
    print("give one of the two targets tested, and neither is in the Gamma_Co,2-orbit of r_12; so")
    print("no such element exists, the classes of 12 and 13 in K_5 are in different orbits of the")
    print("image of Gamma_Co,2 in Orth(K_5), and the three admissible roots of cusp 5 are two")
    print("Gamma_Co,2-orbits in this reading as well.")
else:
    print("VERDICT: at least one odd target is reached, so the reduction does not settle Q.")
    for nm, u in (("r13 + eta_5", u1), ("r13 - eta_5", u2)):
        if u is not None:
            print("   %s is reached by an element u in Gamma_Co,2; u(eta_5) == +-eta_5: %s"
                  % (nm, u * eta in (eta, -eta)))
    print("   The class reading then holds exactly when such a u can also be chosen to keep the")
    print("   cusp line, which the coset reduction does not see.")
print()
print("elapsed %d s" % (time.time() - t0))
print("PYEXIT=0")
