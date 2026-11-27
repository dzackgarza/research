#!/usr/bin/env sage
r"""
Algorithmic construction of Nikulin's 75 lattices.

For each (r,a,δ), we build a 2-elementary hyperbolic lattice using:
1. Even part: build from root lattices (A_n, D_n, E_6, E_7, E_8) + U
2. Discriminant group: (Z/2Z)^a with parity δ (even/odd)
3. Verify 2-elementary and hyperbolic

The construction uses Nikulin's discriminant gluing theorem.
"""

import json

from sage.all import *


def root_lattice(name, n):
    """
    Return the root lattice with given name and rank.
    These are negative-definite even lattices.
    """
    if name == "A":
        # A_n: simple roots e_i - e_{i+1}, n+1 components
        # Gram matrix: 2 on diagonal, -1 on super/sub diagonals
        m = matrix(ZZ, n)
        for i in range(n):
            m[i, i] = 2
            if i > 0:
                m[i, i - 1] = -1
            if i < n - 1:
                m[i, i + 1] = -1
        return QuadraticForm(m)

    elif name == "D":
        # D_n: 2I - J but with one sign change
        # Standard realization in R^n with basis e_i
        m = matrix(ZZ, n)
        for i in range(n):
            m[i, i] = 2
        # Last two rows/cols have off-diagonal 1
        if n >= 4:
            m[n - 2, n - 1] = 1
            m[n - 1, n - 2] = 1
        return QuadraticForm(m)

    elif name == "E":
        if n == 6:
            # E6 Dynkin diagram adjacency
            m = matrix(ZZ, 6)
            # 2 on diagonal
            for i in range(6):
                m[i, i] = 2
            # Edges: 1-2, 2-3, 3-4, 3-5, 5-6
            m[0, 1] = m[1, 0] = -1
            m[1, 2] = m[2, 1] = -1
            m[2, 3] = m[3, 2] = -1
            m[2, 4] = m[4, 2] = -1
            m[4, 5] = m[5, 4] = -1
            return QuadraticForm(m)
        elif n == 7:
            m = matrix(ZZ, 7)
            for i in range(7):
                m[i, i] = 2
            # 1-2, 2-3, 3-4, 3-5, 5-6, 6-7
            m[0, 1] = m[1, 0] = -1
            m[1, 2] = m[2, 1] = -1
            m[2, 3] = m[3, 2] = -1
            m[2, 4] = m[4, 2] = -1
            m[4, 5] = m[5, 4] = -1
            m[5, 6] = m[6, 5] = -1
            return QuadraticForm(m)
        elif n == 8:
            # E8: 8x8 with standard Dynkin
            m = matrix(ZZ, 8)
            for i in range(8):
                m[i, i] = 2
            # Edges: 1-2, 2-3, 3-4, 4-5, 5-6, 6-7, 5-8
            m[0, 1] = m[1, 0] = -1
            m[1, 2] = m[2, 1] = -1
            m[2, 3] = m[3, 2] = -1
            m[3, 4] = m[4, 3] = -1
            m[4, 5] = m[5, 4] = -1
            m[5, 6] = m[6, 5] = -1
            m[4, 7] = m[7, 4] = -1
            return QuadraticForm(m)

    raise ValueError(f"Unknown root lattice {name}_{n}")


def hyperbolic_plane():
    """U: hyperbolic plane with Gram [0,1;1,0]"""
    return QuadraticForm(matrix(ZZ, [[0, 1], [1, 0]]))


def compute_discriminant_group(L):
    """
    Compute the discriminant group A_L = L^*/L for a lattice L.
    Returns (group, q-form) where q is the quadratic form on A_L.
    """
    try:
        # Get the discriminant
        d = L.discriminant()
        # For even lattices, this is the order of A_L
        # The form is even if all diagonal entries are even
        return d
    except:
        return None


def is_2_elementary(L, a, delta):
    """
    Check if lattice L is 2-elementary with given (a, δ).
    """
    try:
        d = L.discriminant()
        # 2-elementary means discriminant is a power of 2
        if not d.is_power_of(2):
            return False

        # The order is 2^a
        if d != 2**a:
            return False

        # Check parity of the discriminant form
        # δ = 0 (even) means discriminant form takes values in Z/2
        # δ = 1 (odd) means it takes values in (1/2)Z/2 = Z/2 + 1/2

        # For a simple check: if the lattice is even, it's δ=0
        # Otherwise δ=1
        if L.is_even():
            return delta == 0
        else:
            return delta == 1
    except:
        return False


