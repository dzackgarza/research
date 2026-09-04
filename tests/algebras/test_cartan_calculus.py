from dzack_research.preamble.all import QQ
from dzack_research.preamble.categories.algebras import (
    DeRhamAlgebra,
    GradedCommutator,
    InteriorProduct,
    LieBracket,
    LieDerivative,
    SymmetricAlgebraOn,
    VectorFields,
)
from dzack_research.preamble.categories.modules import ring_as_module
from dzack_research.static_types import (
    d as static_d,
    form_view,
    interior as static_interior,
    lie_derivative as static_lie_derivative,
    vector_field_view,
    wedge as static_wedge,
)


def _scalar_module_element(module, scalar):
    label = next(iter(module.module_generating_set()))
    return module.scalar_multiple(scalar, module.module_generator(label))


def test_vector_fields_are_derivations_and_have_the_expected_lie_bracket() -> None:
    algebra = SymmetricAlgebraOn(QQ, ("x", "y"))
    x = algebra.algebra_generator("x")
    y = algebra.algebra_generator("y")
    values = ring_as_module(algebra)
    vector_fields = VectorFields(algebra)

    d_dx = vector_fields(
        {
            "x": _scalar_module_element(values, algebra.one()),
            "y": values.zero(),
        }
    )
    x_d_dy = vector_fields(
        {
            "x": values.zero(),
            "y": _scalar_module_element(values, x),
        }
    )
    bracket = LieBracket(d_dx, x_d_dy)

    assert bracket.parent() is vector_fields
    assert bracket(x) == values.zero()
    assert bracket(y) == _scalar_module_element(values, algebra.one())


def test_contraction_and_lie_derivative_are_actual_graded_derivations() -> None:
    algebra = SymmetricAlgebraOn(QQ, ("x", "y"))
    x = algebra.algebra_generator("x")
    y = algebra.algebra_generator("y")
    values = ring_as_module(algebra)
    vector = VectorFields(algebra)(
        {
            "x": _scalar_module_element(values, algebra.one()),
            "y": values.zero(),
        }
    )
    de_rham = DeRhamAlgebra(algebra)
    X = de_rham.from_degree_zero(x)
    Y = de_rham.from_degree_zero(y)
    dx = de_rham.d(X)
    dy = de_rham.d(Y)

    contraction = InteriorProduct(vector)
    lie = LieDerivative(vector)

    assert contraction.degree_shift() == -1
    assert lie.degree_shift() == 0
    assert contraction(X) == de_rham.zero()
    assert contraction(dx) == de_rham.one()
    assert contraction(dy) == de_rham.zero()
    assert contraction(dx * dy) == dy
    assert lie(X) == de_rham.one()
    assert lie(Y) == de_rham.zero()
    assert lie(dx) == de_rham.zero()

    viewed_vector = vector_field_view(vector)
    viewed_dx = form_view(static_d(X))
    viewed_dy = form_view(static_d(Y))
    assert static_wedge(viewed_dx, viewed_dy) == dx * dy
    assert static_interior(viewed_vector, viewed_dx) == de_rham.one()
    assert static_lie_derivative(viewed_vector, X) == de_rham.one()


def test_cartan_commutator_identities_hold_on_the_de_rham_algebra() -> None:
    algebra = SymmetricAlgebraOn(QQ, ("x", "y"))
    x = algebra.algebra_generator("x")
    y = algebra.algebra_generator("y")
    values = ring_as_module(algebra)
    vector_fields = VectorFields(algebra)
    Xfield = vector_fields(
        {
            "x": _scalar_module_element(values, algebra.one()),
            "y": values.zero(),
        }
    )
    Yfield = vector_fields(
        {
            "x": values.zero(),
            "y": _scalar_module_element(values, x),
        }
    )
    bracket = LieBracket(Xfield, Yfield)

    de_rham = DeRhamAlgebra(algebra)
    X = de_rham.from_degree_zero(x)
    Y = de_rham.from_degree_zero(y)
    test_form = X * de_rham.d(Y) + de_rham.d(X) * de_rham.d(Y)

    iX = InteriorProduct(Xfield)
    iY = InteriorProduct(Yfield)
    LX = LieDerivative(Xfield)
    LY = LieDerivative(Yfield)
    iBracket = InteriorProduct(bracket)
    LBracket = LieDerivative(bracket)
    d = de_rham.differential()

    assert GradedCommutator(d, iX)(test_form) == LX(test_form)
    assert GradedCommutator(d, LX)(test_form) == de_rham.zero()
    assert GradedCommutator(LX, iY)(test_form) == iBracket(test_form)
    assert GradedCommutator(LX, LY)(test_form) == LBracket(test_form)
