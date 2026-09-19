r"""Preservation surfaces for shared center and algebra-cokernel constructions."""

from dzack_research.preamble.all import QQ, Algebras, Modules
from dzack_research.preamble.categories.modules import BilinearMap
from dzack_research.preamble.categories.sets import finite_ordered_set


def test_center_of_unital_associative_algebra_retains_its_unit() -> None:
    matrices = QQ.matrix_space(2)
    multiplication = matrices.multiplication_morphism()
    center = matrices.center()
    inclusion = center.center_inclusion()

    assert multiplication.domain().base_ring() is QQ
    assert multiplication.codomain() is matrices
    assert center in Algebras(QQ).Associative().Unital()
    assert center in Algebras(QQ).Commutative()
    unit_map = center.unit_morphism()
    scalar_module = unit_map.domain()
    center_unit = unit_map(scalar_module(QQ.one()))
    assert inclusion(center_unit) == matrices.identity()
    assert center.product(center.one(), center.one()) == center.one()


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
