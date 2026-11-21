#!/usr/bin/env python3
"""research#799: exact first-order witness for the general Cremona locus.

The deformation is G+epsilon H in the first-order Severi tangent space
T_G V = {H of degree 6 : H(p_i)=0}.  The nonzero collinearity derivatives
make every initially collinear node triple noncollinear for small nonzero
epsilon.  The chosen joins (0,1),(0,2),(1,2) already have simple base
intersections and squarefree residual quadratics.  These are open
conditions, hence they persist.  Exact rational arithmetic only.
"""
import itertools
import random
import sympy as sp

x, y, z = sp.symbols('x y z')
V = (x, y, z)
P = [(0,0,1),(1,0,1),(0,1,1),(-1,-1,1),(1,0,2),
     (0,1,2),(-1,-1,2),(1,2,0),(-2,-1,0),(1,-1,0)]
MONS = [(a,b,6-a-b) for a in range(7) for b in range(7-a)]
COLLINEAR = [(0,1,4),(0,2,5),(0,3,6),(1,2,9),(1,3,8),
             (2,3,7),(4,5,9),(4,6,8),(5,6,7),(7,8,9)]

def det3(a,b,c):
    return sp.Matrix([list(a),list(b),list(c)]).det()

def monomial_matrix(condition):
    rows=[]
    for p in P:
        rows.append([condition(m,p) for m in MONS])
    return sp.Matrix(rows)

def substituted(p,m):
    return x**m[0]*y**m[1]*z**m[2]

def evaluate(m,p):
    return substituted(p,m).subs({x:p[0],y:p[1],z:p[2]})

