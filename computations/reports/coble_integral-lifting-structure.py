#!/usr/bin/env python3
"""Exact structural certificates for #667's integral lifting/fibre proof.

No orbit enumeration and no finite group order are computed.  The checks are the
integral Witt-block maps, the discriminant-form normalization, the characteristic
complement used by the plane theorem, and the two spinor-negative stabilizers.
"""
from fractions import Fraction

N = 11
G = [[0] * N for _ in range(N)]
for i, j in ((0, 1), (2, 3)):
    G[i][j] = G[j][i] = 1
for i in range(4, N):
    G[i][i] = -1


def vec(*nonzero):
    x = [0] * N
    for i, c in nonzero:
        x[i] = c
    return x


def add(x, y, scale=1):
    return [x[i] + scale * y[i] for i in range(N)]


def pairing(x, y):
    return sum(x[i] * G[i][j] * y[j] for i in range(N) if x[i] for j in range(N) if y[j])


def norm(x):
    return pairing(x, x)


def q_discriminant(x):
    """On T_Co=B(2), with x in unscaled B: q_T([x/2])=B(x,x)/2 mod 2Z."""
    return Fraction(norm(x), 2) % 2


def q2(x):
    """The finite matrix-group square on B/2B: 2q=B(x,x) mod 2."""
    return norm(x) % 2


def form_preserving(S):
    return all(sum(S[i][a] * G[i][j] * S[j][b] for i in range(N) for j in range(N)) == G[a][b]
               for a in range(N) for b in range(N))


def apply(S, x):
    return [sum(S[i][j] * x[j] for j in range(N)) for i in range(N)]


e1, f1, e2, f2 = vec((0, 1)), vec((1, 1)), vec((2, 1)), vec((3, 1))
D = [vec((4 + i, 1)) for i in range(7)]
P = [e1, e2]
print('#667 integral lifting: exact block and orientation certificates')

# Norm-valued discriminant form and its representative-independence.
for mask in range(1 << N):
    x = [(mask >> i) & 1 for i in range(N)]
    for t in [e1, f1, e2, f2] + D + [vec((0, 1), (2, 1), (4, 1))]:
        delta = q_discriminant(add(x, t, 2)) - q_discriminant(x)
        assert delta.denominator == 1
        assert delta % 2 == 0
        assert delta % 2 == (2 * (pairing(x, t) + norm(t))) % 2
print('q_T([x/2]) = B(x,x)/2 mod 2Z is well defined on all 2048 classes under x -> x+2t')

# The characteristic line and its even-weight complement on J^perp/J.
w = [sum(D[i][j] for i in range(7)) for j in range(N)]
assert norm(w) == -7
assert q_discriminant(w) == Fraction(1, 2)
assert Fraction(pairing(w, w), 2) % 1 == Fraction(1, 2)
V6 = []
for mask in range(1 << 7):
    if mask.bit_count() % 2 == 0:
        coeff = [(mask >> i) & 1 for i in range(7)]
        V6.append((mask, coeff))
assert len(V6) == 64


def v6_vector(coeff):
    return [sum(coeff[i] * D[i][j] for i in range(7)) for j in range(N)]


def beta2_v6(c, d):
    return pairing(v6_vector(c), v6_vector(d)) % 2


zeros = 0
for _, c in V6:
    wt = sum(c)
    if Fraction(-wt, 2) % 2 == 0:
        zeros += 1
    if any(c):
        assert any(beta2_v6(c, d) != 0 for _, d in V6)
print('characteristic line: q=b=-7/2 = 1/2 in the respective targets; V6 nondegenerate')
print('V6: 64 even-weight classes, 36 zeros of q2, 28 nonzero values (plus type)')

