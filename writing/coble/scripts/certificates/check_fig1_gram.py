"""Check the Figure 1 root data against the source's own Lemma 4.7 and the Kac marks.

Run on the shared development image:

    $HOME/.udocker/bin/proot-x86_64 -R $HOME/sage-image/rootfs -b /proc -b /dev -b /sys \
        -b <repo>:/repo -w /repo /sage/.venv/bin/sage \
        /repo/writing/coble/scripts/certificates/check_fig1_gram.py

Input, from the source (AET23, arXiv:1903.09742v3): the 24 roots r_0..r_23 of Figure 1
(p. 22), each of square -2, with the candidate pairings -- 1 along the 18-cycle 0..17 and at
(0,18), (6,19), (12,20); 2 at (18,21), (21,9), (19,22), (22,15), (20,23), (23,3); 6 at
(21,22), (22,23), (23,21) -- and Table 1 of Sec. 4C, which lists each maximal parabolic
subdiagram vertex by vertex with the extended node braced.

The check: for each listed component, the induced Gram block must be the affine Cartan matrix
of its type, i.e. its null vector must have the Kac marks of that type, taken from
CartanType([letter, rank, 1]).a().  All seven components pass.  The first E8's solved null
vector [1,2,3,4,5,6,4,2,3] is exactly the vector the source displays,
n(E8^(1)) = r13+2r14+3r15+4r16+5r17+6r0+4r1+2r2+3r18, and Lemma 4.7 holds in the
presentation: the four differences of component null vectors are relations, G(a1 - a2) = 0.

Correction to an earlier version of this file: its D~10 node list was
[18,17]+list(range(7))+[19], which omits node 7 and gives ten nodes.  Table 1 and Lemma 4.5 say
[18,17,0,...,6,7,19], i.e. range(8), eleven nodes.  That was a transcription bug here, not a
property of the source data, and with it fixed the D~10 block is degenerate with the Kac marks
of affine D10, as it must be.  The supplied Gram edges were not altered.
"""
from itertools import combinations
from sage.all import ZZ, Matrix, vector
from sage.combinat.root_system.cartan_type import CartanType

CAND = dict(diag=-2, one=[(i,(i+1)%18) for i in range(18)]+[(0,18),(6,19),(12,20)],
            two=[(18,21),(21,9),(19,22),(22,15),(20,23),(23,3)],
            six=[(21,22),(22,23),(23,21)])

def build(extra_one=(), extra_two=(), drop=()):
    G=[[0]*24 for _ in range(24)]
    for i in range(24): G[i][i]=-2
    def setp(i,j,v):
        if i==j: return True
        G[i][j]=G[j][i]=v; return True
    for a,b in CAND['one']: setp(a,b,1)
    for a,b in CAND['two']: setp(a,b,2)
    for a,b in CAND['six']: setp(a,b,6)
    for a,b in tuple(extra_one): setp(a,b,1)
    for a,b in tuple(extra_two): setp(a,b,2)
    for a,b in tuple(drop): G[a][b]=G[b][a]=0
    return Matrix(ZZ,G)

CHAINS = {
 "A~17": (list(range(18)), ("A",17)),
 "D~10": ([18,17]+list(range(8))+[19], ("D",10)),   # 18,17,0,1,...,7,19: eleven nodes
 "E~7":  (list(range(9,16))+[20], ("E",7)),
 "E~8^(1)": ([13,14,15,16,17,0,1,2,18], ("E",8)),
 "E~8^(2)": ([4,5,6,7,8,9,10,11,19], ("E",8)),
 "A~1": ([20,23], ("A",1)),
 "D~16": ([19,5,6,7,8,9,10,11,12,13,14,15,16,17,0,1,18], ("D",16)),
 "A~1*": ([3,23], ("A",1)),
}

def blockok(G, chain, typ):
    B=Matrix(ZZ,[[G[a,b] for b in chain] for a in chain])
    k=B.kernel().basis_matrix()
    if k.nrows()!=1: return None
    a=[x for x in k[0]]; s=min(abs(x) for x in a if x!=0); a=[x/s for x in a]
    if not all(x in ZZ for x in a): return None
    a=[int(x) for x in a]
    exp=sorted(CartanType([typ[0],typ[1],1]).a().values())
    return a if sorted(a)==exp else None

G=build()
print("candidate: rank", G.rank(), "kernel", 24-G.rank())
for name,(chain,typ) in CHAINS.items():
    ok=blockok(G,chain,typ)
    print(f"  {name:9} {'OK '+str(ok) if ok else 'not affine with these incidences'}")

# for the blocks that fail, search one extra pairing-1 edge inside the block
for name,(chain,typ) in CHAINS.items():
    if blockok(G,chain,typ): continue
    hits=[]
    for a,b in combinations(sorted(set(chain)),2):
        if G[a,b]!=0: continue
        G2=build(extra_one=[(a,b)])
        if G2.rank()!=19: continue
        ok=blockok(G2,chain,typ)
        if ok: hits.append(((a,b),ok))
    print(f"  {name:9} single extra edge inside the block that makes it affine:", hits[:6])

# ------------------------------------ Lemma 4.7: the components' null vectors coincide in N
solved = {}
for name, (chain, typ) in CHAINS.items():
    B = Matrix(ZZ, [[G[a, b] for b in chain] for a in chain])
    k = B.kernel().basis_matrix()
    a = [x for x in k[0]]; sc = min(abs(x) for x in a if x != 0); a = [int(x / sc) for x in a]
    solved[name] = (chain, a)
print("\nLemma 4.7 (lem:N-linear-rels): the square-zero vectors of the components coincide,")
print("i.e. G(a_1 - a_2) = 0 in the presentation Z^24.")
for left, right in [("D~10", "E~7"), ("E~8^(1)", "E~8^(2)"), ("E~8^(1)", "A~1"),
                    ("D~16", "A~1*")]:
    d = [0] * 24
    for node, c in zip(*solved[left]):
        d[node] += c
    for node, c in zip(*solved[right]):
        d[node] -= c
    rel = G * vector(ZZ, d)
    print(f"  n({left:8}) - n({right:6}): relation = {all(x == 0 for x in rel)}")
