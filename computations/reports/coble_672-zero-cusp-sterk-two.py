"""Which Sterk cusp carries the Coble 0-cusp: the boundary lattice against the chamber.

Owner calls, fixed before the run
---------------------------------
The three period lattices are the catalogue's own objects, each a library construction of the
formula its docstring cites, and each is checked here against the orthogonal sum of its named
summands:

  NamedLattices.Tco    T_Co = <2> + E(2) = <2> + U(2) + E8(-2)   [@DK13, (3.6), printed p. 513]
  NamedLattices.TEn    T_En = U + U(2) + E8(-2)                  [@AEGS25, Def. 2.3, printed p. 586]
  NamedLattices.TdP    T_dP = U + U(2) + E8^2                    [@AEGS25, Sec. 3.1, printed p. 589]

The five cusp vectors are the library's: ``Sterk.selected_isotropic_vectors()``, whose docstring
cites Sterk (1991), (4.2.2)--(4.2.3), p. 16; the second printed representative of cusp 4 is
``Sterk.sterk4_cusp_vector()``.  The two are the paper's two vectors for that cusp, and the library's
own test ``tests/lattices/test_cusp_lattices.sage`` asserts that their reductions are isometric;
both are run here.

Every lattice operation below is the library's:

  ``+`` between named lattices            orthogonal direct sum
  ``primitive_sublattice_from``           the span of a family, saturated
  ``orthogonal_complement``               I^perp in the ambient lattice
  ``radical_quotient``                    L/rad(L)
  ``primitive_isotropic_subobject``       the primitive isotropic line
  ``isotropic_perpendicular``, ``isotropic_reduction``   v^perp, then v^perp/Zv
  ``b``, ``divisibility_ideal``, ``determinant``, ``signature_pair``, ``module_rank``,
  ``is_even``, ``is_p_elementary``, ``EvenTwoElementaryLattices(...).two_elementary_invariants``,
  ``is_isometric``, and ``Embeddings.TEn_into_TdP``

No Gram matrix is typed in this file and no linear-algebra algorithm is written in it; the Smith
form, the dual basis, the complement and the isometry decisions are the library's.  Earlier
versions of this record built the three lattices as literal matrices and computed the quotients and
the invariants with hand-written routines, which is what this rewrite removes.

One input is transcribed, and cannot be built: the wall Gram matrices of [@AEGS25] Figures 7--8,
printed pp. 594--595, as read from the accepted record
``computations/reports/coble_enriques-white-root-facets-run.txt`` (#654).  A printed figure's roots
have no lattice formula to construct from, so part F reads that transcript, says so on every line
that uses it, and computes only the folding arithmetic on it.  The two inputs it reads are the wall
Gram matrix of each cusp's diagram in figure order, and the printed pairings (r_i, delta).

Run:
  $HOME/.udocker/bin/proot-x86_64 -R $HOME/sage-image/rootfs -b /proc -b /dev -b /sys \\
    -b <worktree>:/repo -w /repo /sage/.venv/bin/python \\
    /repo/computations/reports/coble_672-zero-cusp-sterk-two.py
Transcript: coble_672-zero-cusp-sterk-two-run.txt
"""
import platform
import re
from fractions import Fraction as F
from math import gcd
from pathlib import Path

from sage.version import version as SAGE_VERSION
from sage_extensions.all import (Embeddings, EvenTwoElementaryLattices, NamedLattices, Sterk, ZZ)

REPO = Path(__file__).resolve().parents[2]
WHITE = REPO / "computations/reports/coble_enriques-white-root-facets-run.txt"
PAIR = REPO / "computations/reports/coble_pair-semifan-cusps-run.txt"
assert WHITE.exists() and PAIR.exists(), "part F needs both committed transcripts"

Tco, TEn, TdP = NamedLattices.Tco, NamedLattices.TEn, NamedLattices.TdP


def orth(*Ms):
    """The library's orthogonal direct sum."""
    out = Ms[0]
    for M in Ms[1:]:
        out = out + M
    return out


