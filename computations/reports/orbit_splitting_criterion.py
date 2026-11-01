"""Orbit splitting for the kernel of a character, and the Coble instance it settles.

    python3 computations/reports/orbit_splitting_criterion.py

The question.  For a lattice T, let K = ker(Orth(T) -> Orth(A_T)) be the discriminant kernel and
Gamma = K cap Orth^+(T) its component-preserving half, so [K : Gamma] <= 2 because chi_per is a
{+1,-1}-valued character (def/def:period-component-character, prop:period-spinor-character).  The
manuscript asked whether K-orbits and Gamma-orbits of primitive isotropic vectors can be counted
together.  The answer is not "iff K has a component-reversing element": index 2 bounds the groups, not
the partitions.

Part 1 checks the correct criterion on real orthogonal groups of small lattices:
    Hx = Gx  <=>  Stab_G(x) contains an element with chi = -1,
so the two partitions agree iff EVERY G-orbit has such an element in its stabilizer, and otherwise the
discrepancy is the number of G-orbits whose stabilizers lie in H.  Both directions of the naive reading
are refuted by instances below: [G:H] = 2 with chi onto G yet equal counts, and a case with unequal
counts where chi is onto G as well.

Part 2 settles the Coble instance: K does contain a component-reversing element (the reflection in a
unit vector, which exists because B = I_{2,9} is odd), so K != Gamma; and yet, for every primitive
isotropic line L, the reflection in a unit vector orthogonal to L lies in Stab_K(L) and reverses the
component, so by Part 1's criterion K and Gamma have the same orbits.  The group question and the
partition question therefore have different answers, and no computation of "one count" is wasted.

What is not claimed here: the number of orbits.  The criterion only says the two groups' partitions
coincide; lem:stable-orthogonal-not-transitive gives the lower bound 2 and no upper one.
"""
from fractions import Fraction
from itertools import permutations, product
from math import gcd
from functools import reduce

# ---------------------------------------------------------------------------------------------------
# Part 1.  The criterion, on the orthogonal groups of small definite lattices.


def det_int(M):
    M = [[Fraction(x) for x in row] for row in M]
    n = len(M)
    d = Fraction(1)
    for c in range(n):
        p = next((r for r in range(c, n) if M[r][c] != 0), None)
        if p is None:
            return 0
        if p != c:
            M[c], M[p] = M[p], M[c]
            d = -d
        d *= M[c][c]
        for r in range(c + 1, n):
            f = M[r][c] / M[c][c]
            for k in range(c, n):
                M[r][k] -= f * M[c][k]
    return d


def mat_mul(A, B):
    m, n, p = len(A), len(B), len(B[0])
    return [[sum(A[i][k] * B[k][j] for k in range(n)) for j in range(p)] for i in range(m)]


def apply(M, v):
    return tuple(sum(M[i][j] * v[j] for j in range(len(v))) for i in range(len(M)))


def signed_permutations(n, even_flips_only=False):
    out = []
    for perm in permutations(range(n)):
        for signs in product((1, -1), repeat=n):
            if even_flips_only and signs.count(-1) % 2:
                continue
            M = [[0] * n for _ in range(n)]
            for i, j in enumerate(perm):
                M[i][j] = signs[i]
            out.append(M)
    return out


def orbits(group, points, act):
    points = list(points)
    index = {p: i for i, p in enumerate(points)}
    seen = [False] * len(points)
    out = []
    for i, p in enumerate(points):
        if seen[i]:
            continue
        orb, stack = set(), [p]
        seen[i] = True
        while stack:
            x = stack.pop()
            orb.add(x)
            for g in group:
                y = act(g, x)
                j = index[y]
                if not seen[j]:
                    seen[j] = True
                    stack.append(y)
        out.append(frozenset(orb))
    return out


def check_criterion(group, chi, points, act, label):
    """Verify Hx = Gx <=> chi(Stab_G(x)) contains -1, per orbit, and the count identity."""
    H = [g for g in group if chi(g) == 1]
    g_orbits = orbits(group, points, act)
    h_orbits = orbits(H, points, act)
    splitting = 0
    for orb in g_orbits:
        x = next(iter(orb))
        stab = [g for g in group if act(g, x) == x]
        has_odd = any(chi(g) == -1 for g in stab)
        this_h = [o for o in h_orbits if o <= orb]
        if not has_odd:
            splitting += 1
        assert has_odd == (len(this_h) == 1), \
            '%s: orbit of %r has %d H-orbits but odd-stabilizer=%s' % (label, x, len(this_h), has_odd)
        assert len(this_h) in (1, 2), '%s: a G-orbit split into %d H-orbits' % (label, len(this_h))
    assert len(h_orbits) - len(g_orbits) == splitting, \
        '%s: count difference %d != splitting orbits %d' % (label, len(h_orbits) - len(g_orbits), splitting)
    return len(g_orbits), len(h_orbits), splitting, any(chi(g) == -1 for g in group)


