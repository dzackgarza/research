r"""Discriminant modules retain the quotient ``L^# / L`` and its maps.

For the ``A2`` lattice the discriminant module is cyclic of order three.  Its
only primary component is the 3-primary part and its only subgroups are the
trivial subgroup and the whole cyclic group.
"""

from dzack_research.preamble.all import *  # noqa: F401,F403


def _a2_discriminant_module():
    lattice = Lattices(ZZ)("A2")
    return lattice, lattice.discriminant_group()


def test_discriminant_module_retains_lattice_dual_correlation_and_projection() -> None:
    lattice, discriminant = _a2_discriminant_module()
    dual = discriminant.dual_lattice()
    correlation = discriminant.correlation()
    projection = discriminant.projection()

    assert discriminant in DiscriminantModules(ZZ)
    assert discriminant.source_lattice() is lattice
    assert discriminant.cover() is dual
    assert correlation.domain() is lattice
    assert correlation.codomain() is dual
    assert projection.domain() is dual
    assert projection.codomain() is discriminant
    assert discriminant.cardinality() == cardinal(3)


def test_discriminant_classes_lift_back_to_the_selected_dual_lattice() -> None:
    _lattice, discriminant = _a2_discriminant_module()
    generator = discriminant.module_generator(0)
    lift = discriminant.dual_lattice_lift(generator)

    assert discriminant.discriminant_class(lift) == generator
    assert discriminant.projection()(lift) == generator
    assert isinstance(generator, discriminant.ElementType)


def test_a2_discriminant_primary_parts_and_subgroups_are_the_cyclic_order_three_ones() -> None:
    _lattice, discriminant = _a2_discriminant_module()
    generator = discriminant.module_generator(0)
    components = discriminant.primary_components()
    generated = discriminant.subgroup_on((generator,))

    assert components.cardinality() == cardinal(1)
    assert discriminant.primary_part(3).cardinality() == cardinal(3)
    assert discriminant.primary_part(2).cardinality() == cardinal(1)
    assert generated.cardinality() == cardinal(3)
    assert discriminant.subgroups().cardinality() == cardinal(2)


def test_discriminant_module_morphisms_have_identity() -> None:
    _lattice, discriminant = _a2_discriminant_module()
    identity = discriminant.Mor(discriminant).identity()

    assert identity(discriminant.zero()) == discriminant.zero()
    assert identity * identity == identity
