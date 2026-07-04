r"""SLOW / CI-only: rank >= 7 automorphism-group orders for the lattice spike.

These pin ``isometry_group().order()`` at ranks where the GAP/Sage-backed
computation is slow (profiled: E7 ~1s, A8 ~0.5s, D8 ~0.7s, E8 ~8s), so they are
segregated from the fast ``test_lit_isometry.py``. This is exactly the "later
CI/slow tranche" that ``test_literature_citations.py`` defers when it excludes
E_8 from its small-rank order test.

Every expected value is quoted from Conway & Sloane, *Sphere Packings, Lattices
and Groups*, 3rd ed. (1999) [Zotero T2WVLTDB | CS99 | attachment TCJKXU3D], and is
reconstructed here in CS99's own g = g_0 g_1 factorization (g_0 = |Weyl group|,
g_1 = |Coxeter-diagram graph automorphisms|). Each test also asserts the cheap
characterizing invariants (rank, signature pair, determinant, is_even,
is_unimodular) alongside the published group order.
"""

from __future__ import annotations

from math import factorial

import sage_lattice_category_spike.lattice_categories as lc


def test_root_lattice_weyl_group_orders_rank_ge_7_match_conway_sloane_chapter_4():
    r"""CS99 Ch. 4 automorphism-group orders g = g_0 g_1 [CS99]:

      - A_8 (sec 6.1): G_0 = W(A_8) = S_9 (order 9!), g_1 = 2 (negation);
            g = 9! * 2 = 725760.
      - D_8 (sec 7.1): g_0 = 2^{n-1} n! = 2^7 * 8!, g_1 = 2;
            g = 2^7 * 8! * 2 = 10321920.
      - E_7 (sec 8.2): g_0 = |W(E_7)| = 2^10 * 3^4 * 5 * 7 = 2903040, g_1 = 1;
            g = 2903040.
      - E_8 (sec 8.1): g_0 = |W(E_8)| = 2^14 * 3^5 * 5^2 * 7 = 696729600, g_1 = 1;
            g = 696729600.

    The expected orders are the CS99 g_0 g_1 products; the spike computes O(L)
    through Sage's orthogonal_group (PARI/GAP), so a green line is the *published*
    order reproduced by an independent engine.
    """
    # (name, CS99 g = g_0 * g_1, determinant, is_unimodular)
    cases = [
        ("A8", factorial(9) * 2, 9, False),                        # sec 6.1
        ("D8", (2**7) * factorial(8) * 2, 4, False),               # sec 7.1
        ("E7", (2**10 * 3**4 * 5 * 7) * 1, 2, False),              # sec 8.2, g_1 = 1
        ("E8", (2**14 * 3**5 * 5**2 * 7) * 1, 1, True),            # sec 8.1, g_1 = 1
    ]
    # pin the raw CS99 numbers too, so the factored forms above cannot drift silently
    assert [case[1] for case in cases] == [725760, 10321920, 2903040, 696729600]

    for name, published_order, determinant, is_unimodular in cases:
        lattice = lc.Lattice(name)
        # cheap characterizing invariants
        assert lattice.rank() == int(name[1:])
        assert lattice.signature_pair() == (lattice.rank(), 0)     # positive definite root lattice
        assert lattice.determinant() == determinant
        assert lattice.is_even()
        assert lattice.is_unimodular() == is_unimodular
        assert lattice.minimum() == 2                              # roots are the minimal vectors

        group = lattice.isometry_group()
        assert group.is_finite()
        assert group.order() == published_order                    # CS99 g_0 g_1
        assert all(generator.is_isometry() for generator in group.gens())
