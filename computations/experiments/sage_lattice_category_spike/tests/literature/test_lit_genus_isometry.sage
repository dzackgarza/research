from __future__ import annotations

from sage.all import QQ, QuadraticForm, ZZ, matrix

import sage_lattice_category_spike.lattice_categories as lc


def test_dickson_ross_equivalence_uses_splag_unimodular_witness():
    """SPLAG Ch. 15, Sec. 11 gives this Dickson-Ross ternary equivalence.

    Conway-Sloane record the Gram matrices below, note that their genus has one
    class, and give the displayed unimodular transform from the first form to
    the second.
    """
    first_gram = matrix(ZZ, [[3, 1, 0], [1, 23, 0], [0, 0, -1]])
    second_gram = matrix(ZZ, [[7, 3, 0], [3, 11, 0], [0, 0, -1]])
    witness = matrix(ZZ, [[-3, 2, 10], [-2, 3, 14], [-1, 1, 5]])

    first = lc.Lattice(first_gram, label="SPLAG Dickson-Ross A")
    second = lc.Lattice(second_gram, label="SPLAG Dickson-Ross B")

    assert first.signature_pair() == second.signature_pair() == (2, 1)
    assert first.determinant() == second.determinant() == -68
    assert witness.det() == -1
    assert witness * first_gram * witness.transpose() == second_gram

    assert first.is_isometric(second)
    isometry = second.Hom(first).from_matrix(witness.transpose())
    assert isometry.is_isometry()
    assert isometry.inverse().is_isometry()
    assert [isometry(v).q() for v in second.gens()] == [v.q() for v in second.gens()]


def test_hasse_minkowski_rational_diagonal_forms_match_splag_decision():
    """SPLAG Ch. 15, Secs. 5.1-5.2, Thms. 3-4 decide rational equivalence.

    The first two diagonal forms are the rational diagonalizations printed in
    Ch. 15, Sec. 11 for the Dickson-Ross forms.  Hasse-Minkowski separates the
    sign-changed form by its local rational equivalence data.
    """
    first = lc.Lattice(
        matrix.diagonal(QQ, [QQ(3), QQ(68) / 3, -QQ(1)]),
        base_ring=QQ,
        label="<3,68/3,-1>_Q",
    )
    second = lc.Lattice(
        matrix.diagonal(QQ, [QQ(7), QQ(68) / 7, -QQ(1)]),
        base_ring=QQ,
        label="<7,68/7,-1>_Q",
    )
    sign_changed = lc.Lattice(
        matrix.diagonal(QQ, [QQ(3), QQ(68) / 3, QQ(1)]),
        base_ring=QQ,
        label="<3,68/3,1>_Q",
    )

    assert first.signature_pair() == second.signature_pair() == (2, 1)
    assert first.determinant() == second.determinant() == -68
    places = [-1, 2, 17]
    first_form = QuadraticForm(matrix(QQ, 2 * first.gram_matrix()))
    second_form = QuadraticForm(matrix(QQ, 2 * second.gram_matrix()))
    assert [first_form.hasse_invariant(place) for place in places] == [
        second_form.hasse_invariant(place) for place in places
    ]

    assert first.is_isometric(second)
    assert first.determinant() / sign_changed.determinant() == -1
    assert not QQ(-1).is_square()
    assert not first.is_isometric(sign_changed)
    assert not second.is_isometric(sign_changed)


def test_a2_isometry_group_has_splag_dihedral_conjugacy_data():
    """SPLAG Ch. 3, Sec. 4.1 and Ch. 4, Sec. 6 identify Aut(A2).

    The hexagonal lattice has dihedral automorphism group of order 12; Ch. 4,
    Secs. 6.1-6.2 give the A2 Weyl part of order 3! and the extra factor of 2.
    """
    a2 = lc.Lattice("A2(-1)")
    group = a2.isometry_group()

    assert a2.minimum() == 2
    assert len(a2.roots()) == 6
    assert group.order() == 12
    assert group.structure_description() == "D6"

    representatives = group.conjugacy_classes_representatives()
    assert len(representatives) == 6
    assert sorted(representative.order() for representative in representatives) == [
        1,
        2,
        2,
        2,
        3,
        6,
    ]
    assert sorted(
        (
            ZZ(representative.matrix().det()),
            ZZ(representative.matrix().trace()),
            representative.order(),
        )
        for representative in representatives
    ) == [
        (-1, 0, 2),
        (-1, 0, 2),
        (1, -2, 2),
        (1, -1, 3),
        (1, 1, 6),
        (1, 2, 1),
    ]
    assert all(representative in group for representative in representatives)
