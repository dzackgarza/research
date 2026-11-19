"""research#658, item 1: the smallest deciding probe for the Gamma_Co lifting.

What is proved (writing/coble/cusp-correspondence/enriques-to-coble-cusp-correspondence.md):
thm:coble-strong-lifting for O~+(T_Co), and prop:gamma-co-strong-lifting, which says the conclusion
with Gamma_Co in place of O~+(T_Co) is equivalent to Gamma_Co <= O~+(T_Co).  Of that inclusion the
sign half is a theorem (lem:monodromy-is-spinor-positive), so the whole item is the discriminant half

    Gamma_Co <= ker(rho_{T_Co}),  rho = the discriminant representation of T_Co,

and cor:gamma-co-lifting-criterion identifies it, for the family of DK13's presentation, with
triviality of the monodromy action on A_M, M = <2> + <-2>^10 the lattice of the ten exceptional
classes on the K3 double cover.  rmk:coble-lifting-criterion-not-lattice shows the question is not
settled by exhibiting lattice isometries; it is settled by the monodromy group and nothing else.

So the smallest deciding input is: generators of Gamma_Co as integral isometries of T_Co.  This probe
takes exactly that and answers exactly the question, by exact integer arithmetic, and prints
"undecided" when it is given none -- which is the state of the record today: no page, source or
transcript in this repository produces a single element of Gamma_Co beyond what the conjecture would
give.  Two controls are run first, so that the probe's two answers are both exercised on known
elements: the reflection s_r in r = h + a_1 (square -2), which lies in ker rho, and the swap of the
two isotropic generators of the U(2) block, which does not.

Nothing here decides the item while the verdict line says "undecided".  The probe is committed so
that the day generators exist the question is one command away, and so that no later run can mistake
an absence for a computation.

Usage: python3 computations/reports/coble_658-gamma-co-discriminant-probe.py
"""

from __future__ import annotations

from fractions import Fraction as F


# ---------------------------------------------------------------- the lattices

def e8_cartan_negative():
    """E8(2): the negative definite even lattice with Gram -2 * Cartan(E8)."""
    c = [[0] * 8 for _ in range(8)]
    for i in range(8):
        c[i][i] = 2
    for i in range(6):
        c[i][i + 1] = c[i + 1][i] = -1
    c[2][7] = c[7][2] = -1
    return [[-2 * x for x in row] for row in c]


def block_diagonal(blocks):
    n = sum(len(b) for b in blocks)
    g = [[0] * n for _ in range(n)]
    off = 0
    for b in blocks:
        for i in range(len(b)):
            for j in range(len(b)):
                g[off + i][off + j] = b[i][j]
        off += len(b)
    return g


U = [[0, 1], [1, 0]]
G_TCO = block_diagonal([[[2]], [[2 * x for x in row] for row in U], e8_cartan_negative()])


# ------------------------------------------------------------- exact machinery

def det_int(m):
    """Exact determinant by fraction-free elimination over Q."""
    a = [[F(x) for x in row] for row in m]
    n = len(a)
    det = F(1)
    for col in range(n):
        piv = next((r for r in range(col, n) if a[r][col] != 0), None)
        if piv is None:
            return 0
        if piv != col:
            a[col], a[piv] = a[piv], a[col]
            det = -det
        det *= a[col][col]
        pv = a[col][col]
        for r in range(col + 1, n):
            if a[r][col] != 0:
                f = a[r][col] / pv
                a[r] = [x - f * y for x, y in zip(a[r], a[col])]
    assert det.denominator == 1
    return int(det)


def inverse_rational(m):
    n = len(m)
    a = [[F(m[i][j]) for j in range(n)] + [F(int(i == j)) for j in range(n)] for i in range(n)]
    for col in range(n):
        piv = next((r for r in range(col, n) if a[r][col] != 0), None)
        assert piv is not None, "singular matrix"
        a[col], a[piv] = a[piv], a[col]
        pv = a[col][col]
        a[col] = [x / pv for x in a[col]]
        for r in range(n):
            if r != col and a[r][col] != 0:
                f = a[r][col]
                a[r] = [x - f * y for x, y in zip(a[r], a[col])]
    return [row[n:] for row in a]


def transpose(m):
    return [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]


def matmul(a, b):
    inner = len(b)
    return [[sum(a[i][k] * b[k][j] for k in range(inner)) for j in range(len(b[0]))]
            for i in range(len(a))]


def mv(m, v):
    return [sum(m[i][j] * v[j] for j in range(len(v))) for i in range(len(m))]


