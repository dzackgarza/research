"""Why the labelled chamber is not the unpolarized chamber with one node deleted.

The lattice.  K = I_{1,8}(2) = Z H_0 + Z E_1 + ... + Z E_8 with H_0^2 = 2, E_i^2 = -2 and
H_0 orthogonal to every E_i.  A vector is written in the COORDINATES of this basis,
c = (c_0, c_1, ..., c_8)  meaning  c_0 H_0 + c_1 E_1 + ... + c_8 E_8,  so that

    (c, d) = 2 c_0 d_0 - 2 (c_1 d_1 + ... + c_8 d_8).

The page writes the unpolarized chamber's vectors as x = a H_0 - b_1 E_1 - ... - b_8 E_8,
i.e. in coordinates c = (a, -b_1, ..., -b_8); the two notations are converted in one place,
`to_x`, and nowhere else.

The unpolarized chamber (thm:unpolarized-coxeter) is
    b_1 >= b_2 >= ... >= b_8 >= 0,   a >= b_1 + b_2 + b_3.

Part A fixes the two notations and records the pairings, which are positive between simple
roots here; Part B is the parity criterion for the (-4)-roots.  Part C identifies the eight retained simple roots as a B_8 system.  Part D
exhibits a (-2)-root of K, whose reflection lies in Gamma_e at EVERY labelled cusp
(lem:root-reflections-in-the-labelled-cusp), whose wall has one sign on the unpolarized
chamber and the other at a point of the parabolic's chamber; the labelled chamber
therefore sits strictly inside the parabolic's chamber, and the labelled simple system
strictly contains r_1, ..., r_8.

No provider call: the lattice, its discriminant form and every number here are in this file.
"""
from fractions import Fraction as F
from functools import reduce
from itertools import product
from math import gcd

N = 8


# ---------- the lattice ----------

def ip(c, d):
    return 2 * c[0] * d[0] - 2 * sum(c[i + 1] * d[i + 1] for i in range(N))


def sq(c):
    return ip(c, c)


def refl(c, r):
    return [c[i] - F(2 * ip(c, r), sq(r)) * r[i] for i in range(N + 1)]


def cls(c):
    return tuple(F(v) % 1 for v in c)


def basis():
    return [[1 if i == j else 0 for j in range(N + 1)] for i in range(N + 1)]


def integral_reflection(r):
    return all(all(v.denominator == 1 for v in refl(b, r)) for b in basis())


def divisibility(r):
    return reduce(gcd, [abs(int(ip(r, e))) for e in basis()])


def show(c):
    """A vector in the H_0, E_1, ..., E_8 basis, with signs."""
    out = []
    for i, v in enumerate(c):
        if v == 0:
            continue
        name = "H_0" if i == 0 else f"E_{i}"
        mag = abs(F(v))
        term = name if mag == 1 else f"{mag}{name}"
        out.append(("- " if v < 0 else "+ ") + term)
    if not out:
        return "0"
    s = " ".join(out)
    return s[2:] if s.startswith("+ ") else "-" + s[2:]


def to_x(c):
    """Coordinates (a, -b_1, ..., -b_8) -> the page's (a, b_1, ..., b_8)."""
    return [c[0]] + [-c[i + 1] for i in range(N)]


def unpolarized_chamber(c):
    x = to_x(c)
    a, b = x[0], x[1:]
    return (all(b[i] >= b[i + 1] for i in range(N - 1)) and b[-1] >= 0
            and a >= b[0] + b[1] + b[2])


def parabolic_chamber(c):
    """The chamber of <s_{r_1}, ..., s_{r_8}>: the eight retained half-spaces."""
    b = to_x(c)[1:]
    return all(b[i] >= b[i + 1] for i in range(N - 1)) and b[-1] >= 0


# ---------- the discriminant group ----------

def support_of_half_class(r):
    """Where the class of r/2 sits in A_K = A_<h> + A_{E_8(2)}; r is of square -4."""
    half = [F(v, 2) for v in r]
    if all(v.denominator == 1 for v in half):
        return "zero class"
    cl = cls(half)
    head = cl[0] != 0
    tail = any(cl[i] != 0 for i in range(1, N + 1))
    if head and tail:
        return "mixed"
    return "A_<h>" if head else "A_{E_8(2)}"


def moved_across(r):
    """How many of the 512 classes of A_K the action of s_r moves across the decomposition."""
    n = 0
    for eps in product((0, 1), repeat=N + 1):
        v = cls([F(e, 2) for e in eps])
        w = cls(refl([F(e, 2) for e in eps], r))
        if (v[0] == 0) != (w[0] == 0):
            n += 1
    return n


