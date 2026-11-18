"""#760: the pair (12,13) is joined inside Gent, and what is still missing is one intersection's generators.

Two things this record settles, and one it pins.

(1) The provider at this checkout has the stabilizer-generator operations this issue's earlier records
    called missing: ``L.Aut().stabilizer(v)`` / ``vector_stabilizer_generators(v)`` return generators
    of Stab_{O(L)}(v) for an indefinite lattice (lattice_morphisms.py:4282, :4791), and
    ``discriminant_point_stabilizer(point)`` returns rho_L^{-1} of the stabilizer of a set of
    discriminant classes with generators (:3954).  Fifty-one generators of Stab_{O(T_En)}(r12) come
    back in about a minute, and each is verified here (integral, form-preserving, fixing r12).

(2) The pair (12,13) IS joined inside Gent.  Earlier records
    (coble_760-gent-membership-run.txt, coble_760-mod2-orbit-probe-run.txt) showed that the
    transposition built on the saturation of <delta, r12, r13> lies outside Gent, and the page drew
    from that only what it could: that the *witness* is outside Gent.  It does not follow that the
    pair is inequivalent, and it is not: multiplying that witness by a word in the stabilizer
    generators gives an integral, form-preserving, summand-preserving h with h(r12) = r13.  The word
    is found here, not quoted, because the generating family the provider returns varies between runs
    (fifty-one generators in one run, sixty in another), so a word is only meaningful against the
    family the same run produced.

    The search is the subspace-orbit test on the discriminant module.  With V0 = A_{U(2)} and M the
    summand-preserving subgroup, h = g*s lies in Gent exactly when rho(g s)(V0) = V0, so with s
    ranging over the stabilizer of r12 the target is rho(g)^{-1}(V0), reached by a word in the
    stabilizer's images.

    The discriminant action matters here and an earlier draft had it backwards.  For v in L*, the
    class of v is the class of the a-coordinate vector G v, so an isometry m acts on A_L by
    a |-> (m^{-1})^T a, not by m^T a.  The "preserves the summand" test is unaffected, because
    T(V0) = V0 exactly when T^{-1}(V0) = V0; the *transporter* condition is not, and with m^T the
    search targets the wrong subspace and finds nothing.

(3) What is still missing is one subgroup intersection's generators.  Gamma_Co,2 = R_Gent is the image
    of Stab_Gent(delta) (def:gamma-co-groups(5)), and h is in Gent but moves delta and eta_5, so it is
    not Gamma_Co,2-equivalence of the classes in K_5.  The element needed is a transporter in

        Stab_{O(T_En)}(r12)  cap  Stab_{O(T_En)}(delta)  cap  Stab_{O(T_En)}(Z eta_5),

    and the search that produced (2) runs on the first factor alone.  The library builds that
    intersection --- ``Aut.stabilizer(r12).stabilizer(delta).stabilizer(eta)`` returns an
    IntersectionSubgroups object, a pure predicate (predicate_subgroups.py:1378-1429) --- but it
    cannot produce its generators: ``group_generators()`` raises

        ValueError: {g in Orthogonal group O(Integral lattice of rank 12 and signature (2, 10)) :
        g lies in every selected subgroup} has no chosen resolution relative to Category of groups

    With those generators, the same subspace-orbit test that produced (2) decides the pair.  That call
    is the missing unit; this record names it and does not stand in for it.

    usage: python3 computations/reports/coble_760-transporter-in-gent.py
"""
import sys
sys.stdout.reconfigure(line_buffering=True)

from sage.all import ZZ, QQ, matrix, vector, identity_matrix
from sage.env import SAGE_VERSION   # noqa: E402

src = open('/repo/computations/reports/coble_760-witness-13-14.py').read()
exec(src.split('Hre = matrix')[0].split('print("the cusp symmetries')[0])   # G, N, delta, eta, R5, ip

from sage_extensions.all import Lattices   # noqa: E402

Mgram = matrix(ZZ, G)
L = Lattices(ZZ)([[int(G[i, j]) for j in range(N)] for i in range(N)])
def elt(v): return L([int(x) for x in v])
BAS = [L([1 if k == i else 0 for k in range(N)]) for i in range(N)]
def as_matrix(g): return matrix(ZZ, N, N, [list(g(b).to_vector()) for b in BAS]).transpose()

U2, E8M = [2, 3], list(range(4, N))
def in_span(c, block):
    gens = [vector(ZZ, list(Mgram.column(j))) for j in range(N)]
    gens += [vector(ZZ, [1 if k == b else 0 for k in range(N)]) for b in block]
    return vector(ZZ, c) in (ZZ**N).submodule(gens)
def is_gent(m):
    if not all(x in ZZ for x in m.list()): return False
    if matrix(QQ, N, N, list(m.transpose() * G * m)) != matrix(QQ, G): return False
    C = matrix(QQ, m.transpose())
    return all(in_span(list(C * vector(QQ, [1 if k == b else 0 for k in range(N)])), blk)
               for blk in (U2, E8M) for b in blk)

r12, r13 = vector(ZZ, R5[11]), vector(ZZ, R5[12])
dv, ev = vector(ZZ, delta), vector(ZZ, eta)

print("the transporter the pair (12,13) admits, and the one that is still missing")
print("Sage %s; sage-extensions at commit 1488acf on the local checkout" % SAGE_VERSION)
print()

# ---- (1) the provider's stabilizer generators
Aut = L.Aut()
stab = list(Aut.vector_stabilizer_generators(elt(r12)))
Ms = []
for s in stab:
    try: m = as_matrix(s)
    except Exception: continue
    if all(x in ZZ for x in m.list()) and matrix(QQ, N, N, list(m.transpose()*G*m)) == matrix(QQ, G) \
       and m * r12 == r12:
        Ms.append(m)
