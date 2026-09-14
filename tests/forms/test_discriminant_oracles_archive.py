r"""Independent discriminant-form oracles retained from the archive suite.

The finite cokernel presentation is checked against unrelated lattice data:
``|A_L|=|det G|``, root lattices have their classical discriminant groups,
the bilinear pairing is ``G^{-1}`` modulo ``ZZ``, and primary components have
exactly the prime-power orders of the finite abelian group.
"""

from math import prod

from dzack_research.preamble.all import QQ, ZZ, Lattices

ARCHIVE_RECONCILIATION = {
    "archive_module": "preamble/tests/test_discriminant_forms.sage",
    "live_owner": "tests/forms/test_discriminant_oracles_archive.py",
    "owner_overrides": {
        "test_polarization_relates_q_and_b_by_a_factor_of_two": "tests/forms/test_discriminant_convention_archive.py",
        "test_q_is_quadratic_and_b_is_symmetric_bilinear": "tests/forms/test_discriminant_convention_archive.py",
        "test_normal_form_is_an_isometry_onto_a_smaller_generating_set": "tests/forms/test_discriminant_normal_forms_archive.py",
        "test_invariant_factor_form_is_an_isometry_on_invariant_factor_generators": "tests/forms/test_discriminant_normal_forms_archive.py",
        "test_odd_lattices_have_no_quadratic_discriminant_form": "tests/forms/test_discriminant_refinement_archive.py",
        "test_correlation_is_the_gram_matrix_into_the_dual": "tests/forms/test_discriminant_normal_forms_archive.py",
        "test_discriminant_group_of_a_direct_sum_is_the_direct_sum_of_the_groups": "tests/forms/test_discriminant_normal_forms_archive.py",
        "test_discriminant_form_convention_is_nikulins_not_peters_sterks": "tests/forms/test_discriminant_convention_archive.py",
    },
    "disposition": "reconciled-live-owner",
}


def _order(form) -> int:
    return prod(int(factor) for factor in form.invariants()) or 1


def test_discriminant_group_order_is_absolute_gram_determinant() -> None:
    for lattice in (
        Lattices.A2,
        Lattices.A3,
        Lattices.D4,
        Lattices.D5,
        Lattices.E6,
        Lattices.E7,
        Lattices.E8,
        Lattices.U,
        Lattices.U_2,
        Lattices.TEn,
        Lattices.LK3,
    ):
        assert _order(lattice.discriminant_group()) == abs(
            int(lattice.gram_matrix().determinant())
        )


def test_root_lattice_discriminant_groups_are_the_classical_ones() -> None:
    for rank in range(2, 8):
        assert _order(Lattices.root_lattice("A", rank).discriminant_group()) == rank + 1
    for rank in range(4, 8):
        form = Lattices.root_lattice("D", rank).discriminant_group()
        assert _order(form) == 4
        expected = (2, 2) if rank % 2 == 0 else (4,)
        assert tuple(form.invariants()) == expected
    for rank, order in ((6, 3), (7, 2), (8, 1)):
        assert _order(Lattices.root_lattice("E", rank).discriminant_group()) == order


def test_discriminant_bilinear_form_is_inverse_gram_modulo_integers() -> None:
    for lattice in (Lattices.A2, Lattices.D4, Lattices.E7, Lattices.U_2):
        inverse = lattice.gram_matrix().inverse()
        form = lattice.discriminant_bilinear_form()
        generators = tuple(form.module_generators())
        for i, left in enumerate(generators):
            for j, right in enumerate(generators):
                assert QQ(left.b(right).lift() - inverse[i, j]) in ZZ


def test_primary_components_have_the_prime_power_orders_and_exhaust_a5() -> None:
    form = Lattices.A5.discriminant_group()
    components = form.primary_components()

    assert _order(form) == 6
    assert tuple(components) == (ZZ(2), ZZ(3))
    assert components[ZZ(2)].cardinality() == 2
    assert components[ZZ(3)].cardinality() == 3
    assert (
        int(components[ZZ(2)].cardinality())
        * int(components[ZZ(3)].cardinality())
        == int(form.cardinality())
    )
