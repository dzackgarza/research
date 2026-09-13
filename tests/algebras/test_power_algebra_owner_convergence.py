r"""Exterior and divided powers have one constructor owner and functor route."""

from dzack_research.preamble.all import (
    AlternatingAlgebraOf,
    BasedFreeModule,
    DividedPowerAlgebraOf,
    ZZ,
    module_homset,
)
from dzack_research.preamble.categories.algebras.power_algebras import (
    AlternatingAlgebraOf as defining_alternating_algebra,
)
from dzack_research.preamble.categories.algebras.power_algebras import (
    DividedPowerAlgebraOf as defining_divided_power_algebra,
)
from dzack_research.preamble.categories.functors.free_algebras import (
    alternating_algebra_functor,
    divided_power_algebra_functor,
)
from dzack_research.preamble.categories.sets.finite_ordered_sets import (
    finite_ordered_set,
)


def test_power_algebra_public_constructor_and_nonidentity_functor_share_one_owner() -> None:
    source = BasedFreeModule(ZZ, finite_ordered_set(("x", "y")))
    target = BasedFreeModule(ZZ, finite_ordered_set(("a", "b")))
    morphism = module_homset(source, target)(
        {
            "x": 2 * target.module_generator("a"),
            "y": target.module_generator("b"),
        }
    )

    for public_constructor, defining_constructor, functor in (
        (AlternatingAlgebraOf, defining_alternating_algebra, alternating_algebra_functor(ZZ)),
        (DividedPowerAlgebraOf, defining_divided_power_algebra, divided_power_algebra_functor(ZZ)),
    ):
        assert public_constructor is defining_constructor
        source_algebra = public_constructor(source)
        target_algebra = public_constructor(target)
        induced = functor(morphism)

        assert source_algebra is defining_constructor(source)
        assert target_algebra is defining_constructor(target)
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
