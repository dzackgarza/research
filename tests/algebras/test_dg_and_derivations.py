from dzack_research.preamble.all import QQ
from dzack_research.preamble.categories.algebras import (
    DeRhamAlgebra,
    SymmetricAlgebraOn,
)
from dzack_research.preamble.categories.modules import (
    DifferentialGradedModules,
    GradedAlgebraModules,
    regular_dg_module,
)


def test_de_rham_differential_is_a_degree_one_graded_derivation() -> None:
    algebra = SymmetricAlgebraOn(QQ, ("x", "y"))
    dga = DeRhamAlgebra(algebra)
    differential = dga.differential()

    x, y = algebra.algebra_generators()
    assert differential.degree_shift() == 1
    assert differential(x * y) == differential(x) * y + x * differential(y)
    assert differential(differential(x)) == dga.zero()


def test_a_dga_is_canonically_its_regular_dg_module() -> None:
    algebra = SymmetricAlgebraOn(QQ, ("x",))
    x = algebra.algebra_generator("x")
    dga = DeRhamAlgebra(algebra)
    regular = regular_dg_module(dga)
    X = regular.from_degree_zero(x)
    dX = regular.d(X)

    assert regular is dga
    assert regular in GradedAlgebraModules(dga)
    assert regular in DifferentialGradedModules(dga)
    assert regular.graded_algebra() is dga
    assert regular.dga() is dga
    assert regular.act(X, dX) == X * dX
    assert regular.d(X * dX) == regular.d(X) * dX + X * regular.d(dX)
