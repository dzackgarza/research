r"""Lie cokernels are quotients by generated Lie ideals, not module quotients."""

from dzack_research.preamble.all import QQ
from dzack_research.preamble.categories.algebras import Algebras, LieAlgebras
from dzack_research.preamble.categories.modules import (
    BasedFreeModule,
    BilinearMap,
    Modules,
    module_homset,
)
from dzack_research.preamble.categories.sets import finite_ordered_set


def _lie_algebra(labels, brackets):
    module = BasedFreeModule(QQ, finite_ordered_set(labels))
    multiplication = Modules(QQ).tensor_product((module, module)).from_bilinear(
        BilinearMap(
            module,
            module,
            module,
            {
                (left, right): module.linear_combination(
                    {
                        label: QQ(coefficient)
                        for label, coefficient in brackets.get((left, right), {}).items()
                    }
                )
                for left in labels
                for right in labels
            },
        )
    )
    return Algebras(QQ).Lie()(module, multiplication)


def test_lie_is_a_constructible_algebra_axiom_category() -> None:
    lie = Algebras(QQ).Lie()

    assert lie.is_subcategory(Algebras(QQ))
    assert LieAlgebras(QQ).is_subcategory(lie)


def test_cartan_inclusion_in_sl2_has_zero_lie_cokernel_but_nonzero_module_cokernel() -> None:
    sl2 = _lie_algebra(
        ("e", "f", "h"),
        {
            ("h", "e"): {"e": 2},
            ("e", "h"): {"e": -2},
            ("h", "f"): {"f": -2},
            ("f", "h"): {"f": 2},
            ("e", "f"): {"h": 1},
            ("f", "e"): {"h": -1},
        },
    )
    cartan = _lie_algebra(("h",), {})

    underlying = module_homset(cartan.underlying_module(), sl2.underlying_module())(
        {"h": sl2.underlying_module().module_generator("h")}
    )
    inclusion = LieAlgebras(QQ).Mor(cartan, sl2)(underlying)

    module_cokernel = underlying.cokernel()
    lie_cokernel = inclusion.cokernel()

    assert module_cokernel.module_rank() == 2
    assert lie_cokernel.underlying_module().is_zero()
    assert lie_cokernel in LieAlgebras(QQ)
    assert inclusion.cokernel_projection().codomain() is lie_cokernel
