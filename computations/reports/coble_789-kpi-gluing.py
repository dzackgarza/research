"""#789: the structure of K_Pi = Pi^perp/Pi at the five 1-cusp types.

Serves lem:k-pi-orthogonal-lines on the B2 page.

For each of Sterk's five 1-cusp types with nonempty fibre, the quotient
K_Pi = Pi^perp/Pi is a negative definite lattice of rank 8 and determinant 64
(lem:five-one-cusps-nonempty(1)).  This run shows that its sixteen vectors of
square -2 are EIGHT pairwise orthogonal pairs, that they span a sublattice
A = <-2>^8 of index 2, and that the overlattice is

    K_Pi = A + ZZ * (l_1 + ... + l_8)/2 ,

i.e. the gluing class in A*/A = (ZZ/2)^8 is the all-ones vector, so that
g(v) - v = -sum_{i: eps_i = -1} l_{sigma(i)} lies in A for EVERY signed
permutation g(l_i) = eps_i l_{sigma(i)}: the image of O(K_Pi) in the signed
permutations of the eight lines is all of {+-1}^8 x| S_8, and O(K_Pi) acts on
the eight antipodal pairs as the full symmetric group, hence transitively.

Inputs: AEGS, Nagoya Math. J. 259 (2025), Def. 2.3 (T_En); Sterk, Math. Z.
207 (1991), 4.3.17 (the five 1-cusp types); the plane realisations of
computations/reports/coble_gammaEn2-planes-published.py.
"""
from sage.all import matrix, vector, ZZ, QQ, RR
src = open(__file__.replace('coble_789-kpi-gluing.py',
                            'coble_789-one-cusp-divisibility.py')).read()
exec(src.split('for lab, (uu, vv) in PLANES.items():')[0])

print("det Gram(A) = (-2)^8 = %d, det K_Pi = 64, so [K_Pi : A]^2 = %d"
      % (2**8, 2**8 // 64))
for lab, (uu, vv) in PLANES.items():
    u, v = vector(ZZ, uu), vector(ZZ, vv)
    K, G0, lift = build(u, v)
    assert abs(G0.det()) == 64
    roots = short_vectors_cholesky(G0)
    assert len(roots) == 16
    lines, seen = [], set()
    for r in roots:
        if tuple(r) in seen:
            continue
        lines.append(r); seen.add(tuple(r)); seen.add(tuple(-r))
    assert len(lines) == 8
    assert all(lines[i] * G0 * lines[j] == 0
               for i in range(8) for j in range(8) if i != j)
    A = matrix(ZZ, lines)
    Ai = A.inverse()                      # the rows of A are the eight lines
    assert abs(A.det()) == 2, A.det()     # [K_Pi : A] = 2
    w = None
    for i in range(8):
        e = vector(ZZ, [1 if k == i else 0 for k in range(8)])
        c = e * Ai
        if not all(x in ZZ for x in c):
            w = e
            break
    assert w is not None
    c = w * Ai                           # w = sum c_j l_j with c_j half-integral
    weight = sum(1 for x in c if x.denominator() == 2)
    print("type %-9s eight orthogonal (-2)-lines; w = %s has dual coordinates %s,"
          % (str(lab), list(w), [str(x) for x in c]))
    print("            so the gluing class in A*/A has weight %d of 8%s"
          % (weight, "" if weight == 8 else "  <-- NOT all-ones"))
    assert weight == 8
print("")
print("conclusion: K_Pi = A + ZZ*(l_1+...+l_8)/2 in each of the five cases, so")
print("O(K_Pi) permutes the eight antipodal pairs as the full symmetric group S_8")
print("and is transitive on them.  The orbits of the SUBGROUP")
print("im(Stab_{Gamma_En,2}(Pi)) are not computed here.")
