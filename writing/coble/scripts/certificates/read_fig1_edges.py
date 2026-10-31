"""Edges of AET Figure 1's subdiagrams, from the e-print artwork (transcription only).

Source: arXiv:1903.09742v3 e-print, the five vector PDFs of the figure environment that
builds Figure 1 (p. 22) -- `fig-Vinberg` for the labelled diagram, and `fig-wA17`,
`fig-2wE8wA1`, `fig-wD10wE7`, `fig-wD16wA1` for the small ones.  Reads stroke geometry
with `mutool draw -F trace`; computes no lattice and is not a certificate.

State of the transcription
--------------------------
Vertex sets: settled.  They come from the filled disks, and `read_fig1.py` asserts that
every black disk sits on a printed node position; run on the four small figures it gives
18, 19, 20 and 19 vertices, and the 18 of them for `fig-wA17` are exactly the rim.

Edges: not settled.  With the rule below (drop the closed border polyline, snap every
point, join consecutive snapped nodes) the subdiagram figures reproduce the expected
structure for one of the four -- `fig-wA17` gives an 18-cycle, every vertex of degree 2 --
and not for the other three, whose induced edge lists then contain strokes that are not
edges of G_cox, such as (0,18), (3,20), (9,18), (12,20) in `fig-wD10wE7`.

Why: the diagram is drawn as a few long polylines, not as one stroke per edge, and some of
their bend points are not nodes at all -- in `fig-Vinberg` a spoke runs through the
triangle's centroid (0,0) and through (0,63.78) in the artwork's data frame, neither of
which is a vertex.  A polyline broken at such a point yields pieces that snap to nothing,
so its real edges are dropped while the strokes that do read cleanly are kept, which is
exactly the mixture of missing and spurious edges observed.  Segmenting these polylines
needs an explicit model of how the figure was drawn (which bends are geometric and which
are nodes); that model is the next step, and until it exists no mark is recovered from
these graphs and the cusps other than A~17 are left without a null vector.

"""
"""Induced graphs from the e-print artwork of AET Figure 1 (transcription only).

Rule per stroke polyline: drop closed polylines (the triangle border, which runs through
nodes 0, 6 and 12 without being a diagram edge); then walk the points, snap each one that
lands on a node, ignore points that do not (the redundant collinear midpoints), and add an
edge between consecutive snapped nodes.  That handles both a single edge drawn with a
redundant midpoint and a chain drawn through several nodes.
"""
import subprocess
from collections import Counter, defaultdict
exec(open('trace_gram.py').read().split("subprocess.run(")[0])
exec(open('induced2.py').read().split("def strokes(")[0].split("for name,f in FILES.items():")[0].split("exec(open")[0] or "pass")

BLACK = {
 'A~17':     tuple(range(18)),
 'D~10 E~7':(0,1,2,3,4,5,6,7,9,10,11,12,13,14,15,17,18,19,20),
 'E~8^2 A~1':(0,1,2,4,5,6,7,8,9,10,11,13,14,15,16,17,18,19,20,23),
 'D~16 A~1': (0,1,3,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,23),
}
FILES={'A~17':'fig-wA17','D~10 E~7':'fig-wD10wE7','E~8^2 A~1':'fig-2wE8wA1',
       'D~16 A~1':'fig-wD16wA1'}
ROWS=[(1,[12]),(2,[13,11]),(3,[14,20,10]),(2,[15,9]),(2,[22,21]),(2,[16,8]),
      (5,[17,18,23,19,7]),(7,[0,1,2,3,4,5,6])]

def load(f):
    TR=f'.scratch_{f}.xml'
    subprocess.run(['mutool','draw','-F','trace','-o',TR,'-q','../refs/aet_src/'+f+'.pdf'],
                   check=True, capture_output=True)
    nodes=[]
    for attrs,body in blocks(TR,'fill_path'):
        for s,curved in subpaths(body,attrs['T']):
            xs=[p[0] for p in s]; ys=[p[1] for p in s]
            if curved and 4<max(xs)-min(xs)<8 and 4<max(ys)-min(ys)<8 and len(s)>=8:
                nodes.append(((min(xs)+max(xs))/2,(min(ys)+max(ys))/2))
    rows={}
    for c in nodes: rows.setdefault(round(c[1],1),[]).append(c[0])
    ys=sorted(rows)
    assert [len(rows[y]) for y in ys]==[n for n,_ in ROWS],[len(rows[y]) for y in ys]
    return TR,{l:(x,y) for y,(n,ls) in zip(ys,ROWS) for x,l in zip(sorted(rows[y]),ls)}

def edges(TR,lab):
    def snap(p,tol=6.0):
        b=min(lab,key=lambda L:(lab[L][0]-p[0])**2+(lab[L][1]-p[1])**2)
        d=((lab[b][0]-p[0])**2+(lab[b][1]-p[1])**2)**0.5
        return b if d<tol else None
    E=defaultdict(list)
    for attrs,body in blocks(TR,'stroke_path'):
        for s,curved in subpaths(body,attrs['T']):
            if curved or len(s)<2: continue
            if abs(s[0][0]-s[-1][0])<0.2 and abs(s[0][1]-s[-1][1])<0.2: continue
            last=None
            for p in s:
                v=snap(p)
                if v is None: continue
                if last is not None and v!=last:
                    E[tuple(sorted((last,v)))].append(
                        (round(attrs['lw'],3), attrs['color'], attrs['dash']))
                last=v
    return E

if __name__=="__main__":
    TR,lab=load('fig-Vinberg'); A=edges(TR,lab)
    print(f'ambient G_cox: {len(A)} edges on 24 nodes')
    for e in sorted(A): print('  ',e,sorted(set(A[e])))
