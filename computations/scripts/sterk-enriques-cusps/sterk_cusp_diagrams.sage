r"""
Sterk's Coxeter diagrams for the cusps of the Enriques period space.

Source: H. Sterk, *Compactifications of the period space of Enriques surfaces*
(Nijmegen thesis, 1988), Chap. 2 SS3.2-3.3; published as Math. Z. 207 (1991)
SS4.2-4.3 (part I) with the section numbers shifted by one.
Zotero: Ste95a / Ste91 / Ste88a.

What this reconstructs
----------------------
L_- = H (+) H(2) (+) E_8(-2) is the Enriques period lattice, signature (2,10).
(3.2.3) gives five Gamma-orbits of primitive isotropic vectors, hence five
0-dimensional cusps of the Baily-Borel compactification.  For each such v,
v^perp/Zv is hyperbolic of signature (1,9), and Sterk runs Vinberg's algorithm
to obtain the Coxeter diagram of the reflection subgroup W_v ⊂ G_v.  The
maximal parabolic subdiagrams (rank n-1 = 8) enumerate the isotropic lines of
v^perp/Zv modulo G_v, i.e. the isotropic planes of L_- through v -- the
1-dimensional cusps incident to v.

The diagrams are printed *figures* in the source and the parabolic subdiagrams
are marked by circling vertices, which no text extraction recovers.  This
script instead rebuilds each diagram from the root vectors, which the text
gives in closed form, and recomputes the parabolic subdiagrams directly.  The
computed Gram matrices are checked against the figures and against Sterk's own
stated invariants.

Notation (SS2, p.32): alpha_1..alpha_8 are the simple roots of E_8; the
`abar_i` are the *dual* basis, (abar_i, alpha_j) = delta_ij -- they are not
roots.  In E_8(-2) this reads (abar_i, alpha_j) = 2 delta_ij, which is the
remark under (3.3.7).  So abar_1 has norm -8 and abar_8 has norm -4: these are
the vectors called alpha and omega in (3.2.3).

Run: sage sterk_cusp_diagrams.sage
"""

# ---------------------------------------------------------------- the lattice

C = CartanMatrix(['E', 8])                 # positive definite, 2 on the diagonal
H = matrix(ZZ, [[0, 1], [1, 0]])
H2 = matrix(ZZ, [[0, 2], [2, 0]])
GRAM = block_diagonal_matrix(H, H2, -2 * C)
V = ZZ ** 12

e, f, ep, fp = (V.gen(i) for i in range(4))
alpha = [V.gen(4 + i) for i in range(8)]                     # alpha_1..alpha_8
Cinv = C.inverse()
abar = [V(sum(QQ(-Cinv[k, i]) * alpha[k] for k in range(8))) for i in range(8)]


def ip(x, y):
    return vector(ZZ, x) * GRAM * vector(ZZ, y)


# ------------------------------------------------- Coxeter diagram combinatorics

def gram_of(roots):
    n = len(roots)
    return matrix(ZZ, n, n, lambda i, j: ip(roots[i], roots[j]))


def edge_label(M, i, j):
    """Vinberg's edge datum: cos^2 of the angle, 1 meaning parallel (infinity)."""
    return M[i, j] ** 2 / (M[i, i] * M[j, j])


def components(M, S):
    S = list(S)
    adj = {i: set() for i in S}
    for i in S:
        for j in S:
            if i < j and M[i, j] != 0:
                adj[i].add(j)
                adj[j].add(i)
    seen, out = set(), []
    for i in S:
        if i in seen:
            continue
        stack, comp = [i], set()
        while stack:
            k = stack.pop()
            if k in comp:
                continue
            comp.add(k)
            stack += [t for t in adj[k] if t not in comp]
        seen |= comp
        out.append(sorted(comp))
    return out


def corank_if_semidefinite(M, S):
    """Corank of -M[S,S] when that is positive semidefinite, else None."""
    A = -M[list(S), list(S)]
    if not all(A[i, i] > 0 for i in range(A.nrows())):
        return None
    ev = A.change_ring(QQbar).eigenvalues()
    if any(x < 0 for x in ev):
        return None
    return sum(1 for x in ev if x == 0)


