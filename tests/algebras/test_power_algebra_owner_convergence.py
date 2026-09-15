r"""Exterior and divided powers converge on module-owned constructions and functors."""

from dzack_research.preamble.all import ZZ, BasedFreeModule
from dzack_research.preamble.categories.functors.free_algebras import (
    alternating_algebra_functor,
    divided_power_algebra_functor,
)
from dzack_research.preamble.categories.sets.finite_ordered_sets import (
    finite_ordered_set,
)


def test_power_algebra_module_owner_and_nonidentity_functor_share_one_construction() -> None:
    source = BasedFreeModule(ZZ, finite_ordered_set(("x", "y")))
    target = BasedFreeModule(ZZ, finite_ordered_set(("a", "b")))
    morphism = source.module_category().Mor(source, target)(
        {
            "x": 2 * target.module_generator("a"),
            "y": target.module_generator("b"),
        }
    )

    for source_algebra, target_algebra, functor in (
        (source.exterior_algebra(), target.exterior_algebra(), alternating_algebra_functor(ZZ)),
        (
            source.divided_power_algebra(),
            target.divided_power_algebra(),
            divided_power_algebra_functor(ZZ),
        ),
    ):
        assert functor(source) is source_algebra
        assert functor(target) is target_algebra
        induced = functor(morphism)

        assert induced.domain() is source_algebra
        assert induced.codomain() is target_algebra
        assert induced(source_algebra.algebra_generator("x")) == (
            2 * target_algebra.algebra_generator("a")
        )
        assert induced(source_algebra.algebra_generator("y")) == (
            target_algebra.algebra_generator("b")
        )
        source_product = (
            source_algebra.algebra_generator("x")
            * source_algebra.algebra_generator("y")
        )
        assert induced(source_product) == (
            induced(source_algebra.algebra_generator("x"))
            * induced(source_algebra.algebra_generator("y"))
        )
