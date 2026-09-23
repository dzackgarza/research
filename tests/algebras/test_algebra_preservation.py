r"""Preservation surfaces for shared center and algebra-cokernel constructions."""

from dzack_research.preamble.all import QQ, Algebras, Modules
from dzack_research.preamble.categories.modules import BilinearMap
from dzack_research.preamble.categories.sets import finite_ordered_set




def test_nonassociative_center_remains_a_central_submodule() -> None:
    module = QQ.free_module(finite_ordered_set(("x", "y")))
    multiplication = BilinearMap(
        module,
        module,
        module,
        {
            ("x", "x"): module.module_generator("y"),
            ("x", "y"): module.module_generator("x"),
            ("y", "x"): module.module_generator("x"),
            ("y", "y"): module.zero(),
        },
    )
    algebra = Algebras(QQ)(module, multiplication)
    center = algebra.center()

    assert center in Modules(QQ)
    assert center not in Algebras(QQ)
    assert center.module_rank() == 2
    assert center.inclusion().codomain() is module

    x = module.module_generator("x")
    y = module.module_generator("y")
    assert algebra.product(algebra.product(x, x), y) != algebra.product(
        x,
        algebra.product(x, y),
    )
