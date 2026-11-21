import sympy as sp, itertools
x,y,z,t=sp.symbols('x y z t'); V=(x,y,z)
F=27*x**5*z+5*x**3*y**3+150*x**2*y**2*z**2-120*x*y*z**4+27*y**5*z+32*z**6
q2=t**2+6*t+4
qs=[t**4-8*t**3+24*t**2+8*t+16,t**4+2*t**3+24*t**2-32*t+16]

def inv(a,p): return pow(int(a)%p,-1,p)
def roots(f,p): return [a for a in range(p) if f.subs(t,a)%p==0]
def xrel(q):
    return sp.Poly(sp.rem(-t**9/sp.Integer(1760)-987*t**4/sp.Integer(440),q,t),t)
def ev(poly,a,p): return sum(int(c)*pow(int(a),int(m[0]),p) for c,m in zip(poly.coeffs(),poly.monoms()))%p

def hessdet(F0,pt,p):
    i=next(k for k in range(3) if pt[k]%p); oth=[k for k in range(3) if k!=i]
    f=sp.expand(F0.subs({V[i]:1})); sub={V[k]:pt[k]*inv(pt[i],p) for k in oth}
    return sp.hessian(f,[V[k] for k in oth]).subs(sub).det()%p

def run(p):
    ys=[(q2,a) for a in roots(q2,p)]
    for q in qs: ys += [(q,a) for a in roots(q,p)]
    if len(ys)!=10: return
    rels={q:xrel(q) for q,a in ys}
    pts=[(ev(rels[q],a,p),a,1) for q,a in ys]
    if len(set(pts))!=10: return
    print('prime',p,'ys',ys,'pts',pts)
    for inds in itertools.combinations(range(10),3):
        T=sp.Matrix.hstack(*[sp.Matrix(pts[i]) for i in inds]); det=int(T.det())%p
        if det==0: continue
        Ti=T.inv_mod(p); new=[tuple((Ti*sp.Matrix(pt)).applyfunc(lambda a:a%p)) for pt in pts]
        if any(new[i][k]==0 for k in range(3) for i in range(10) if i not in inds): continue
        Ft=sp.expand(F.subs(dict(zip(V,T*sp.Matrix(V))),simultaneous=True)); Ft=sp.Poly(Ft,V,modulus=p).as_expr()
        residual=[]
        for k in range(3):
            oth=[j for j in range(3) if j!=k]; a,b=oth
            fl=sp.Poly(Ft.subs({V[k]:0}),V[a],V[b],modulus=p)
            if any(m[0]<2 or m[1]<2 for m in fl.monoms()): break
            rr=sum(c*V[a]**(m[0]-2)*V[b]**(m[1]-2) for c,m in zip(fl.coeffs(),fl.monoms()))
            pp=sp.Poly(rr,V[a],V[b],modulus=p)
            if sp.total_degree(rr)!=2: break
            A=pp.coeff_monomial(V[a]**2)%p; B=pp.coeff_monomial(V[b]**2)%p; C=pp.coeff_monomial(V[a]*V[b])%p; D=(C*C-4*A*B)%p
            if A==0 or B==0 or D==0: break
            residual.append((rr,D))
        else:
            FS=sp.Poly(sp.expand(Ft.subs({x:y*z,y:x*z,z:x*y},simultaneous=True)),V,modulus=p)
            if any(min(m)<2 for m in FS.monoms()): continue
            Q=sum(c*x**(m[0]-2)*y**(m[1]-2)*z**(m[2]-2) for c,m in zip(FS.coeffs(),FS.monoms())); Q=sp.Poly(Q,V,modulus=p).as_expr()
            mapped=[new[i] for i in range(10) if i not in inds]
            qpts=[(yz%p,xz%p,xy%p) for xx,yy,zz in []] if False else [(pp[1]*pp[2]%p,pp[0]*pp[2]%p,pp[0]*pp[1]%p) for pp in mapped]
            sing=[tuple(sp.eye(3).row(i)) for i in range(3)]+qpts
            if len(set(tuple(v%p for v in pt) for pt in sing))!=10: continue
            hs=[hessdet(Q,pt,p) for pt in sing]
            if all(hs):
                print('GOOD',inds,'residual',residual)
                print('Q=',Q)
                print('sing=',sing,'hess=',hs)
                return inds
    print('no good')

for p in [11,19,29,31,41,59,61,71,79,89,101,109,131,139,149,151,179,181,191]:
    if pow(5,(p-1)//2,p)==1:
        ans=run(p)
        if ans is not None: break