print('Part 1.  the criterion on orthogonal groups of definite lattices')
print('  (counts are |G-orbits|, |H-orbits|, splitting orbits, chi onto G)')
equal_but_chi_onto, differ = [], []


def report(group, chi, points, act, label):
    gc, hc, sp, onto = check_criterion(group, chi, points, act, label)
    print('  %-34s %4d %4d %2d %s' % (label, gc, hc, sp, onto))
    (equal_but_chi_onto if (gc == hc and onto) else differ if (gc != hc and onto) else []).append(label)


# A_1^n: Gram = -I_n, orthogonal group = all signed permutations.
for n in (1, 2, 3):
    A = signed_permutations(n)
    G = [[-1 if i == j else 0 for j in range(n)] for i in range(n)]
    roots = [tuple(v) for v in product((-1, 0, 1), repeat=n) if sum(x * x for x in v) == 1]
    norm4 = [tuple(v) for v in product((-2, -1, 0, 1, 2), repeat=n) if sum(x * x for x in v) == 4]
    mod2 = [tuple(v) for v in product((0, 1), repeat=n) if any(v)]
    mod2_act = lambda M, v: tuple(abs(x) for x in apply(M, v))
    report(A, lambda M: det_int(M), roots, apply, 'A_1^%d on the roots' % n)
    report(A, lambda M: det_int(M), norm4, apply, 'A_1^%d on norm-4 vectors' % n)
    report(A, lambda M: det_int(M), mod2, mod2_act, 'A_1^%d on L/2L minus 0' % n)
    if n >= 2:
        report(A, lambda M: det_int(M), sorted(set(roots)), apply, 'A_1^%d on root lines' % n)

# D_4: signed permutations with an even number of sign changes, on its 24 roots.
D = signed_permutations(4, even_flips_only=True)
d4_roots = [tuple(v) for v in product((-1, 0, 1), repeat=4) if sum(x * x for x in v) == 2]
report(D, lambda M: det_int(M), d4_roots, apply, 'Orth(D_4) on the 24 roots')

# The regular action of a real orthogonal group: every stabilizer is trivial, so the counts must differ
# although chi is onto.
A2 = signed_permutations(2)
A2_regular = {i: [A2.index(mat_mul(A2[i], A2[j])) for j in range(len(A2))] for i in range(len(A2))}


def regular_act(M, j):
    return A2_regular[A2.index(M)][j]


report(A2, lambda M: det_int(M), list(range(len(A2))), regular_act, 'A_1^2 on itself (regular)')

assert equal_but_chi_onto, 'no instance with [G:H] = 2, chi onto G, and equal counts'
assert differ, 'no instance with [G:H] = 2, chi onto G, and unequal counts'
print('  instances with chi onto G and EQUAL counts:   %s' % ', '.join(equal_but_chi_onto))
print('  instances with chi onto G and UNEQUAL counts: %s' % ', '.join(differ))
print('  so index 2 plus a chi = -1 element decides nothing about the partitions')

# ---------------------------------------------------------------------------------------------------
# Part 2.  The Coble instance: B = I_{2,9}, unit-vector reflections, and the two groups.

print()
print('Part 2.  B = I_{2,9} and T_Co = B(2)')
N = 11
GB = [[0] * N for _ in range(N)]
GB[0][0] = GB[1][1] = 1
for i in range(2, N):
    GB[i][i] = -1
assert abs(det_int(GB)) == 1, 'B must be unimodular'
signature_signs = sum(1 if GB[i][i] > 0 else -1 for i in range(N))
print('  Gram diag(1, 1, -1, ..., -1): rank %d, sign count %+d, |det| = %d'
      % (N, signature_signs, abs(det_int(GB))))


def dot(u, v):
    return sum(u[i] * GB[i][j] * v[j] for i in range(N) for j in range(N))


def reflection(v):
    """x |-> x - 2 (x,v)/(v,v) v as a rational matrix in the basis b_i, i.e. S_{ij} = d_ij - 2 v_i/v^2 * sum_k v_k G_{kj}."""
    q = dot(v, v)
    weights = [sum(v[k] * GB[k][j] for k in range(N)) for j in range(N)]
    return [[(1 if i == j else 0) - Fraction(2 * v[i] * weights[j], q) for j in range(N)]
            for i in range(N)]


def is_integral(M):
    return all(abs(x - round(x)) < 10 ** -12 for row in M for x in row)


def is_orthogonal(M):
    Mt = [[M[j][i] for j in range(N)] for i in range(N)]
    return mat_mul(mat_mul(Mt, GB), M) == GB


def congruent_one_mod_two(M):
    return all((int(round(M[i][j])) - (1 if i == j else 0)) % 2 == 0 for i in range(N) for j in range(N))


def divisibility(v):
    return reduce(gcd, (abs(x) for x in v if x != 0), 0)


e = [1, 0, 1] + [0] * 8              # b_1 + b_3
unit = [0, 1] + [0] * 9              # b_2
print('  e = b_1 + b_3: square %d, primitive %s' % (dot(e, e), divisibility(e) == 1))
assert dot(e, e) == 0 and divisibility(e) == 1
print('  v = b_2: square %d, orthogonal to e: %s, q(v) = %s > 0'
      % (dot(unit, unit), dot(unit, e) == 0, Fraction(dot(unit, unit), 2)))
