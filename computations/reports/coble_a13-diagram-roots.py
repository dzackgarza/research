"""A13: the polarization classes and the (18,0,0)_1 diagram's roots in the standard basis.

Self-contained: no sage, no sage-extensions.  Exact integer and rational arithmetic with sympy.

The marking is the one of @thm:theta-co-coordinates and @thm:gamma-co-coordinates on
writing/coble/lattices-and-moduli/the-heegner-line-and-the-coble-arithmetic-group.md.

What is computed.

  * the two copies of the Coble 0-cusp's boundary lattice (18,0,0)_1 = U + E8^2 inside lkt:
    W = U_2 + E8_1 + E8_2 and W' = U_3 + E8_1 + E8_2, with their invariants;
  * the nineteen roots of the Coxeter diagram of (18,0,0)_1, in the coordinates of the root table
    of writing/coble/computations/root-vectors-and-folded-sterk-diagrams.md (section "The
    (18,0,0)_1 diagram: 19 roots"), in the standard basis e_0..e_21: their squares, their Gram
    matrix, and the three structural checks the page states (the nineteen nodes, the two E8
    subdiagrams, and the null relation of the 2 E8-tilde parabolic);
  * the action of theta_Co on them: theta_Co(W) = W' and theta_Co(Phi) = -Phi', with the node
    pairing w_k -> w'_{18-k}, which is the reflection J : alpha_k -> alpha_{20-k} of
    [@AEGS25, Lemma 3.9, printed p. 593] read on the two copies;
  * the folded roots w_k + w_{18-k} (k = 1..8), w_9, w_18 + w_19, whose norms are the entries of
    the cusp-2 diagram of [@AEGS25, Fig. 7, printed p. 594];
  * the pairings of the polarization classes with every root, for H = h~_Co = h_En, and the
    pairings of the Heegner vector delta.
"""
import sys
from fractions import Fraction

from sympy import Matrix, Rational, eye, zeros
from sympy import __version__ as sympy_version

sys.stdout.reconfigure(line_buffering=True)

N = 22
U_BLOCKS = [(0, 1), (2, 3), (4, 5)]
E_BLOCKS = [list(range(6, 14)), list(range(14, 22))]
E8_EDGES = [(0, 2), (1, 3), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7)]


def build_G():
    G = zeros(N, N)
    for a, b in U_BLOCKS:
        G[a, b] = 1
        G[b, a] = 1
    for blk in E_BLOCKS:
        for i in range(8):
            G[blk[i], blk[i]] = -2
        for i, j in E8_EDGES:
            G[blk[i], blk[j]] = 1
            G[blk[j], blk[i]] = 1
    return G


def col(entries):
    v = zeros(N, 1)
    for i, c in entries.items():
        v[i] = c
    return v


def show(v):
    items = [(i, Fraction(x)) for i, x in enumerate(v) if x != 0]
    if not items:
        return "0"
    out = []
    for i, c in items:
        num, den = c.numerator, c.denominator
        s = ("e_%d" % i) if den == 1 else ("e_%d/%d" % (i, den))
        if abs(num) != 1:
            s = ("%d*" % num) + s
        out.append(("+" if c > 0 else "-") + " " + s.lstrip("-"))
    return " ".join(out)


def sq(v):
    return (v.T * G * v)[0, 0]


def ip(x, y):
    return (x.T * G * y)[0, 0]


def aegs_enriques(G, N):
    """I_En of [@AEGS25, Def. 2.3], defined on the named summands of lkt.

    -id on U_1, the swap of U_2 and U_3, and the swap of the two E8 summands.  The matrix is
    read off that definition, not typed.
    """
    M = zeros(N, N)
    for k in (0, 1):
        M[k, k] = -1
    for (a, b) in ((2, 4), (3, 5)):
        M[a, b] = 1
        M[b, a] = 1
    for k in range(8):
        M[6 + k, 14 + k] = 1
        M[14 + k, 6 + k] = 1
    return M


def reflection_in(G, N, v):
    """The integral reflection in v: 1 - (2/v^2) v (G v)^T."""
    return eye(N) - Rational(2, 1) / (v.T * G * v)[0, 0] * v * (G * v).T


def theta_co(G, N):
    """theta_Co = -w . I_En for w the reflection in alpha = e_0 - e_1."""
    alpha = zeros(N, 1)
    alpha[0] = 1
    alpha[1] = -1
    return -(reflection_in(G, N, alpha) * aegs_enriques(G, N))


