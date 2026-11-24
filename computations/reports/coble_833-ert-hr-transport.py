"""Exact checks for research#833's ERT/HR integral transport.

The mathematical generation conclusions use HR Theorems 2.1--2.2 and ERT
Theorem 2.1, as cited on the research page.  This script checks only the
integral matrices, coordinate changes and finite root orbit used to apply them.
It is not a generation proof by computation.  Run with Python 3 + SymPy.
"""
import sympy as sp

I9 = sp.eye(9)
G = sp.zeros(9)  # K = U perp <-1>^7, coordinates e,f,d1,...,d7
G[0, 1] = G[1, 0] = 1
for i in range(2, 9):
    G[i, i] = -1
H = sp.diag(*([-1] + [1] * 8))  # HR coordinates eps0,...,eps8


def vec(*xs):
    return sp.Matrix(xs)


e, f = vec(1, 0, *([0] * 7)), vec(0, 1, *([0] * 7))
ds = [sp.zeros(9, 1)] + [vec(0, 0, *[int(k == j) for k in range(1, 8)])
                          for j in range(1, 8)]
a = -2 * e - 2 * f + sum(ds[1:], sp.zeros(9, 1))
betas = [f - ds[1] - ds[2],
         -e - 2 * f + sum(ds[2:], sp.zeros(9, 1))]
betas += [ds[j - 1] - ds[j] for j in range(2, 8)]
z = ds[7] - f
C = sp.Matrix.hstack(a, *betas)


def eps(i):
    return sp.Matrix([int(k == i) for k in range(9)])


v8 = 3 * eps(0)
for i in range(1, 9):
    v8 -= eps(i)
alphas = [eps(0) - eps(1) - eps(2) - eps(3)]
alphas += [eps(i) - eps(i + 1) for i in range(1, 8)]
A = sp.Matrix.hstack(v8, *alphas)
Phi = A * C.inv()

print("1. integral HR basis transport")
print("   det(C), det(A), det(Phi):", C.det(), A.det(), Phi.det())
print("   Phi has integral entries:", all(x.q == 1 for x in Phi))
print("   Phi^T H Phi = -G:", Phi.T * H * Phi == -G)
print("   Phi(z) = eps8:", Phi * z == eps(8), "| z^2 =", (z.T * G * z)[0])
assert all(x.q == 1 for x in Phi)
assert Phi.T * H * Phi == -G
assert Phi * z == eps(8)


def reflection(w, gram):
    return sp.eye(w.rows) - 2 * w * (w.T * gram) / (w.T * gram * w)[0]


m = -reflection(a, G)
M_ert = sp.Matrix([[-3] + [-2] * 7 + [6]] +
                  [[-2] * i + [-3] + [-2] * (7 - i) + [6]
                   for i in range(1, 8)] + [[-6] * 8 + [17]])
J_ert = sp.diag(*([1] * 8 + [-1]))
P = sp.zeros(9)  # HR eps0=ERT time, HR eps_i=-ERT space_i
P[0, 8] = 1
for i in range(1, 9):
    P[i, i - 1] = -1
print("\n2. ERT's nth-longest matrix and its integral lift")
print("   ERT matrix preserves its own Lorentz form:",
      M_ert.T * J_ert * M_ert == J_ert)
print("   permutation changes the coordinate convention:", P.T * H * P == J_ert)
print("   Phi (-r_a) Phi^-1 = permuted ERT matrix:",
      Phi * m * Phi.inv() == P * M_ert * P.inv())
print("   m integral and level two:", all(x.q == 1 for x in m),
      all(x % 2 == 0 for x in m - I9))
assert M_ert.T * J_ert * M_ert == J_ert
assert P.T * H * P == J_ert
assert Phi * m * Phi.inv() == P * M_ert * P.inv()
assert all(x.q == 1 for x in m) and all(x % 2 == 0 for x in m - I9)

print("\n3. the 240 norm-one side roots")
long_reflections = [reflection(alpha, H) for alpha in alphas]
roots = {tuple(eps(8))}
front = [eps(8)]
while front:
    new = []
    for x in front:
        for S in long_reflections:
            y = S * x
            if tuple(y) not in roots:
                roots.add(tuple(y))
                new.append(y)
    front = new
print("   orbit cardinality:", len(roots))
print("   all have norm one:",
      {(sp.Matrix(x).T * H * sp.Matrix(x))[0] for x in roots} == {1})
print("   each is eta+v8 with eta in v8-perp of norm two:",
      all((v8.T * H * (sp.Matrix(x) - v8))[0] == 0 and
          ((sp.Matrix(x) - v8).T * H * (sp.Matrix(x) - v8))[0] == 2
          for x in roots))
assert len(roots) == 240
assert all((sp.Matrix(x).T * H * sp.Matrix(x))[0] == 1 for x in roots)
assert all((v8.T * H * (sp.Matrix(x) - v8))[0] == 0 and
           ((sp.Matrix(x) - v8).T * H * (sp.Matrix(x) - v8))[0] == 2
           for x in roots)


def eichler(u, k):
    kk = (k.T * G * k)[0]
    assert kk % 2 == 0 and (u.T * G * k)[0] == 0
    return (I9 - u * (k.T * G) + k * (u.T * G)
            - (kk / 2) * u * (u.T * G))


print("\n4. why the old 35-family lies in the norm-one reflection subgroup")
for j in range(1, 8):
    rd = reflection(ds[j], G)
    te = eichler(e, 2 * ds[j])
    tf = eichler(f, 2 * ds[j])
    assert te == reflection(e + ds[j], G) * rd
    assert tf == reflection(f + ds[j], G) * rd
    for w in (ds[j], e + ds[j], f + ds[j]):
        assert (w.T * G * w)[0] == -1
        assert all(x % 2 == 0 for x in reflection(w, G) - I9)
    assert all(x.q == 1 for x in te) and all(x.q == 1 for x in tf)
    assert all(x % 2 == 0 for x in te - I9)
    assert all(x % 2 == 0 for x in tf - I9)
print("   t_K(e,2d_j) = r_(e+d_j) r_d_j and "
      "t_K(f,2d_j) = r_(f+d_j) r_d_j for all j: True")
print("   all old 35 generators are integral level-two elements in that subgroup: True")
print("   m is the separate n=8 coset witness supplied by ERT/HR (matrix checked above)")

print("\n5. the explicit one-coordinate counterexample to the old family")
old35 = []
for j in range(1, 8):
    rd = reflection(ds[j], G)
    old35 += [rd, eichler(e, 2 * ds[j]), eichler(f, 2 * ds[j]),
              reflection(e + ds[j], G), reflection(f + ds[j], G)]

def leading_level_four_entry(g):
    return ((g * e - e)[0] / 2) % 2

witness = e + f + ds[1]
rw = reflection(witness, G)
print("   (e,e)-entry on all 35 old level-four classes:",
      sorted({leading_level_four_entry(g) for g in old35}))
print("   witness w=e+f+d1 has norm one:", (witness.T * G * witness)[0] == 1,
      "| r_w integral level two:", all(x.q == 1 for x in rw) and
      all(x % 2 == 0 for x in rw - I9),
      "| its (e,e)-entry:", leading_level_four_entry(rw))
assert all(leading_level_four_entry(g) == 0 for g in old35)
assert leading_level_four_entry(rw) == 1
assert rw.T * G * rw == G and all(x % 2 == 0 for x in rw - I9)