def component_invariant(M, comp):
    """Isomorphism invariant of one connected Coxeter subdiagram.

    Vertex count, the multiset of (norm, degree) per vertex, and the multiset of
    edge labels.  Edge labels are what separates the tilde-B / tilde-C diagrams
    from tilde-D / tilde-E ones, which share a degree sequence.
    """
    degs = sorted((M[i, i], sum(1 for j in comp if j != i and M[i, j] != 0))
                  for i in comp)
    labels = sorted(edge_label(M, i, j)
                    for i in comp for j in comp if i < j and M[i, j] != 0)
    return (len(comp), tuple(degs), tuple(labels))


def symmetrizer_of(A):
    """Positive rationals d with d_i A_ij = d_j A_ji, normalized to min 1.

    Propagated along a spanning walk of the diagram; `A.symmetrizer()` is not
    available on a transposed Cartan matrix, and the transpose is exactly the
    case this table needs.
    """
    m = A.nrows()
    d = {0: QQ(1)}
    changed = True
    while changed:
        changed = False
        for i in list(d):
            for j in range(m):
                if j in d or A[i, j] == 0:
                    continue
                d[j] = d[i] * A[i, j] / A[j, i]
                changed = True
    assert len(d) == m, "diagram is disconnected"
    lo = min(d.values())
    return [d[i] / lo for i in range(m)]


def affine_type_table():
    """Invariants of the extended Dynkin diagrams, keyed as `component_invariant`.

    Each affine type is symmetrized to a Gram matrix and entered under both
    normalizations of the root lengths (long = 4 with short = 2, and the plain
    simply-laced scaling), which is what separates B~_n from C~_n here.
    """
    table = {}
    fams = ([('A', n) for n in range(1, 12)] + [('B', n) for n in range(3, 12)]
            + [('C', n) for n in range(2, 12)] + [('D', n) for n in range(4, 12)]
            + [('E', 6), ('E', 7), ('E', 8), ('F', 4), ('G', 2)])
    swap = {'B': 'C', 'C': 'B'}
    for letter, n in fams:
      A0 = CartanMatrix(CartanType([letter, n, 1]))
      # A0 and its transpose are the Cartan matrices of a dual pair; transposing
      # exchanges long and short roots, which is what tells B~_n from C~_n.
      for A, name in ((A0, letter), (A0.transpose(), swap.get(letter, letter))):
        m = A.nrows()
        d = symmetrizer_of(A)
        S = matrix(QQ, m, m, lambda i, j: d[i] * A[i, j])
        for scale in (1, 2, 4):
            G = -scale * S
            if not all(x in ZZ for x in G.list()):
                continue
            G = matrix(ZZ, G)
            if not all(G[i, i] in (-2, -4) for i in range(m)):
                continue
            inv = component_invariant(G, list(range(m)))
            table.setdefault(inv, "%s~%d" % (name, n))
    return table


AFFINE_TYPES = None


def affine_name(M, comp):
    global AFFINE_TYPES
    if AFFINE_TYPES is None:
        AFFINE_TYPES = affine_type_table()
    return AFFINE_TYPES.get(component_invariant(M, comp), "?")


def maximal_parabolic_subdiagrams(M, rank):
    """Parabolic subdiagrams of the given rank, maximal under inclusion.

    Parabolic = each connected component is an extended Dynkin diagram, i.e. the
    restricted form is negative semidefinite with a one-dimensional radical per
    component.  Rank = #vertices - #components (Vinberg).  Vertices at infinity
    of the fundamental polyhedron correspond to rank n-1.
    """
    n = M.nrows()
    found = {}
    for k in range(2, n + 1):
        for sub in Subsets(range(n), k):
            S = tuple(sorted(sub))
            comps = components(M, S)
            ck = corank_if_semidefinite(M, S)
            if ck is None or ck != len(comps) or len(S) - len(comps) != rank:
                continue
            found[S] = comps
    keys = list(found)
    return [(S, found[S]) for S in sorted(keys)
            if not any(set(S) < set(T) for T in keys)]