print("(1) Stab_{O(T_En)}(r12): %d generators returned, %d verified (integral, form-preserving, fixing r12)"
      % (len(stab), len(Ms)))
print()

# ---- (2) the witness h in Gent carrying r12 to r13
def rebuild_g():
    rows = [list(G * v) for v in (dv, r12, r13)]
    Sv, _, Vv = matrix(ZZ, 3, N, rows).smith_form()
    K3 = [vector(ZZ, [Vv[i, j] for i in range(N)]) for j in range(N) if all(Sv[k, j] == 0 for k in range(3))]
    S2b, _, V2b = matrix(ZZ, len(K3), N, [list(G * vector(ZZ, k)) for k in K3]).smith_form()
    P = [vector(ZZ, [V2b[i, j] for i in range(N)]) for j in range(N) if all(S2b[k, j] == 0 for k in range(len(K3)))]
    T = matrix(QQ, [list(dv), list(r12), list(r13)]).transpose()
    swapped = []
    for b in P:
        co = T.solve_right(vector(QQ, b))
        swapped.append(int(co[0]) * dv + int(co[2]) * r12 + int(co[1]) * r13)
    PP = matrix(ZZ, 12, 12, [list(v) for v in P] + [list(v) for v in K3]).transpose()
    im = matrix(ZZ, 12, 12, [list(v) for v in swapped] + [list(v) for v in K3]).transpose()
    return matrix(ZZ, matrix(QQ, im) * matrix(QQ, PP).inverse())

g = rebuild_g()
print("(2) the witness g of coble_760-witness-12-13: isometry %s, in Gent %s"
      % (matrix(QQ, N, N, list(g.transpose()*G*g)) == matrix(QQ, G), is_gent(g)))

# the discriminant module A = Z^12 / G Z^12, canonical keys through the Smith form
S, U, V = Mgram.smith_form()
d = [int(S[i, i]) for i in range(N)]
Uq, Uinv = matrix(QQ, U), matrix(QQ, matrix(ZZ, U).inverse())
def key(a):
    b = Uq * vector(QQ, a)
    return tuple(0 if d[i] == 1 else int(b[i]) % d[i] for i in range(N))
def lift(k): return vector(ZZ, Uinv * vector(QQ, k))
zero = tuple(0 for _ in range(N))
e = lambda i: tuple(1 if j == i else 0 for j in range(N))
def subspace_of(vecs):
    Sset = {zero}
    for v in vecs:
        Sset = Sset | {key(vector(ZZ, lift(w)) + vector(ZZ, lift(v))) for w in Sset}
    return frozenset(Sset)
def rho(m): return matrix(QQ, matrix(ZZ, m.inverse()).transpose())   # a |-> (m^{-1})^T a
def act(T_, k): return key(T_ * vector(ZZ, lift(k)))

V0 = subspace_of([e(2), e(3)])
target = subspace_of([matrix(QQ, g.transpose()) * vector(ZZ, e(2)),
                      matrix(QQ, g.transpose()) * vector(ZZ, e(3))])
print("    A_{U(2)} has %d classes; the target rho(g)^{-1}(A_{U(2)}) has %d" % (len(V0), len(target)))
acts = [rho(m) for m in Ms]
seen, frontier, word, depth = {V0: ()}, [V0], None, 0
while frontier and word is None:
    depth += 1
    new = []
    for W in frontier:
        for idx, T_ in enumerate(acts):
            img = frozenset(act(T_, k) for k in W)
            if img in seen:
                continue
            seen[img] = seen[W] + (idx,)
            if img == target:
                word = seen[img]
                break
            new.append(img)
        if word is not None:
            break
    frontier = new
print("    subspace orbit: %d classes of the Grassmannian reached at depth %d; target reached: %s"
      % (len(seen), depth, word is not None))
if word is not None:
    s = matrix(ZZ, identity_matrix(ZZ, N))
    for idx in reversed(word):
        s = s * Ms[idx]
    h = g * s
    print("    word %s (length %d): h integral %s, isometry %s, h(r12) == r13 %s, in Gent %s"
          % (word, len(word), all(x in ZZ for x in h.list()),
             matrix(QQ, N, N, list(h.transpose()*G*h)) == matrix(QQ, G), h * r12 == r13, is_gent(h)))
    print("    so roots 12 and 13 lie in one Gent-orbit: the pair is not separated by Gent")
    print("    h(delta) == delta: %s    h(eta_5) == +-eta_5: %s"
          % (h * dv == dv, h * ev in (ev, -ev)))
    print("    h therefore lies outside Stab_Gent(delta), whose image is Gamma_Co,2 = R_Gent, and")
    print("    outside the stabilizer of the eta_5 line: it does not decide the K_5 classes.")
print()

# ---- (3) the call that does not resolve
print("(3) the intersection whose generators are missing")
S1 = Aut.stabilizer(elt(r12))
S2 = S1.stabilizer(elt(dv))
S3 = S2.stabilizer(elt(ev))
print("    Aut.stabilizer(r12).stabilizer(delta).stabilizer(eta_5) builds a %s" % type(S3).__name__)
try:
    gens = S3.group_generators()
    print("    group_generators() returned %d generators" % len(list(gens)))
except Exception as exc:
    print("    group_generators() raises %s: %s" % (type(exc).__name__, str(exc).splitlines()[0]))
print()
print("    That is the missing unit: generators of Stab_O(r12) cap Stab_O(delta) cap Stab_O(Z eta_5).")
print("    With them the subspace-orbit test that produced (2) decides the pair, by the same argument:")
print("    the target is rho(g)^{-1}(A_{U(2)}) in A_{T_En}, reached by a word in the stabilizer's images.")
print()
print("PYEXIT=0")
