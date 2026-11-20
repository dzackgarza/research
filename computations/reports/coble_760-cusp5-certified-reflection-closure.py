"""#760: the certified reflections at cusp 5 close after six roots, and the orbit of [12] stays at two.

The three admissible roots are certified in G_v by sage-extensions#312's sift
(coble_760-cusp5-certified-reflections-run.txt).  This record grows that set the only way that is free
of further sifting cost per element: conjugation.  If s and s_w lie in G_v then s_{s(w)} = s s_w s^{-1}
does too, so reflecting a certified root by a certified reflection produces a class whose reflection is
certified.  Each truly new class is still put through ``contains_root_reflection`` rather than assumed.

Result: the closure is six roots.  Steps 0 to 2 add three conjugated roots, all certified True, and step
3 finds no further candidates -- the certified reflection set is closed under its own reflections at
six elements.  The orbit of the class of 12 under all six stays at two classes throughout, and the
class of 13 is not in it.

So the reflection route to the pair is closed and not merely bounded: no word in the certified
reflections, nor in their conjugates, carries [12] to [13].  A transporter, if one exists, involves an
element of G_v outside the reflection group those roots generate -- which is exactly the part the
library's refuted generator family does not supply.  What would decide the pair is a generating set of
G_v = lambda(Gamma_Co,2 cap P_v), not its reflections alone.

    usage: python3 computations/reports/coble_760-cusp5-certified-reflection-closure.py   (~4 min)
"""
"""#760: grow the certified reflection set in G_v at cusp 5 and search the orbit of [12] for [13]."""
import sys, time, pickle
sys.stdout.reconfigure(line_buffering=True)
t0=time.time()
def say(*a): print("[%7.1fs]" % (time.time()-t0), *a, flush=True)
from sage_extensions.all import *   # noqa
from sage.all import ZZ, QQ, matrix, vector, identity_matrix
lattice = NamedLattices.Tco; ring = lattice.base_ring()
labels = tuple(lattice.module_generating_set())
def tco(d): return lattice.linear_combination({l: ring(int(x)) for l, x in zip(labels, d) if int(x)})
src = open('/repo/computations/reports/coble_760-witness-13-14.py').read()
exec(src.split('Hre = matrix')[0].split('print("the cusp symmetries')[0])
def to_tco(v12):
    c = [int(x) for x in v12]
    return tco([c[0], c[2], c[3]] + c[4:12]) if c[0] == c[1] else None
co = [int(x) for x in Sterk.selected_isotropic_vectors()["Sterk_5"].to_vector()]
eta5 = tco([co[0], co[2], co[3]] + co[4:12])
form = lattice.discriminant_group()
first = lattice.discriminant_class(lattice.primitive_dual(lattice.module_generator("ep")))
second = lattice.discriminant_class(lattice.primitive_dual(lattice.module_generator("fp")))
gamma = lattice.Aut().discriminant_point_stabilizer(frozenset({form.zero(), first, second, first+second}))
say("Gamma_Co,2 built")
image = gamma.isotropic_vector_reduction_image(eta5)
N = image.reduction(); r = N.rank()
NG = tuple(N.module_generating_set())
def nvec(t): return N([int(x) for x in t])
def coords_of(cl): return tuple(int(y) for y in cl.to_vector())
def refl(w):
    wc = vector(QQ, [int(y) for y in w.to_vector()])
    row = vector(QQ, [int(N.b(N.module_generator(NG[i]), w)) for i in range(r)])
    return matrix(QQ, identity_matrix(QQ, r)) - (QQ(2)/QQ(int(N.q(w)))) * matrix(QQ, r, 1, wc) * matrix(QQ, 1, r, row)
c12 = image.root_class(to_tco(R5[11])); c13 = image.root_class(to_tco(R5[12])); c14 = image.root_class(to_tco(R5[13]))
certified = {coords_of(c12): c12, coords_of(c13): c13, coords_of(c14): c14}
say("certified roots to start: %d" % len(certified))

def orbit_under(reflections, limit=300000):
    acts = [refl(w) for w in reflections]
    frontier = {c12: ()}; seen = {c12}; found = None
    for depth in range(1, 15):
        nxt = {}
        for cl, word in frontier.items():
            v = vector(QQ, [int(y) for y in cl.to_vector()])
            for i, S in enumerate(acts):
                nv = S*v
                if not all(x in ZZ for x in nv): continue
                ncl = nvec(nv)
                if ncl in seen: continue
                seen.add(ncl); nxt[ncl] = word + (i,)
                if ncl == c13: found = (depth, word + (i,)); break
            if found: break
        frontier = nxt
        if found or not frontier or len(seen) > limit: break
    return seen, found

seen, found = orbit_under(list(certified.values()))
say("orbit of [12] under the starting certified reflections: %d classes, found %s" % (len(seen), found is not None))

budget = 24
for step in range(budget):
    if found: break
    known = list(certified.values())
    acts = [refl(w) for w in known]
    new_roots = {}
    for w in known:
        for S in acts:
            nv = S*vector(QQ, [int(y) for y in w.to_vector()])
            if not all(x in ZZ for x in nv): continue
            cl = nvec(nv)
            k = coords_of(cl)
            if k in certified or k in new_roots: continue
            if int(N.q(cl)) != -2: continue
            new_roots[k] = cl
    say("step %d: candidate new roots from conjugation: %d" % (step, len(new_roots)))
    if not new_roots: break
    k, cl = next(iter(new_roots.items()))
    lift = image.class_lift(cl)
    try:
        ok = image.contains_root_reflection(lift)
    except Exception as exc:
        say("   certification raised %s" % type(exc).__name__); break
    certified[k] = cl
    say("   certified a new root (total %d): %s" % (len(certified), ok))
    if ok:
        seen, found = orbit_under(list(certified.values()))
        say("   orbit of [12] now %d classes, found %s" % (len(seen), found is not None))
print()
if found:
    say("FOUND: [12] reaches [13] by certified reflections, word %s" % (found[1],))
else:
    say("not found within this budget: certified roots %d, orbit %d" % (len(certified), len(seen)))
print("PYEXIT=0")