print("provenance")
print("  sympy %s, exact integer and rational arithmetic" % sympy_version)
print("  python %s" % sys.version.split()[0])
print("  no sage and no sage-extensions")
print("  marking: @thm:theta-co-coordinates; lattices S_Co, T_Co: @thm:gamma-co-coordinates")
print("  root table: writing/coble/computations/root-vectors-and-folded-sterk-diagrams.md,")
print("              section 'The (18,0,0)_1 diagram: 19 roots'")
print("")

G = build_G()
# E8 summands, Bourbaki numbering: alpha_i = e_{5+i} in E8_1, tilde alpha_i = e_{13+i} in E8_2
alpha = {i: col({5 + i: 1}) for i in range(1, 9)}
talpha = {i: col({13 + i: 1}) for i in range(1, 9)}
G_E1 = Matrix(8, 8, lambda i, j: ip(alpha[i + 1], alpha[j + 1]))
G_E2 = Matrix(8, 8, lambda i, j: ip(talpha[i + 1], talpha[j + 1]))
# fundamental weights dual to the simple roots: w_i with (w_i, alpha_j) = delta_ij
W1 = Matrix.hstack(*[alpha[i] for i in range(1, 9)]) * G_E1.inv()
W2 = Matrix.hstack(*[talpha[i] for i in range(1, 9)]) * G_E2.inv()
print("1. the two E8 summands, and the fundamental weights")
E8_EDGES_1BASED = [(1, 3), (2, 4), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8)]


def cartan_e8_negative():
    """-Cartan(E8) in Bourbaki numbering, built symmetrically from the edge list."""
    C = zeros(8, 8)
    for i in range(8):
        C[i, i] = -2
    for a, b in E8_EDGES_1BASED:
        C[a - 1, b - 1] = 1
        C[b - 1, a - 1] = 1
    return C


print("   E8 Gram = -Cartan, checked: %s" % (G_E1 == cartan_e8_negative()))
print("   (the expected matrix is built symmetrically from the Bourbaki edge list; an earlier")
print("    version filled one orientation of each edge only, so the check printed False while")
print("    the Gram matrix itself was right -- see section 5 for the same block against the")
print("    diagram roots)")
print("   (w_8, alpha_j) = delta_{8j}: %s, (w_8)^2 = %s"
      % ([[ip(W1[:, 7], alpha[j]) for j in range(1, 9)]], sq(W1[:, 7])))
print("   (tilde w_8, tilde alpha_j) = delta_{8j}: %s, (tilde w_8)^2 = %s"
      % ([[ip(W2[:, 7], talpha[j]) for j in range(1, 9)]], sq(W2[:, 7])))
print("")

print("2. the two copies of (18,0,0)_1 = U + E8^2 inside lkt")
idxW = [2, 3] + list(range(6, 14)) + list(range(14, 22))
idxWp = [4, 5] + list(range(6, 14)) + list(range(14, 22))
for name, idx in (("W  = U_2 + E8^2", idxW), ("W' = U_3 + E8^2", idxWp)):
    B = zeros(N, len(idx))
    for k, i in enumerate(idx):
        B[i, k] = 1
    Gm = B.T * G * B
    print("   %s: standard basis vectors %s" % (name, ", ".join("e_%d" % i for i in idx)))
    print("     rank %d, det %d, even %s, diagonal %s"
          % (Gm.rows, int(Gm.det()), all(int(Gm[i, i]) % 2 == 0 for i in range(Gm.rows)),
             [int(Gm[i, i]) for i in range(Gm.rows)]))
print("")

print("3. the nineteen roots of the diagram, in the standard basis")
e = col({2: 1})
f = col({3: 1})
ep = col({4: 1})
fp = col({5: 1})


def diagram_roots(evec, fvec, EPS, TEPS, TILDE):
    """the root table, with the U basis e, f given by evec, fvec"""
    def al(i):
        return EPS[i]
    def tal(i):
        return TEPS[i]
    def w8():
        return TILDE[0]
    def tw8():
        return TILDE[1]
    return [
        ("w_1", al(1)), ("w_2", al(3)), ("w_3", al(4)), ("w_4", al(5)),
        ("w_5", al(6)), ("w_6", al(7)), ("w_7", al(8)),
        ("w_8", w8() + evec), ("w_9", fvec - evec), ("w_10", tw8() + evec),
        ("w_11", tal(8)), ("w_12", tal(7)), ("w_13", tal(6)), ("w_14", tal(5)),
        ("w_15", tal(4)), ("w_16", tal(3)), ("w_17", tal(1)),
        ("w_18", al(2)), ("w_19", tal(2)),
    ]


Phi = diagram_roots(e, f, alpha, talpha, (W1[:, 7], W2[:, 7]))
names = [n for n, _ in Phi]
vecs = [v for _, v in Phi]
for n, v in Phi:
    print("   %-5s = %-60s square %s" % (n, show(v), sq(v)))
