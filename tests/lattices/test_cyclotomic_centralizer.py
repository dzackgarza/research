r"""Higher finite-order lattice centralizers retain cyclotomic gluing data."""

from dzack_research.preamble.all import Lattices, ZZ


def _cubic_rotation():
    lattice = Lattices(ZZ)([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
    labels = tuple(lattice.module_generating_set())
    first, second, third = tuple(lattice.module_generators())
    rotation = lattice.O()(
        {labels[0]: second, labels[1]: third, labels[2]: first}
    )
    return lattice.with_isometry(rotation)


def _negation(lattice):
    return lattice.O()(tuple(-generator for generator in lattice.module_generators()))


def test_order_three_cyclotomic_decomposition_retains_nontrivial_glue() -> None:
    decorated = _cubic_rotation()
    decomposition = decorated.cyclotomic_decomposition(3)

    assert tuple(int(divisor) for divisor in decomposition.nonzero_divisors()) == (1, 3)
    assert decomposition.summand(1).module_rank() == 1
    assert decomposition.summand(3).module_rank() == 2
    assert decomposition.index() == 3
    assert decomposition.gluing_quotient().cardinality() == 3

    restrictions = decomposition.component_isometries()
    assert restrictions[1] == decomposition.summand(1).O().one()
    assert restrictions[3] != decomposition.summand(3).O().one()

    cyclotomic = decomposition.summand(3)
    root_reflection = cyclotomic.reflection(cyclotomic.module_generator(0))
    assert root_reflection in cyclotomic.O()
    assert root_reflection not in decomposition.component_centralizers()[3]


def test_cyclotomic_component_tuple_lifts_exactly_when_it_preserves_the_glue() -> None:
    decorated = _cubic_rotation()
    decomposition = decorated.cyclotomic_decomposition(3)
    restrictions = decomposition.component_isometries()

    lifted = decomposition.lift_component_isometries(
        {1: restrictions[1], 3: restrictions[3]}
    )

    assert lifted == decorated.isometry()
    assert lifted in decomposition.centralizer_group()

    incompatible = {
        1: decomposition.summand(1).O().one(),
        3: _negation(decomposition.summand(3)),
    }
    assert incompatible[3] in decomposition.component_centralizers()[3]
    assert not decomposition.component_isometries_extend(incompatible)


def test_the_exact_order_is_part_of_the_cyclotomic_construction() -> None:
    decorated = _cubic_rotation()

    try:
        decorated.cyclotomic_decomposition(6)
    except ValueError:
        pass
    else:
        raise AssertionError("an order-three isometry cannot be declared to have exact order six")
