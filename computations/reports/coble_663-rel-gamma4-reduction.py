"""research#663: the block sign of (REL) is a known word times an explicit element of Gamma(4).

(REL) of research#720 holds if delta_{E8} = -id on E8(2) lies in W(T_Co).  h(s_v) = (s_v - id)/2
depends only on v mod 2 and is additive modulo 2 on the congruence subgroup, so the span of the
h(s_v) over the finitely many classes that carry a (-2)-vector is computable; and if h(delta_{E8})
lies in that span, the corresponding product w of reflections is an element of W with
w == delta_{E8} (mod 4), leaving k = w^-1 delta_{E8} in the level-4 congruence subgroup.

This script does exactly that: it enumerates genuine (-2)-vectors, computes the span over the
classes they realise, solves for a certificate by elimination over F2 with bitmask bookkeeping,
verifies that every factor is an exact isometry of T_Co and that their product is delta_{E8}
modulo 4, and prints k = w^-1 delta_{E8} with its integrality and its congruence.

Usage: python3 computations/reports/coble_663-rel-gamma4-reduction.py
"""
import itertools, numpy as np, sympy
C = sympy.zeros(8)
for i in range(8): C[i,i]=2
for i,j in [(0,1),(1,2),(2,3),(3,4),(4,5),(5,6),(2,7)]: C[i,j]=C[j,i]=-1
Cs=np.array(C.tolist(),dtype=np.int64)
GT=np.zeros((11,11),dtype=np.int64); GT[0,0]=2; GT[1,2]=GT[2,1]=2; GT[3:,3:]=-2*Cs
GB=GT//2
coeffs=np.array(list(itertools.product(range(-2,3),repeat=8)),dtype=np.int64)
norm=np.einsum('ij,jk,ik->i',coeffs,Cs,coeffs)
reps={}
for a in (-1,1):
    for e in range(-2,3):
        for f in range(-2,3):
            sel=np.nonzero(norm==2+2*e*f)[0]
            if sel.size==0: continue
            for idx in sel:
                V=(int(a),e,f)+tuple(int(x) for x in coeffs[idx])
                cls=tuple(x%2 for x in V)
                reps.setdefault(cls,V)
print("realised classes:", len(reps))
def h_bits(v):
    gv=[sum(GB[i][j]*v[j] for j in range(11))%2 for i in range(11)]
    bits=0
    for i in range(11):
        for k in range(11):
            if (v[i]*gv[k])%2: bits |= 1<<(i*11+k)
    return bits
def proj_bits(coords):
    b=0
    for i in coords: b |= 1<<(i*11+i)
    return b
keys=sorted(reps)
hv=[h_bits(reps[k]) for k in keys]
basis={}
for i,bits in enumerate(hv):
    cur=bits; mask=1<<i
    while cur:
        piv=cur.bit_length()-1
        if piv in basis:
            cur ^= basis[piv][0]; mask ^= basis[piv][1]
        else:
            basis[piv]=(cur,mask); break
print("span dimension:", len(basis))
T=proj_bits(range(3,11))
cur=T; mask=0; ok=True
while cur:
    piv=cur.bit_length()-1
    if piv not in basis: ok=False; break
    cur ^= basis[piv][0]; mask ^= basis[piv][1]
print("h(delta_E8) in span:", ok)
if ok:
    chosen=[keys[i] for i in range(len(keys)) if (mask>>i)&1]
    Vs=[reps[c] for c in chosen]
    acc=0
    for v in Vs: acc ^= h_bits(v)
    print("certificate size:", len(Vs), "| XOR of h's == target:", acc==T)
    print("all squares -2:", all(int(np.array(v)@GT@np.array(v))==-2 for v in Vs))
    M=np.eye(11,dtype=np.int64)
    iso=True
    for v in Vs:
        vv=np.array(v,dtype=np.int64); R=np.eye(11,dtype=np.int64)+np.outer(vv, GT.dot(vv))
        if not np.array_equal(R.T@GT@R,GT): iso=False
        M=M.dot(R)
    D=np.diag([(-1 if 3<=i<=10 else 1) for i in range(11)]).astype(np.int64)
    print("every factor an isometry:", iso, "| w == delta_E8 mod 4:", bool(np.all((M-D)%4==0)))
    print("vectors:")
    for v in Vs: print("   ", list(v))

if ok:
    Ms=sympy.Matrix(M.tolist()); Ds=sympy.Matrix(D.tolist())
    print("w == delta_E8 exactly:", Ms==Ds)
    K=Ms.inv()*Ds
    Ki=all(x.q==1 for x in K)
    print("k = w^-1 delta_E8 integral:", Ki)
    print("k == id mod 4:", all(int(K[i,j]-(1 if i==j else 0))%4==0 for i in range(11) for j in range(11)))
    print("k == id exactly:", K==sympy.eye(11))
    print("k is an isometry:", (K.T*Ds*0+ (K.T*sympy.Matrix(GT.tolist())*K))==sympy.Matrix(GT.tolist()))
    if Ki:
        print("k rows:")
        for r in K.tolist(): print("   ", [int(x) for x in r])
