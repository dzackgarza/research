#!/usr/bin/env python3
"""#788: the discriminant form of T_Co, its characteristic class, and the index [Orth(T_Co) : R].

Objects, all from the page (@def:gamma-co-groups, @prop:gamma-co-images):
  T_Co = <2> + E_10(2) = <h> + U(2) + E_8(2), rank 11, signature (2,9), A_{T_Co} = (Z/2)^11.
  T_En = U + E_10(2) = (T_Co + Z delta)_H with H = <(h/2, delta/2)>, delta^2 = -2.
  R = rho-bar^{-1}(P), P the stabiliser in Orth(q_{T_Co}) of the decomposition
  [h/2]^perp = A_{U(2)} + A_{E_8(2)}  (prop:gamma-co-images(3)).

A is written as F_2^11; q: A -> (1/2)Z/2Z is tabulated as an integer v with q = v/2 mod 2Z,
v in Z/4, and b = B/2 with B in F_2.  Nothing is taken from the library.

Conventions. For an even lattice L, q_L(x + L) = x^2 mod 2Z and b_L(x,y) = x.y mod Z
[Nik80, Sec. 1.3, printed p. 109].  With q = v/2 the defining relation
q(x+y) - q(x) - q(y) = 2 b(x,y) (mod 2Z) reads v(x+y) - v(x) - v(y) = 2 B(x,y) (mod 4).
The characteristic class is the c with b(c,x) = q(x) mod 1 for all x, i.e. B(c,x) = v(x) mod 2.

E_8 is negative definite in the corpus, so E_8(2) has alpha_i^2 = -4 and
q_{E_8(2)}(alpha_i/2) = -1 mod 2Z.  Replacing q by -q preserves Orth(q) and {q = 0}, so
every count below is convention independent; part 8 runs the other sign as a check.
"""
IDX_W = 0
N = 11
SIZE = 1 << N

# E_8 Cartan matrix, Bourbaki numbering: 1-3-4-5-6-7-8 with 2-4.
CARTAN = [[0] * 8 for _ in range(8)]
for i in range(8):
    CARTAN[i][i] = 2
for (i, j) in [(0, 2), (1, 3), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7)]:
    CARTAN[i][j] = CARTAN[j][i] = -1


def bits(x):
    return [(x >> i) & 1 for i in range(N)]


def val(x):
    """v(x) in Z/4 with q(x) = v/2 mod 2Z."""
    b = bits(x)
    v = b[0]                              # <2>: q(h/2) = h^2/4 = 1/2
    v += 2 * (b[1] * b[2])                # U(2): q(e/2) = q(f/2) = 0, q((e+f)/2) = 1
    lam = b[3:]
    q8 = sum(lam)                         # E_8(2): q(alpha_i/2) = alpha_i^2/2 = 1
    for i in range(8):
        for j in range(i + 1, 8):
            q8 += lam[i] * lam[j] * CARTAN[i][j]
    return (v + 2 * q8) % 4


VAL = [val(x) for x in range(SIZE)]


def pairrow(i):
    """bitmask of the y with B(e_i, y) = 1."""
    m = 0
    for y in range(SIZE):
        b = bits(y)
        B = 0
        if i == 0:
            B = b[0]
        elif i == 1:
            B = b[2]
        elif i == 2:
            B = b[1]
        else:
            k = i - 3
            for j in range(8):
                B += b[3 + j] * CARTAN[k][j]
        if B % 2:
            m |= 1 << y
    return m


ROWS = [pairrow(i) for i in range(N)]


def mask_of(x):
    """bitmask of the y with B(x, y) = 1."""
    m = 0
    b = bits(x)
    for i in range(N):
        if b[i]:
            m ^= ROWS[i]
    return m


MASK = [mask_of(x) for x in range(SIZE)]
V_MASK = sum(1 << x for x in range(SIZE) if not (x & 1))
S0 = sum(1 << x for x in range(SIZE) if VAL[x] % 4 == 0)
S1 = sum(1 << x for x in range(SIZE) if VAL[x] % 4 == 2)


