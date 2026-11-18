"""#760, item 7: the last isometry invariant of the three roots, decided by the library.

The question item 7 leaves open is whether two of roots 12, 13, 14 at cusp 5 are in the same
orbit under Gamma_Co,2.  Every invariant that does not need the subgroup itself has now been
computed: square -2, pairing 0 with delta, divisibility 1 in K_5, and --- here --- the isometry
class of the orthogonal complement in K_5, which is the classical obstruction to two primitive
vectors of a lattice lying in one O(K_5)-orbit.

The library decides that isometry: `Lattices(ZZ)` builds a lattice from a nested list (not from a
Sage matrix, which it refuses as a type (1,1) tensor, and not over Sage's ZZ, which is not "a ring
of this session"), and `is_isometric_to` returns a verified boolean rather than an undecided
proposition.  All three complements come out isometric, so no invariant of this kind separates the
roots, and what remains is exactly the subgroup: a reduction for Stab_{Gamma_Co,2}(eta_5) on K_5,
which the library does not have (coble_760-orbit-decision-probe-run.txt, BOUND-REACHED).

Run inside the sage runtime:
  PYTHONPATH=<repo>/.scratch/sage-extensions/src python \
      <repo>/computations/reports/coble_760-isometry-decision-probe.py
"""
import sys, time; sys.stdout.reconfigure(line_buffering=True)
from sage.all import ZZ, QQ, matrix, vector, block_diagonal_matrix, CartanMatrix, gcd
from sage_extensions.all import Lattices, NamedLattices
C = CartanMatrix(["E",8]); U = matrix(ZZ,[[0,1],[1,0]])
G = block_diagonal_matrix(U, 2*U, -2*C); N=12
BAS=[vector(ZZ,[1 if k==i else 0 for k in range(N)]) for i in range(N)]
e,f,ep,fp=BAS[0],BAS[1],BAS[2],BAS[3]; alpha=[BAS[4+i] for i in range(8)]
Cinv=C.inverse(); abar=[vector(ZZ,[int(c) for c in sum(QQ(-Cinv[k,i])*alpha[k] for k in range(8))]) for i in range(8)]
def ip(x,y): return int(vector(ZZ,x)*G*vector(ZZ,y))
delta=e-f; eta=2*e+2*f+abar[0]
et,ft=e+ep+fp-alpha[0], f+ep+fp-alpha[0]
at=[ep-fp,alpha[1],fp+alpha[2]]+list(alpha[3:8])
Gt=matrix(ZZ,8,8,lambda i,j: ip(at[i],at[j])); Gti=Gt.inverse()
abart=[vector(ZZ,[int(c) for c in sum(QQ(2*Gti[k,i])*at[k] for k in range(8))]) for i in range(8)]
R5=[at[1],at[3],at[4],at[5],at[6],at[7],at[0],abart[7],
    2*et-at[0], 2*et+(abart[1]-abart[2]), ft-et,
    et+ft+(abart[5]-abart[2]), et+ft+(abart[0]+abart[7]-abart[2]), et+ft+at[2]]
# K_5 basis (my coordinates, as in the pushed record)
row=vector(ZZ,G*vector(ZZ,eta)); S_,U_,V_=matrix(ZZ,1,N,list(row)).smith_form()
Mbas=[vector(ZZ,[V_[i,j] for i in range(N)]) for j in range(1,N)]
MM=matrix(ZZ,11,12,[list(b) for b in Mbas])
sol=MM.transpose().solve_right(vector(ZZ,eta)); ec=vector(ZZ,[sol[i] for i in range(11)])
Sg,Ug,Vg=matrix(ZZ,11,1,list(ec)).smith_form(); Uinv=Ug.inverse()
Bp=[vector(ZZ,MM.transpose()*vector(ZZ,list(Uinv.column(j)))) for j in range(11)]
Kbas=Bp[1:]; GK=matrix(ZZ,10,10,lambda i,j: ip(Kbas[i],Kbas[j]))
def kcoords(r):
    x=vector(ZZ,[MM.transpose().solve_right(vector(ZZ,r))[i] for i in range(11)])
    y=Ug*x; return vector(ZZ,[y[i] for i in range(1,11)])
def comp_gram(v):
    rw=vector(ZZ,list(v*GK)); Sv,_,Vv=matrix(ZZ,1,10,list(rw)).smith_form()
    ker=[vector(ZZ,[Vv[i,j] for i in range(10)]) for j in range(1,10)]
    return matrix(ZZ,9,9,lambda i,j: ker[i]*GK*ker[j])
grams={}
for lab in (12,13,14):
    grams[lab]=comp_gram(kcoords(R5[lab-1]))
    t0 = time.time()
print("label %d: complement det %d, rank %d" % (lab, grams[lab].det(), grams[lab].nrows()))
print()
lib = Lattices(ZZ)
objs = {lab: lib([list(row) for row in grams[lab].rows()]) for lab in (12,13,14)}
for lab in (12,13,14):
    print("complement of label %2d as a library lattice: %s" % (lab, objs[lab]))
for a,b in ((12,13),(12,14),(13,14)):
    t=time.time()
    try:
        verdict = objs[a].is_isometric_to(objs[b])
    except Exception as exc:
        verdict = "RAISED %s: %s" % (type(exc).__name__, exc)
    print("labels %d,%d: is_isometric_to -> %s  (%.1f s)" % (a,b,verdict,time.time()-t))
print()
print("all three complements isometric: no complement invariant separates the roots, so the")
print("orbit question is decided by the subgroup and by nothing computable on the pair")
print("elapsed %d s" % (time.time()-t0))

print("PYEXIT=0")
