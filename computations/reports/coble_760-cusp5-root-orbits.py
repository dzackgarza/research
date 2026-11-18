"""#760: the operation #370 delivered, run at cusp 5 -- three singleton orbits, and why that decides nothing.

sage-extensions#370 is closed and delivered the call this issue needed: on
``IsotropicVectorReductionImage``, ``root_class(vector)`` reads the class in K_I of a root written in
the ambient lattice, and ``root_class_orbits(roots, *, stabilizer_generators=None)`` returns the orbits
of a finite family of root classes with one transporter per class, checked by re-application.  It is
built on T_Co, not on T_En, which is why the preimage that failed on T_En succeeds here.

Run at cusp 5 on the three admissible roots -- Sterk's printed labels 12, 13, 14 -- the call returns
three singleton orbits.  By its own docstring that is not a proof of inequivalence: the acting family
is not certified to generate G_v at a primitive isotropic line.  This record makes that caveat concrete
rather than quoting it, by exhibiting an element of G_v that the acting family misses:

    g_{13<->14}, verified in coble_760-witness-13-14-run.txt and again in
    coble_760-gent-membership-run.txt as an integral, form-preserving isometry of T_En in Gent,
    fixing delta and eta_5 exactly.  It therefore lies in Gamma_Co,2 cap Stab(ZZ eta_5), its
    reduction lies in G_v, and inside K_5 it carries the class of 13 to the class of 14.

So the family the call acts with separates two classes that are Gamma_Co,2-equivalent, and its
singleton orbits carry no information about the pair (12,13).  What is missing is not the orbit
call but a *complete* generating family at a primitive isotropic line -- the certificate that
``generators_are_certified_complete`` reports as False (sage-extensions#312).  The failing expression
is the ``stabilizer_generators=`` argument below: the 36 generators
``supergroup().isotropic_stabilizer_generators(line)`` returns are not complete.

    usage: python3 computations/reports/coble_760-cusp5-root-orbits.py     (~4 min)
"""
import sys, time
sys.stdout.reconfigure(line_buffering=True)
t0 = time.time()
def say(*a): print("[%7.1fs]" % (time.time()-t0), *a, flush=True)

from sage_extensions.all import *   # noqa: F401,F403
from sage.all import ZZ, QQ, matrix, vector, identity_matrix
from sage.env import SAGE_VERSION

src = open('/repo/computations/reports/coble_760-witness-13-14.py').read()
exec(src.split('Hre = matrix')[0].split('print("the cusp symmetries')[0])   # G, delta, eta, R5, ip

lattice = NamedLattices.Tco
ring = lattice.base_ring()

print("the Gamma_Co,2-orbits of the three admissible roots at cusp 5, by sage-extensions#370")
print("Sage %s; sage-extensions at commit 1488acf" % SAGE_VERSION)
print()

def to_tco(vec):
    co = [int(x) for x in vec]
    assert co[0] == co[1], co          # in T_Co = delta^perp the e and f coefficients agree
    coeffs = {}
    if co[0]:
        coeffs["h"] = ring(co[0])
    for pos, name in ((2, "ep"), (3, "fp")):
        if co[pos]:
            coeffs[name] = ring(co[pos])
    for i in range(8):
        if co[4 + i]:
            coeffs["a%d" % (i + 1)] = ring(co[4 + i])
    return lattice.linear_combination(coeffs)

roots = [to_tco(R5[i]) for i in (11, 12, 13)]
print("roots 12, 13, 14 transported into T_Co: squares %s, all primitive %s"
      % ([lattice.q(v) for v in roots], all(v.is_primitive() for v in roots)))

say("building Gamma_Co,2 by discriminant_point_stabilizer on T_Co")
form = lattice.discriminant_group()
first = lattice.discriminant_class(lattice.primitive_dual(lattice.module_generator("ep")))
second = lattice.discriminant_class(lattice.primitive_dual(lattice.module_generator("fp")))
gamma = lattice.Aut().discriminant_point_stabilizer(frozenset({form.zero(), first, second, first + second}))
say("Gamma_Co,2 built")

eta5 = to_tco(Sterk.selected_isotropic_vectors()["Sterk_5"].to_vector())
image = gamma.isotropic_vector_reduction_image(eta5)
say("K_5 rank %s; the cusp vector is the line, its class is zero: %s"
      % (image.reduction().rank(), image.root_class(eta5) == image.reduction().zero()))

