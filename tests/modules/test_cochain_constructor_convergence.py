r"""Every public cochain route delegates to the category-owned construction."""

from dzack_research.preamble.all import (
    ZZ,
    BasedFreeModule,
    CochainComplexes,
)
from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
    module_homset,
)
from dzack_research.preamble.categories.sets.finite_ordered_sets import finite_ordered_set
from dzack_research.preamble.categories.sets.indexed_families import indexed_family


def _two_term_data():
    source = BasedFreeModule(ZZ, finite_ordered_set(("e",)))
    target = BasedFreeModule(ZZ, finite_ordered_set(("f",)))
    differential = source.module_category().Mor(source, target)(
        {"e": 2 * target.module_generator("f")}
    )
    return source, target, differential


def test_finite_complex_uses_the_category_constructor() -> None:
    source, target, differential = _two_term_data()
    category = CochainComplexes(ZZ)
    complex_ = category({0: source, 1: target}, {0: differential})

    assert complex_ in category
    assert complex_.graded_piece(0) is source
    assert complex_.graded_piece(1) is target
    assert complex_.differential_component(0)(source.module_generator("e")) == (
        2 * target.module_generator("f")
    )


def test_lazy_complex_uses_the_category_family_constructor() -> None:
    category = CochainComplexes(ZZ)
    degrees = category.base_ring()
    zero = BasedFreeModule(ZZ, finite_ordered_set(()))
    pieces = indexed_family(degrees, lambda _degree: zero, name="Zero pieces")
    differentials = indexed_family(
        degrees,
        lambda _degree: zero.module_category().Mor(zero, zero).zero(),
        name="Zero differentials",
    )

    complex_ = category.from_family(pieces, differentials)

    assert complex_ in category
    assert not complex_.has_finite_support()
    assert complex_.degree_index_set() is degrees