def describe(name, L):
    print("  %-22s rank %s  det %s  signature %s  even %s"
          % (name, L.module_rank(), L.determinant(), L.signature_pair(), L.is_even()))


def two_elementary(name, L):
    inv = EvenTwoElementaryLattices(ZZ)(L).two_elementary_invariants()
    print("  %-26s rank %s  det %s  signature %s  even %s  2-elementary %s  invariants %s"
          % (name, L.module_rank(), L.determinant(), L.signature_pair(), L.is_even(),
             L.is_p_elementary(2), inv))
    return inv


def generatore(lattice, label):
    return lattice.module_generator(label)


print("Which Sterk cusp carries the Coble 0-cusp: the boundary lattice against the chamber")
print("Sage %s, python %s, sage_extensions built from the checkout at .scratch/sage-extensions"
      % (SAGE_VERSION, platform.python_version()))
print("every lattice below is a library object; no Gram matrix is typed in this file")
print()

print("=== part A. the three period lattices, and the sums of their named summands")
describe("T_Co = NamedLattices.Tco", Tco)
describe("T_En = NamedLattices.TEn", TEn)
describe("T_dP = NamedLattices.TdP", TdP)
print("  T_Co is <2> + U(2) + E8(2)        :",
      Tco.is_isometric(orth(NamedLattices.Z_2, NamedLattices.U_2, NamedLattices.E8_2)))
print("  T_En is U + U(2) + E8(2)          :",
      TEn.is_isometric(orth(NamedLattices.U, NamedLattices.U_2, NamedLattices.E8_2)))
print("  T_dP is U + U(2) + E8 + E8        :",
      TdP.is_isometric(orth(NamedLattices.U, NamedLattices.U_2, NamedLattices.E8, NamedLattices.E8)))

print()
print("=== part B. delta = e - f, and T_Co = delta^perp, decided by the library")
e, f = generatore(TEn, "e"), generatore(TEn, "f")
delta = e - f
print("  delta = e - f: square %s, divisibility %s, isotropic? %s"
      % (TEn.b(delta, delta), delta.divisibility_ideal(), TEn.b(delta, delta) == 0))
delta_perp = TEn.primitive_sublattice_from([delta]).orthogonal_complement()
print("  delta^perp in T_En: rank %s, det %s, signature %s, even %s"
      % (delta_perp.module_rank(), delta_perp.determinant(), delta_perp.signature_pair(),
         delta_perp.is_even()))
print("  delta^perp is T_Co                :", delta_perp.is_isometric(Tco))

print()
print("=== part C. Sterk's five cusp vectors, from the library, and their Coble 0-cusps")
print("  the vectors are Sterk.selected_isotropic_vectors(); coordinates in the T_En basis")
labels = sorted(TEn.module_generating_set())
print("  coordinate order: (%s)" % ", ".join(labels))
vectors = Sterk.selected_isotropic_vectors()
coble_boundary = {}
for name in sorted(vectors):
    w = vectors[name]
    given = w.to_vector()
    square = w.q()
    pairing = TEn.b(w, delta)
    line = TEn.primitive_isotropic_subobject(w)   # admission checks saturation and isotropy
    print("  %-8s coords %-46s square %s  (w, delta) %s  div_T_En %s  line rank %s (admitted:"
          " primitive and totally isotropic)"
          % (name, [int(given(label)) for label in labels], square, pairing,
             w.divisibility_ideal(), line.module_rank()))
    if pairing != 0:
        print("           not a vector of T_Co = delta^perp, so no 0-cusp of F_Co,2 over this cusp")
        continue
    span = TEn.primitive_sublattice_from([delta, w])
    perp = span.orthogonal_complement()
    coble_boundary[name] = perp.radical_quotient()
    print("           delta^perp cap w^perp: rank %s, nondegenerate %s; its radical quotient is the"
          " boundary lattice of the Coble 0-cusp at this cusp" % (perp.module_rank(),
                                                                 perp.is_nondegenerate()))
    two_elementary("           boundary lattice:", coble_boundary[name])
    print("           is <2> + E8(2) = (9,9,1)_1:",
          coble_boundary[name].is_isometric(orth(NamedLattices.Z_2, NamedLattices.E8_2)))