def main():
    # Construct G as the integral null vector of all first-derivative node conditions.
    rows=[]
    for p in P:
        for var in V:
            rows.append([sp.diff(substituted(p,m),var).subs({x:p[0],y:p[1],z:p[2]}) for m in MONS])
    ns=sp.Matrix(rows).nullspace()
    assert len(ns)==1
    G=sp.expand(4*sum(ns[0][i]*substituted(None,m) for i,m in enumerate(MONS)))
    assert G != 0
    print('G =',G)
    for p in P:
        assert all(sp.diff(G,v).subs({x:p[0],y:p[1],z:p[2]})==0 for v in V)
    print('all ten points are singular; their ordinary-node Hessians were checked by coble_787-s10-symmetric-sextic.py')

    # H ranges over evaluation-only conditions, the tangent space identified in HM (1.49) proof.
    ev=monomial_matrix(evaluate)
    basis=ev.nullspace()
    assert len(basis)==18
    random.seed(7)
    vec=[0]*28
    for v in basis:
        r=random.randint(-5,5)
        for i in range(28):
            vec[i] += r*v[i]
    H=sp.expand(sum(vec[i]*substituted(None,m) for i,m in enumerate(MONS)))
    assert all(H.subs({x:p[0],y:p[1],z:p[2]})==0 for p in P)
    print('H =',H)

    # Implicit node velocities: Hess(G)(p) v = -grad H(p), with v.p=0.
    hg=sp.hessian(G,V)
    velocity=[]
    for p in P:
        hp=hg.subs({x:p[0],y:p[1],z:p[2]})
        gh=sp.Matrix([sp.diff(H,v).subs({x:p[0],y:p[1],z:p[2]}) for v in V])
        assert (gh.T*sp.Matrix(p))[0]==0
        # The Hessian has rank two and image p^perp.  Pick the solution orthogonal to p.
        sol=sp.linsolve((hp.row_join(-gh),sp.symbols('w0:3')) if False else (hp,-gh),sp.symbols('w0:3'))
        vv=list(sol)[0]
        # Instantiate any free parameters at zero and then orthogonally project to p^perp.
        free=sorted(vv.free_symbols & set(sp.symbols('w0:3')),key=str)
        vv=sp.Matrix([q.subs({a:0 for a in free}) for q in vv])
        pdotp=sp.Rational(sum(a*a for a in p))
        vv -= sp.Matrix(p)*(vv.dot(sp.Matrix(p))/pdotp)
        assert all(sp.simplify(a)==0 for a in hp*vv+gh)
        velocity.append(vv)

    print('collinearity derivatives at epsilon=0')
    for i,j,k in COLLINEAR:
        pi,pj,pk=map(lambda n:sp.Matrix(P[n]),(i,j,k))
        vi,vj,vk=velocity[i],velocity[j],velocity[k]
        d=sp.simplify(det3(vi,pj,pk)+det3(pi,vj,pk)+det3(pi,pj,vk))
        print((i,j,k),d)
        assert d!=0

    # First derivative of every residual discriminant. Along the moving join
    # R(eps)=R0+eps R1 after removing the double base points. A residual is
    # squarefree for small nonzero eps if its discriminant is nonzero at eps=0
    # or has nonzero first derivative there.
    s,t=sp.symbols('s t')
    def coeff(poly,mon):
        return sp.Poly(sp.expand(poly),s,t).coeff_monomial(mon)
    def residual_data(i,j):
        A,B=sp.Matrix(P[i]),sp.Matrix(P[j]); VA,VB=velocity[i],velocity[j]
        line=s*A+t*B; direction=s*VA+t*VB
        sub={x:line[0],y:line[1],z:line[2]}
        R0=sp.expand(G.subs(sub)/(s**2*t**2))
        R1=sp.expand((sum(sp.diff(G,V[k]).subs(sub)*direction[k] for k in range(3))+H.subs(sub))/(s**2*t**2))
        assert sp.total_degree(R0)==2 and sp.total_degree(R1)==2
        a0,b0,c0=coeff(R0,s**2),coeff(R0,s*t),coeff(R0,t**2)
        a1,b1,c1=coeff(R1,s**2),coeff(R1,s*t),coeff(R1,t**2)
        d0=sp.simplify(b0**2-4*a0*c0)
        d1=sp.simplify(2*b0*b1-4*a0*c1-4*a1*c0)
        return R0,R1,d0,d1
    residual={(i,j):residual_data(i,j) for i,j in itertools.combinations(range(10),2)}
    collinearity={}
    for i,j,k in itertools.combinations(range(10),3):
        pi,pj,pk=map(lambda n:sp.Matrix(P[n]),(i,j,k))
        d0=det3(pi,pj,pk)
        d1=det3(velocity[i],pj,pk)+det3(pi,velocity[j],pk)+det3(pi,pj,velocity[k])
        collinearity[i,j,k]=(sp.simplify(d0),sp.simplify(d1))

    def good(pair):
        return pair[0]!=0 or pair[1]!=0
    print('TEST RESIDUAL 01',residual[(0,1)])
    for chosen in itertools.combinations(range(10),3):
        if not good(collinearity[chosen]): continue
        ok=True
        for other in range(10):
            if other in chosen: continue
            for a,b in itertools.combinations(chosen,2):
                if not good(collinearity[tuple(sorted((a,b,other)))]): ok=False
        if not ok: continue
        if all(good(residual[tuple(sorted((a,b)))][2:]) for a,b in itertools.combinations(chosen,2)):
            break
    else:
        raise AssertionError('this tangent vector has no good triple; good residuals = '+str([pair+(d[2],d[3]) for pair,d in residual.items() if good(d[2:])]) )
    print('chosen node triple:',chosen)
    for a,b in itertools.combinations(chosen,2):
        R0,R1,d0,d1=residual[tuple(sorted((a,b)))]
        print('join',(a,b),'R0 =',R0,'; R1 =',R1,'; D0 =',d0,'; D1 =',d1)
    print('collinearity values/first derivatives for triples through a chosen join:')
    for other in range(10):
        if other in chosen: continue
        for a,b in itertools.combinations(chosen,2):
            tri=tuple(sorted((a,b,other)))
            if collinearity[tri][0]==0:
                print(tri,collinearity[tri])
                assert good(collinearity[tri])
    print('central triple',collinearity[chosen])
    print('CONCLUSION: all ten nodes persist as ordinary nodes for small epsilon by the nonsingular-Hessian implicit branches.')
    print('For small nonzero epsilon every chosen-join third-node collinearity is excluded and every chosen-join')
    print('residual quadratic is squarefree: each bad condition either fails at epsilon=0 or has nonzero derivative there.')
    print('ALL ASSERTIONS HOLD.')

if __name__=='__main__':
    main()
