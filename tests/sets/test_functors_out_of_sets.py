r"""The functors and adjunctions whose domain is Set, asked of Set.

Each row states the functor's domain and codomain, its action on a set map
rather than only on objects, and the construction's own content on a small
specimen.  Each adjunction states the endpoints of its unit and counit and
the value of one of them.
"""

from dzack_research.preamble.all import (
    ZZ,
    Cardinalities,
    FiniteSets,
    Groups,
    Modules,
    Sets,
    cardinal,
)
from dzack_research.preamble.categories.sets import finite_ordered_set


def _shift(source, target):
    r"""The set map raising each ordinal label by one."""
    return Sets().Mor(source, target)(lambda label: target(int(label) + 1))


def test_the_free_module_functor_carries_a_set_map_to_generators() -> None:
    functor = Sets().free_module(ZZ)
    assert functor.domain() == Sets()
    assert functor.codomain() == Modules(ZZ)

    labels = Sets.Δ[1]
    larger = Sets.Δ[2]
    free = functor(labels)
    target = functor(larger)
    carried = functor(_shift(labels, larger))

    assert free.module_rank() == 2
    assert target.module_rank() == 3
    assert carried.domain() is free
    assert carried.codomain() is target
    assert carried(free.module_generator(labels(0))) == target.module_generator(larger(1))
    assert carried(free.module_generator(labels(1))) == target.module_generator(larger(2))


def test_the_free_module_adjunction_has_a_unit_of_generators_and_an_evaluating_counit() -> None:
    adjunction = Sets().free_module_adjunction(ZZ)
    assert adjunction.left_adjoint().domain() == Sets()
    assert adjunction.left_adjoint().codomain() == Modules(ZZ)
    assert adjunction.right_adjoint().domain() == Modules(ZZ)
    assert adjunction.right_adjoint().codomain() == Sets()

    labels = Sets.Δ[1]
    free = adjunction.left_adjoint()(labels)
    unit = adjunction.unit(labels)
    assert unit.domain() is labels
    assert unit.codomain() is adjunction.right_adjoint()(free)
    assert unit(labels(0)) == free.module_generator(labels(0))

    counit = adjunction.counit(free)
    assert counit.codomain() is free
    assert counit.domain() is adjunction.left_adjoint()(adjunction.right_adjoint()(free))
    element = free.module_generator(labels(0)) + free.module_generator(labels(1))
    assert counit(counit.domain().module_generator(element)) == element


def test_the_free_group_functor_carries_a_set_map_to_free_generators() -> None:
    functor = Sets().free_group()
    assert functor.domain() == Sets()
    assert functor.codomain() == Groups()

    letters = Sets.Δ[1]
    larger = Sets.Δ[2]
    free = functor(letters)
    target = functor(larger)
    carried = functor(_shift(letters, larger))

    assert free.free_basis().cardinality() == cardinal(2)
    assert free.free_generator(letters(0)) != free.free_generator(letters(1))
    assert carried.domain() is free
    assert carried.codomain() is target
    assert carried(free.free_generator(letters(0))) == target.free_generator(larger(1))
    assert carried(free.free_generator(letters(1))) == target.free_generator(larger(2))


def test_the_free_group_adjunction_has_a_unit_of_letters_and_a_multiplying_counit() -> None:
    adjunction = Sets().free_group_adjunction()
    assert adjunction.left_adjoint().domain() == Sets()
    assert adjunction.left_adjoint().codomain() == Groups()
    assert adjunction.right_adjoint().domain() == Groups()
    assert adjunction.right_adjoint().codomain() == Sets()

    letters = Sets.Δ[1]
    free = adjunction.left_adjoint()(letters)
    unit = adjunction.unit(letters)
    assert unit.domain() is letters
    assert unit.codomain() is adjunction.right_adjoint()(free)
    assert unit(letters(0)) == free.free_generator(letters(0))

    symmetric = Groups.S(3)
    counit = adjunction.counit(symmetric)
    assert counit.codomain() is symmetric
    assert counit.domain() is adjunction.left_adjoint()(adjunction.right_adjoint()(symmetric))
    transposition = next(
        element for element in symmetric.group_generators() if element.order() == 2
    )
    assert counit(counit.domain().free_generator(transposition)) == transposition


def test_the_cardinality_functor_is_defined_on_the_core_of_sets() -> None:
    functor = Sets().cardinality_functor()
    assert functor.domain().base_category() == Sets()
    assert functor.codomain() == Cardinalities()

    ordinal = Sets.Δ[2]
    letters = finite_ordered_set(("x", "y", "z"))
    relabelling = Sets().Mor(ordinal, letters)(lambda index: letters.unrank(int(index)))

    assert functor(ordinal) == cardinal(3)
    assert functor(letters) == cardinal(3)
    carried = functor(relabelling)
    assert carried.domain() == cardinal(3)
    assert carried.codomain() == cardinal(3)


def test_the_power_set_functor_has_all_of_sets_for_its_domain() -> None:
    functor = FiniteSets().power_set_functor()
    assert functor is Sets().power_set_functor()
    assert functor.domain() == Sets()
    assert functor.codomain() == Sets()

    source = Sets.Δ[3]
    target = Sets.Δ[1]
    parity = Sets().Mor(source, target)(lambda value: target(int(value) % 2))
    subsets = functor(source)
    images = functor(target)
    carried = functor(parity)

    assert subsets.cardinality() == cardinal(16)
    assert carried.domain() is subsets
    assert carried.codomain() is images
    assert carried(subsets({0, 2})) == images({0})
    assert carried(subsets({0, 1, 2})) == images({0, 1})
