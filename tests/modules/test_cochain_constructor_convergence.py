r"""Every public cochain route delegates to the category-owned construction."""

from dzack_research.preamble.all import (
    ZZ,
    BasedFreeModule,
    CochainComplex,
    CochainComplexes,
    CochainComplexFromFamily,
)
from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
    module_homset,
)
from dzack_research.preamble.categories.sets.finite_ordered_sets import finite_ordered_set
from dzack_research.preamble.categories.sets.indexed_families import indexed_family


def _two_term_data():
    source = BasedFreeModule(ZZ, finite_ordered_set(("e",)))
    target = BasedFreeModule(ZZ, finite_ordered_set(("f",)))
    differential = module_homset(source, target)(
        {"e": 2 * target.module_generator("f")}
    )
    return source, target, differential


def test_finite_notation_uses_the_category_constructor() -> None:
    source, target, differential = _two_term_data()
    category = CochainComplexes(ZZ)
    declared = category({0: source, 1: target}, {0: differential})
    notation = CochainComplex(ZZ, {0: source, 1: target}, {0: differential})

    assert declared in category
    assert notation in category
    assert declared.graded_piece(0) is source
    assert notation.graded_piece(1) is target
    assert declared.differential_component(0)(source.module_generator("e")) == (
        2 * target.module_generator("f")
    )
    assert notation.differential_component(0)(source.module_generator("e")) == (
        declared.differential_component(0)(source.module_generator("e"))
    )


def test_lazy_notation_uses_the_category_family_constructor() -> None:
    category = CochainComplexes(ZZ)
    degrees = category.base_ring()
    zero = BasedFreeModule(ZZ, finite_ordered_set(()))
    pieces = indexed_family(degrees, lambda _degree: zero, name="Zero pieces")
    differentials = indexed_family(
        degrees,
        lambda _degree: module_homset(zero, zero).zero(),
        name="Zero differentials",
    )

    declared = category.from_family(pieces, differentials)
    notation = CochainComplexFromFamily(ZZ, pieces, differentials)

    assert declared in category
    assert notation in category
    assert not declared.has_finite_support()
    assert not notation.has_finite_support()
    assert declared.degree_index_set() is notation.degree_index_set()