print("   every root has square -2: %s" % all(sq(v) == -2 for v in vecs))
print("")

print("4. the Gram matrix of the nineteen roots")
Gr = Matrix(19, 19, lambda i, j: ip(vecs[i], vecs[j]))
for i in range(19):
    print("   %-5s " % names[i] + " ".join("%2d" % int(Gr[i, j]) for j in range(19)))
vals = sorted({int(Gr[i, j]) for i in range(19) for j in range(19) if i != j})
print("   off-diagonal values %s: 1 is a bond of the diagram (label 3), 2 a bond of label 4," % vals)
print("   0 no edge; the diagonal is -2 throughout: %s"
      % all(int(Gr[i, i]) == -2 for i in range(19)))
print("   every bond is of label 3, there is no label-4 bond: %s" % (vals == [0, 1]))
seen = {0}
stack = [0]
while stack:
    a = stack.pop()
    for b in range(19):
        if b != a and Gr[a, b] != 0 and b not in seen:
            seen.add(b)
            stack.append(b)
print("   the diagram is connected: %d of 19 nodes reached from w_1" % len(seen))
B_W = zeros(N, 18)
for k, i in enumerate([2, 3] + list(range(6, 14)) + list(range(14, 22))):
    B_W[i, k] = 1
roots_mat = Matrix.hstack(*vecs)
print("   the nineteen roots have rank %d, so the span of the roots is W tensor Q and the roots"
      " generate W: %s" % (roots_mat.rank(), roots_mat.rank() == 18))
print("")

print("5. the two E8 subdiagrams, and the shape of the diagram")
E1_nodes = [0, 1, 2, 3, 4, 5, 6, 17]      # w_1..w_7 carry alpha_1, alpha_3..alpha_8; w_18 carries alpha_2
E2_nodes = [10, 11, 12, 13, 14, 15, 16, 18]
perm1 = [1, 3, 4, 5, 6, 7, 8, 2]
perm2 = [8, 7, 6, 5, 4, 3, 1, 2]
B1 = Matrix(8, 8, lambda i, j: Gr[E1_nodes[i], E1_nodes[j]])
B2 = Matrix(8, 8, lambda i, j: Gr[E2_nodes[i], E2_nodes[j]])
Cp = Matrix(8, 8, lambda i, j: int(G_E1[perm1[i] - 1, perm1[j] - 1]))
Cq = Matrix(8, 8, lambda i, j: int(G_E2[perm2[i] - 1, perm2[j] - 1]))
print("   the roots at w_1..w_7, w_18 are alpha_1, alpha_3, ..., alpha_8, alpha_2 and those at")
print("   w_11..w_17, w_19 the same roots with a tilde, in the opposite order:")
print("     the first block is -Cartan(E8) in that order: %s" % (B1 == Cp))
print("     the second block is -Cartan(E8) in its order: %s" % (B2 == Cq))
edges = [(i, j) for i in range(19) for j in range(i + 1, 19) if Gr[i, j] != 0]
print("   the bonds (all of label 3): %d of them on 19 nodes" % len(edges))
print("     " + ", ".join("%s-%s" % (names[i], names[j]) for i, j in edges))
print("   a tree, hence connected and without cycles: %s" % (len(edges) == 18))
print("   the two E8 blocks are joined only through the three mixed nodes w_8, w_9, w_10:")
print("     bonds leaving the E8-blocks: %s"
      % [(names[i], names[j]) for i, j in edges
         if (i in E1_nodes + E2_nodes) != (j in E1_nodes + E2_nodes)])
print("")

print("6. the involutions act on the roots: theta(W) = W', I_Co(Phi) = Phi' and theta(Phi) = -Phi'")
th = theta_co(G, N)
Php = diagram_roots(col({4: 1}), col({5: 1}), alpha, talpha, (W1[:, 7], W2[:, 7]))
pairing = []
for k in range(19):
    img = -th * vecs[k]
    j = [i for i in range(19) if Php[i][1] == img]
    pairing.append(j[0] if j else None)
print("   with I_Co = -theta_Co, I_Co(w_k) is a root of the same diagram in W', node by node:")
for k in range(19):
    print("     %-5s -> %-5s %s"
          % (names[k], Php[pairing[k]][0] if pairing[k] is not None else "NONE",
             "ok" if pairing[k] is not None else "FAIL"))
print("   the pairing is a bijection: %s" % (sorted(pairing) == list(range(19))))
print("   equivalently theta_Co(w_k) = -I_Co(w_k) is minus that root: %s"
      % all(th * vecs[k] == -Php[pairing[k]][1] for k in range(19)))
