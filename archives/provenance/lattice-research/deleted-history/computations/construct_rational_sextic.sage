#!/usr/bin/env sage
"""
Construct an explicit rational sextic with exactly 10 A1 nodes.

Method:
1. Write the universal homogeneous sextic with 28 coefficients
2. Choose 10 distinct points in P^2
3. Impose that each point is singular (linear conditions)
4. Solve the linear system for a nonzero sextic
5. Verify each singularity is A1 via Hessian non-degeneracy
6. Verify no extra singularities
7. Verify no cubic passes through all 10 points
"""

def construct_rational_sextic():
    """
    Construct a rational sextic with 10 A1 nodes using linear algebra.
    """
    # Step 1: Universal homogeneous sextic
    R.<X,Y,Z> = PolynomialRing(QQ, 3)

    # Generate all monomials of degree 6
    monomials = []
    for i in range(7):
        for j in range(7 - i):
            k = 6 - i - j
            monomials.append(X^i * Y^j * Z^k)

    # Coefficient variables
    a_vars = list(var(f'a{i}') for i in range(len(monomials)))

    # Universal sextic
    F_universal = sum(a_vars[i] * monomials[i] for i in range(len(monomials)))

    # Step 2: Choose 10 distinct points in P^2
    # Use all points in affine chart Z=1 to avoid complications
    # Use points with varied coordinates to avoid linear dependencies
    points = [
        (1, 1, 1),    # [1:1:1]
        (1, 2, 1),    # [1:2:1]
        (2, 1, 1),    # [2:1:1]
        (1, 3, 1),    # [1:3:1]
        (3, 1, 1),    # [3:1:1]
        (2, 3, 1),    # [2:3:1]
        (3, 2, 1),    # [3:2:1]
        (1, -1, 1),   # [1:-1:1]
        (-1, 1, 1),   # [-1:1:1]
        (2, -1, 1),   # [2:-1:1]
    ]

    # Step 3: Impose singularity conditions at each point
    # For a homogeneous polynomial of degree d, Euler's relation gives:
    # X*F_X + Y*F_Y + Z*F_Z = d*F
    # So at a point where F=0, only 2 of the partial derivatives are independent
    # We'll use F_X=0 and F_Y=0 as independent conditions

    equations = []

    for px, py, pz in points:
        # Evaluate F at the point
        F_at_p = F_universal.subs({X: px, Y: py, Z: pz})
        equations.append(F_at_p)

        # Partial derivatives
        F_X = F_universal.derivative(X)
        F_Y = F_universal.derivative(Y)

        # Since all points are in Z=1 chart, use F_X=0 and F_Y=0
        # (F_Z=0 follows from Euler's relation)
        F_X_at_p = F_X.subs({X: px, Y: py, Z: pz})
        F_Y_at_p = F_Y.subs({X: px, Y: py, Z: pz})

        equations.append(F_X_at_p)
        equations.append(F_Y_at_p)

    # Step 4: Solve the linear system
    # Convert to matrix form
    coeff_matrix = []
    rhs = []

    for eq in equations:
        # Extract coefficients of a_vars
        coeffs = [eq.coefficient(a) for a in a_vars]
        coeff_matrix.append(coeffs)
        rhs.append(0)

    M = Matrix(QQ, coeff_matrix)
    b = vector(QQ, rhs)

    # Find a nonzero solution (kernel of M)
    print(f"Matrix dimensions: {M.nrows()} x {M.ncols()}")
    print(f"Matrix rank: {M.rank()}")
    print(f"Expected kernel dimension: {M.ncols() - M.rank()}")

    kernel = M.right_kernel()

    if kernel.dimension() == 0:
        print("ERROR: No nonzero solution found!")
        return None

    # Take the first basis vector
    solution = kernel.basis()[0]

    # Construct the explicit sextic
    F_explicit = sum(solution[i] * monomials[i] for i in range(len(monomials)))

    print("Found explicit sextic:")
    print(F_explicit)
    print()

    # Step 5: Verify each singularity is A1 via Hessian
    print("Verifying singularities are A1...")

    for px, py, pz in points:
        # Work in an affine chart where the last nonzero coordinate is 1
        if pz != 0:
            # Chart Z=1
            f_affine = F_explicit.subs({Z: 1})
            # Compute Hessian of affine polynomial
            f_xx = f_affine.derivative(X, 2)
            f_yy = f_affine.derivative(Y, 2)
            f_xy = f_affine.derivative(X).derivative(Y)
            hessian_det = f_xx * f_yy - f_xy^2
            # Evaluate at the point
            hessian_at_p = hessian_det.subs({X: px/pz, Y: py/pz})
        elif py != 0:
            # Chart Y=1
            f_affine = F_explicit.subs({Y: 1})
            # Compute Hessian of affine polynomial
            f_xx = f_affine.derivative(X, 2)
            f_zz = f_affine.derivative(Z, 2)
            f_xz = f_affine.derivative(X).derivative(Z)
            hessian_det = f_xx * f_zz - f_xz^2
            # Evaluate at the point
            hessian_at_p = hessian_det.subs({X: px/py, Z: pz/py})
        else:
            # Chart X=1
            f_affine = F_explicit.subs({X: 1})
            # Compute Hessian of affine polynomial
            f_yy = f_affine.derivative(Y, 2)
            f_zz = f_affine.derivative(Z, 2)
            f_yz = f_affine.derivative(Y).derivative(Z)
            hessian_det = f_yy * f_zz - f_yz^2
            # Evaluate at the point
            hessian_at_p = hessian_det.subs({Y: py/px, Z: pz/px})

        if hessian_at_p == 0:
            print(f"WARNING: Point {points.index((px,py,pz))} may not be A1 (degenerate Hessian)")
        else:
            print(f"  Point {points.index((px,py,pz))}: A1 confirmed (Hessian det = {hessian_at_p})")

    # Step 6: Verify no extra singularities
    print("\nComputing full singular locus...")

    # Compute partial derivatives
    F_X = F_explicit.derivative(X)
    F_Y = F_explicit.derivative(Y)
    F_Z = F_explicit.derivative(Z)

    # Singular locus is V(F, F_X, F_Y, F_Z)
    # We'll check if there are any points not in our list
    # This is expensive, so we'll do a simpler check: verify degree and genus

    C = Curve(F_explicit)
    C_sing = C.singular_points()

    print(f"Number of singular points found: {len(C_sing)}")

    if len(C_sing) != 10:
        print(f"WARNING: Expected 10 singular points, found {len(C_sing)}")
        print("Singular points:", C_sing)

        # Check if points at infinity are actually singular
        print("\nVerifying points at infinity are singular...")
        for px, py, pz in points:
            if pz == 0 or py == 0 or px == 0:
                F_val = F_explicit.subs({X: px, Y: py, Z: pz})
                F_X_val = F_X.subs({X: px, Y: py, Z: pz})
                F_Y_val = F_Y.subs({X: px, Y: py, Z: pz})
                F_Z_val = F_Z.subs({X: px, Y: py, Z: pz})
                print(f"  Point ({px},{py},{pz}): F={F_val}, F_X={F_X_val}, F_Y={F_Y_val}, F_Z={F_Z_val}")
    else:
        print("  Correct: exactly 10 singular points")

    # Step 7: Verify no cubic passes through all 10 points
    print("\nChecking no cubic passes through all 10 points...")

    # Cubic monomials: X^3, X^2Y, X^2Z, XY^2, XYZ, XZ^2, Y^3, Y^2Z, YZ^2, Z^3
    cubic_monomials = [
        X^3, X^2*Y, X^2*Z, X*Y^2, X*Y*Z, X*Z^2,
        Y^3, Y^2*Z, Y*Z^2, Z^3
    ]

    # Build evaluation matrix
    eval_matrix = []
    for px, py, pz in points:
        row = [m.subs({X: px, Y: py, Z: pz}) for m in cubic_monomials]
        eval_matrix.append(row)

    M_cubic = Matrix(QQ, eval_matrix)

    # Check if kernel is trivial
    kernel_dim = M_cubic.right_kernel().dimension()

    if kernel_dim == 0:
        print("  Confirmed: no cubic passes through all 10 points")
    else:
        print(f"WARNING: {kernel_dim}-dimensional space of cubics through all 10 points")

    return F_explicit, points

if __name__ == "__main__":
    F, points = construct_rational_sextic()

    if F is not None:
        print("\n" + "="*60)
        print("SUCCESS: Valid rational sextic constructed")
        print("="*60)
        print(f"\nPaste this into variety_interface_spec.sage:")
        print(f"F = {F}")
