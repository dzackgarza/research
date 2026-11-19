"""Bidegree-(1,1) curves y = (a x + b)/(c x + d) over F_p whose preimage in
z^2 = f_star(x, y) splits over F_p-bar: the restriction of f_star, a binary
octic, is a constant times a square.  Run: coble_766_a20_curve_search.py 11 13."""
from sage.all import *
import itertools, sys
C={(4,4):8,(4,2):7,(4,0):6,(3,3):5,(3,1):4,(2,4):3,(2,2):2,(2,0):3,(1,3):-13,(1,1):-28,(0,4):-10,(0,2):13}
for p in map(int, sys.argv[1:]):
    F=GF(p); P=PolynomialRing(F,['X','W']); X,W=P.gens()
    hits=[]
    for a,b,c,d in itertools.product(range(p),repeat=4):
        if (a*d-b*c)%p==0: continue
        # normalize: first nonzero of (a,b,c,d) = 1
        v=[a,b,c,d]; fnz=next(e for e in v if e)
        if fnz!=1: continue
        num=a*X+b*W; den=c*X+d*W
        g=sum(F(val)*X**i*W**(4-i)*num**j*den**(4-j) for (i,j),val in C.items())
        if g==0: continue
        fa=g.factor()
        if all(e%2==0 for f,e in fa): hits.append((a,b,c,d,fa))
    print(p, len(hits)); [print('  ',h) for h in hits[:12]]