classes = [image.root_class(v) for v in roots]
stabilizer = tuple(image.subgroup().supergroup().isotropic_stabilizer_generators(image.line()))
print("the acting family: %d generators of the line stabilizer, reduced to K_5" % len(stabilizer))
say("calling root_class_orbits")
orbits = image.root_class_orbits(tuple(classes), stabilizer_generators=stabilizer)
print("returned %d orbits:" % len(orbits))
for orbit in orbits:
    members = tuple(orbit.index_set())
    names = [label for label, cls in zip(("12", "13", "14"), classes) if cls in members]
    print("   %d class(es): %s" % (len(members), names))
print()

# ---- the refutation of the acting family, from the committed witness
def refl(w):
    w = vector(ZZ, w)
    S = identity_matrix(QQ, 12) - (QQ(2) / ip(w, w)) * matrix(QQ, 12, 1, list(w)) * matrix(QQ, 1, 12, list(G * w))
    return matrix(ZZ, S)
def as_witness_13_14():
    """the diagram symmetry of coble_760-witness-13-14.py, rebuilt here"""
    import itertools
    Hre = matrix(ZZ, 14, 12, [list(r) for r in R5])
    L0 = [vector(ZZ, list(Hre.hermite_form(include_zero_rows=False).row(i)))
          for i in range(Hre.hermite_form(include_zero_rows=False).nrows())
          if any(x != 0 for x in Hre.hermite_form(include_zero_rows=False).row(i))]
    rows2 = matrix(ZZ, 14, 12, [list(G * vector(ZZ, r)) for r in R5])
    S2, _, V2 = rows2.smith_form()
    K = [vector(ZZ, [V2[i, j] for i in range(12)]) for j in range(12) if all(S2[k, j] == 0 for k in range(14))]
    L0q = matrix(QQ, matrix(ZZ, len(L0), 12, [list(v) for v in L0]))
    L0pinv = L0q.transpose() * (L0q * L0q.transpose()).inverse()
    basisq = matrix(QQ, matrix(ZZ, 12, 12, [list(v) for v in L0] + [list(v) for v in K]).transpose())
    SIG = [8, 6, 5, 4, 3, 2, 7, 1, 9, 10, 11, 12, 14, 13]
    Him = matrix(ZZ, 14, 12, [list(R5[SIG[i] - 1]) for i in range(14)])
    Cq = matrix(ZZ, matrix(QQ, Hre) * L0pinv)
    Dq = matrix(ZZ, matrix(QQ, Him) * L0pinv)
    F = (matrix(QQ, Cq).pseudoinverse() * matrix(QQ, Dq)).transpose()
    imgs = [sum((int(F[j, i]) * L0[j] for j in range(len(L0))), vector(ZZ, [0] * 12)) for i in range(len(L0))]
    img = matrix(ZZ, 12, 12, [list(v) for v in imgs] + [list(v) for v in K]).transpose()
    return matrix(ZZ, img * basisq.inverse())

U2, E8M = [2, 3], list(range(4, 12))
def in_span(c, block):
    gens = [vector(ZZ, list(G.column(j))) for j in range(12)]
    gens += [vector(ZZ, [1 if k == b else 0 for k in range(12)]) for b in block]
    return vector(ZZ, c) in (ZZ**12).submodule(gens)
def in_gent(m):
    C = matrix(QQ, m.transpose())
    return (all(x in ZZ for x in m.list())
            and matrix(QQ, 12, 12, list(m.transpose() * G * m)) == matrix(QQ, G)
            and all(in_span(list(C * vector(QQ, [1 if k == b else 0 for k in range(12)])), blk)
                    for blk in (U2, E8M) for b in blk))

g = as_witness_13_14()
dv, ev = vector(ZZ, delta), vector(ZZ, eta)
print("the exhibited element the acting family misses:")
print("   g_{13<->14}: integral %s, isometry %s, in Gent %s"
      % (all(x in ZZ for x in g.list()), matrix(QQ, 12, 12, list(g.transpose() * G * g)) == matrix(QQ, G), in_gent(g)))
print("   fixes delta %s, fixes eta_5 %s, swaps the lifts of 13 and 14 %s"
      % (g * dv == dv, g * ev == ev, g * vector(ZZ, R5[12]) == vector(ZZ, R5[13])))
print("   so its reduction lies in G_v and joins the classes of 13 and 14, which the call separates")
print()
print("VERDICT: three singleton orbits are not a decision.  The orbit call exists (#370, closed);")
print("what is missing is a complete generating family at a primitive isotropic line, the certificate")
print("sage-extensions#312 reports as False.  The pair (12,13) is not decided by this run.")
print()
print("PYEXIT=0")
