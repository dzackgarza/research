"""#760: the three admissible roots are certified in G_v, and their reflections' orbit of [12] is two classes.

sage-extensions#312's sift decides membership in G_v on the discriminant image: sigma in G_v if and only
if rho(g) lies in rho(K_v) rho(Gamma) for any lift g, and rho(K_v) is trivial at Sterk's cusps.  Its
`contains_root_reflection` is the per-root form, and this record runs it at cusp 5 on every printed wall
that lies in T_Co.

What it settles: the walls of labels 1--8 are of square -4 in T_Co and are not roots; labels 9, 10, 11
are not in T_Co at all; and labels 12, 13, 14 are roots orthogonal to eta_5 whose reflections ARE
certified in G_v.  So the three reflections s_r12, s_r13, s_r14 lie in the group acting on K_5 -- the
first positive statement about that group obtained without the library's refuted generator family.

What it does not settle: the orbit of the class of 12 under those three certified reflections has two
classes and does not contain the class of 13.  Since s_r12 fixes the class of r12, and the other two
generate only a small group with it, a transporter of [12] to [13] -- if one exists -- is not a word in
these three reflections.  More certified elements would be needed, and each certification of a further
root costs tens of seconds through the sift.

    usage: python3 computations/reports/coble_760-cusp5-certified-reflections.py   (~4 min)
"""
import sys, time
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
certified = []
for ix in range(14):
    v = to_tco(R5[ix])
    if v is None:
        say("   label %2d: not in T_Co" % (ix+1)); continue
    q = lattice.q(v); b = lattice.b(v, eta5)
    tag = "q=%s, (.,eta5)=%s" % (q, b)
    if int(q) != -2 or int(b) != 0:      # the lattice's ring is not Sage's ZZ
        say("   label %2d: %s -> not an admissible root" % (ix+1, tag)); continue
    ok = image.contains_root_reflection(v)
    say("   label %2d: %s -> certified in G_v: %s" % (ix+1, tag, ok))
    if ok: certified.append((ix+1, v))
say("certified: %s" % [n for n, _ in certified])
if len(certified) >= 2:
    c12, c13 = image.root_class(to_tco(R5[11])), image.root_class(to_tco(R5[12]))
    def refl(w):
        """s_w = I - (2/q(w)) * w * b(., w), as a matrix in N's coordinates"""
        wc = vector(QQ, [int(y) for y in w.to_vector()])
        row = vector(QQ, [int(N.b(N.module_generator(tuple(N.module_generating_set())[i]), w)) for i in range(r)])
        return matrix(QQ, identity_matrix(QQ, r)) - (QQ(2)/QQ(int(N.q(w)))) * matrix(QQ, r, 1, wc) * matrix(QQ, 1, r, row)
    acts = [(n, refl(image.root_class(v))) for n, v in certified]
    frontier = {c12: ()}; seen = {c12}; found = None
    for depth in range(1, 13):
        nxt = {}
        for cl, word in frontier.items():
            vv = cl
            for i, (n, S) in enumerate(acts):
                nv = S*vector(QQ, [int(y) for y in vv.to_vector()])   # the class's own K_5 coordinates
                if not all(x in ZZ for x in nv): continue
                ncl = N([int(x) for x in nv])      # the reflected class, as an element of K_5
                if ncl in seen: continue
                seen.add(ncl); nxt[ncl] = word + (n,)
                if ncl == c13: found = (depth, word + (n,)); break
            if found: break
        frontier = nxt
        say("   depth %d: orbit %d, found %s" % (depth, len(seen), found is not None))
        if found or not frontier or len(seen) > 200000: break
    print()
    print("FOUND: the class of 12 reaches that of 13 by certified reflections, %s" % (found[1],) if found else "not reached in the bound")
print("PYEXIT=0")
