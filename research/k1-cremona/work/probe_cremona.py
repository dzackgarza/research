import itertools
import sympy as sp
x,y,z=sp.symbols('x y z'); V=(x,y,z)
R=sp.Matrix([[0,-1,0],[1,-1,0],[0,0,1]])
def act(p): return tuple(R*sp.Matrix(p))
def line(p,q): return sp.Matrix([p[1]*q[2]-p[2]*q[1],p[2]*q[0]-p[0]*q[2],p[0]*q[1]-p[1]*q[0]])
def meet(l,m): return (l[1]*m[2]-l[2]*m[1],l[2]*m[0]-l[0]*m[2],l[0]*m[1]-l[1]*m[0])
O=(0,0,1); A=(1,0,1); B=act(A); C=act(B); Ap=(1,0,2); Bp=act(Ap); Cp=act(Bp)
pts=[O,A,B,C,Ap,Bp,Cp,meet(line(B,C),line(Bp,Cp)),meet(line(C,A),line(Cp,Ap)),meet(line(A,B),line(Ap,Bp))]
mons=[(i,j,6-i-j) for i in range(7) for j in range(7-i)]
mon=[x**i*y**j*z**k for i,j,k in mons]
rows=[[sp.diff(m,V[v]).subs({x:p[0],y:p[1],z:p[2]}) for m in mon] for p in pts for v in range(3)]
ns=sp.Matrix(rows).nullspace(); assert len(ns)==1
G=sp.expand(4*sum(ns[0][i]*mon[i] for i in range(28)))

def hessdet(F,p):
    i=next(k for k in range(3) if p[k]!=0); oth=[k for k in range(3) if k!=i]
    f=sp.expand(F.subs({V[i]:1})); sub={V[k]:sp.Rational(p[k],p[i]) for k in oth}
    return sp.simplify(sp.hessian(f,[V[k] for k in oth]).subs(sub).det())

def base_hess(F):
    out=[]
    for i in range(3):
        oth=[j for j in range(3) if j!=i]
        f=sp.expand(F.subs({V[i]:1}))
        sub={V[j]:0 for j in oth}
        out.append(sp.simplify(sp.hessian(f,[V[j] for j in oth]).subs(sub).det()))
    return out

good=[]
for inds in itertools.combinations(range(10),3):
    T=sp.Matrix.hstack(*[sp.Matrix(pts[i]) for i in inds])
    if T.det()==0: continue
    newpts=[tuple(T.inv()*sp.Matrix(p)) for p in pts]
    if any(newpts[i][k]==0 for k in range(3) for i in range(10) if i not in inds): continue
    F=sp.expand(G.subs(dict(zip(V,T*sp.Matrix(V))),simultaneous=True))
    # exact double points at the vertices, so this substitution is divisible by x^2 y^2 z^2
    Q0=sp.expand(F.subs({x:y*z,y:x*z,z:x*y},simultaneous=True))
    rem=sp.expand(Q0/(x**2*y**2*z**2))
    if any(sp.denom(c)!=1 for c in sp.Poly(rem,V).coeffs()): continue
    # residual quadratics on the three fundamental lines
    residual=[]
    for k in range(3):
        oth=[j for j in range(3) if j!=k]; a,b=oth
        fl=sp.Poly(F.subs({V[k]:0}),V[a],V[b])
        qa=fl.as_expr().factor(V[a]**2*V[b]**2)
        # direct exact division; fail if either base multiplicity is >2
        r=sp.expand(fl.as_expr()/(V[a]**2*V[b]**2))
        if any(sp.denom(c)!=1 for c in sp.Poly(r,V[a],V[b]).coeffs()): break
        if sp.total_degree(r)!=2: break
        pa=sp.Poly(r,V[a],V[b]); aa=pa.coeff_monomial(V[a]**2); bb=pa.coeff_monomial(V[b]**2); ab=pa.coeff_monomial(V[a]*V[b])
        disc=sp.simplify(ab**2-4*aa*bb)
        if aa==0 or bb==0 or disc==0: break
        residual.append((r,disc))
    else:
        h=base_hess(rem)
        mapped=[tuple(p[1]*p[2],p[0]*p[2],p[0]*p[1]) for p in [newpts[i] for i in range(10) if i not in inds]]
        sing=list(map(tuple,sp.eye(3).tolist()))+mapped
        hess=[hessdet(rem,p) for p in sing]
        fac=sp.factor_list(rem)[1]
        good.append((inds,F,rem,residual,h,sing,hess,fac))
        print('CANDIDATE',inds,'base_hess',h,'all_hess_nonzero',all(a!=0 for a in hess),'factor_count',len(fac))
        print(' residual',residual)
        print(' mapped points',mapped)
        print(' image',rem)
print('TOTAL',len(good))
