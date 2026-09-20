r"""A module is an abelian group with a ring morphism into its endomorphisms.

The general module states that definition and nothing else: a represented set,
its addition, zero and negation, and the action.  It is built through the owned
module chain, so its count is its underlying set's, its annihilator is the
kernel of the action morphism, and a second ring can act on the same abelian
group by naming a second morphism into the same endomorphisms.
"""

import pytest
from sage.misc.unknown import Unknown

from dzack_research.preamble.all import (
    GF,
    GeneralModules,
    Modules,
    QQ,
    Set,
    ZZ,
)

from dzack_research.preamble.categories.sets.set_categories import FiniteSets


def _integers_mod(size):
    r"""Return ``ZZ/size`` as an abelian group on the residues."""
    return GeneralModules(ZZ).from_operations(
        Set(list(range(size))),
        addition=lambda left, right: (left + right) % size,
        zero=0,
        negation=lambda value: (-value) % size,
        scalar_action=lambda scalar, value: (int(scalar) * value) % size,
    )


def test_a_general_module_is_placed_by_the_module_graph() -> None:
    module = _integers_mod(6)

    assert module in GeneralModules(ZZ)
    assert module in Modules(ZZ)
    assert module.base_ring() is ZZ


def test_a_decidably_invalid_elementwise_action_is_rejected() -> None:
    field = GF(2)

    with pytest.raises(AssertionError, match="1 does not act as the identity"):
        GeneralModules(field).from_operations(
            Set([0, 1]),
            addition=lambda left, right: (left + right) % 2,
            zero=0,
            negation=lambda value: value,
            scalar_action=lambda _scalar, _value: 0,
        )


def test_a_decidable_operation_presentation_records_established_module_laws() -> None:
    field = GF(2)
    module = GeneralModules(field).from_operations(
        Set([0, 1]),
        addition=lambda left, right: (left + right) % 2,
        zero=0,
        negation=lambda value: value,
        scalar_action=lambda scalar, value: (int(scalar) * value) % 2,
    )

    assert module.module_laws_decision() is True


def test_an_undecidable_operation_presentation_retains_its_module_law_hypothesis() -> None:
    module = GeneralModules(QQ).from_operations(
        Set(QQ),
        addition=lambda left, right: left + right,
        zero=QQ.zero(),
        negation=lambda value: -value,
        scalar_action=lambda scalar, value: scalar * value,
    )

    assert module.module_laws_decision() is Unknown


def test_the_count_of_a_general_module_is_its_underlying_sets() -> None:
    module = _integers_mod(6)

    assert module.cardinality() == module.underlying_set().cardinality()
    assert module in FiniteSets()


def test_the_annihilator_is_the_kernel_of_the_action_morphism() -> None:
    module = _integers_mod(6)

    assert module.annihilator() == module.scalar_action().kernel()
    assert module.annihilator() == ZZ.ideal(ZZ(6))


def test_a_second_ring_acts_through_a_second_morphism_into_the_endomorphisms() -> None:
    r"""``ZZ/3`` as an abelian group carries a ``GF(3)``-module structure."""
    group = _integers_mod(3)
    field = GF(3)
    endomorphisms = Modules(ZZ).End(group)
    action = field.Mor(endomorphisms)(
        lambda scalar: endomorphisms.elementwise(
            lambda element: group(int(scalar) * element.underlying_element() % 3),
        ),
    )

    over_the_field = Modules(field)(group, action)

    assert over_the_field in Modules(field)
    assert over_the_field.base_ring() is field
    assert over_the_field.module_laws_decision() is True
    assert over_the_field.cardinality() == group.cardinality()
    assert over_the_field.scalar_multiple(
        field(2), over_the_field(group(2))
    ) == over_the_field(group(1))
