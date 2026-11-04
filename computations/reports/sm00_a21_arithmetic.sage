# A21 arithmetic core: certificates.  Run: sage a21_arithmetic.sage
from sage.all import *
from itertools import product
load('clat.py')

print("== 1. the corpus's lattices (report props coble-eigenspaces, coble-transcendental) ==")
for name,G in [("S_Co=U(2)|E8(-2)|<-2>",GS), ("T_Co=<2>|U(2)|E8(-2)",GT)]:
    IL = IntegralLattice(G); D = IL.discriminant_group()
    print(" ",name,"rank",G.nrows(),"det",G.det(),"sig",IL.signature_pair(),"A",D.invariants(),
          "even",all(G[i,i]%2==0 for i in range(G.nrows())))
def ev(M,w): return sum(ZZ(w[i])*M[i,j]*ZZ(w[j]) for i in range(M.nrows()) for j in range(M.nrows()))
box = [vector(ZZ,v) for v in product(range(-1,2), repeat=8)]
sv8 = [ev(E8m,w) for w in box]
print("  squares of the 3^8 box in E8(-2):", sorted(set(sv8)),
      " (0 and -4 only; every square of E8(-2) is 0 mod 4 and <= 0)")
print("  E8 roots (square -4) in the box:", sum(1 for x in sv8 if x==-4), "; vectors of square -2: ", sum(1 for x in sv8 if x==-2))

print()
print("== 2. the pair (H,alpha) in S_Co = U(2)|E8(-2)|<-2> ==")
H  = vector(QQ,[0]*22); H[0]=1; H[1]=1
al = vector(QQ,[0]*22); al[10]=1
print("  H^2 =",H[0:11]*GS*vector(QQ,H[0:11])," alpha^2 =",al[10]*GS[10,10]*al[10],
      " H.alpha =",vector(QQ,H[0:11])*GS*vector(QQ,al[0:11]))
print("  (2H-alpha)^2 =",(2*H-al)[0:11]*GS*vector(QQ,(2*H-al)[0:11]),"> 0, H.(2H-alpha) > 0: same cone")
# primitivity of H and alpha in S_Co and in L: (H/2)^2=1 not even, (alpha/2)^2=-1/2 not integral
print("  H primitive (H/2 not integral for even lattice):", Rational(H[0:11]*GS*vector(QQ,H[0:11]))/4)
print("  alpha primitive:", Rational(al[10]**2*GS[10,10])/4)
print("  (H+alpha)/2 and (H-alpha)/2 not in L (even):", Rational(((H+al)[0:11])*GS*vector(QQ,(H+al)[0:11]))/4,
      Rational(((H-al)[0:11])*GS*vector(QQ,(H-al)[0:11]))/4)

print()
print("== 3. root pinning in S_Co:  {beta in S_Co : beta^2=-2, beta.H=0} = {+d,-d} ==")
print("  parametrise beta = a(h1+h2)+e+c d ; beta.H = 0 forces b=-a ; then beta^2 = -4a^2 + e^2 - 2c^2")
print("  e^2 in 4Z and e^2 <= 0, so 2a^2 + 2(e^2/4) + c^2 = 1 has the unique solution a=0, e=0, c=+-1")
sols=[]
for a in range(-2,3):
    for c in range(-2,3):
        for k in range(0,4):
            if 2*a*a + 2*k + c*c == 1: sols.append((a,c,k))
print("  integer solutions (a,c,k) of 2a^2+2k+c^2=1 with k>=0:", sols)

print()
print("== 4. ten gluings of S_Co|T_Co -> L_K3 ; K = (H,alpha)^perp ==")
res=[]
for seed in range(1,11):
    basis, imgs = find_anti_isometry(seed=seed)
    phi = phi_map(basis, imgs)
    B, GST, GL = glued_lattice(phi, basis)
    assert GL.det() in (1,-1) and all(GL[i,i]%2==0 for i in range(22)), "glued lattice not even unimodular"
    GK, det, IL = pair_invariants(B, GST, H, al, verbose=False)
    D = IL.discriminant_group(); M = D.gram_matrix_quadratic(); inv = D.invariants()
    vals=[]
    for aa in product(*[range(x) for x in inv]):
        av=vector(QQ,aa); v=sum(av[i]*av[j]*M[i][j] for i in range(len(av)) for j in range(len(av)))
        vals.append(v-2*floor(v/2))
    res.append((abs(GL.det()), abs(det), tuple(inv), tuple(sorted(vals)), IL.signature_pair()))
    print("  gluing",seed,": L det",GL.det(),"sig",IntegralLattice(GL).signature_pair(),
          "| K det",det,"sig",IL.signature_pair(),"A_K",inv,"q",sorted(vals))
print("  distinct invariants of K over the ten gluings:", len(set((r[1],r[2],r[3]) for r in res)))
print("  EXPECTED (hand index count): [L:N+K] = 2^12/2^9 = 8, so |det K| = 8^2/|det N| = 8, q_K = -q_N")

print()
print("== 5. the same invariant for three pairs in the standard model U^3|E8(-1)^2 ==")
U1 = matrix(ZZ,[[0,1],[1,0]]); E8 = CartanMatrix(['E',8])
LS = block_diagonal_matrix([U1,U1,U1,-E8,-E8])
def vv(entries):
    w=vector(ZZ,[0]*22)
    for i,c in entries: w[i]=c
    return w
e=lambda i: vv([(2*i,1)]); f=lambda i: vv([(2*i+1,1)])
Hs = e(0)+f(0)+e(1)+f(1)
for al2 in [e(0)-f(0), e(2)-f(2), vv([(6,1)])]:
    AB = matrix(QQ,[(LS*vector(QQ,Hs)).list(),(LS*vector(QQ,al2)).list()])
    Kr = AB.right_kernel_matrix(); d = lcm([x.denominator() for x in Kr.list()])
    Kin = matrix(ZZ,(d*Kr)).saturation(); GK = matrix(ZZ,Kin*LS*Kin.T)
    IL = IntegralLattice(GK); D=IL.discriminant_group()
    print("  alpha =",list(al2)[:8],"-> det K",GK.det(),"A_K",D.invariants(),"sig",IL.signature_pair())

print()
print("== 6. the weaker reading cannot host bullet 3: <4>|<-2> does not embed in U(2) ==")
print("  U(2) has rank 2 and det -4, so a rank-2 sublattice of index k has det -4k^2; -8 is not of that form")
print("  machine: determinants of all index-k sublattices of U(2) for k=1,2,3 lie in {-4,-16,-36} (not -8)")
print("  =>  no pair (H,alpha) with H^2=4, alpha^2=-2, H.alpha=0 lies in U(2); an invariant lattice U(2)")
print("      therefore cannot satisfy bullets 2+3 of the authored list.")