def is_integral(m):
    return all(getattr(x, "denominator", 1) == 1 for row in m for x in row)


def is_isometry(g, gram):
    return is_integral(g) and matmul(transpose(g), matmul(gram, g)) == gram


def acts_trivially_on_discriminant(g, gram):
    """Does g act trivially on A = L^v/L?

    A is Z^n / (gram Z^n) in the coordinates v_j = (x, e_j) of x in L^v, so g acts by v |-> g^{-T} v.
    For g in O(L) one has g^{-T} = gram g gram^{-1}, so triviality is equivalent to g(y) - y in Z^n for
    the n generators y = gram^{-1} e_i of A.  (Using g^{-T} itself here would test the wrong condition:
    that is what this file first did, and the check below is the correction.)
    """
    n = len(gram)
    gin = inverse_rational(gram)
    for i in range(n):
        basis = [F(0)] * n
        basis[i] = F(1)
        y = mv(gin, basis)
        z = mv(g, y)
        if any((zi - yi).denominator != 1 for zi, yi in zip(z, y)):
            return False
    return True


def reflection(gram, r):
    """s_r(v) = v + (v, r) r, for r of square -2, as the matrix acting on coordinates."""
    n = len(gram)
    gr = mv(gram, r)
    assert sum(r[i] * gr[i] for i in range(n)) == -2, "reflection needs r^2 = -2"
    out = [[0] * n for _ in range(n)]
    for j in range(n):
        e = [0] * n
        e[j] = 1
        coef = sum(e[i] * gr[i] for i in range(n))     # (e_j, r)
        for i in range(n):
            out[i][j] = e[i] + coef * r[i]
    return out


# ------------------------------------------------------------------- controls

def controls():
    n = len(G_TCO)
    r = [0] * n
    r[0], r[3] = 1, 1                      # r = h + a_1, a_1 the first root of E8(2)
    s_r = reflection(G_TCO, r)
    assert is_isometry(s_r, G_TCO), "s_r is not an isometry of T_Co"
    assert acts_trivially_on_discriminant(s_r, G_TCO), "s_r should act trivially on A_{T_Co}"

    swap = [[int(i == j) for j in range(n)] for i in range(n)]
    swap[1][1] = swap[2][2] = 0            # e' <-> f' in the U(2) block
    swap[1][2] = swap[2][1] = 1
    assert is_isometry(swap, G_TCO), "the swap is not an isometry of T_Co"
    assert not acts_trivially_on_discriminant(swap, G_TCO), "the swap should move a class"
    return s_r, swap


def decide(generators):
    """The verdict for gens of Gamma_Co.  Empty input => undecided."""
    if not generators:
        return "undecided", []
    bad = []
    for idx, g in enumerate(generators):
        if not is_isometry(g, G_TCO):
            bad.append((idx, "not an isometry of T_Co"))
        elif not acts_trivially_on_discriminant(g, G_TCO):
            bad.append((idx, "moves a class of A_{T_Co}"))
    if bad:
        return "excluding", bad
    return "inclusion-holds", []


def main():
    n = len(G_TCO)
    print("T_Co: rank %d, determinant %d (want -2048)" % (n, det_int(G_TCO)))

    s_r, swap = controls()
    print("control 1, s_r for r = h + a_1 of square -2: isometry %s, acts trivially on A_{T_Co} %s"
          % (is_isometry(s_r, G_TCO), acts_trivially_on_discriminant(s_r, G_TCO)))
    print("control 2, the swap e' <-> f' of the U(2) block: isometry %s, acts trivially on A_{T_Co} %s"
          % (is_isometry(swap, G_TCO), acts_trivially_on_discriminant(swap, G_TCO)))
    print("the probe therefore returns both answers on known elements; "
          "the two controls lie on opposite sides.")
    print()

    verdict, detail = decide([])
    print("generators of Gamma_Co on record: 0")
    print("verdict: %s" % verdict)
    if verdict == "undecided":
        print("  The record contains no element of Gamma_Co except through conj:gamma-co-stable, so the")
        print("  half of item 1 that is not the sign cannot be decided here.  Supply generators as")
        print("  integral 11x11 matrices preserving G_TCO and this probe returns 'inclusion-holds' or")
        print("  'excluding' with the offending indices; prop:gamma-co-strong-lifting then gives the")
        print("  Gamma_Co form of thm:coble-strong-lifting or refutes it.")


if __name__ == "__main__":
    main()
