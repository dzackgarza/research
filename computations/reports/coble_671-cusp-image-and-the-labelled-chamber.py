"""The image of the labelled cusp stabilizer, and the labelled Coxeter chamber.

The framework is the page's, prop:cusp-stabilizer-orthogonal-coble and lem:cusp-image-is-finite:
T_Co = <h> + U(2) + E_8(2) with eta = e the isotropic vector of U(2), K = eta^perp / Z eta
= <h> + E_8(2), and Gamma_{Co,2} = rho^{-1}(P) with P = O(q_{U(2)}) x O(q_{E_8(2)}) acting on
those two summands of A_{T_Co} and trivially on A_<h>.

Part A  the image in one class: Gamma_e = rho_K^{-1}(Stab_{O(q_K)}(e_0)) with e_0 = [h/2], so a
        reflection s_r lies in Gamma_e exactly when rho_K(s_r) fixes e_0; no prescribed action on
        the U(2) block is needed, because P contains all of O(q_{U(2)}).  This is the step the
        page recorded as waiting on the lifting theory of [Wal62].
Part B  which class e_0 is.  It must satisfy q(e_0) = 1/2 and e_0^perp = the E_8(-2) form.  Over
        the 512 classes of A_K exactly ONE does, and in the model <2>_H0 + <-2>^8 it is the
        all-ones class.
Part C  every root of K has an even number of odd coordinates in that model, so every reflection
        fixes e_0; hence every reflection of K lies in Gamma_e.
Part D  therefore W_e = W(K) and the labelled chamber is the unpolarized chamber of
        thm:unpolarized-coexeter: the labelled diagram is the nine-node Coble diagram, and no
        node is deleted.
Part E  why the earlier census reached a different verdict: it used the class [H_0/2] in place of
        [h/2].  Those are different because the complements of H_0 and of h are not isometric --
        <-2>^8 has (a, delta) = (8, 1) and E_8(-2) has (8, 0) -- so no isometry of K carries one
        to the other, and the two classes give different verdicts.

No provider call: A_K, its form and every number here are written in this file.
"""
from itertools import product
from fractions import Fraction as F

N = 9                                  # coordinates (h or H_0, E_1, ..., E_8)


def q(m):
    """2q(m) in Z/4 for the class of (sum m_i b_i)/2, b_0 = H_0, b_i = E_i:  q = (m_0 - sum m_i)/2."""
    return (m[0] - sum(m[1:])) % 4


def b(m, k):
    """The discriminant bilinear form, values in Z/2."""
    return (m[0] * k[0] - sum(m[i] * k[i] for i in range(1, N))) % 2


CLASSES = [tuple(m) for m in product((0, 1), repeat=N)]


def ip(x, y):
    """The form on K = <2> + <-2>^8 in coordinates: (x,y) = 2 x_0 y_0 - 2 sum_{i>=1} x_i y_i."""
    return 2 * x[0] * y[0] - 2 * sum(x[i] * y[i] for i in range(1, N))


def half_class(x):
    """The class of x/2 in A_K, as a bit vector, for x with all coordinates even or all half-integral."""
    return tuple(int(c) % 2 for c in x)


def orth_basis(f):
    """A basis of f^perp in F_2^9, for f with b(f,f) = 1 (so f^perp has dimension 8)."""
    e = [tuple(1 if j == i else 0 for j in range(N)) for i in range(N)]
    piv = [(i, e[i]) for i in range(N) if b(f, e[i]) == 1]
    i0, e0 = piv[0]
    basis = [tuple((v[j] + e0[j]) % 2 for j in range(N)) for i, v in piv[1:]]
    basis += [e[i] for i in range(N) if not any(i == p[0] for p in piv)]
    assert len(basis) == 8
    return basis


def subspace_profile(basis):
    """(value profile of q, delta) on the subspace spanned by `basis`."""
    d = len(basis)
    vecs, prof = [], {}
    for coeff in product((0, 1), repeat=d):
        v = [0] * N
        for c, w in zip(coeff, basis):
            if c:
                v = [t + u for t, u in zip(v, w)]
        v = tuple(t % 2 for t in v)
        vecs.append(v)
        prof[q(v)] = prof.get(q(v), 0) + 1
    delta = next((c for c in vecs if all(b(v, v) == b(v, c) for v in vecs)), None)
    return prof, delta


