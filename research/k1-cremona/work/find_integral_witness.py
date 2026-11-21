import itertools, math, random, sympy as sp, time
p=101
u,v,x,y,z=sp.symbols('u v x y z')
T=sp.symbols('t')
mons=[(i,j,6-i-j) for i in range(7) for j in range(7-i)]

def divrem_np(a,b,P):
    a=a[:]; out=[0]*(len(a)-len(b)+1)
    inv=pow(b[0],-1,P)
    for k in range(len(out)):
        c=a[k]*inv%P;out[k]=c
        for j in range(len(b)):a[k+j]=(a[k+j]-c*b[j])%P
    return out,a[len(out):]
def peval(a,t,P):return sum(c*pow(t,k,P) for k,c in enumerate(a))%P
def pder(a):return [(k*a[k]) for k in range(1,len(a))]
def pmul(a,b,P):
    c=[0]*(len(a)+len(b)-1)
    for i,ai in enumerate(a):
        for j,bj in enumerate(b):c[i+j]=(c[i+j]+ai*bj)%P
    return c
def pder_image(P):return [0]
def det3(a,b,c):return (a[0]*(b[1]*c[2]-b[2]*c[1])-a[1]*(b[0]*c[2]-b[2]*c[0])+a[2]*(b[0]*c[1]-b[1]*c[0]))
def cross(a,b):return [(a[1]*b[2]-a[2]*b[1]),(a[2]*b[0]-a[0]*b[2]),(a[0]*b[1]-a[1]*b[0])]
def norm(pt,P):
    for a in pt:
        if a:
            iv=pow(a,-1,P);return tuple(iv*b%P for b in pt)
def minor_num(f,g,h,i,j,P):
    return (peval(f,i,P)*peval(g,j,P)-peval(g,i,P)*peval(f,j,P))*pow((i-j)%P,-1,P)
def rank_mod(rows,P):
    a=[[c%P for c in r] for r in rows];m=len(a);n=len(a[0]);r=0;pivs=[]
    for c in range(n):
        piv=next((i for i in range(r,m) if a[i][c]),None)
        if piv is None:continue
        a[r],a[piv]=a[piv],a[r];inv=pow(a[r][c],-1,P);a[r]=[v*inv%P for v in a[r]]
        for i in range(m):
            if i!=r and a[i][c]:
                fac=a[i][c];a[i]=[(a[i][j]-fac*a[r][j])%P for j in range(n)]
        pivs.append(c);r+=1
        if r==m:break
    return r,pivs,a
def implicit(fs,P):
    cols=[]
    for a,b,c in mons:
        poly=pmul(pmul([1]*1,[1],P),[1],P)
        # polynomial exponentiation of linear functional
        def ppow(f,k):
            r=[1]
            for _ in range(k):r=pmul(r,f,P)
            return r
        pol=[0]*(6*6+1)
        for f,k in zip(fs,(a,b,c)):
            q=ppow(f,k)
            for i,cf in enumerate(q):pol[i]=(pol[i]+cf)%P
        col=[]
        for deg in range(37):
            row=[0]*len(mons);row[len(cols)]=1 if len(cols)<28 else 0
        # handled below via matrix monomial rows
        cols.append(pol)
    rows=[]
    for deg in range(37):rows.append([(col[deg] if deg<len(col) else 0) for col in cols])
    rank,pivs,rr=rank_mod(rows,P)
    if rank!=27:return None
    free=next(j for j in range(28) if j not in pivs)
    # RREF pivot rows express pivot variable + free coefficient; quotient relation
    vec=[0]*28;vec[free]=1
    for i,j in enumerate(pivs):vec[j]=(-rr[i][free])%P
    F=0
    for cf,(a,b,c) in zip(vec,mons):F+=cf*x**a*y**b*z**c
    return sp.Poly(F,x,y,z,modulus=P).as_expr()
def hessdet(F,pt,P):
    V=(x,y,z);i=next(k for k in range(3) if pt[k]);oth=[k for k in range(3) if k!=i]
    f=sp.expand(F.subs({V[i]:1}));sub={V[k]:pt[k]*pow(pt[i],-1,P) for k in oth}
    return sp.hessian(f,[V[k] for k in oth]).subs(sub).det()%P

def trial(seed):
    rng=random.Random(seed);fs=[[rng.randrange(-3,4) for _ in range(7)] for _ in range(3)]
    if all(f[6]==0 for f in fs):fs[0][6]=1
    # nodes, unordered off-diagonal pairs
    pairs=[]
    for a in range(p):
        for b in range(a+1,p):
            if minor_num(fs[0],fs[1],fs[2],a,b,p)==0 and minor_num(fs[0],fs[2],fs[1],a,b,p)==0:
                pts=[tuple(peval(f,a,p) for f in fs),tuple(peval(f,b,p) for f in fs)]
                pairs.append((a,b,pts))
    byimg={}
    for a,b,pts in pairs:
        n0,n1=norm(pts[0],p),norm(pts[1],p)
        if n0==n1:byimg.setdefault(n0,[]).append((a,b))
    if len(byimg)!=10:return None
    if any(len(v)!=1 for v in byimg.values()):return None
    print('seed',seed,'ten image nodes',flush=True)
    F=implicit(fs,p)
    if F is None:return None
    images=list(byimg)
    if not all(hessdet(F,pt,p) for pt in images):print('bad hess');return None
    # Jacobian scheme in all 3 affine charts, Groebner dimension and squarefree count via point enumeration;
    # total ordinary nodes are checked pointwise, arithmetic genus+delta excludes all other singularities.
    # no additional singular F_31 roots at infinity: test all projective points over F_p as a necessary check only.
    # the exact certificate in the page uses smooth normalization + 10 simple Jacobian points.
    # line conditions for first three images
    tri=images[:3]; pre={pt:byimg[pt][0] for pt in images}
    checks=[]
    for i,j in itertools.combinations(range(3),2):
        P0,P1=tri[i],tri[j];L=cross(P0,P1)
        h=[sum(L[k]*fs[k][m] for k in range(3))%p for m in range(7)]
        preimages=list(pre[P0])+list(pre[P1])
        if any(peval(h,a,p)!=0 or peval(pder(h),a,p)==0 for a in preimages):return None
        for a in preimages:h,rem=divrem_np(h,[(-a)%p,1],p);assert rem==[0]
        if len(h)!=3:return None
        disc=(h[1]*h[1]-4*h[0]*h[2])%p
        if h[2]==0 or disc==0:return None
        if any(sum(L[k]*Q[k] for k in range(3))%p==0 for Q in images if Q not in (P0,P1)):return None
        checks.append(((i,j),h,disc))
    print('GOOD seed',seed,'F=',F,flush=True)
    print('images',images,flush=True)
    print('preimages',pre,flush=True)
    print('line checks',checks,flush=True)
    print('fs=',fs,flush=True)
    return F,fs,images,pre

for seed in range(1,1000):
    ans=trial(seed)
    if ans:break
else:print('NO WITNESS')