# ------------------------------------------------------------------ the cusps
# Each entry: Sterk's section, the isotropic vector, and the roots of the
# diagram of W_v in the order the figure labels them.

def cusp_e():
    """(3.3.5)-(3.3.7)  v = e.  M(2) = H(2)+E_8(-2) maps isomorphically to v^perp/Zv."""
    roots = list(alpha)
    roots += [fp - ep,                                  # alpha_9
              abar[7] + 2 * ep,                         # alpha_10
              2 * ep + 2 * fp + abar[0] + abar[7],      # alpha_11
              5 * ep + 3 * fp + 2 * abar[1]]            # alpha_12
    return roots


def cusp_ep():
    """(3.3.8)-(3.3.9)  v = e'.  v^perp/Zv = H + E_8(-2)."""
    return list(alpha) + [abar[7] + 2 * f,              # alpha_9
                          e - f]                        # alpha_10


def cusp_epfpa8():
    """(3.3.10)  v = e' + f' + abar_8.  v^perp/Zv = H + E_8(-2).

    The vertices are alpha_1..alpha_7 and alpha_9..alpha_13; alpha_8 itself is
    not a mirror here (only alpha_8 - f' enters the span).
    """
    a9 = f - e
    a10 = 2 * fp + abar[7]
    return (alpha[0:7]
            + [a9,
               a10,
               (e + f) - a9 - a10,                      # alpha_11 = 2e - 2f' - abar_8
               2 * e + (abar[0] - abar[7]),             # alpha_12
               (e + f) + (alpha[7] - fp)])              # alpha_13


def cusp_2epfpa1():
    """(3.3.11)  v = 2e' + f' + abar_1.  v^perp/Zv = H + E_8(-2).

    Vertices alpha_2..alpha_12; alpha_1 is replaced by alpha_11.
    """
    return (list(alpha[1:8])                            # alpha_2..alpha_8
            + [f - e,                                   # alpha_9
               abar[7] + 2 * ep,                        # alpha_10
               e + f + alpha[0] - ep,                   # alpha_11
               2 * e - 2 * ep + abar[7] - abar[0]])     # alpha_12


def cusp_2e2fa1():
    """(3.3.12)  v = 2e + 2f + abar_1.

    A different splitting of v^perp/Zv: et, ft span the H-summand and
    at_1..at_8 the E_8(-2)-summand, with at_1 = e' - f', at_3 = f' + alpha_3
    and at_i = alpha_i otherwise.  abart is the dual basis of that summand.
    """
    et = e + ep + fp - alpha[0]
    ft = f + ep + fp - alpha[0]
    at = [ep - fp, alpha[1], fp + alpha[2]] + list(alpha[3:8])
    # dual basis of the at-summand: (abart_i, at_j) = 2 delta_ij
    Gt = matrix(ZZ, 8, 8, lambda i, j: ip(at[i], at[j]))
    Gti = Gt.inverse()
    abart = [sum(QQ(2 * Gti[k, i]) * at[k] for k in range(8)) for i in range(8)]
    for x in abart:
        assert all(c in ZZ for c in x), "dual basis of the tilde summand is not integral"
    abart = [V(x) for x in abart]
    return ([at[1], at[3], at[4], at[5], at[6], at[7]]   # alpha_2, alpha_4..alpha_8
            + [at[0],                                    # alpha~_1
               abart[7],                                 # abar~_8
               2 * et - at[0],                           # alpha_9
               2 * et + (abart[1] - abart[2]),           # alpha_10
               ft - et,                                  # alpha_11
               et + ft + (abart[5] - abart[2]),          # alpha_12
               et + ft + (abart[0] + abart[7] - abart[2]),   # alpha_13
               et + ft + at[2]])                         # alpha_14