def number(v):
    v = F(v)
    return str(v.numerator) if v.denominator == 1 else str(v)


def main():
    print("K = I_{1,8}(2) = Z H_0 + Z E_1 + ... + Z E_8,  H_0^2 = 2,  E_i^2 = -2,")
    print("vectors in the coordinates of that basis; (c,d) = 2 c_0 d_0 - 2 sum c_i d_i.")
    print()

    # ---------------- A ----------------
    print("=== A. the notation, and the sign of the pairings between simple roots ===")
    r0 = [1, -1, -1, -1, 0, 0, 0, 0, 0]        # H_0 - E_1 - E_2 - E_3, the page's r_0
    r1 = [0, 1, -1, 0, 0, 0, 0, 0, 0]          # E_1 - E_2
    r2 = [0, 0, 1, -1, 0, 0, 0, 0, 0]          # E_2 - E_3
    r3 = [0, 0, 0, 1, -1, 0, 0, 0, 0]          # E_3 - E_4
    on_wall = [5, -2, -2, -1, 0, 0, 0, 0, 0]   # a = 5, b = (2, 2, 1): a = b_1 + b_2 + b_3
    print(f"  r_0 = {show(r0)}, square {number(sq(r0))}")
    print(f"  (x, r_0) = 2(a - b_1 - b_2 - b_3) identically, and at a = b_1 + b_2 + b_3 = 5 it is"
          f" {number(ip(on_wall, r0))},")
    print("  so r_0 is the vector cutting the printed inequality a >= b_1 + b_2 + b_3.  The pairing")
    print(f"  (r_0, r_3) = {number(ip(r0, r3))} is POSITIVE, and so is (r_1, r_2) = {number(ip(r1, r2))}.")
    print("  That is ordinary here and is not a defect: the chamber lies in the positive cone and")
    print("  these are its inward normals, so two walls can meet at an obtuse dihedral angle.  A")
    print("  single bond is decided by 2(r_i,r_j)^2/(r_i^2 r_j^2) = 1/2, which both pairs have.")
    print()

    # ---------------- B ----------------
    print("=== B. the (-4)-roots: an even a-coordinate is exactly the E_8(2) support ===")
    print("  A (-4)-root has a^2 - sum b_i^2 = -2 with gcd(a, b_1..b_8) = 1, since a prime square")
    print("  cannot divide -2; so its divisibility is 2 and its reflection is integral.  The class")
    print("  of r/2 has a/2 as its A_<h> coordinate, so it meets A_<h> exactly when a is odd.")
    print("  For a odd, a^2 = 1 mod 8, so sum b_i^2 = a^2 + 2 = 3 mod 8 and SOME b_i is odd.")
    print("  Hence: every (-4)-root with a odd is mixed, and none with a odd sits in A_<h>.")
    print()

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

    print(f"  {'a parity':>8}  {'support of [r/2]':>17}  {'mixed?':>6}  patterns")
    seen = {}
    for a in range(-4, 5):
        for b in patterns(a * a + 2, N, 4):
            if reduce(gcd, [abs(a)] + [v for v in b if v]) != 1:
                continue
            r = [a] + [-v for v in b]
            key = (a % 2, support_of_half_class(r))
            seen[key] = seen.get(key, 0) + 1
    for (parity, sup), count in sorted(seen.items()):
        print(f"  {('odd' if parity else 'even'):>8}  {sup:>17}  {str(sup == 'mixed'):>6}  "
              f"{count} up to the signs and the order of the b_i, |a| <= 4")
    print("  => a (-4)-root's reflection lies in Gamma_e iff its a-coordinate is even.")
    print("     r_1, ..., r_7 have a = 0 and do; H_0 - E_1 - E_2 - E_3 has a = 1 and does not.")
    print("     That is the earlier census record's verdict; here the criterion is stated once")
    print("     for every (-4)-root instead of root by root.")
    print()

    # ---------------- C ----------------
    print("=== C. the eight retained simple roots are a B_8 system ===")
    roots = {}
    for i in range(1, 8):
        v = [0] * (N + 1)
        v[i] = 1
        v[i + 1] = -1
        roots[f"r_{i}"] = v
    v = [0] * (N + 1)
    v[N] = 1
    roots[f"r_{N}"] = v
    names = [f"r_{i}" for i in range(1, N + 1)]
    cart = [[F(2 * ip(roots[i], roots[j]), sq(roots[i])) for j in names] for i in names]
    print("  Cartan matrix 2(r_i,r_j)/r_i^2:")
    for i, row in zip(names, cart):
        print(f"    {i:>4}  " + " ".join(f"{number(v):>3}" for v in row))

    def minor(m, k):
        m = [row[:k] for row in m[:k]]
        d = F(1)
        for c in range(k):
            p = next((t for t in range(c, k) if m[t][c] != 0), None)
            if p is None:
                return F(0)
            if p != c:
                m[c], m[p] = m[p], m[c]
                d = -d
            d *= m[c][c]
            for t in range(c + 1, k):
                f = m[t][c] / m[c][c]
                for l in range(c, k):
                    m[t][l] -= f * m[c][l]
        return d

    print("  leading principal minors: " + ", ".join(number(minor(cart, k)) for k in range(1, N + 1)))
    print("  all positive, so positive definite; the off-diagonal is -1 along a chain and the")
    print("  last node pairs -2, so the diagram is B_8 and the group is finite.  A finite")
    print("  reflection group's chamber is the intersection of its retained half-spaces, so")
    print("  chamber<s_{r_1},...,s_{r_8}> = {b_1 >= ... >= b_8 >= 0}: no condition on a at all,")
    print("  which strictly contains the unpolarized chamber.")
    print()

    # ---------------- D ----------------
    print("=== D. a (-2)-root of Gamma_e whose wall leaves the parabolic chamber ===")
    rho = [3, -2, -2, -1, -1, 0, 0, 0, 0]      # 3H_0 - 2E_1 - 2E_2 - E_3 - E_4
    print(f"  rho = {show(rho)}:  square {number(sq(rho))}, divisibility {divisibility(rho)},")
    print(f"  integral reflection on a basis: {integral_reflection(rho)}, "
          f"classes of A_K moved across the decomposition: {moved_across(rho)}.")
    print("  A (-2)-root has gcd(a, b_1..b_8) = 1, else a prime square divides")
    print("  sum b_i^2 - a^2 = 1; hence divisibility 2, hence its reflection is trivial on A_K")
    print("  and lies in Gamma_e at every labelled cusp (lem:root-reflections-in-the-labelled-cusp).")
    print()
    print(f"  (x, rho) = 2(3a - 2b_1 - 2b_2 - b_3 - b_4).  On a >= b_1 + b_2 + b_3,")
    print("    3a - 2b_1 - 2b_2 - b_3 - b_4 >= b_1 + b_2 + 2b_3 - b_4 >= b_1 + b_2 + b_3,")
    print("  so (x, rho) > 0 on the interior of the unpolarized chamber.")
    p = [F(16, 5), -2, -2, -1, -1, F(-1, 10), F(-1, 10), F(-1, 10), F(-1, 10)]  # b = (2,2,1,1,.1,.1,.1,.1)
    print(f"  witness {show(p)},\n  i.e. a = 16/5 and b = (2, 2, 1, 1, 1/10, 1/10, 1/10, 1/10):")
    print(f"    every b-coordinate is positive, so p is in the INTERIOR of the parabolic chamber,")
    print(f"    parabolic chamber {parabolic_chamber(p)},  unpolarized chamber {unpolarized_chamber(p)},")
    print(f"    (p,p) = {number(sq(p))} > 0, so p is a point of the parabolic chamber inside the cone,")
    print(f"    (p, rho) = {number(ip(p, rho))} < 0, while (x, rho) > 0 on the unpolarized chamber.")
    print("  s_rho fixes rho^perp pointwise, so no labelled chamber straddles it; the labelled")
    print("  chamber contains the unpolarized one and lies on the positive side.  Hence p is")
    print("  outside the labelled chamber, and the labelled chamber is a proper subregion of")
    print("  chamber<s_{r_1},...,s_{r_8}>.")
    print()
    q = refl(p, r0)
    print(f"  The same point also separates that chamber from the two unpolarized ones: s_{{r_0}}(p) =")
    print(f"  {show(q)},\n  whose b-coordinates {[number(v) for v in to_x(q)[1:]]} are not ordered,")
    print("  so s_{r_0}(p) is outside the unpolarized chamber, and p is too.  Hence")
    print("    {b_1 >= ... >= b_8 >= 0}  is strictly larger than  C  u  s_{r_0}(C),")
    print("  and the chamber of the eight retained roots is not the union of those two chambers.")
    print()
    print("=== verdict ===")
    print("  The eight retained nodes are walls of the labelled chamber, and they do not bound it:")
    print("  its simple system strictly contains r_1, ..., r_8.  So the labelled diagram is not the")
    print("  unpolarized diagram with the node rho_0 deleted, at any labelled cusp, and it is the")
    print("  (-2)-part, which lies in Gamma_e unconditionally, that defeats the deletion.")


if __name__ == "__main__":
    main()
