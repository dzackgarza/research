#!/usr/bin/env sage
# Robust automorphism group helper across Sage group types.
# Minimal imports keep startup light.
from sage.all import libgap, PermutationGroup, sage_eval


def _is_graph(obj):
    """Detect Sage graph-like objects by module path."""
    mod = getattr(obj, "__module__", "")
    return "sage.graphs" in mod and hasattr(obj, "automorphism_group")


def _has_gap_backend(obj):
    return hasattr(obj, "_gap_") or hasattr(obj, "gap")


def _gap_to_sage(aut_gap, as_permutation=True):
    """
    Convert a libgap group to a Sage object.
    - Prefer the fast .sage() conversion.
    - Optionally force a permutation image from generators.
    """
    try:
        H = aut_gap.sage()
        if not as_permutation or isinstance(H, PermutationGroup):
            return H
    except Exception:
        H = None
    try:
        gens = [g.sage() for g in aut_gap.GeneratorsOfGroup()]
        return PermutationGroup(gens)
    except Exception:
        return H if H is not None else aut_gap


def compute_aut(G, *, as_permutation=True, return_order=False, verbose=False):
    """
    Compute Aut(G) for graphs, abelian groups, GAP-backed groups, FP groups, or SmallGroup specs.

    Quick doctests (lightweight sanity checks):
    >>> compute_aut(SymmetricGroup(3)).order()
    6
    >>> compute_aut(DihedralGroup(4)).order() >= 8
    True
    >>> compute_aut(CyclicPermutationGroup(5)).order()
    4
    >>> compute_aut(AbelianGroup([2, 4])).order() > 0
    True
    >>> compute_aut(GL(2, GF(3))).order() >= 24
    True
    """
    # Graphs first (native Bliss backend).
    if _is_graph(G):
        H = G.automorphism_group()
        return (H, H.order()) if return_order else H

    # Finite abelian groups: dedicated fast implementation.
    if hasattr(G, "is_abelian") and G.is_abelian() and hasattr(G, "aut"):
        try:
            H = G.aut()
            return (H, H.order()) if return_order else H
        except Exception as e:
            if verbose:
                print(f"[abelian] fallback because {e}")

    # SmallGroup construction via (order, index).
    if isinstance(G, (tuple, list)) and len(G) == 2 and all(isinstance(x, int) for x in G):
        g_gap = libgap.SmallGroup(G[0], G[1])
        H = _gap_to_sage(libgap.AutomorphismGroup(g_gap), as_permutation)
        return (H, H.order()) if return_order else H

    # Anything with a GAP backend.
    if _has_gap_backend(G):
        try:
            g_gap = G._gap_() if hasattr(G, "_gap_") else G.gap()
            H = _gap_to_sage(libgap.AutomorphismGroup(g_gap), as_permutation)
            return (H, H.order()) if return_order else H
        except Exception as e:
            if verbose:
                print(f"[gap] primary path failed: {e}")

    # Finitely presented fallback if available.
    if hasattr(G, "as_finitely_presented_group"):
        try:
            fp = G.as_finitely_presented_group()
            H = _gap_to_sage(libgap.AutomorphismGroup(libgap(fp)), as_permutation)
            return (H, H.order()) if return_order else H
        except Exception as e:
            if verbose:
                print(f"[fp] fallback failed: {e}")

    raise TypeError("Unsupported object type for automorphism computation.")


def _parse_cli():
    import argparse

    p = argparse.ArgumentParser(description="Compute automorphism group for many Sage object types.")
    p.add_argument("object", nargs="?", help="Sage expression for a group/graph (e.g. SymmetricGroup(4))")
    p.add_argument("--small", nargs=2, type=int, metavar=("order", "idx"), help="Use GAP SmallGroup(order, idx)")
    p.add_argument("--no-perm", action="store_true", help="Keep native representation (skip permutation image)")
    p.add_argument("--order", action="store_true", help="Also print |Aut(G)|")
    p.add_argument("--verbose", action="store_true", help="Print diagnostic fallbacks")
    args = p.parse_args()

    if args.small:
        G = tuple(args.small)
    elif args.object:
        G = sage_eval(args.object, locals=globals())
    else:
        raise SystemExit("Provide a Sage object expression or --small order idx.")

    H = compute_aut(G, as_permutation=not args.no_perm, return_order=args.order, verbose=args.verbose)
    if args.order:
        group, ord_val = H
        print(group)
        print(f"|Aut(G)| = {ord_val}")
    else:
        print(H)


if __name__ == "__main__":
    _parse_cli()
