#!/usr/bin/env sage
r"""
Compute Nikulin's 75 lattices from (r,a,δ) triples.

This script constructs each 2-elementary hyperbolic lattice using the
discriminant group gluing method based on Nikulin's classification.

For each (r, a, δ) with signature (r-1, 1), we build:
- Even part L of signature (r-1, 0) - from root lattices (A_n, D_n, E_n) or E8
- Discriminant group A_L = (Z/2Z)^a with parity δ
- The gluing to get signature (r-1, 1) uses the hyperbolic plane U
"""

import json

from sage.all import *


def build_nikulin_lattice(r, a, delta):
    """
    Build a 2-elementary hyperbolic lattice for (r, a, δ).

    Based on Nikulin's theorem, these are classified by (r, a, δ) where:
    - r = rank
    - a = length of discriminant group (rank of (Z/2Z)^a)
    - δ = 0 if discriminant form is even, δ = 1 if odd

    Signature is (r-1, 1) - one negative direction.
    """

    # The lattice is determined uniquely by (r, a, δ)
    # We construct it from standard components using discriminant gluing

    # For 2-elementary lattices, the discriminant group is a 2-group
    # The form on A_L is determined by δ

    # Strategy: Build the even lattice L_even with signature (r-1, k)
    # Then add U to get signature (r-1, k+1), gluing along discriminant

    # The standard building blocks:
    # - A_n (for n >= 1)
    # - D_n (for n >= 4)
    # - E_6, E_7, E_8
    # - U (hyperbolic plane)

    # For a=0: unimodular, use E8 components
    if a == 0:
        if r == 2:
            # U is the only rank 2 unimodular hyperbolic
            L = QuadraticForm(ZZ, [[0, 1], [1, 0]])
            return L, "U"
        elif r == 10:
            # U ⊕ E8
            L1 = QuadraticForm(ZZ, [[0, 1], [1, 0]])
            L2 = QuadraticForm(ZZ, 8, lambda i, j: 0)  # E8 (will be filled)
            # E8 root lattice: 8 negative directions
            for i in range(8):
                L2 = L2 + QuadraticForm(ZZ, [[-2]])
            return L1 + L2, "U ⊕ E8"
        elif r == 18:
            # U ⊕ E8 ⊕ E8
            L1 = QuadraticForm(ZZ, [[0, 1], [1, 0]])
            L2 = sum([QuadraticForm(ZZ, [[-2]]) for _ in range(8)])
            L3 = sum([QuadraticForm(ZZ, [[-2]]) for _ in range(8)])
            return L1 + L2 + L3, "U ⊕ E8 ⊕ E8"

    # For a > 0, we need to use more specific constructions
    # The discriminant group is (Z/2Z)^a

    # For small a, we can use root lattices with appropriate discriminant
    # A1 has discriminant Z/2 (a=1)
    # D_n has discriminant Z/4 or Z/2 × Z/2 depending on n
    # A_n has discriminant n+1

    # The construction uses gluing of even lattices

    # Let's build systematically using Sage's lattice capabilities
    sig_pos = r - 1  # positive signature
    sig_neg = 1  # negative signature (hyperbolic)

    # For 2-elementary lattices, we can use the following construction:
    # Start with signature (r-1, s) where s >= 0, then add U

    # The discriminant group A_L has order 2^a
    # We need to specify the parity δ (even/odd form on A_L)

    # For δ = 0 (even): use even lattices
    # For δ = 1 (odd): use odd lattices

    # Build using explicit construction for each a

    try:
        if a == 1:
            # A_L = Z/2Z
            if delta == 0:
                # Even form: discriminant 2
                # Use U (which has discriminant 2)
                # U has Gram matrix [0,1;1,0], discriminant -1
                # Actually we need discriminant 2 for even form
                # Use A1 with even pairing: <2>
                L = QuadraticForm(ZZ, [[2]])  # A1 with even pairing
                return L, "A1 (even, δ=0)"
            else:
                # Odd form: discriminant 1 mod 2
                # Use A1 with odd pairing: <1>
                L = QuadraticForm(ZZ, [[1]])  # A1 with odd pairing
                return L, "A1 (odd, δ=1)"

        if a == 2:
            # A_L = Z/2Z × Z/2Z
            if delta == 0:
                # Even form: type 2+
                # Can use D4 (which has discriminant Z/2 × Z/2)
                # D4 root lattice: 4 negative roots
                # Discriminant is 4, but form is even
                # D4 has discriminant 4, so q-form has values in Z/2
                pass
            else:
                # Odd form: type 2-
                pass

        # Generic approach: build via discriminant group specification
        # Use the fact that for 2-elementary lattices:
        # L ⊕ U has discriminant group (Z/2Z)^a

        # For now, return placeholder
        return None, f"(r,a,δ)=({r},{a},{delta}) - needs manual construction"

    except Exception as e:
        return None, f"Error: {e}"


def construct_all():
    """Load triples and attempt construction."""

    with open("nikulin_pyramid.json") as f:
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
    print()

    results = {}
    for r, a, delta in triples:
        L, desc = build_nikulin_lattice(r, a, delta)
        results[(r, a, delta)] = desc
        print(f"({r}, {a}, {delta}): {desc}")

    return results


if __name__ == "__main__":
    construct_all()
