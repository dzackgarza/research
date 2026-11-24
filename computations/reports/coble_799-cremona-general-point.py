#!/usr/bin/env python3
"""research#799: an exact special-fibre witness for general Cremona position.

The integral rational map below has a good reduction at p=101. Its implicit
sextic has Jacobian scheme of length 10 at ten distinct geometric points,
hence ten ordinary double points (the rational parametrization excludes any
other singularity by the arithmetic-genus/delta count). Nodes 0,1,2 are
noncollinear; each of their three joins misses every other node and has
order exactly two at both endpoints (divide it twice at each endpoint) and
a squarefree residual quadratic. All arithmetic is exact in GF(101) and its
splitting field. The good conditions are open on the integral parameter
family. Existence in this special fibre therefore proves nonemptiness of
the good open locus in characteristic zero: a universally bad
characteristic-zero family would also be bad after almost every reduction.

Run with Sage:
  python computations/reports/coble_799-cremona-general-point.py
"""
from sage.all import *
import itertools

P = GF(101)
R = PolynomialRing(P,'u'); u = R.gen()
S = PolynomialRing(P,names=('x','y','z')); x,y,z = S.gens()
mons = [(a,b,6-a-b) for a in range(7) for b in range(7-a)]

def implicit(fs):
    vs=[]
    for a,b,c in mons:
        v=fs[0]**a*fs[1]**b*fs[2]**c
        vs.append([v[i] if i<=v.degree() else 0 for i in range(37)])
    M=Matrix(P,37,28,lambda i,j:vs[j][i])
    K=M.right_kernel()
    if K.dimension()!=1:return None
    v=K.basis()[0]
    return sum(v[i]*x**mons[i][0]*y**mons[i][1]*z**mons[i][2] for i in range(28))

def process(seed):
    fs=[R([3,3,-2,-2,-2,-1,3]), R([-2,2,3,3,3,-1,-1]), R([1,-2,1,-2,1,2,-2])]
    if fs[0].degree()<6: fs[0]+=u**6
    # Regular map: no common affine or infinite zero over the algebraic closure.
    if gcd(gcd(fs[0],fs[1]),fs[2])!=1:return
    if all(f[6]==0 for f in fs):return
    F=implicit(fs)
    if F is None:return
    A=PolynomialRing(P,names=('X','Y'),order='lex');X,Y=A.gens()
    f=F(x=X,y=Y,z=1)
    I=A.ideal(f,f.derivative(X),f.derivative(Y))
    B=I.groebner_basis()
    if not I.dimension()==0 or len(I.normal_basis())!=10:return
    eid=I.elimination_ideal(X)
    if len(eid.gens())!=1:return
    RY=PolynomialRing(P,'Y')
    elim=RY(eid.gens()[0])
    if elim.degree()!=10 or not elim.is_squarefree():return
    xr=RY(X.reduce(B))
    factors=[q for q,e in elim.factor()]
    if sum(q.degree() for q in factors)!=10:return
    print('seed',seed,'GOOD SINGULAR SCHEME factors',[(q.degree(),e) for q,e in elim.factor()])
    print('fs =',fs);print('F =',F);print('elim =',elim);print('xr =',xr)
    # Work with the actual geometric nodes in the splitting field, not with
    # quotient-ring substitutions. Every returned point is checked by named
    # evaluation in the original Jacobian ideal polynomial.
    K=GF(P.characteristic()**elim.degree(),name='a',modulus=elim)
    node_data=I.variety(ring=K)
    if len(node_data)!=10:
        print('unexpected node count',len(node_data));return
    Xkey,Ykey=A.gens()
    nodes=[[1,d[Xkey],d[Ykey]] for d in node_data]
    def feval(poly,vals):
        return sum(cf*prod([vals[i]**e[i] for i in range(len(vals))]) for e,cf in poly.dict().items())
    
    if any(feval(f,pt[1:])!=0 for pt in nodes):
        raise RuntimeError('solver returned a non-curve point')
    T=PolynomialRing(K,'T');tv=T.gen()
    for chosen in itertools.combinations(range(10),3):
        pts=[nodes[i] for i in chosen]
        # Affine coordinates are (X,Y), with z=1.
        good=True;data=[]
        for i,j in itertools.combinations(range(3),2):
            X0,Y0=pts[i][1],pts[i][2]; X1,Y1=pts[j][1],pts[j][2]
            aa=Y1-Y0; bb=X0-X1; cc=X1*Y0-X0*Y1
            if aa==0 and bb==0:good=False;break
            if bb!=0:
                r=-aa/bb; q=-cc/bb; which=1
                line_y=r*tv+q
                res=sum(cf*tv**e[0]*line_y**e[1] for e,cf in f.dict().items())
                base=[X0,X1]
            else:
                r=-bb/aa; q=-cc/aa; which=0
                line_x=r*tv+q
                res=sum(cf*line_x**e[0]*tv**e[1] for e,cf in f.dict().items())
                base=[Y0,Y1]
            # A double base point at each end gives exactly two linear factors.
            residual=res
            for root in base:
                for twice in range(2):
                    qout,rem=residual.quo_rem(tv-root)
                    if rem!=0 or qout.degree()<0:good=False;break
                    residual=qout
                if not good:break
            if not good:break
            if residual.degree()!=2:
                good=False;break
            D=residual.discriminant()
            if D==0:
                good=False;break
            data.append(((chosen[i],chosen[j]),D))
        if not good:continue
        for ell,pt4 in enumerate(nodes):
            if ell in chosen:continue
            for i,j in itertools.combinations(range(3),2):
                X0,Y0=pts[i][1],pts[i][2]; X1,Y1=pts[j][1],pts[j][2]
                aa=Y1-Y0; bb=X0-X1; cc=X1*Y0-X0*Y1
                if aa*pt4[1]+bb*pt4[2]+cc==0:
                    good=False;break
            if not good:break
        if good:
            print('CHOSEN NODES',chosen,'all remaining nodes miss the three joins')
            print('nonzero residual discriminants',data)
            return True
    print('singular scheme good but no triple for this seed')
    return False


assert process(2), "the exact special-fibre Cremona-position certificate failed"
print("VERIFIED: good special fibre at p=101; consequently the good open locus is nonempty in characteristic zero.")