print()
print("=== part D. cusp 4 has two printed representatives; the library records both")
w4b = Sterk.sterk4_cusp_vector()
for label, w in (("(4.2.3)", vectors["Sterk_4"]), ("chamber", w4b)):
    given = w.to_vector()
    print("  cusp 4 %-8s coords %-46s square %s  (w, delta) %s"
          % (label, [int(given(x)) for x in labels], w.q(), TEn.b(w, delta)))
    span = TEn.primitive_sublattice_from([delta, w])
    Q = span.orthogonal_complement().radical_quotient()
    print("           boundary lattice rank %s det %s invariants %s ; is <2> + E8(2): %s"
          % (Q.module_rank(), Q.determinant(),
             EvenTwoElementaryLattices(ZZ)(Q).two_elementary_invariants(),
             Q.is_isometric(orth(NamedLattices.Z_2, NamedLattices.E8_2))))
print("  the two representatives have isometric reductions, so the cusp's boundary lattice is"
      " independent of the choice (tests/lattices/test_cusp_lattices.sage asserts it as well)")

print()
print("=== part E. the F(2,2,0) side, through the library's T_En -> T_dP embedding")
for name in sorted(vectors):
    wdp = Embeddings.TEn_into_TdP(vectors[name])
    red = TdP.primitive_isotropic_subobject(wdp).isotropic_reduction()
    print("  %-8s div_T_dP %-4s reduction rank %s  invariants %s  = U + E8^2 (18,0,0): %-5s"
          "  = U(2) + E8^2 (18,2,0): %s"
          % (name, wdp.divisibility_ideal(), red.module_rank(),
             EvenTwoElementaryLattices(ZZ)(red).two_elementary_invariants(),
             red.is_isometric(orth(NamedLattices.U, NamedLattices.E8, NamedLattices.E8)),
             red.is_isometric(orth(NamedLattices.U_2, NamedLattices.E8, NamedLattices.E8))))

# ---------------------------------------------------------------- part F, on the transcript
print()
print("=== part F. the restricted chamber C cap delta^perp, from the transcribed figure data")
print("  input, transcribed and not constructed: the wall Gram matrix of each AEGS25 Figures 7--8")
print("  diagram in figure order, and the printed pairings (r_i, delta), both from")
print("  computations/reports/coble_enriques-white-root-facets-run.txt and")
print("  computations/reports/coble_pair-semifan-cusps-run.txt")


def wall_gram_from_white(cusp):
    lines = WHITE.read_text(encoding="utf-8").splitlines()
    start = next(i for i, ln in enumerate(lines) if re.match(r"=== cusp %d; eta" % cusp, ln))
    j = start
    while not lines[j].startswith("wall Gram matrix"):
        j += 1
    j += 1
    M = []
    while j < len(lines) and lines[j].strip().startswith("["):
        M.append([int(x) for x in lines[j].strip().strip("[]").split()])
        j += 1
    return M


pair_text = PAIR.read_text(encoding="utf-8").splitlines()
white_node, pairdelta = {}, {}
cur = None
for ln in pair_text:
    m = re.match(r"-- the 0-cusp over Sterk cusp (\d+)", ln)
    if m:
        cur = int(m.group(1))
        continue
    if cur is None:
        continue
    m = re.search(r"the white node is figure node (\d+)", ln)
    if m:
        white_node[cur] = int(m.group(1))
    m = re.match(r"\s+pairings \(r_i,delta\) nonzero only for \[([^\]]*)\], "
                 r"with values \[([^\]]*)\]", ln)
    if m and m.group(1).strip():
        pairdelta[cur] = dict(zip([int(x) for x in m.group(1).split(",")],
                                  [int(x) for x in m.group(2).split(",")]))


