"""Read AET's Figure 1 subdiagrams off their own artwork (source transcription only).

This is not a mathematical certificate and computes no lattice: it transcribes which
nodes of Alexeev--Engel--Thompson's Coxeter diagram are marked in each of the four small
figures of their Figure 1, from the arXiv e-print artwork rather than from a raster
preview.

Source: arXiv:1903.09742v3 e-print (`f2-arXiv-Feb14-2023.tex`, the figure environment at
"includegraphics{fig-wA17}" etc.), whose Figure 1 is assembled from five vector PDFs:
`fig-Vinberg.pdf` (the labelled diagram `G_cox`) and, in the 2x2 block beside it,
`fig-wA17.pdf`, `fig-2wE8wA1.pdf`, `fig-wD10wE7.pdf`, `fig-wD16wA1.pdf`.  Rendered as
SVG with `pdftocairo -svg`; the subdiagram's nodes are the black-filled disks, the rest
are white disks, and both sets carry real vector coordinates.

Method.  Every figure's 24 node disks are clustered into the eight horizontal rows of the
layout, with row sizes 1,2,3,2,2,2,5,7 top to bottom; the labels of the *labelled* figure
are assigned by that row structure (the apex is 12, the bottom row 0..6), and a black disk
in a small figure is assigned the label of the white disk at the same position.  Every
black disk must land within 0.5 pt of a white disk, and the labels must be distinct; both
are asserted, so a mis-scaled or mis-flipped figure fails rather than mislabels.

Run from a directory containing the five `.svg` files.
"""
"""Read the black (subdiagram) nodes of AET Fig. 1's four small figures from the
arXiv source artwork (150 dpi vector PDFs -> SVG), by position."""
import re, xml.etree.ElementTree as ET

def mul(A, B):
    a,b,c,d,e,f = A; a2,b2,c2,d2,e2,f2 = B
    return (a*a2+b*c2, a*b2+b*d2, c*a2+d*c2, c*b2+d*d2, e*a2+f*c2+e2, e*b2+f*d2+f2)

def parse(f):
    root = ET.parse(f).getroot(); out = []
    def walk(node, T):
        tr = node.get('transform')
        if tr:
            m = re.search(r'matrix\(([-\d.eE ,]+)\)', tr)
            if m:
                T = mul(T, tuple(float(x) for x in m.group(1).replace(',', ' ').split()))
        if node.tag.endswith('path'):
            out.append((node.get('fill'), node.get('d') or '', T))
        for ch in node:
            walk(ch, T)
    walk(root, (1,0,0,1,0,0)); return out

def subpaths(d):
    return [s.strip() for s in re.split(r'(?=M )', d) if s.strip()]

def center(s, T):
    toks = re.findall(r'[MLCZ]|-?\d+\.?\d*', s); pts = []; i = 0
    while i < len(toks):
        if toks[i] in 'MLCZ':
            i += 1; continue
        pts.append((float(toks[i]), float(toks[i+1]))); i += 2
    a,b,c,d,e,f = T
    P = [(a*x+c*y+e, b*x+d*y+f) for x, y in pts]
    xs = [p[0] for p in P]; ys = [p[1] for p in P]
    return ((min(xs)+max(xs))/2, (min(ys)+max(ys))/2)

def disks(f):
    white, black = [], []
    for fill, d, T in parse(f):
        for s in subpaths(d):
            if 'C' not in s and 'A' not in s:
                continue
            c = center(s, T)
            if fill == 'rgb(100%, 100%, 100%)':
                white.append(c)
            elif fill == 'rgb(0%, 0%, 0%)':
                black.append(c)
    return white, black

# Row structure of the printed layout, top to bottom, with the labels of AET Fig. 1.
ROWS = [(1,[12]), (2,[13,11]), (3,[14,20,10]), (2,[15,9]), (2,[22,21]), (2,[16,8]),
        (5,[17,18,23,19,7]), (7,[0,1,2,3,4,5,6])]

def label(white):
    rows = {}
    for c in white:
        rows.setdefault(round(c[1], 1), []).append(c[0])
    ys = sorted(rows)
    assert [len(rows[y]) for y in ys] == [n for n, _ in ROWS], [len(rows[y]) for y in ys]
    return {lab: (x, y) for y, (n, labs) in zip(ys, ROWS) for x, lab in zip(sorted(rows[y]), labs)}

FILES = [('A~17', 'fig-wA17.svg'), ('D~10 E~7', 'fig-wD10wE7.svg'),
         ('E~8^2 A~1', 'fig-2wE8wA1.svg'), ('D~16 A~1', 'fig-wD16wA1.svg')]
res = {}
for name, f in FILES:
    w, b = disks(f)
    assert len(w) == 24, (name, len(w))
    lab = label(w)
    got = []
    for c in b:
        best = min(lab, key=lambda L: (lab[L][0]-c[0])**2 + (lab[L][1]-c[1])**2)
        dist = ((lab[best][0]-c[0])**2 + (lab[best][1]-c[1])**2) ** 0.5
        assert dist < 0.5, (name, best, dist)
        got.append(best)
    assert len(set(got)) == len(got)
    res[name] = sorted(got)
    print(f'{name:12} {len(got):2} black nodes: {res[name]}')
    print(f'{"":12}    complement ({24-len(got)}): {sorted(set(range(24))-set(got))}')

RIM = sorted([12,13,14,15,16,17] + list(range(12)))
print('\nA~17 = rim of the triangle:', res['A~17'] == RIM,
      '| symmetric difference:', sorted(set(res['A~17']) ^ set(RIM)))