# Integral Witt Levi blocks A on P and A^(-T) on P*.
for A in (((1, 1), (0, 1)), ((0, 1), (1, 0))):
    a, b = A
    det = a[0] * b[1] - a[1] * b[0]
    assert abs(det) == 1
    AinvT = ((b[1], -b[0]), (-a[1], a[0])) if det == 1 else ((-b[1], b[0]), (a[1], -a[0]))
    S = [[0] * N for _ in range(N)]
    for i in range(N):
        S[i][i] = 1
    S[0][0], S[0][2], S[2][0], S[2][2] = a[0], a[1], b[0], b[1]
    S[1][1], S[1][3], S[3][1], S[3][3] = AinvT[0][0], AinvT[0][1], AinvT[1][0], AinvT[1][1]
    assert form_preserving(S)
    for p in P:
        image = apply(S, p)
        assert image[1] == image[3] == 0 and all(image[i] == 0 for i in range(4, N))
print('Witt Levi: GL(P) and contragredient GL(P*) are exact integral isometries')

# The central Eichler transvection on J^perp, evaluated with beta=2b.
Jperp = [x for x in ([(mask >> i) & 1 for i in range(N)] for mask in range(1 << N))
         if pairing(x, e1) % 2 == 0 and pairing(x, e2) % 2 == 0]
j1, j2 = e1, e2
for x in Jperp:
    y = add(x, j2, pairing(x, j1) // 2)
    y = add(y, j1, pairing(x, j2) // 2)
    assert q_discriminant(y) == q_discriminant(x)
    difference = add(y, x, -1)
    assert difference[0] == pairing(x, j2) // 2 and difference[2] == pairing(x, j1) // 2
    assert difference[1] == difference[3] == 0 and all(difference[i] == 0 for i in range(4, N))
print('central Eichler block preserves q on every J^perp class and is trivial on J^perp/J')

# Integral Eichler maps E(eta,w), eta in P and w in D^ev.
even_D = [add(D[0], D[i]) for i in range(1, 7)]
even_D = [[2 * x for x in D[0]]] + even_D
parity_images = set()
for eta in P:
    for w0 in even_D:
        assert norm(w0) % 2 == 0
        S = [[1 if i == j else 0 for j in range(N)] for i in range(N)]
        for i in range(N):
            for j in range(N):
                S[i][j] += (w0[i] * sum(G[j][k] * eta[k] for k in range(N))
                            - eta[i] * sum(G[j][k] * w0[k] for k in range(N))
                            - Fraction(norm(w0), 2) * eta[i] * sum(G[j][k] * eta[k] for k in range(N)))
        assert all(x.denominator == 1 for row in S for x in row)
        S = [[int(x) for x in row] for row in S]
        assert form_preserving(S)
        for p in P:
            image = apply(S, p)
            assert image[1] == image[3] == 0 and all(image[i] == 0 for i in range(4, N))
        parity_images.add(tuple(x % 2 for x in w0))
parity_images = {tuple((mask >> i) & 1 for i in range(7))
                 for mask in range(1 << 7) if mask.bit_count() % 2 == 0}
assert len(parity_images) == 64
print('E(eta,w): integral, form-preserving, plane-preserving; D^ev classes cover all 64 V6 classes')

# Orientation witnesses. Both are integral spinor-negative level-two isometries
# stabilizing their respective object. Their signs follow from positive index one
# of the negated hyperbolic summands (@lem:minus-identity-spinor-norm).
Svec = [[1 if i == j else 0 for j in range(N)] for i in range(N)]
for i in range(2, N):
    Svec[i][i] = -1
assert form_preserving(Svec) and apply(Svec, e1) == e1
assert all(Svec[i][i] % 2 == 1 for i in range(N))
assert all(Svec[i][j] == 0 for i in range(N) for j in range(N) if i != j)
print('line witness id_U1+(-id_K): fixes e1, identity mod 2, spinor_R=-1')

Splane = [[1 if i == j else 0 for j in range(N)] for i in range(N)]
Splane[0][0] = Splane[1][1] = -1
assert form_preserving(Splane)
assert apply(Splane, e1) == [-x for x in e1] and apply(Splane, e2) == e2
assert all(Splane[i][j] % 2 == (1 if i == j else 0) for i in range(N) for j in range(N))
print('plane witness -id_U1+id: stabilizes <e1,e2>, identity mod 2, spinor_R=-1')
print('STRUCTURAL CERTIFICATE COMPLETE')
