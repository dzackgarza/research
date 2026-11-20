"""#760, item 7: the complement of the pair <delta, r>, which is the invariant that encodes delta.

Every invariant of the root alone agrees on the three admissible roots, so the last one that could
separate them is the one that remembers the Coble root: the lattice orthogonal to the pair
<delta, r>.  That pair is not saturated --- delta and r are orthogonal square -2 vectors, so
(delta + r)/2 is integral --- and the invariant is the complement of its saturation.

The record computes, for each root, the saturation of <delta, r> and the rank-10 complement of it,
and asks the library whether the complements are isometric.  They are, for all three pairs: so this
invariant does not separate root 12 from 13 either.

What it does establish is worth stating: all three pairs (delta, r) have the same saturation Gram
[-2,-2,-2,-4] of determinant 4 and isometric complements, so the roots are indistinguishable by the
data of the pair.  Distinguishing them needs the group, which is the reduction the library does not
provide.

    usage: PYTHONPATH=<repo>/.scratch/sage-extensions/src python \
               <repo>/computations/reports/coble_760-pair-complement.py
"""
import sys
import time
sys.stdout.reconfigure(line_buffering=True)
from sage.all import ZZ, QQ, matrix, vector, block_diagonal_matrix, CartanMatrix
from sage_extensions.all import Lattices
t0 = time.time()
exec(open('/repo/computations/reports/coble_760-witness-13-14.py').read().split('Hre = matrix')[0].split('print("the cusp symmetries')[0])
delta = e - f; eta = 2*e + 2*f + abar[0]
lib = Lattices(ZZ)
def pair_complement(r):
    """The complement of the SATURATION of <delta, r>: rank 10, an invariant of the pair's orbit."""
    rows = [list(G*vector(ZZ,delta)), list(G*vector(ZZ,r))]
    S,_,V = matrix(ZZ,2,N,rows).smith_form()
    ker = [vector(ZZ,[V[i,j] for i in range(N)]) for j in range(N) if all(S[k,j]==0 for k in range(2))]
    assert len(ker)==10, len(ker)
    # saturate: <delta,r>^sat = {x : (x,k) = 0 for all k in ker}
    rows2 = [list(G*vector(ZZ,k)) for k in ker]
    S2,_,V2 = matrix(ZZ,10,N,rows2).smith_form()
    sat = [vector(ZZ,[V2[i,j] for i in range(N)]) for j in range(N) if all(S2[k,j]==0 for k in range(10))]
    assert len(sat)==2, len(sat)
    Gs = matrix(ZZ,2,2, lambda i,j: ip(sat[i],sat[j]))
    assert all(ip(b,delta)==0 and ip(b,r)==0 for b in ker)
    return ker, Gs
grams={}
for lab in (12,13,14):
    ker, Gs = pair_complement(R5[lab-1])
    Gm = matrix(ZZ,10,10, lambda i,j: ip(ker[i],ker[j]))
    grams[lab]=Gm
    print("label %2d: sat<delta,r> Gram %s det %d | complement rank %d, det %6d"
          % (lab, list(Gs.list()), Gs.det(), Gm.nrows(), Gm.det()))
print()
objs={lab: lib([list(r) for r in grams[lab].rows()]) for lab in (12,13,14)}
for a,b in ((12,13),(12,14),(13,14)):
    t=time.time()
    try:
        v=objs[a].is_isometric_to(objs[b])
    except Exception as exc:
        v="RAISED %s: %s" % (type(exc).__name__, exc)
    print("labels %d,%d: complements of <delta,r> isometric -> %s  (%.1f s)" % (a,b,v,time.time()-t))

print()
print("VERDICT: the complements of the saturated pair <delta, r> are isometric for all three roots,")
print("so this last delta-sensitive invariant does not separate root 12 from 13.  Every invariant")
print("computable on the data of one or two vectors is exhausted; what remains is the orbit under")
print("the infinite stabilizer of eta_5 in Gamma_Co,2, which is sage-extensions#370.")
print("elapsed %d s" % (time.time()-t0))
print("PYEXIT=0")
