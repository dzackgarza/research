from z3 import *
#from z3 import IntVector, Solver, sat, Sum, Or

def find_ineq_int_soln():
    x = Int('x')
    y = Int('y')

    solver = Solver()
    solver.add(x > 10, y == x + 2)

    if solver.check() == sat:
        print(solver.model())
    else:
        print("No solution")


def bilinear_form(G, x):
    n = len(x)
    return Sum([
        x[i] * G[i][j] * x[j]
        for i in range(n) for j in range(n)
    ])

def find_roots(G, k, bounds=None):
    n = len(G)
    x = IntVector("x", n)
    s = Solver()
    s.add(bilinear_form(G, x) == k)
    s.add(Sum([x[i]*x[i] for i in range(n)]) > 0)

    if bounds:
        for i in range(n):
            s.add(x[i] >= bounds[0], x[i] <= bounds[1])

    roots = []
    while s.check() == sat:
        m = s.model()
        r = [m[x[i]].as_long() for i in range(n)]
        roots.append(r)
        s.add(Or([x[i] != r[i] for i in range(n)]))
    return roots

G = [
    [0, 1, 0, 0],
    [1, 0, 0, 0],
    [0, 0, 0, 2],
    [0, 0, 2, 0]
]

N = 20
roots = find_roots(G, k=-2, bounds=(-N, N))
for r in roots:
    print(r)

print(f"{len(roots)} roots found")