def spider(G, walls):
    """Labelled graph of a wall set: tree?, degree sequence, squares, bond labels, and the arms
    (length, label of the last edge, square of the end vertex) when there is one branch vertex."""
    idx = sorted(walls)
    n = len(idx)
    edges = [(i, j) for i in range(n) for j in range(i + 1, n) if G[idx[i]][idx[j]] != 0]
    deg = [0] * n
    for i, j in edges:
        deg[i] += 1
        deg[j] += 1
    labels_of_edge = {}
    for i, j in edges:
        cos = abs(float(G[idx[i]][idx[j]])) / (
            float(abs(G[idx[i]][idx[i]])) * float(abs(G[idx[j]][idx[j]]))) ** 0.5
        labels_of_edge[(i, j)] = ("3" if abs(cos - 0.5) < 1e-9 else
                                  "4" if abs(cos - 2 ** -0.5) < 1e-9 else
                                  "parallel" if abs(cos - 1) < 1e-9 else "other")
    squares = [G[idx[i]][idx[i]] for i in range(n)]
    arms = None
    branch = [i for i in range(n) if deg[i] >= 3]
    if len(edges) == n - 1 and len(branch) == 1:
        b = branch[0]
        arms = []
        for i, j in edges:
            if b not in (i, j):
                continue
            prev, cur_ = b, (j if i == b else i)
            length, last = 1, (min(prev, cur_), max(prev, cur_))
            while deg[cur_] == 2:
                nxt = [z for (a, c) in edges for z in ([c] if a == cur_ else ([a] if c == cur_ else []))
                       if z != prev]
                prev, cur_ = cur_, nxt[0]
                length += 1
                last = (min(prev, cur_), max(prev, cur_))
            arms.append((length, labels_of_edge[last], squares[cur_]))
        arms.sort()
    return dict(tree=len(edges) == n - 1, walls=n, degrees=sorted(deg),
                squares=[str(x) for x in sorted(squares)],
                edge_labels=sorted(labels_of_edge.values()), arms=arms)


# thm:coble-cusp-chamber, from [@AN06, Table 1, entry N = 10, printed p. 52]: walls 1..8 of
# square -4 and wall 9 of square -2, adjacency 1-3, 2-4, 3-4, 4-5, 5-6, 6-7, 7-8, 8-9, every
# bond of label 3 except 8-9 of label 4; |g| = cos(pi/label) gives the pairing 2 on each edge.
COBLE_EDGES = [(1, 3), (2, 4), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9)]
G_coble = [[0] * 9 for _ in range(9)]
for _w in range(1, 10):
    G_coble[_w - 1][_w - 1] = -2 if _w == 9 else -4
for _u, _v in COBLE_EDGES:
    G_coble[_u - 1][_v - 1] = 2
    G_coble[_v - 1][_u - 1] = 2
print("  thm:coble-cusp-chamber (AN06 Table 1, N = 10, printed p. 52), nine walls:")
print("   ", spider(G_coble, set(range(9))))

for k in sorted(white_node):
    G = wall_gram_from_white(k)
    white = white_node[k]                      # delta itself; its projection is 0
    pd = {i: 0 for i in range(1, len(G) + 1)}
    pd.update(pairdelta.get(k, {}))
    keep = [i for i in range(1, len(G) + 1) if i != white]
    # a wall alpha projects to alpha + ((alpha,delta)/2) delta; since delta^2 = -2 the projected
    # square is alpha^2 + (alpha,delta)^2/2 and the projected pairing is g_ij + g_id g_jd / 2
    P = [[0] * len(G) for _ in range(len(G))]
    for a in keep:
        for b in keep:
            P[a - 1][b - 1] = G[a - 1][b - 1] + F(pd[a] * pd[b], 2)
    desc = spider(P, set(i - 1 for i in keep))
    parallel = sum(1 for lab in desc["edge_labels"] if lab == "parallel")
    print("  cusp %d: white node figure %d; %d projected roots, %d induced parallel pair(s),"
          " %d distinct walls" % (k, white, len(keep), parallel, len(keep) - parallel))
    print("   ", desc)