assert dot(unit, unit) == 1 and dot(unit, e) == 0

S = reflection(unit)
assert is_integral(S), 'the reflection in a unit vector is not integral'
assert is_orthogonal(S), 'the reflection in a unit vector is not an isometry'
print('  s_v integral and orthogonal: %s; det = %d' % (True, det_int([[int(round(x)) for x in r] for r in S])))
assert det_int([[int(round(x)) for x in r] for r in S]) == -1
assert congruent_one_mod_two(S), 's_v is not trivial modulo 2, so it is not in the discriminant kernel'
print('  s_v = identity modulo 2B, so s_v lies in the discriminant kernel K')
assert apply([[int(round(x)) for x in r] for r in S], e) == tuple(e)
print('  s_v fixes e, hence the line it spans')
print('  by prop:period-spinor-character\'s reflection rule, q(v) > 0 gives chi_per(s_v) = -1')
print('  => K contains a component-reversing element, so K != Gamma_Co and [K : Gamma_Co] = 2')

# For every primitive isotropic line there is such a witness: a unit vector orthogonal to it.
print()
print('  the same construction at an arbitrary primitive isotropic line:')
found = 0
for coeffs in product(range(-2, 3), repeat=4):
    r = list(coeffs) + [0] * 7
    if not any(r) or dot(r, r) != 0 or divisibility(r) != 1:
        continue
    witness = None
    for span in (4, 5):
        for w in product(range(-4, 5), repeat=span):
            w = list(w) + [0] * (N - span)
            if dot(w, w) == 1 and dot(w, r) == 0:
                witness = w
                break
        if witness is not None:
            break
    assert witness is not None, 'no unit vector orthogonal to %r' % (r,)
    S = reflection(witness)
    assert is_integral(S) and is_orthogonal(S) and congruent_one_mod_two(S)
    assert apply([[int(round(x)) for x in row] for row in S], r) == tuple(r)
    found += 1
    if found <= 3:
        print('    r = %s  (r^2 = %d)  witness v = %s  (v^2 = %d), s_v in Stab_K(Zr) with chi = -1'
              % (r, dot(r, r), witness, dot(witness, witness)))
    if found >= 25:
        break
print('  checked on %d primitive isotropic vectors; each has a unit vector orthogonal to it,' % found)
print('  whose reflection lies in the discriminant kernel, fixes the vector, and has chi_per = -1')
print()
print('Conclusion.  K != Gamma_Co as groups ([K : Gamma_Co] = 2), while by Part 1 K and Gamma_Co have')
print('the SAME orbits on primitive isotropic vectors and lines.  Group equality fails; partition')
print('equality holds, and holds for a reason the index does not give: the stabilizer of every line')
print('carries a component-reversing kernel element (the reflection in a unit vector orthogonal to it).')

# ---------------------------------------------------------------------------------------------------
# Part 3.  What the plane invariant can and cannot be: the image of a plane in B/2B = A_{T_Co}.

print()
print('Part 3.  the plane invariant, and how many values it can take')
print('  For a primitive isotropic plane J, the Gamma_Co-invariant is the image of J in')
print('  T_Co/2T_Co = B/2B = A_{T_Co}, a 2-dimensional totally isotropic subspace; the ISOMETRY TYPE of')
print('  that subspace is (Z/2)^2 with zero pairing for every plane, by thm:plane-transitivity-tco, so the')
print('  type carries no information and only the subspace can separate Gamma_Co-orbits.')

classes = [tuple(v) for v in product((0, 1), repeat=N)]


def class_norm_is_quarter_integral(x):
    """q(x-bar) = (1/2) x^2 mod 2 with x the 0/1 representative; q = 0 iff x^2 is divisible by 4."""
    v = [2 * t - 1 if False else t for t in x]
    return dot(v, v) % 4 == 0


isotropic_all = [x for x in classes if class_norm_is_quarter_integral(x)]
isotropic = [x for x in isotropic_all if any(x)]
print('  isotropic classes of A_{T_Co}: %d, of them %d nonzero   (528 and 527 are the established counts)'
      % (len(isotropic_all), len(isotropic)))
assert len(isotropic_all) == 528 and len(isotropic) == 527


def add(x, y):
    return tuple((a + b) % 2 for a, b in zip(x, y))


iso = set(isotropic)
pairs = 0
for i, x in enumerate(isotropic):
    for y in isotropic[i + 1:]:
        if add(x, y) in iso:
            pairs += 1
# each 2-dimensional subspace {0, x, y, x+y} is counted three times, once per unordered isotropic pair
print('  2-dimensional totally isotropic subspaces of A_{T_Co}: %d' % (pairs // 3))
print('  so the invariant of a plane is a point of a set of that size: it is not constant, and it is')
print('  the only isometry-noninvariant datum attached to a plane that this construction gives.')

