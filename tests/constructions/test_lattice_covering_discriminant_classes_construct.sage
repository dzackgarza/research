r"""The unimodular hyperbolic plane has one discriminant class covering root square."""

from dzack_research.preamble.all import *  # noqa: F401,F403


def test_hyperbolic_plane_root_square_has_only_zero_covering_class() -> None:
    lattice = NamedLattices.U
    classes = lattice.covering_discriminant_classes(-2)

    assert classes.cardinality() == cardinal(1)
    assert lattice.discriminant_group().zero() in classes


def test_covering_classes_match_the_defining_discriminant_predicate() -> None:
    lattice = Lattices(ZZ)("A3").twist(ZZ(2))
    discriminant = lattice.discriminant_group()
    values = discriminant.quadratic_value_module()
    field = lattice.base_ring().fraction_field()

    for square in (ZZ.zero(), ZZ(2)):
        target = field(square)
        expected = tuple(
            element
            for element in discriminant.elements()
            if discriminant.q(element)
            == values(target / field(element.additive_order()) ** 2)
        )

        assert tuple(lattice.covering_discriminant_classes(square)) == expected
