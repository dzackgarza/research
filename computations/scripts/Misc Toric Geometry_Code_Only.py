"""
Code extracted from: Misc Toric Geometry.ipynb
This file contains only the code cells from the notebook.
"""

# === Code Cell 1 ===

# Intersection matrix of T-invariant divisors in P2
points = [
    (0, 0), (1, 0), (0, 1)
]
P2 = LatticePolytope(points)
show(P.plot3d())
P2_fan = NormalFan(P2)
P2_var = ToricVariety(P2_fan)
show( plot(P2_var) )

A = P2_var.Chow_group(QQ)
Ma = matrix([ [ 
    A(P2_var.divisor(i))
    .intersection_with_divisor(P2_var.divisor(j))
    .count_points() 
    for i in range(0,3) ] for j in range(0,3) ]
)
show(Ma)


# === Code Cell 2 ===

points = [
    (-2, 0, 0), (-1, 0, 0), (0, 0, 0), (1, 0, 0), (2, 0, 0),
    (-1, 1, 0), (0, 1, 0), (1, 1, 0),
    (0, 2, 0),
    (0, 0, 2)
]
P = LatticePolytope(points)
P.plot3d()


# === Code Cell 3 ===

lattice_polytope.positive_integer_relations(P.points().column_matrix())


# === Code Cell 4 ===

P.points()


# === Code Cell 5 ===

points = [
    (-2, 0), (-1, 0), (0, 0), (1, 0), (2, 0),
    (-1, 1), (0, 1), (1, 1),
    (0, 2)
]
P = LatticePolytope(points)
show(P.plot3d())

P.points().matrix().kernel().echelonized_basis_matrix()


# === Code Cell 6 ===

points = [
    (-1, 0), (0, 0), (1, 0),
    (0, 1)
]
P = LatticePolytope(points)
show(P.plot3d())
show(P.points())
P.points().matrix().kernel().echelonized_basis_matrix()


# === Code Cell 7 ===

P2_123 = toric_varieties.P2_123()
HH = P2_123.cohomology_ring()
D = [ HH(c) for c in P2_123.fan(dim=1) ]
show(  )

A = P2_123.Chow_group(QQ)
show( matrix([ [ A(P2_123.divisor(i))
           .intersection_with_divisor(P2_123.divisor(j))
           .count_points() for i in range(0,3) ] for j in range(0,3) ])
    )


# === Code Cell 8 ===

fan1 = NormalFan(P)
Xs = ToricVariety(fan1)
plot(Xs)


# === Code Cell 9 ===

# HH = Xs.cohomology_ring()
# D = [ HH(c) for c in Xs.fan(dim=1) ]
# M = matrix([ [ Xs.integrate(D[i]*D[j]) for i in range(0,3) ] for j in range(0,3) ])

# show(HH)
# show(D)
# show(M)


# === Code Cell 10 ===

A = Xs.Chow_group(QQ)
Ma = matrix([ [ A(Xs.divisor(i))
           .intersection_with_divisor(Xs.divisor(j))
           .count_points() for i in range(0,3) ] for j in range(0,3) ]
           )
show(Ma)