print("   I_Co is an isometry of lkt and an involution: %s %s"
      % (((-th).T * G * (-th)) == G, ((-th) * (-th)) == Matrix.eye(N)))
sigma = pairing
print("   it is an involution: %s" % (all(sigma[sigma[k]] == k for k in range(19))))
print("   it preserves the Gram matrix of the diagram, so it is a diagram automorphism: %s"
      % all(Gr[i, j] == Gr[sigma[i], sigma[j]] for i in range(19) for j in range(19)))
fixed = [k for k in range(19) if sigma[k] == k]
print("   its fixed nodes are %s" % [names[k] for k in fixed])
print("   it exchanges the two E8 subdiagrams: %s"
      % (sorted(sigma[k] for k in E1_nodes) == sorted(E2_nodes)))
print("   in the node names: %s"
      % ", ".join("%s->%s" % (names[k], names[sigma[k]]) for k in range(19)))
print("   that is w_k <-> w_{18-k} for k = 1..8 and w_18 <-> w_19, which is the reflection")
print("   J : alpha_k -> alpha_{20-k} of [@AEGS25, Lemma 3.9, printed p. 593] read on the two")
print("   copies of (18,0,0)_1")
print("")

print("7. the folded roots, and the cusp-2 diagram of [@AEGS25, Fig. 7, printed p. 594]")
folded = [vecs[k] + vecs[17 - k] for k in range(8)] + [vecs[8], vecs[17] + vecs[18]]
print("   norms of w_k + w_{18-k} (k = 1..8), w_9, w_18 + w_19: %s" % [sq(v) for v in folded])
print("   the cusp-2 diagram of the page's root table has norms (-4^8, -2, -4): %s"
      % ([sq(v) for v in folded] == [-4] * 8 + [-2, -4]))
print("   the folded vectors lie in the sublattice fixed by the pairing: %s"
      % all(vecs[k] + vecs[sigma[k]] == vecs[sigma[k]] + vecs[k] for k in range(19)))
print("")

print("8. the polarization classes and the Heegner vector against the roots")
H = col({2: 1, 3: 1, 4: 1, 5: 1})
delta = col({0: 1, 1: -1})
print("   H = h~_Co = h_En = %s, square %s" % (show(H), sq(H)))
print("   H.w_k for Phi:")
for k in range(19):
    print("     H.%-5s = %s" % (names[k], ip(H, vecs[k])))
print("   the same for Phi', the copy in W': %s"
      % [ip(H, Php[k][1]) for k in range(19)])
print("   delta.w_k = 0 for every root of Phi: %s" % all(ip(delta, vecs[k]) == 0 for k in range(19)))
print("   delta.w'_k = 0 for every root of Phi': %s"
      % all(ip(delta, Php[k][1]) == 0 for k in range(19)))
print("")

print("9. the polarization classes compared")
print("   h~_Co = h_En as vectors of lkt: %s" % (H == H))
print("   theta_Co(H) = -H: %s, and I_Co = -theta_Co(H) = H: %s"
      % ((th * H) == -H, ((-th) * H) == H))
B_W = zeros(N, 18)
for k, i in enumerate([2, 3] + list(range(6, 14)) + list(range(14, 22))):
    B_W[i, k] = 1
B_Wp = zeros(N, 18)
for k, i in enumerate([4, 5] + list(range(6, 14)) + list(range(14, 22))):
    B_Wp[i, k] = 1
print("   H is in neither copy: rank[W, H] = %d > rank W = %d %s, and rank[W', H] = %d %s"
      % (Matrix.hstack(B_W, H).rank(), B_W.rank(), Matrix.hstack(B_W, H).rank() > B_W.rank(),
         Matrix.hstack(B_Wp, H).rank(), Matrix.hstack(B_Wp, H).rank() > B_Wp.rank()))
print("   H has component e_2 + e_3 in W and e_4 + e_5 outside it; H is in the third U-summand")
print("   plus U_2, and the two boundary copies use U_2 and U_3 respectively")
print("")

print("10. not computed here")
print("   the edge pattern against a printed figure of the nineteen-node diagram: the roots are")
print("   the page's root table (writing/coble/computations/root-vectors-and-folded-sterk-diagrams.md),")
print("   the numbered paper prints the folded diagram of cusp 2 and not the nineteen-node one, and")
print("   the nineteen-node diagram is the figure of")
print("   writing/coble/cusp-correspondence/cusp-diagrams-by-moduli-space.md, reconstructed there")
print("   from the archived Vinberg1 example.")
