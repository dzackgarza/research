"""Exact chamber and Type II contraction data for the ambient semifan restrictions.

Input: coble_enriques-white-root-facets-run.txt, the wall Gram matrices in
figure order and the actual cut roots. The marking is read from AEGS25
Figures 5, 7, 8 and Definitions 5.3--5.4, not a permutation of Sterk's printed
labels. The dihedral restriction criterion is proved in
thm:semifan-restriction; the extreme-ray and affine-group criteria are
proved in thm:coble-pair-semifan. Run with Sage's Python.
"""
from itertools import combinations
from math import gcd
import re
from pathlib import Path
from sage.all import QQ, ZZ, matrix, vector, lcm

# Figure order matches the Gram matrices, not the printed Sterk root order.
# AEGS25 Figures 5,7,8: the interior nodes in the displayed folded graphs.
CUT = {2:10,3:5,4:9,5:11}
IRR = {2:{4},3:{10,11,12},4:{10,11},5:{9,10,11,12,13,14}}
text = Path(__file__).with_name('coble_enriques-white-root-facets-run.txt').read_text()
gram = {}
for m in re.finditer(r"=== cusp (\d+);[^\n]*\n(?:[^\n]*\n)*?wall Gram matrix in figure order:\n((?:\s*\[[^\n]*\]\n)+)",text):
    k=int(m[1])
    gram[k]=matrix(QQ,[[int(x) for x in re.findall(r"-?\d+",r)] for r in m[2].splitlines() if r.strip()])
assert set(gram)=={1,2,3,4,5}
for k,d in CUT.items():
    G=gram[k]
    assert G==G.transpose() and G.rank()==10 and G[d-1,d-1]==-2
    nodes=[i for i in range(1,G.nrows()+1) if i!=d]
    P=matrix(QQ, [[G[i-1,j-1]+G[i-1,d-1]*G[j-1,d-1]/2 for j in nodes] for i in nodes])
    assert P.rank()==9
    assert all(P[i,i]<0 for i in range(len(nodes)))
    assert all(matrix(QQ,[P[i],P[j]]).rank()==2 for i,j in combinations(range(len(nodes)),2))
    assert all(G[i-1,d-1] in (0,2) for i in nodes)
    assert all(G[i-1,i-1]==-4 for i in nodes if G[i-1,d-1]==2)
    J=[i for i in nodes if i in IRR[k] and (G[i-1,d-1]==0 or d in IRR[k])]
    assert J=={2:[4],3:[10,12],4:[10,11],5:[9,10,12,13,14]}[k]
    inds=[nodes.index(i) for i in J]
    PG=P.matrix_from_rows_and_columns(inds,inds)
    B=list(P.pivots())
    assert len(B)==9
    GB=P.matrix_from_rows_and_columns(B,B)
    assert GB.is_invertible()
    A=P.matrix_from_columns(B)
    rays=set()
    for S in combinations(range(len(nodes)),8):
        K=A.matrix_from_rows(S).right_kernel()
        if K.dimension()!=1:
            continue
        v=K.basis()[0]
        vals=A*v
        if all(t<=0 for t in vals):
            v=-v; vals=-vals
        if not all(t>=0 for t in vals):
            continue
        w=vector(ZZ,v*lcm([t.denominator() for t in v]))
        w=tuple(int(t//gcd(*[abs(int(x)) for x in w])) for t in w)
        rays.add(w)
    assert matrix(QQ, list(rays)).rank()==9
    for i in range(len(nodes)):
        assert matrix(QQ,[w for w in rays if (A*vector(QQ,w))[i]==0]).rank()==8
    interior=sum((vector(QQ,w) for w in rays),vector(QQ,[0]*9))
    assert interior*GB*interior>0
    assert all(t>0 for t in A*interior)
    assert all(interior*GB*vector(QQ,w)>0 for w in rays)
    types={1:0,0:0,-1:0}
    parabolic=[]
    for w in sorted(rays):
        v=vector(QQ,w)
        q=v*GB*v
        sg=1 if q>0 else (-1 if q<0 else 0)
        types[sg]+=1
        if q==0:
            zeros=[nodes[j] for j,t in enumerate(A*v) if t==0]
            jj=[nodes.index(i) for i in zeros if i in J]
            jjg=P.matrix_from_rows_and_columns(jj,jj)
            non_toroidal=jjg.rank()<len(jj)
            parabolic.append((zeros,non_toroidal))
    print('cusp',k,'delta',d,'ambient irrelevant',sorted(IRR[k]),'effective irrelevant',J,flush=True)
    print('irrelevant Gram',list(map(list,PG.rows())),'rank',PG.rank(),flush=True)
    print('rays (ordinary, ideal, outside)',[types[1],types[0],types[-1]],flush=True)
    for z,bad in parabolic:
        print('ideal',z,'non-toroidal',bad,flush=True)
    assert [types[1],types[0],types[-1]]=={2:[8,1,0],3:[22,3,0],4:[18,3,0],5:[61,9,0]}[k]
    assert sum(bad for _,bad in parabolic)==(2 if k==5 else 0)
    if k==5:
        assert PG.rank()==5 and PG.det()>0
        assert set(tuple(z) for z,bad in parabolic if bad)=={
            (2,3,4,6,7,8,9,10,12,14),(1,2,4,5,6,8,9,10,12,13)}
        assert PG.matrix_from_rows_and_columns([0,2,4],[0,2,4]).rank()==2
        assert PG.matrix_from_rows_and_columns([1,3],[1,3]).rank()==1
print("All exact checks passed.")
