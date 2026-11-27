#!/usr/bin/env sage
r"""
Build Nikulin's 75 lattices by combining 2-elementary components.

Strategy:
1. Build a LIBRARY of known 2-elementary lattices (root lattices, U, twists)
2. For each (r,a,δ), find combination giving signature (r-1, 1) and correct discriminant
"""

import json

from sage.all import IntegralLattice


def compute_signature(L):
    mat = L.inner_product_matrix()
    try:
        eigenvalues = mat.eigenvalues()
    except:
        return None, None
    p = sum(1 for e in eigenvalues if e > 0)
    q = sum(1 for e in eigenvalues if e < 0)
    return p, q


def analyze_lattice(L, name):
    """Get invariants of a lattice."""
    inv = L.discriminant_group().invariants()
    is_2el = all(i == 2 for i in inv)
    a = len(inv) if is_2el else None
    delta = 0 if L.is_even() else 1
    p, q = compute_signature(L)
    return {
        "name": name,
        "rank": L.rank(),
        "p": p,
        "q": q,
        "a": a,
        "delta": delta,
        "invariants": list(inv),
        "even": L.is_even(),
    }


def build_library():
    """Build library of 2-elementary lattices."""
    library = []

    # Basic root lattices that ARE 2-elementary
    two_el_name = ["A1", "D4", "D6", "D8", "E7", "E8", "U"]

    for name in two_el_name:
        try:
            L = IntegralLattice(name)
            info = analyze_lattice(L, name)
            if info["a"] is not None:
                library.append(info)
                print(
                    f"Added: {name}: r={info['rank']}, sig=({info['p']},{info['q']}), a={info['a']}, δ={info['delta']}"
                )
        except Exception as e:
            print(f"Failed {name}: {e}")

    # Try twists - scale by n changes discriminant
    # twist by n: gram *= n, changes discriminant and parity
    for name in two_el_name:
        try:
            L_orig = IntegralLattice(name)
            for n in [2, 3, 4]:
                L_twist = IntegralLattice(n * L_orig.inner_product_matrix())
                info = analyze_lattice(L_twist, f"{name}({n})")
                if info["a"] is not None:
                    library.append(info)
                    print(
                        f"Added twist: {name}({n}): r={info['rank']}, sig=({info['p']},{info['q']}), a={info['a']}, δ={info['delta']}"
                    )
        except:
            pass

    # Also try NEGATIVE versions (for different signatures)
    for name in two_el_name:
        try:
            L_orig = IntegralLattice(name)
            L_neg = IntegralLattice(-L_orig.inner_product_matrix())
            info = analyze_lattice(L_neg, f"{name}(-)")
            if info["a"] is not None:
                library.append(info)
                print(
                    f"Added negative: {name}(-): r={info['rank']}, sig=({info['p']},{info['q']}), a={info['a']}, δ={info['delta']}"
                )
        except:
            pass

    return library


