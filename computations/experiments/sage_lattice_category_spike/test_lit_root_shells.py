from __future__ import annotations

import sage_lattice_category_spike.lattice_categories as lc


def test_d4_theta_shell_counts_match_conway_sloane_chapter_4():
    r"""Conway-Sloane Ch. 4 tabulates the theta-shell data of the D_4 root
    lattice: one zero vector, 24 roots of norm 2, 24 vectors of norm 4, and
    96 vectors of norm 6. This pins the enumeration vocabulary beyond the
    kissing number/root count and checks that the negative-definite convention
    transports the same shells by sign.
    """
    d4 = lc.Lattice("D4")
    negative_d4 = d4.twist(-1)

    assert d4.is_even() and d4.minimum() == 2
    assert [len(d4.vectors_of_square(k)) for k in (0, 2, 4, 6)] == [
        1,
        24,
        24,
        96,
    ]
    assert [len(shell) for shell in d4.short_vectors(7)] == [1, 0, 24, 0, 24, 0, 96]

    assert negative_d4.is_even() and negative_d4.maximum() == -2
    assert [len(negative_d4.vectors_of_square(-k)) for k in (2, 4, 6)] == [
        24,
        24,
        96,
    ]
    assert [len(shell) for shell in negative_d4.short_vectors(7)] == [
        1,
        0,
        24,
        0,
        24,
        0,
        96,
    ]


def test_a2_direct_sum_theta_shell_convolution_matches_conway_sloane():
    r"""For an orthogonal direct sum, theta series multiply. Combining the
    Conway-Sloane Ch. 4 A_2 shell data gives 12 roots in A_2 + A_2 and
    36 vectors of norm 4: 6+6 roots, and the norm-4 shell from
    ``(root, root)`` pairs plus the two summand norm-4 shells.
    """
    a2_sum = lc.Lattice("A2").direct_sum(lc.Lattice("A2"))
    negative_sum = a2_sum.twist(-1)

    assert a2_sum.is_even()
    assert a2_sum.discriminant_group().invariants() == (3, 3)
    assert len(a2_sum.roots()) == 12
    assert len(a2_sum.vectors_of_square(4)) == 36
    assert [len(shell) for shell in a2_sum.short_vectors(5)] == [1, 0, 12, 0, 36]

    assert negative_sum.is_even()
    assert len(negative_sum.roots()) == 12
    assert len(negative_sum.vectors_of_square(-4)) == 36
    assert [len(shell) for shell in negative_sum.short_vectors(5)] == [
        1,
        0,
        12,
        0,
        36,
    ]