def main():
    print("provenance")
    print("  python 3, exact integer arithmetic, no library, no sage, no sage-extensions")
    print("  objects: @def:gamma-co-groups, @prop:gamma-co-images, @lem:primitive_embedding_eta")
    print()
    print("1. A_{T_Co} = (Z/2)^11 and its quadratic form")
    print("   |A| = %d = 2^%d" % (SIZE, N))
    print("   q takes the values %s (as v/2, v in Z/4), i.e. q in {0, 1/2, 1, 3/2}"
          % sorted(set(VAL)))
    bad = 0
    for x in range(SIZE):
        for y in range(SIZE):
            if (VAL[x ^ y] - VAL[x] - VAL[y]) % 4 != (2 * ((MASK[x] >> y) & 1)) % 4:
                bad += 1
    print("   the quadratic-form relation v(x+y) = v(x)+v(y)+2B(x,y) mod 4: violations = %d" % bad)
    print("   B nondegenerate over F_2: %s" % _nondeg())
    print()
    print("2. the characteristic class")
    w = 1 << IDX_W
    print("   B(w,x) = v(x) mod 2 for all x (i.e. b(w,x) = q(x) mod 1): %s"
          % all(((MASK[w] >> x) & 1) == (VAL[x] % 2) for x in range(SIZE)))
    print("   q(h/2) = 1/2, q(e/2) = q(f/2) = 0, q((e+f)/2) = 1, q(alpha_i/2) = 1")
    print("   q is Z-valued on A_{E_10(2)} = A_{U(2)} + A_{E_8(2)}, so q mod 1 = 0 there: %s"
          % all(VAL[x] % 2 == 0 for x in range(SIZE) if not (x & 1)))
    print()
    print("3. the hyperbolic space V = [h/2]^perp = A_{U(2)} + A_{E_8(2)}")
    print("   |V| = %d = 2^10; q is Z-valued on V: %s"
          % (bin(V_MASK).count("1"), all(VAL[x] % 2 == 0 for x in range(SIZE) if not (x & 1))))
    n0 = bin(V_MASK & S0).count("1")
    n1 = bin(V_MASK & S1).count("1")
    print("   #{q = 0 on V} = %d (including 0), #{q = 1 on V} = %d" % (n0, n1))
    print("   plus type: 2^9 + 2^5 - 2^4 = %d; minus type would give 2^9 - 2^5 + 2^4 = %d"
          % (2**9 + 2**5 - 2**4, 2**9 - 2**5 + 2**4))
    a, seq = 3, [3]
    for m in range(2, 6):
        a = 2**(2 * m - 2) + 2 * a
        seq.append(a)
    print("   #{q=0 in a plus space of dim 2m}: a_m = 2^(2m-2) + 2 a_{m-1}, a_1 = 3 -> %s" % seq)
    print()
    print("4. the count of 2-dimensional summands isometric to A_{U(2)}")
    pairs = 0
    for x in range(SIZE):
        if not (x & 1) and x != 0 and VAL[x] % 4 == 0:
            pairs += bin(MASK[x] & V_MASK & S0).count("1")
    print("   ordered pairs (a,b) in V with q(a) = q(b) = 0, b(a,b) = 1/2: %d" % pairs)
    print("   each such subspace {0,a,b,a+b} is met by exactly 2 of them, so the number of")
    print("   2-dimensional subspaces isometric to A_{U(2)} is %d" % (pairs // 2))
    print("   = (N0 * 2^8)/2 with N0 = %d nonzero singular vectors of V: %d"
          % (n0 - 1, ((n0 - 1) * 2**8) // 2))
    seen = set()
    badperp = 0
    plus8 = 2**7 + 2**4 - 2**3
    for x in range(SIZE):
        if (x & 1) or x == 0 or VAL[x] % 4 != 0:
            continue
        m = MASK[x] & V_MASK & S0
        while m:
            low = m & -m
            y = low.bit_length() - 1
            m ^= low
            if (x, y) in seen or (y, x) in seen:
                continue
            seen.add((x, y))
            perp = (~MASK[x] & ~MASK[y]) & V_MASK
            if bin(perp).count("1") != 2**8 or bin(perp & S0).count("1") != plus8:
                badperp += 1
    print("   subspaces checked: %d; those whose perp in V is not a plus space of dim 8: %d"
          % (len(seen), badperp))
    print()
    print("5. |Orth(q_{T_Co})| and |P| by the count of ordered hyperbolic bases")
    print("   an isometry of a hyperbolic space is determined by, and determines, the image of a")
    print("   fixed hyperbolic basis, so |Orth| = #(ordered hyperbolic bases); in dimension 2m a")
    print("   first hyperbolic pair can be chosen in (2^(2m-1)+2^(m-1)-1)*2^(2m-2) ways")
    A = [None, 2]
    for m in range(2, 6):
        A.append((2**(2 * m - 1) + 2**(m - 1) - 1) * 2**(2 * m - 2) * A[m - 1])
        print("     dim %2d: %d * %d * %d = %d"
              % (2 * m, 2**(2 * m - 1) + 2**(m - 1) - 1, 2**(2 * m - 2), A[m - 1], A[m]))
    orth_q, orth_e8 = A[5], A[4]
    P = 2 * orth_e8
    print("   |Orth(q_{T_Co})| = |Orth^+(10,2)| = %d" % orth_q)
    print("   |Orth(q_{U(2)})| = 2 (brute force: the identity and the swap of e/2, f/2)")
    print("   |Orth(q_{E_8(2)})| = %d" % orth_e8)
    print("   |P| = |Orth(q_{U(2)})| * |Orth(q_{E_8(2)})| = %d" % P)
    print("   |Orth(q)|/|P| = %d, and the count of part 4 equals it: %s"
          % (orth_q // P, (orth_q // P) == pairs // 2))
    print()
    print("6. the index, exactly")
    n = pairs // 2
    print("   [Orth(T_Co) : R] = [Orth(q) : P] = %d" % n)
    print("   = 2^7 * 17 * 31 = %d * %d * %d = %d" % (2**7, 17, 31, 2**7 * 17 * 31))
    print("   527 = 2^9 + 2^4 - 1 = 17 * 31: %s" % (527 == 17 * 31 == 2**9 + 2**4 - 1))
    print("   |Orth(q)| = 2^21*3^5*5^2*7*17*31: %s"
          % (orth_q == 2**21 * 3**5 * 5**2 * 7 * 17 * 31))
    print("   |P| = 2^14*3^5*5^2*7 = |W(E_8)| = 696729600: %s"
          % (P == 2**14 * 3**5 * 5**2 * 7 == 696729600))
    print()
    print("7. the two indices [Orth(T_Co) : R] and [Orth^+(T_Co) : R cap Orth^+]")
    print("   -id lies in ker rho-bar and preserves the decomposition, so -id lies in R, and")
    print("   p = 2 is even, so -id lies in Orth^+(T_Co) [@lem:minus-identity-spinor-norm].")
    print("   s_zeta (zeta^2 = 2) has spinor norm -1 [@prop:gamma-co-reflective-set(2)], lies in")
    print("   ker rho_{T_En} and fixes delta [@thm:gamma-co-2-comparison(5)], so s_zeta lies in R")
    print("   and outside Orth^+(T_Co). Hence R*Orth^+ = Orth(T_Co) and")
    print("   [Orth(T_Co) : R] = [Orth^+(T_Co) : R cap Orth^+(T_Co)] = %d." % n)
    print()
    print("8. the other sign for E_8: the counts must not move")
    VAL2 = [(2 * (v // 2)) % 4 if v % 2 == 0 else v for v in VAL]
    V2 = [x for x in range(SIZE) if not (x & 1)]
    n0b = sum(1 for x in V2 if VAL2[x] % 4 == 0)
    n1b = sum(1 for x in V2 if VAL2[x] % 4 == 2)
    pairsb = 0
    for x in V2:
        if x == 0 or VAL2[x] % 4 != 0:
            continue
        for y in V2:
            if y != 0 and VAL2[y] % 4 == 0 and ((MASK[x] >> y) & 1):
                pairsb += 1
    print("   under q -> -q on the E_10(2) part: #{q=0} = %d, #{q=1} = %d, subspaces = %d"
          % (n0b, n1b, pairsb // 2))
    print("   unchanged: %s" % ((n0b, n1b, pairsb // 2) == (n0, n1, n)))


def _nondeg():
    rows = []
    for i in range(N):
        rows.append(sum(((MASK[1 << i] >> (1 << j)) & 1) << j for j in range(N)))
    rank = 0
    for col in range(N):
        piv = None
        for r in range(rank, N):
            if (rows[r] >> col) & 1:
                piv = r
                break
        if piv is None:
            continue
        rows[rank], rows[piv] = rows[piv], rows[rank]
        for r in range(N):
            if r != rank and (rows[r] >> col) & 1:
                rows[r] ^= rows[rank]
        rank += 1
    return rank == N


if __name__ == "__main__":
    main()
