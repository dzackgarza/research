r"""Higher finite-order lattice centralizers retain cyclotomic gluing data."""

from dzack_research.preamble.all import (
    Sets,
    ZZ,
    Lattices,
    finite_ordered_set,
)
from dzack_research.preamble.categories.sets import finite_indexed_family


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
    root_reflection = cyclotomic.reflection(cyclotomic.module_generator(0))
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


def test_ambient_centralizer_restriction_round_trips_through_the_glue() -> None:
    isometry = _cubic_rotation()
    decomposition = isometry.cyclotomic_decomposition(3)
    lattice = isometry.domain()

    for ambient in (isometry, _negation(lattice)):
        components = decomposition.restrict_centralizer_element(ambient)
        assert all(
            components[divisor] in decomposition.component_centralizers()[divisor]
            for divisor in decomposition.nonzero_divisors()
        )
        assert decomposition.lift_component_isometries(components) == ambient


def test_the_exact_order_is_part_of_the_cyclotomic_construction() -> None:
    isometry = _cubic_rotation()

    try:
        isometry.cyclotomic_decomposition(6)
    except ValueError:
        pass
    else:
        raise AssertionError("an order-three isometry cannot be declared to have exact order six")


def _same_sublattice(left, right) -> bool:
    try:
        left.inclusion().factor_through(right.inclusion())
        right.inclusion().factor_through(left.inclusion())
    except ValueError:
        return False
    return True


def test_equivariant_coordinate_lines_have_exact_centralizer_orbits_and_transporters() -> None:
    lattice = Lattices(ZZ)([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
    isometry = _negation(lattice)
    generators = lattice.module_generators()
    lines = finite_indexed_family(
        generators.index_set(),
        lambda label: lattice.subobject_on((generators[label],)),
        name="Coordinate lines",
    )

    decomposition = isometry.equivariant_sublattice_orbit_decomposition(lines)

    assert decomposition in Sets()
    assert decomposition.orbits().cardinality() == 1
    assert decomposition.representatives().cardinality() == 1
    transporter = decomposition.transporter(lines[0], lines[2])
    assert transporter is not None
    assert transporter in isometry.centralizer_group()
    assert _same_sublattice((transporter * lines[0].inclusion()).image(), lines[2])
    stabilizer = decomposition.stabilizer(lines[0])
    assert stabilizer.supergroup() is isometry.centralizer_group()
    assert all(
        _same_sublattice((element * lines[0].inclusion()).image(), lines[0])
        for element in (stabilizer.one(),)
    )


def test_equivariant_line_plane_flags_have_exact_centralizer_orbits_and_transporters() -> None:
    lattice = Lattices(ZZ)([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
    isometry = _negation(lattice)
    generators = lattice.module_generators()
    lines = finite_indexed_family(
        generators.index_set(),
        lambda label: lattice.subobject_on((generators[label],)),
        name="Coordinate lines",
    )
    planes = {
        (left, right): lattice.subobject_on(
            (generators[left], generators[right])
        )
        for left in range(3)
        for right in range(left + 1, 3)
    }
    flag_labels = finite_ordered_set([
        (line, other)
        for line in range(3)
        for other in range(3)
        if line != other
    ])
    flags = finite_indexed_family(
        flag_labels,
        lambda pair: isometry.equivariant_flag(
            (
                lines[pair[0]],
                planes[(min(pair), max(pair))],
            )
        ),
        name="Coordinate line-plane flags",
    )

    decomposition = isometry.equivariant_flag_orbit_decomposition(flags)

    assert decomposition in Sets()
    assert decomposition.orbits().cardinality() == 1
    assert decomposition.representatives().cardinality() == 1
    transporter = decomposition.transporter(flags[flag_labels[0]], flags[flag_labels[-1]])
    assert transporter is not None
    assert transporter in isometry.centralizer_group()
    source_terms = flags[flag_labels[0]].terms()
    target_terms = flags[flag_labels[-1]].terms()
    assert all(
        _same_sublattice((transporter * source.inclusion()).image(), target)
        for source, target in zip(source_terms, target_terms, strict=True)
    )
    assert decomposition.stabilizer(flags[0]).supergroup() is isometry.centralizer_group()