E8_MINUS_2 = ({0: 136, 2: 120}, tuple([0] * N))     # q-1/2-free: values 0 and 1, delta = 0
MINUS_2_POW_8 = ({0: 72, 1: 64, 2: 56, 3: 64}, None)  # for contrast



def fixes_e0(r, e0):
    """Does s_r fix the class e0 of A_K?  And how many of the 512 classes does it move?"""
    sqr = ip(r, r)
    moved = 0
    fixed_e0 = None
    for m in CLASSES:
        v = [F(c, 2) for c in m]                      # a representative of the class m
        t = F(-2 * ip(v, r), sqr)
        w = [v[i] + t * r[i] for i in range(N)]
        # the class of w: strip the integral part, then read the half-integral part
        frac = [c % 1 for c in w]
        assert all(c in (F(0), F(1, 2)) for c in frac), (r, m, frac)
        k = tuple(int(2 * c) for c in frac)
        if k != m:
            moved += 1
        if m == e0:
            fixed_e0 = (k == e0)
    return fixed_e0, moved


def main():
    print("K = <h> + E_8(2) = I_{1,8}(2) = <2>_H0 + <-2>_{E_1..E_8}, A_K = (Z/2)^9,")
    print("q(m) = (m_0 - m_1 - ... - m_8)/2 mod 2Z,  b(m,k) = m_0k_0 - sum m_ik_i mod 2")
    prof = {}
    for m in CLASSES:
        prof[q(m)] = prof.get(q(m), 0) + 1
    print("  value profile of q over the 512 classes:", dict(sorted(prof.items())),
          " (in Z/4, level 1 = q = 1/2)")
    print()

    # ---------------- A ----------------
    print("=== A. a reflection lies in Gamma_e exactly when it fixes e_0 = [h/2] ===")
    print("  A lift of a bar g in O(K) is sigma(bar g) = id_{U(2)} + bar g, and its discriminant")
    print("  action on A_{T_Co} = A_<h> + A_{U(2)} + A_{E_8(2)} is (id on A_{U(2)}, rho_K(bar g)).")
    print("  P = O(q_{U(2)}) x O(q_{E_8(2)}) acts trivially on A_<h>, so the condition 'action in P'")
    print("  is exactly 'rho_K(bar g) fixes e_0', with no action prescribed on the U(2) block.")
    print("  Two lifts differ by ker(Orth(T_Co) -> Orth(K)), which is trivial on K and hence on")
    print("  A_K, so every lift of a given bar g acts the same way there (lem:cusp-image-is-finite).")
    print()
    h = [3] + [-1] * 8                                  # 3H_0 - E_1 - ... - E_8, square 2
    print(f"  the cusp's h is a primitive vector of square 2 with h^perp = E_8(2);");
    print(f"  taking h = 3H_0 - E_1 - ... - E_8 (square {ip(h, h)}), the class [h/2] is")
    print(f"  {half_class(h)} -- the all-ones class.")
    print()
    print("  The action on A_K is computed, not paraphrased: s_r maps a class [v] with v in (1/2)K")
    print("  to [v - 2(v,r)/(r,r) . r], and the class is fixed exactly when that shift lies in K.")
    print()
    e0 = half_class(h)
    for r in ([1, -1, -1, -1, 0, 0, 0, 0, 0], [0, 1, -1, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 1], [3, -2, -2, -1, -1, 0, 0, 0, 0]):
        sq = ip(r, r)
        fixes, moves = fixes_e0(r, e0)
        print(f"    r = {r}, square {sq:>2}:  fixes e_0: {fixes};  classes of A_K it moves: {moves}")
    print("  For a (-4)-root the shift of [h/2] is ((h,r)/4) r, so it fixes e_0 exactly when 4")
    print("  divides (h,r), that is exactly when b([r/2],e_0) = 0; for a (-2)-root the shift is")
    print("  ((h,r)/2) r with (h,r) even, so it always lies in K and e_0 is always fixed -- which")
    print("  is the triviality of a (-2)-reflection on A_K recorded in")
    print("  lem:root-reflections-in-the-labelled-cusp.")
    print()

    # ---------------- B ----------------
    print("=== B. e_0 is the only class of square 1/2 whose orthogonal complement is E_8(-2) ===")
    print("  First the two complements.  Their roots of smallest square separate them: E_8(-2) has")
    print("  square -2 vectors NONE and 240 vectors of square -4, while <-2>^8 has 16 of square -2.")
    print("  A vector v = aH_0 - sum b_j E_j lies in w^perp when (v,w) = 0.")

    def vectors_with_square_sum(target, parts, bound):
        """all tuples in Z^parts with sum of squares target, by pruning"""
        if parts == 0:
            if target == 0:
                yield ()
            return
        m = min(bound, int(target ** 0.5))
        for v in range(-m, m + 1):
            for rest in vectors_with_square_sum(target - v * v, parts - 1, bound):
                yield (v,) + rest

    print("  For w = 3H_0 - E_1 - ... - E_8 a root of w^perp has sum b_j = 3a and sum b_j^2 = a^2+1,")
    print("  so (sum b_j)^2 <= 8 sum b_j^2 gives 9a^2 <= 8a^2+8, that is |a| <= 2: the box below")
    print("  is exhaustive.  For w = H_0 the first condition reads a = 0.")
    for name, w in (("3H_0 - E_1 - ... - E_8", [3] + [-1] * 8), ("H_0", [1] + [0] * 8)):
        counts = {}
        for target in (-2, -4):
            n = 0
            for a in range(-4, 5):
                for bvec in vectors_with_square_sum(a * a - target // 2, 8, 8):
                    v = (a,) + bvec
                    if ip(v, v) == target and ip(v, w) == 0:
                        n += 1
            counts[target] = n
        print(f"    complement of {name:22}: {counts[-2]:>3} vectors of square -2, "
              f"{counts[-4]:>4} of square -4")
    print("  so the complement of h has the root count of E_8(-2) and that of H_0 that of <-2>^8; the")
    print("  discriminant forms below say which lattice each is, and they are not the same one.")
    print("  For h of square 2 with h^perp = E_8(2), K = Zh + h^perp is a direct sum, so")
    print("  A_K = <e_0> + e_0^perp with q(e_0) = 1/2 and e_0^perp the discriminant form of E_8(-2).")
    cands = [f for f in CLASSES if q(f) == 1 and subspace_profile(orth_basis(f)) == E8_MINUS_2]
    print(f"  classes of square 1/2: {sum(1 for m in CLASSES if q(m) == 1)};"
          f"  with the E_8(-2) complement: {len(cands)}")
    print(f"  and it is {cands}")
    e0 = cands[0]
    assert e0 == half_class(h), (e0, half_class(h))
    print("  which is the class of [h/2] computed in Part A.  So e_0 is pinned by the lattice.")
    print()

    # ---------------- C ----------------
    print("=== C. every root of K has an even number of odd coordinates, so fixes e_0 ===")
    print("  Let r = a H_0 - sum b_i E_i be a primitive root, so 2 dwv(r)/r^2 is an integer;")
    print("  for primitive r the divisibility is 2, hence 4/r^2 in Z and r^2 is -2 or -4.")
    print("  The (-2)-roots need no parity argument: their reflections are trivial on A_K.")
    print("  For a (-4)-root, a^2 - sum b_i^2 = -2.  For a even, sum b_i^2 = 2 mod 4, so the number")
    print("  of odd b_i is 2 or 6; for a odd, a^2 = 1 mod 8 gives sum b_i^2 = 3 mod 4, so that")
    print("  number is 3 or 7.  In either case a + #{i : b_i odd} is even, and")
    print("  (h,r) = 2(3a - sum b_i) is divisible by 4 exactly when that number is even.")
    print("  Exhaustive check over the patterns with |a| <= 4 and |b_i| <= 4 (the parity of the")
    print("  number of odd coordinates does not depend on the signs or the order):")

    def patterns(target, parts, biggest):
        if target < 0:
            return
        if parts == 0:
            if target == 0:
                yield ()
            return
        for v in range(min(biggest, int(target ** 0.5)), -1, -1):
            for rest in patterns(target - v * v, parts - 1, v):
                yield (v,) + rest

    counts = {"-2": 0, "-4": 0}
    bad = []
    for a in range(-4, 5):
        for sq in (-4,):
            target = a * a - sq // 2
            for bpat in patterns(target, 8, 4):
                if __import__("math").gcd(abs(a), __import__("functools").reduce(__import__("math").gcd, [v for v in bpat if v] or [0])) != 1:
                    continue
                counts[str(sq)] += 1
                if (abs(a) % 2 + sum(1 for v in bpat if v % 2)) % 2 != 0:
                    bad.append((a, sq, bpat))
    print(f"    primitive (-4)-root patterns tested: {counts['-4']}")
    print(f"    with an odd number of odd coordinates: {len(bad)}   {bad[:3]}")
    print("  Every (-4)-root pattern has an even number, so b([r/2], e_0) = 0 and (h,r) is divisible by 4.")
    print()

    # ---------------- D ----------------
    print("=== D. the image contains every reflection, so the labelled chamber is the unpolarized one ===")
    print("  The (-2)-reflections act trivially on A_K (lem:root-reflections-in-the-labelled-cusp),")
    print("  so they fix e_0; the (-4)-reflections fix e_0 by Part C.  Hence every reflection of")
    print("  W(K) lies in Gamma_e, W_e = W(K), and the chamber of W_e containing the unpolarized")
    print("  chamber is that chamber: the labelled diagram is the nine-node Coble diagram of")
    print("  thm:unpolarized-coexeter, with the branch point, at every cusp where eta is the")
    print("  isotropic vector e of the fixed decomposition.")
    print()
    print("  the nine simple roots, by the criterion of Part A:")
    roots = {"r_0": [1, -1, -1, -1, 0, 0, 0, 0, 0]}
    for i in range(1, 8):
        v = [0] * 9
        v[i] = 1
        v[i + 1] = -1
        roots[f"r_{i}"] = v
    roots["r_8"] = [0] * 8 + [1]
    for name, r in roots.items():
        sq = ip(r, r)
        cl = half_class(r)
        if sq == -2:
            verdict = "in (acts trivially on A_K)"
        else:
            verdict = "in" if b(cl, e0) == 0 else "OUT"
        print(f"    {name:4} square {sq:>2}  class {cl}  b([r/2],e_0) = {b(cl, e0)}  {verdict}")
    print()

    # ---------------- E ----------------
    print("=== E. why the earlier census differed: [H_0/2] is not [h/2] ===")
    eH = half_class([1, 0, 0, 0, 0, 0, 0, 0, 0])
    print(f"  the class of H_0/2 is {eH}; its orthogonal complement has profile")
    profH, deltaH = subspace_profile(orth_basis(eH))
    print(f"    {dict(sorted(profH.items()))} with delta {deltaH}  -- the form of <-2>^8, not of E_8(-2)")
    print("  and q of it is 1/2, so it passes the first test and fails the second: its complement")
    print("  is the form of <-2>^8, whose delta is nonzero, not the form of E_8(-2).")
    print("  H_0's complement in K is <-2>^8 and h's is E_8(2); the two rank-8 lattices have")
    print("  different discriminant forms, (a,delta) = (8,1) against (8,0), so they are not")
    print("  isometric and no isometry of K carries H_0 to h.  The criterion computed against")
    print("  [H_0/2] is therefore a criterion for a class that is not the cusp's, and its verdicts")
    print("  differ from the ones above:")
    print()
    print(f"  {'root':5} {'square':>6}  {'b([r/2],[H_0/2])':>16}  {'with [H_0/2]':>13}  {'with [h/2] = e_0':>16}")
    for name, r in roots.items():
        sq = ip(r, r)
        cl = half_class(r)
        if sq == -2:
            a, bb = "in (trivial)", "in (trivial)"
        else:
            a = "in" if b(cl, eH) == 0 else "OUT"
            bb = "in" if b(cl, e0) == 0 else "OUT"
        print(f"  {name:5} {sq:>6}  {b(cl, eH):>16}  {a:>13}  {bb:>16}")
    print()
    print("  That is the whole of the discrepancy: the earlier record's 'a even' is 'b(.,[H_0/2]) = 0',")
    print("  and the cusp's class is [h/2], for which every root is in.")
    print()
    print("=== verdict ===")
    print("  At a labelled cusp, that is for a representative eta that is the isotropic vector e of the")
    print("  fixed decomposition T_Co = <h> + U(2) + E_8(2), the image Gamma_e of the cusp stabilizer is")
    print("  rho_K^{-1}(Stab(e_0)) with e_0 = [h/2] the unique class of square 1/2 whose orthogonal")
    print("  complement carries the E_8(-2) form.  Every root of K fixes e_0, so Gamma_e contains every")
    print("  reflection of the cusp lattice, W_e = W(K), and the labelled chamber is the unpolarized")
    print("  chamber of thm:unpolarized-coexeter: the nine-node Coble diagram, no node deleted.")
    print("  No provider call: the lattice, its discriminant form and every number here are in this file.")


if __name__ == "__main__":
    main()
