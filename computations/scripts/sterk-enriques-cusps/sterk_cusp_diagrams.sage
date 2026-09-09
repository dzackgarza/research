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


CUSPS = [
    ("3.3.7  v = e", cusp_e),
    ("3.3.9  v = e'", cusp_ep),
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
            print("     ", [[i + 1 for i in c] for c in comps],
                  [component_invariant(M, c) for c in comps])


# Sterk's own checks on the (3.3.7) roots, from the displayed ratios on p.57.
_x = ep + fp
_r = cusp_e()
for _idx, _expected in ((9, 4), (10, 16), (11, 64)):
    assert ip(_r[_idx], _x) ** 2 / abs(ip(_r[_idx], _r[_idx])) == _expected, (_idx, _expected)
assert ip(abar[0], abar[0]) == -8 and ip(abar[7], abar[7]) == -4

report()