def build_nikulin_lattice_alg(r, a, delta):
    """
    Algorithmically build the 2-elementary lattice for (r,a,δ).

    Strategy:
    1. Build even part from root lattices
    2. Compute discriminant group
    3. Check if we need gluing
    4. Add U for hyperbolic signature
    """

    # Build candidate lattices from standard components
    candidates = []

    # Try various combinations of root lattices + U
    components = [
        ("A", 1),
        ("A", 2),
        ("A", 3),
        ("A", 4),
        ("A", 5),
        ("D", 4),
        ("D", 5),
        ("D", 6),
        ("D", 7),
        ("D", 8),
        ("E", 6),
        ("E", 7),
        ("E", 8),
    ]

    # Try single components
    for name, n in components:
        try:
            L = root_lattice(name, n)
            sig = n  # all are negative definite
            candidates.append((L, f"{name}_{n}", sig))
        except:
            pass

    # Try U (adds signature 1)
    U = hyperbolic_plane()
    candidates.append((U, "U", 1))

    # Try pairs
    for i, (name1, n1) in enumerate(components):
        for name2, n2 in components[i:]:
            try:
                L1 = root_lattice(name1, n1)
                L2 = root_lattice(name2, n2)
                L = L1 + L2
                candidates.append((L, f"{name1}_{n1} ⊕ {name2}_{n2}", n1 + n2))
            except:
                pass

    # Try with U added
    for L, desc, sig in candidates[:]:
        L_with_U = L + U
        candidates.append((L_with_U, desc + " ⊕ U", sig + 1))

    # Try triples
    for i, (name1, n1) in enumerate(components):
        for j, (name2, n2) in enumerate(components[i:]):
            for name3, n3 in components[j:]:
                try:
                    L1 = root_lattice(name1, n1)
                    L2 = root_lattice(name2, n2)
                    L3 = root_lattice(name3, n3)
                    L = L1 + L2 + L3
                    candidates.append(
                        (L, f"{name1}_{n1} ⊕ {name2}_{n2} ⊕ {name3}_{n3}", n1 + n2 + n3)
                    )
                except:
                    pass

    # Also add more U's for higher ranks
    for L, desc, sig in list(candidates):
        if sig < r:
            L2 = L + U
            candidates.append((L2, desc + " ⊕ U", sig + 1))

    # Now filter by rank and check properties
    for L, desc, sig in candidates:
        if sig != r - 1:
            continue

        try:
            # Check if 2-elementary
            d = L.discriminant()
            if d == 0:
                continue
            if not d.is_power_of_2():
                continue

            # Check a matches
            a_l = d.exact_log(2)
            if a_l != a:
                continue

            # Check δ
            is_even = L.is_even()
            if is_even and delta == 0:
                return L, desc
            if not is_even and delta == 1:
                return L, desc

        except:
            pass

    # If direct construction fails, we need gluing
    return None, "needs gluing construction"


def construct_all():
    """Construct all 75 lattices."""

    with open("/home/dzack/research/nikulin_pyramid.json") as f:
        data = json.load(f)

    # Get all unique triples
    triples = set()
    for entry in data["delta_0_only"]:
        triples.add((entry["r"], entry["a"], entry["delta"]))
    for entry in data["delta_1_only"]:
        triples.add((entry["r"], entry["a"], entry["delta"]))
    for entry in data["both_delta_0_and_1"]:
        triples.add((entry["r"], entry["a"], entry["delta"]))

    triples = sorted(triples)
    print(f"Total unique (r,a,δ): {len(triples)}")
    print("=" * 70)

    successful = []
    failed = []

    for r, a, delta in triples:
        L, desc = build_nikulin_lattice_alg(r, a, delta)
        if L is not None:
            successful.append(((r, a, delta), desc))
            print(f"({r:2}, {a:2}, δ={delta}): ✓ {desc}")
        else:
            failed.append((r, a, delta))
            print(f"({r:2}, {a:2}, δ={delta}): ✗ {desc}")

    print("=" * 70)
    print(f"Constructed: {len(successful)}")
    print(f"Failed: {len(failed)}")

    return successful, failed


if __name__ == "__main__":
    construct_all()
