r"""Higher finite-order lattice centralizers retain cyclotomic gluing data."""

from dzack_research.preamble.all import (
    ZZ,
    Lattices,
    finite_ordered_set,
)


def _cubic_rotation():
    lattice = Lattices(ZZ)([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
    labels = lattice.module_generating_set()
    first, second, third = lattice.module_generators()
    rotation = lattice.O()(
        {labels[0]: second, labels[1]: third, labels[2]: first}
    )
    return rotation


def _negation(lattice):
    return lattice.O()(
        {
            label: -lattice.module_generator(label)
            for label in lattice.module_generating_set()
        }
    )


def test_order_three_cyclotomic_decomposition_retains_nontrivial_glue() -> None:
    isometry = _cubic_rotation()
    decomposition = isometry.cyclotomic_decomposition(3)

    assert decomposition.nonzero_divisors() == finite_ordered_set((ZZ(1), ZZ(3)))
    assert decomposition.summand(1).module_rank() == 1
    assert decomposition.summand(3).module_rank() == 2
    assert decomposition.index() == 3
    assert decomposition.gluing_quotient().cardinality() == 3

    restrictions = decomposition.component_isometries()
    assert restrictions[1] == decomposition.summand(1).O().one()
    assert restrictions[3] != decomposition.summand(3).O().one()

    cyclotomic = decomposition.summand(3)
    root_reflection = cyclotomic.reflection(cyclotomic.basis_vector(0))
    assert root_reflection in cyclotomic.O()
    assert root_reflection not in decomposition.component_centralizers()[3]


def test_cyclotomic_component_tuple_lifts_exactly_when_it_preserves_the_glue() -> None:
    isometry = _cubic_rotation()
    decomposition = isometry.cyclotomic_decomposition(3)
    restrictions = decomposition.component_isometries()

    lifted = decomposition.lift_component_isometries(
        {1: restrictions[1], 3: restrictions[3]}
    )

    assert lifted == isometry
    assert lifted in decomposition.centralizer_group()

    incompatible = {
        1: decomposition.summand(1).O().one(),
        3: _negation(decomposition.summand(3)),
    }
    assert incompatible[3] in decomposition.component_centralizers()[3]
    assert not decomposition.component_isometries_extend(incompatible)