CUSPS = [
    ("3.3.7   v = e", cusp_e),
    ("3.3.9   v = e'", cusp_ep),
    ("3.3.10  v = e' + f' + abar_8", cusp_epfpa8),
    ("3.3.11  v = 2e' + f' + abar_1", cusp_2epfpa1),
    ("3.3.12  v = 2e + 2f + abar_1", cusp_2e2fa1),
]


def report():
    for name, build in CUSPS:
        roots = build()
        M = gram_of(roots)
        print("=" * 68)
        print(name, " -- %d roots, norms %s" % (len(roots), [M[i, i] for i in range(M.nrows())]))
        for i in range(M.nrows()):
            for j in range(i + 1, M.nrows()):
                if M[i, j]:
                    lab = edge_label(M, i, j)
                    print("   a%-2d a%-2d  (.)=%-3s  cos^2=%-6s %s"
                          % (i + 1, j + 1, M[i, j], lab, "infinity" if lab == 1 else ""))
        maxl = maximal_parabolic_subdiagrams(M, rank=8)
        print("   maximal parabolic subdiagrams of rank 8: %d" % len(maxl))
        for S, comps in maxl:
            print("      %-28s %s"
                  % (" + ".join(affine_name(M, c) for c in comps),
                     [[i + 1 for i in c] for c in comps]))


# Sterk's own checks on the (3.3.7) roots, from the displayed ratios on p.57.
_x = ep + fp
_r = cusp_e()
for _idx, _expected in ((9, 4), (10, 16), (11, 64)):
    assert ip(_r[_idx], _x) ** 2 / abs(ip(_r[_idx], _r[_idx])) == _expected, (_idx, _expected)
assert ip(abar[0], abar[0]) == -8 and ip(abar[7], abar[7]) == -4

report()


# ---------------------------------------------------------- V13 primitivity

def isotropic_vector_of(M, roots, comp):
    """The vector u(Sigma_0) a connected parabolic component represents.

    Vinberg 1983 §1.9: the e_i for i in the component span a parabolic subspace
    whose radical is a line; u(Sigma_0) is the generator of that radical, taken
    with nonnegative coefficients.  Vinberg's Lemma there warns that u(Sigma_0)
    NEED NOT be primitive in L, and gives a sufficient condition for it to be.
    This computes the vector and asks whether it is in fact primitive.
    """
    A = matrix(QQ, len(comp), len(comp), lambda i, j: M[comp[i], comp[j]])
    ker = A.right_kernel().basis()
    if len(ker) != 1:
        return None
    c = ker[0]
    c = c / gcd([x for x in c if x != 0]) if any(x != 0 for x in c) else c
    if any(x < 0 for x in c):
        c = -c
    v = sum(QQ(c[i]) * vector(ZZ, roots[comp[i]]) for i in range(len(comp)))
    if not all(x in ZZ for x in v):
        return ("non-integral", v)
    v = vector(ZZ, v)
    g = gcd(list(v))
    return (v, g)


def primitivity_report():
    print()
    print("=" * 68)
    print("V13: is u(Sigma_0) primitive for each maximal parabolic component?")
    for name, build in CUSPS:
        roots = build()
        M = gram_of(roots)
        print("---", name)
        seen = set()
        for S, comps in maximal_parabolic_subdiagrams(M, rank=8):
            for c in comps:
                key = tuple(c)
                if key in seen:
                    continue
                seen.add(key)
                r = isotropic_vector_of(M, roots, c)
                if r is None:
                    print("    %-22s radical not one-dimensional" % affine_name(M, c))
                    continue
                v, g = r
                if v == "non-integral":
                    print("    %-22s u(Sigma_0) not integral: %s" % (affine_name(M, c), g))
                else:
                    flag = "primitive" if g == 1 else "NOT primitive, content %d" % g
                    assert ip(v, v) == 0, "u(Sigma_0) is not isotropic"
                    print("    %-22s %s" % (affine_name(M, c), flag))


primitivity_report()