def try_combinations(target_r, target_a, target_delta, library):
    """Try to find combination giving signature (r-1, 1) and (a, δ)."""
    target_p = target_r - 1
    target_q = 1

    # Need to combine library elements to get:
    # - signature (target_p, target_q)
    # - discriminant group (Z/2Z)^target_a with parity target_delta
    # - final rank = target_r

    # Try combinations of 1, 2, 3 library elements
    for i, lib1 in enumerate(library):
        # Single: lib1 must have target signature
        if lib1["p"] == target_p and lib1["q"] == target_q:
            if lib1["a"] == target_a and lib1["delta"] == target_delta:
                return [lib1["name"]]

        for j, lib2 in enumerate(library[i + 1 :], i + 1):
            # Pair: need p1+p2 = target_p, q1+q2 = target_q
            if lib1["p"] + lib2["p"] == target_p and lib1["q"] + lib2["q"] == target_q:
                # a adds: a1 + a2 = target_a (for 2-elementary, concatenate invariants)
                combined_a = len(lib1["invariants"]) + len(lib2["invariants"])
                if combined_a == target_a:
                    # delta: both must be even or both odd for combined to have same parity?
                    # Actually if both are even -> even, if both odd -> odd?
                    # Need to check actual parity of direct sum
                    try:
                        L1 = (
                            IntegralLattice(lib1["name"])
                            if "(" not in lib1["name"]
                            else None
                        )
                        # This is messy - let me just compute the combined and check
                        pass
                    except:
                        pass

    # Simpler approach: brute force try all combinations
    results = []

    # Single
    for lib in library:
        if lib["p"] == target_p and lib["q"] == target_q:
            results.append(([lib["name"]], lib["a"], lib["delta"]))

    # Pairs
    for i, lib1 in enumerate(library):
        for lib2 in library[i + 1 :]:
            p, q = lib1["p"] + lib2["p"], lib1["q"] + lib2["q"]
            if p == target_p and q == target_q:
                # Compute actual combined
                try:
                    if "(" in lib1["name"] and lib1["name"].endswith(")"):
                        # Handle twist
                        base = lib1["name"].split("(")[0]
                        n = int(lib1["name"].split("(")[1].rstrip(")"))
                        L1 = IntegralLattice(
                            n * IntegralLattice(base).inner_product_matrix()
                        )
                    else:
                        L1 = IntegralLattice(lib1["name"])

                    if "(" in lib2["name"] and lib2["name"].endswith(")"):
                        base = lib2["name"].split("(")[0]
                        n = int(lib2["name"].split("(")[1].rstrip(")"))
                        L2 = IntegralLattice(
                            n * IntegralLattice(base).inner_product_matrix()
                        )
                    else:
                        L2 = IntegralLattice(lib2["name"])

                    L_comb = L1.direct_sum(L2)
                    info = analyze_lattice(L_comb, f"{lib1['name']} ⊕ {lib2['name']}")
                    if info["a"] == target_a and info["delta"] == target_delta:
                        return [f"{lib1['name']} ⊕ {lib2['name']}"]
                except:
                    pass

    # Triples
    for i, lib1 in enumerate(library):
        for j, lib2 in enumerate(library[i + 1 :], i + 1):
            for lib3 in library[j + 1 :]:
                p, q = (
                    lib1["p"] + lib2["p"] + lib3["p"],
                    lib1["q"] + lib2["q"] + lib3["q"],
                )
                if p == target_p and q == target_q:
                    try:

                        def get_lattice(name):
                            if "(" in name and name.endswith(")"):
                                base = name.split("(")[0]
                                n = int(name.split("(")[1].rstrip(")"))
                                return IntegralLattice(
                                    n * IntegralLattice(base).inner_product_matrix()
                                )
                            return IntegralLattice(name)

                        L1 = get_lattice(lib1["name"])
                        L2 = get_lattice(lib2["name"])
                        L3 = get_lattice(lib3["name"])
                        L_comb = L1.direct_sum(L2).direct_sum(L3)
                        info = analyze_lattice(
                            L_comb, f"{lib1['name']} ⊕ {lib2['name']} ⊕ {lib3['name']}"
                        )
                        if info["a"] == target_a and info["delta"] == target_delta:
                            return [f"{lib1['name']} ⊕ {lib2['name']} ⊕ {lib3['name']}"]
                    except:
                        pass

    return None


def main():
    print("Building library of 2-elementary lattices...")
    library = build_library()
    print(f"\nLibrary size: {len(library)}")

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
    print(f"\nTotal unique (r,a,δ): {len(triples)}")
    print("=" * 70)

    results = {}
    for r, a, delta in triples:
        combo = try_combinations(r, a, delta, library)
        results[(r, a, delta)] = combo
        status = "✓" if combo else "✗"
        print(f"({r:2}, {a:2}, δ={delta}): {status} {combo}")

    success = sum(1 for v in results.values() if v)
    print("=" * 70)
    print(f"Constructed: {success}/75")


if __name__ == "__main__":
    main()
