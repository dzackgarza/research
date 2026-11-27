#!/usr/bin/env sage
r"""
Construct Nikulin's 75 lattices using Sage's IntegralLattice.

For each (r,a,δ), build a 2-elementary hyperbolic lattice with signature (r-1, 1).
Use direct_sum() for combining lattices, compute signature from eigenvalues.
"""

import json

from sage.all import IntegralLattice


def compute_signature(L):
    """Compute (p,q) signature from Gram matrix eigenvalues."""
    mat = L.inner_product_matrix()
    try:
        eigenvalues = mat.eigenvalues()
    except:
        return None, None
    p = sum(1 for e in eigenvalues if e > 0)
    q = sum(1 for e in eigenvalues if e < 0)
    return p, q


def is_hyperbolic(L, r):
    """Check if L has signature (r-1, 1)."""
    p, q = compute_signature(L)
    return p is not None and p == r - 1 and q == 1


def is_2_elementary(L, a):
    """Check if discriminant group is (Z/2Z)^a."""
    inv = L.discriminant_group().invariants()
    # All invariants must be 2
    if not all(i == 2 for i in inv):
        return False
    return len(inv) == a


def check_2_elementary(L, a, delta):
    """Check if lattice L has discriminant (Z/2Z)^a with parity δ."""
    if not is_2_elementary(L, a):
        return False
    # Check parity: δ=0 means even form, δ=1 means odd form
    if L.is_even():
        return delta == 0
    else:
        return delta == 1


def build_components():
    """Build standard component lattices (positive-definite root lattices)."""
    components = []

    # Root lattices (positive-definite as given by Sage)
    for n in range(1, 9):
        try:
            L = IntegralLattice(f"A{n}")
            p, q = compute_signature(L)
            components.append((L, f"A{n}", p, q))
        except:
            pass

    for n in range(4, 9):
        try:
            L = IntegralLattice(f"D{n}")
            p, q = compute_signature(L)
            components.append((L, f"D{n}", p, q))
        except:
            pass

    for n in [6, 7, 8]:
        try:
            L = IntegralLattice(f"E{n}")
            p, q = compute_signature(L)
            components.append((L, f"E{n}", p, q))
        except:
            pass

    # U (hyperbolic): signature (1,1)
    try:
        U = IntegralLattice("U")
        p, q = compute_signature(U)
        components.append((U, "U", p, q))
    except:
        pass

    return components


def build_for_triple(r, a, delta, components):
    """Try to build lattice for (r,a,δ) by combining components."""
    U = IntegralLattice("U")
    U_p, U_q = compute_signature(U)  # U has (1,1)

    # Try single component + U
    for L1, desc1, p1, q1 in components:
        total_p = p1 + U_p
        total_q = q1 + U_q
        if total_p == r - 1 and total_q == 1:
            try:
                L = L1.direct_sum(U)
                if check_2_elementary(L, a, delta):
                    return L, f"{desc1} ⊕ U"
            except:
                pass

    # Try pairs + U
    for i, (L1, desc1, p1, q1) in enumerate(components):
        for L2, desc2, p2, q2 in components[i + 1 :]:
            total_p = p1 + p2 + U_p
            total_q = q1 + q2 + U_q
            if total_p == r - 1 and total_q == 1:
                try:
                    L = L1.direct_sum(L2).direct_sum(U)
                    if check_2_elementary(L, a, delta):
                        return L, f"{desc1} ⊕ {desc2} ⊕ U"
                except:
                    pass

    # Try triples + U
    for i, (L1, desc1, p1, q1) in enumerate(components):
        for j, (L2, desc2, p2, q2) in enumerate(components[i + 1 :], i + 1):
            for L3, desc3, p3, q3 in components[j + 1 :]:
                total_p = p1 + p2 + p3 + U_p
                total_q = q1 + q2 + q3 + U_q
                if total_p == r - 1 and total_q == 1:
                    try:
                        L = L1.direct_sum(L2).direct_sum(L3).direct_sum(U)
                        if check_2_elementary(L, a, delta):
                            return L, f"{desc1} ⊕ {desc2} ⊕ {desc3} ⊕ U"
                    except:
                        pass

    return None, "not found"

    # Try pairs + U
    for i, (L1, desc1, p1, q1) in enumerate(components):
        for L2, desc2, p2, q2 in components[i + 1 :]:
            total_p = p1 + p2 + U_p
            total_q = q1 + q2 + U_q
            if total_p == r - 1 and total_q == 1:
                try:
                    L = L1.direct_sum(L2).direct_sum(U)
                    if check_2_elementary(L, a, delta):
                        return L, f"{desc1} ⊕ {desc2} ⊕ U"
                except:
                    pass

    return None, "not found"


def main():
    # Load triples
    with open("/home/dzack/research/nikulin_pyramid.json") as f:
        data = json.load(f)

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

    components = build_components()
    print(f"Components: {[c[1] for c in components]}")
    print()

    results = []
    for r, a, delta in triples:
        L, desc = build_for_triple(r, a, delta, components)
        results.append(((r, a, delta), L is not None, desc))
        status = "✓" if L is not None else "✗"
        print(f"({r:2}, {a:2}, δ={delta}): {status} {desc}")

    success = sum(1 for _, ok, _ in results if ok)
    print("=" * 70)
    print(f"Constructed: {success}/75")


if __name__ == "__main__":
    main()
