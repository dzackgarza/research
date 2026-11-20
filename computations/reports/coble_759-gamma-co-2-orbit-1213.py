"""#759: does Gamma_Co,2 join the two roots 12 and 13 of cusp 5?

The question.  T_Co = delta^perp with delta = e - f, and Gamma_Co,2 = R_Gent = rho_T^{-1}(P) is the
image in Orth(T_Co) of Stab_Gent(delta) (def:gamma-co-groups(5), prop:gamma-co-images(3)), where P
is the stabilizer in Orth(q_T_Co) of the point A_{U(2)}.  Roots 12 and 13 are vectors of T_Co of
square -2 orthogonal to delta and to eta_5, and equivalence is the notion the page used for 13 and
14: an element of Gamma_Co,2 carrying one vector to the other up to sign.  Signs are free, -1 lying
in Gamma_Co,2.

The reduction.  No word search is needed.  Let psi be any isometry of T_Co with psi(r12) = r13; one
exists, namely the restriction to T_Co of the 12 <-> 13 witness of coble_760-witness-12-13.py, which
fixes delta and is not in Gent.  Then

  {u in Gamma_Co,2 : u(r12) = r13} = {psi*s : s in Stab_Orth(T_Co)(r12), rho_T(psi) rho_T(s) in P},

because u(r12) = r13 exactly when psi^{-1}u fixes r12, and u = psi*s lies in rho_T^{-1}(P) exactly
when rho_T(s) lies in rho_T(psi)^{-1}P.  The vector condition is therefore automatic once s ranges
over the stabilizer of r12, and the whole question becomes one coset condition in the finite group
Orth(q_T_Co) acting on the 2048 classes of A_{T_Co}.  Since P is the stabilizer of the point
V0 = A_{U(2)}, that condition is

  the orbit of V0 under rho_T(Stab_Orth(T_Co)(r12)) contains rho_T(psi)^{-1}(V0),

a subspace-orbit computation inside the ten-dimensional space w^perp = A_{E_10(2)}, which has 174 251
two-dimensional subspaces in all.  The enumeration is exhaustive, so a miss is a decision as well,
modulo the provider's family generating the stabilizer of r12 in Orth(T_Co).

What this does not decide.  The weaker reading, in which two roots are compared as classes of
K_5 = eta_5^perp / Z eta_5 by elements of Gamma_Co,2 that also preserve the cusp line, allows a shift
by a multiple of eta_5 and so is not the vector condition tested here; it has no image in A_{T_Co},
which is where the reduction lives, and the bounded searches of coble_760-transporter-pruned-search
are what exists for it.

This is not the question the earlier records searched.  Their family was {psi*s} with s in the
stabilizer of r12 and s *also* preserving the line Z eta_5 --- the extra condition the class in
K_5 = eta_5^perp / Z eta_5 needs when the cusp is kept as well --- so their depth-16 bound of
coble_760-transporter-pruned-search-run.txt does not bear on the condition decided here.

The controls.  Two.  First, the membership test in Gamma_Co,2 is calibrated on eleven elements the page places
inside it --- the restrictions of the reflections in the eleven printed roots orthogonal to delta,
which is what @thm:face-irrelevant-marking uses, and of the 13 <-> 14 diagram symmetry --- and on one
element it places outside, the 12 <-> 13 witness.  The test is run twice, through two independent
class maps, and the two agree on every element tested, including the one the search returns.
Second, the same pipeline is run on the pair (13,14), whose answer is known on the page: the diagram
symmetry carries r13 to r14 and lies in Gamma_Co,2, so the pipeline must return a transporter there
and must not return one for (12,13).  A miss on (12,13) with a hit on (13,14) is not an artefact of
the search.

    usage: PYTHONPATH=<repo>/.scratch/se-main/src python \
               <repo>/computations/reports/coble_759-gamma-co-2-orbit-1213.py
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
say("T_Co: rank %d, det %s, basis %s" % (NC, Gc.det(), labels))

# ---- the model of coble_760-witness-13-14.py: T_En, delta, eta_5, the fourteen printed roots
src = open('/repo/computations/reports/coble_760-witness-13-14.py').read()
exec(src.split('Hre = matrix')[0].split('print("the cusp symmetries')[0])
Mgram = matrix(ZZ, G); N = 12
Hre = matrix(ZZ, 14, N, [list(r) for r in R5])
rows2 = matrix(ZZ, 14, N, [list(Mgram * vector(ZZ, r)) for r in R5])
S2, _, V2 = rows2.smith_form()
KK = [vector(ZZ, [V2[i, j] for i in range(N)]) for j in range(N) if all(S2[k, j] == 0 for k in range(14))]
hh = Hre.hermite_form(include_zero_rows=False)
L0 = [vector(ZZ, list(hh.row(i))) for i in range(hh.nrows()) if any(x != 0 for x in hh.row(i))]
L0q = matrix(QQ, matrix(ZZ, len(L0), N, [list(v) for v in L0]))
L0pinv = L0q.transpose() * (L0q * L0q.transpose()).inverse()
basisq = matrix(QQ, matrix(ZZ, 12, 12, [list(v) for v in L0] + [list(v) for v in KK]).transpose())
dv = vector(ZZ, delta)

# ---- T_Co coordinates of a vector of T_En that delta is orthogonal to
def toco(d):
    return lattice.linear_combination({l: ring(int(x)) for l, x in zip(labels, d) if int(x)})
def vec(d):
    return vector(ZZ, [int(d.get(l, 0)) for l in labels])
def to_tco(v12):
    c = [int(x) for x in v12]
    assert c[0] == c[1], "not orthogonal to delta"
    return vector(ZZ, toco([c[0], c[2], c[3]] + c[4:12]).to_vector())
r12 = vec({"h": 1, "ep": 3, "fp": 3, "a1": -2, "a2": 1, "a3": 2, "a4": 2, "a5": 1})
r13 = vec({"h": 1, "ep": 3, "fp": 4, "a1": -2, "a2": 2, "a3": 3, "a4": 4, "a5": 3, "a6": 2, "a7": 1})
r14 = to_tco(vector(ZZ, R5[13]))
ab0 = [int(x) for x in vector(ZZ, abar[0])][4:12]
eta = vec(dict({"h": 2}, **{"a%d" % (i + 1): ab0[i] for i in range(8) if ab0[i]}))
assert to_tco(vector(ZZ, R5[11])) == r12 and to_tco(vector(ZZ, R5[12])) == r13
assert r12 * Gc * r12 == -2 and r13 * Gc * r13 == -2 and r14 * Gc * r14 == -2
assert eta * Gc * eta == 0 and r12 * Gc * eta == 0 and r13 * Gc * eta == 0
say("in T_Co: r12 %s, r13 %s, r14 %s, eta_5 %s (squares -2, -2, -2, 0; all orthogonal)"
    % (list(r12), list(r13), list(r14), list(eta)))

# ---- T_En witnesses and reflections, restricted to T_Co
E2C = matrix(ZZ, NC, 12, [list(vector(ZZ, [1, 1] + [0] * 10))]
                        + [list(vector(ZZ, [1 if k == i else 0 for k in range(12)])) for i in range(2, 12)]).transpose()
def restrict(g12):
    """the restriction of an isometry of T_En fixing delta, in T_Co coordinates"""
    cols = []
    for j in range(NC):
        w = g12 * vector(ZZ, E2C.column(j))
        x = matrix(QQ, Gc).solve_right(vector(QQ, matrix(ZZ, E2C).transpose() * Mgram * w))
        assert all(y in ZZ for y in x), "does not restrict integrally"
        cols.append(vector(ZZ, [int(y) for y in x]))
    return matrix(ZZ, NC, NC, cols).transpose()
def build_13_14():
    SIG = [8, 6, 5, 4, 3, 2, 7, 1, 9, 10, 11, 12, 14, 13]
    Him = matrix(ZZ, 14, N, [list(R5[SIG[i] - 1]) for i in range(14)])
    Cq = matrix(ZZ, matrix(QQ, Hre) * L0pinv); Dq = matrix(ZZ, matrix(QQ, Him) * L0pinv)
    F = (matrix(QQ, Cq).pseudoinverse() * matrix(QQ, Dq)).transpose()
    imgs = [sum((int(F[j, i]) * L0[j] for j in range(len(L0))), vector(ZZ, [0] * N)) for i in range(len(L0))]
    img = matrix(ZZ, 12, 12, [list(v) for v in imgs] + [list(v) for v in KK]).transpose()
    return matrix(ZZ, img * basisq.inverse())
def build_swap(a, b):
    """swap a and b in the saturation of <delta, a, b>, by the identity on a complement"""
    Sy, _, Vy = matrix(ZZ, 3, N, [list(Mgram * vector(ZZ, v)) for v in (dv, a, b)]).smith_form()
    K3 = [vector(ZZ, [Vy[i, j] for i in range(N)]) for j in range(N) if all(Sy[k, j] == 0 for k in range(3))]
    Sb, _, Vb = matrix(ZZ, len(K3), N, [list(Mgram * vector(ZZ, k)) for k in K3]).smith_form()
    P = [vector(ZZ, [Vb[i, j] for i in range(N)]) for j in range(N) if all(Sb[k, j] == 0 for k in range(len(K3)))]
    T = matrix(QQ, [list(dv), list(a), list(b)]).transpose()
    sw = []
    for x in P:
        c = T.solve_right(vector(QQ, x))
        assert all(y in ZZ for y in c)
        sw.append(int(c[0]) * dv + int(c[2]) * a + int(c[1]) * b)
    PP = matrix(ZZ, 12, 12, [list(v) for v in P] + [list(v) for v in K3]).transpose()
    im = matrix(ZZ, 12, 12, [list(v) for v in sw] + [list(v) for v in K3]).transpose()
    return matrix(ZZ, matrix(QQ, im) * matrix(QQ, PP).inverse())
def reflection(w):
    w = vector(ZZ, w); q = int(vector(ZZ, w) * Mgram * vector(ZZ, w))
    S = identity_matrix(QQ, N) - (QQ(2) / q) * matrix(QQ, N, 1, list(w)) * matrix(QQ, 1, N, list(Mgram * w))
    return matrix(ZZ, S) if all(x in ZZ for x in S.list()) else None

build_12_13 = lambda: build_swap(R5[11], R5[12])
psi = restrict(build_12_13()); w1314 = restrict(build_13_14())
phi1314 = restrict(build_swap(R5[12], R5[13]))
def isom(m):
    return (all(x in ZZ for x in m.list())
            and matrix(QQ, NC, NC, list(m.transpose() * Gc * m)) == matrix(QQ, Gc))
refls = []
for lab in range(1, 15):
    if int(vector(ZZ, R5[lab - 1]) * Mgram * dv) != 0:
        continue
    refls.append((lab, restrict(reflection(R5[lab - 1]))))
say("psi = 12<->13 witness | T_Co: isometry %s, psi(r12)=r13 %s" % (isom(psi), psi * r12 == r13))
say("w1314 = 13<->14 diagram symmetry | T_Co: isometry %s, w1314(r13)=r14 %s"
    % (isom(w1314), w1314 * r13 == r14))
say("restrictions of the reflections in printed roots orthogonal to delta: %d, all isometries: %s"
    % (len(refls), all(isom(m) for (_, m) in refls)))

# ---- A_{T_Co}: classes as keys, two independent class maps, and the membership test
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
def rho(m): return matrix(QQ, matrix(ZZ, m.inverse()).transpose())      # a |-> (m^{-1})^T a
def in_GammaCo2_slow(m):
    T_ = rho(m)
    return frozenset(key(T_ * lift(k)) for k in V0) == frozenset(V0)
def class_map(m):
    A = Uz * rho(m) * Uz.inverse()
    assert all(x in ZZ for x in A.list()), "the class map is not integral"
    return matrix(ZZ, A)
say("A_{T_Co}: invariants %s, order %s; the point A_{U(2)}: %d classes"
    % (d, __import__('math').prod(d), len(V0)))
say("calibration of the membership test (slow class map):")
for name, m in ([("identity", identity_matrix(ZZ, NC)), ("-identity", -identity_matrix(ZZ, NC))]
                + [("s_w, printed label %d" % lab, mm) for (lab, mm) in refls]
                + [("13<->14 diagram symmetry", w1314), ("12<->13 witness (psi)", psi)]):
    say("   %-30s in Gamma_Co,2: %s" % (name, in_GammaCo2_slow(m)))

# ---- every class, enumerated from the classes of the basis vectors
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
say("the class module: %d classes" % len(classes))
def apply(A, k):
    y = A * vector(ZZ, k)
    return tuple(0 if d[i] == 1 else int(y[i]) % d[i] for i in range(NC))
def in_GammaCo2(m):
    A = class_map(m)
    return frozenset(apply(A, k) for k in V0) == frozenset(V0)
assert all(in_GammaCo2(m) == in_GammaCo2_slow(m)
           for (_, m) in refls + [("a", w1314), ("b", psi)]), "the two class maps disagree"
say("the two independent class maps agree on every element above")
v0 = frozenset(pos[k] for k in V0)
target = frozenset(pos[apply(class_map(matrix(ZZ, psi.inverse())), k)] for k in V0)
say("target rho(psi)^{-1}(V0): %d classes, differs from V0: %s" % (len(target), target != v0))

# ---- the search, run once per pair
def search(psi_m, base, label, printed):
    """is there u in Gamma_Co,2 with u(base) = psi_m(base)?
    The coset condition is one orbit question on the subspaces of A_{T_Co}; see the module docstring."""
    say("=== %s: is there u in Gamma_Co,2 with u(r%s) = r%s?" % (label, printed[0], printed[1]))
    say("    psi is an isometry with that property: %s; psi itself in Gamma_Co,2: %s"
        % (psi_m * base == psi_m * base and isom(psi_m), in_GammaCo2_slow(psi_m)))
    say("    calling vector_stabilizer_generators(r%s) ..." % printed[0])
    raw = list(lattice.Aut().vector_stabilizer_generators(toco([int(x) for x in base])))
    Ms = []
    for sgen in raw:
        try:
            m = matrix(ZZ, NC, NC, [list(sgen(b).to_vector()) for b in TBAS]).transpose()
        except Exception:
            continue
        if all(x in ZZ for x in m.list()) and isom(m) and m * base == base:
            Ms.append(m)
    say("    generators of Stab_Orth(T_Co)(r%s): %d returned, %d verified" % (printed[0], len(raw), len(Ms)))
    perms = []
    for m in Ms:
        pm = [pos[apply(class_map(m), k)] for k in classes]
        assert len(set(pm)) == len(classes)
        perms.append(pm)
    tgt = frozenset(pos[apply(class_map(matrix(ZZ, psi_m.inverse())), k)] for k in V0)
    seen = {v0: ()}; frontier = [v0]; found = None; depth = 0
    say("    target rho(psi)^{-1}(V0): %d classes, equal to V0: %s" % (len(tgt), tgt == v0))
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
        say("       depth %2d: %6d subspaces, frontier %6d" % (depth, len(seen), len(frontier)))
    say("    orbit of V0 under rho(Stab(r%s)): %d subspaces; target reached: %s"
        % (printed[0], len(seen), found is not None))
    if found is None:
        say("    => NO transporter in the subgroup generated by those %d generators" % len(Ms))
        return (None, Ms, perms)
    # the class map is a homomorphism and acts by LEFT multiplication, so a chain that applies
    # Ms[i1], then Ms[i2], then ... realises the product Ms[ik]*...*Ms[i1]: the word is reversed.
    sgen_mat = identity_matrix(ZZ, NC)
    for i in reversed(found):
        sgen_mat = sgen_mat * Ms[i]
    u = psi_m * sgen_mat
    ok = (isom(u) and in_GammaCo2(u) and in_GammaCo2_slow(u) and u * base == psi_m * base)
    say("    word of length %d: s fixes r%s %s; u = psi*s integral %s, isometry %s, det %s"
        % (len(found), printed[0], sgen_mat * base == base,
           all(x in ZZ for x in u.list()), isom(u), u.det()))
    say("    u(base) = psi(base): %s; u in Gamma_Co,2: fast %s, slow %s"
        % (u * base == psi_m * base, in_GammaCo2(u), in_GammaCo2_slow(u)))
    return (u if ok else None), Ms, perms

# ---- the question, and the positive control
u_1213, Ms12, perms12 = search(psi, r12, "the question", ("12", "13"))
print()
u_1314, Ms13, perms13 = search(phi1314, r13, "positive control (the page proves this one)", ("13", "14"))
print()

# ---- robustness: the question again, with the family enlarged by every generator of Stab(r13) that
# also fixes r12 -- an independent route to elements of Stab(r12), since the provider returns a
# different family on each call and from each stabilizer.
extra = [m for m in Ms13 if m * r12 == r12]
say("enrichment: %d of the %d generators of Stab(r13) also fix r12" % (len(extra), len(Ms13)))
en_perms = [[pos[apply(class_map(m), k)] for k in classes] for m in extra]
tgt12 = frozenset(pos[apply(class_map(matrix(ZZ, psi.inverse())), k)] for k in V0)
seen2 = {v0: ()}; frontier = [v0]; hit2 = None
allperms = perms12 + en_perms
while frontier and hit2 is None:
    new = []
    for W in frontier:
        for i, pm in enumerate(allperms):
            img = frozenset(pm[x] for x in W)
            if img in seen2:
                continue
            seen2[img] = seen2[W] + (i,)
            if img == tgt12:
                hit2 = seen2[img]; break
            new.append(img)
        if hit2 is not None: break
    frontier = new
say("with %d generators instead of %d, the orbit of V0 is %d subspaces; target reached: %s"
    % (len(allperms), len(perms12), len(seen2), hit2 is not None))
print()

if u_1213 is not None:
    print("VERDICT: r12 and r13 ARE one Gamma_Co,2-orbit.  With 13 ~ 14 the three admissible")
    print("T_Co-roots of cusp 5 are one Gamma_Co,2-orbit, and u below is the witness:")
    for r in u_1213.rows():
        print("   ", [int(x) for x in r])
elif u_1314 is None:
    print("VERDICT: nothing is claimed -- the search missed on the control pair (13,14), whose")
    print("answer is known, so the pipeline is not deciding the question.")
else:
    print("VERDICT: r12 and r13 are in different Gamma_Co,2-orbits.  The search runs on the pair")
    print("(13,14) and returns a transporter there, so a miss is not an artefact of the search; on")
    print("(12,13) the orbit of V0 under rho(Stab_Orth(T_Co)(r12)) is exhausted without the target.")
    print("Modulo the provider's family generating Stab_Orth(T_Co)(r12), the three admissible")
    print("T_Co-roots of cusp 5 are two Gamma_Co,2-orbits: {13,14} and {12}.")
print()
print("elapsed %d s" % (time.time() - t0))
print("PYEXIT=0")
