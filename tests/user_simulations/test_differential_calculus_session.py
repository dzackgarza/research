r"""A session in algebraic differential calculus on affine space.

Vector fields, differential forms, the exterior derivative, interior
products and Lie derivatives with the Cartan formula, connections and
their curvature, and de Rham cohomology of affine space and of the
punctured plane, over several fields.
"""

import pytest
from sage.misc.latex import latex

from dzack_research.preamble.all import *  # noqa: F401,F403


def rendered(obj) -> str:
    text = repr(obj)
    assert "object at 0x" not in text
    assert "object at 0x" not in latex(obj)
    return text


FIELDS = {"QQ": lambda: QQ, "QQ(i)": lambda: QuadraticField(-1, "i"), "GF(5)": lambda: GF(5), "GF(7)": lambda: GF(7)}


@pytest.mark.parametrize("name", sorted(FIELDS))
@pytest.mark.parametrize("dimension", [2, 3])
def test_a_differential_calculus_session(name, dimension) -> None:
    field = FIELDS[name]()
    names = ("x", "y", "z")[:dimension]
    algebra = PolynomialRing(field, names)
    rendered(algebra)
    coordinates = [algebra.algebra_generator(label) for label in names]
    x, y = coordinates[0], coordinates[1]

    # Differential forms and the exterior derivative.
    omega = KahlerDifferentials(algebra)
    de_rham = DeRhamAlgebra(algebra)
    rendered(omega)
    rendered(de_rham)
    assert omega.rank() == dimension
    assert de_rham in StrictlyCommutativeDifferentialGradedAlgebras(field)
    d = de_rham.differential()
    differentials = [de_rham(omega.differential_generator(label)) for label in names]
    dx, dy = differentials[0], differentials[1]
    assert d(de_rham(x * y)) == de_rham(y) * dx + de_rham(x) * dy
    assert d(d(de_rham(x**2 * y))) == de_rham.zero()
    assert dx * dy == -(dy * dx)
    assert dx * dx == de_rham.zero()
    top = differentials[0]
    for form in differentials[1:]:
        top = top * form
    assert top != de_rham.zero()
    assert top * dx == de_rham.zero()
    assert de_rham.graded_piece(dimension).rank() == 1
    assert de_rham.graded_piece(dimension + 1).rank() == 0
    for degree in range(dimension + 1):
        rendered(de_rham.graded_piece(degree))

    # Vector fields, brackets, interior products, Lie derivatives, Cartan's formula.
    values = algebra.regular_module()
    vector_fields = VectorFields(algebra)
    rendered(vector_fields)

    def field_of(**components):
        return vector_fields({label: values.scalar_multiple(components.get(label, algebra.zero()), values.module_generator(0)) for label in names})

    d_dx = field_of(x=algebra.one())
    d_dy = field_of(y=algebra.one())
    euler = field_of(**{label: coordinate for label, coordinate in zip(names, coordinates)})
    rotation = field_of(x=-y, y=x)
    rendered(euler)
    assert d_dx(x) == algebra.one()
    assert euler(x * y) == 2 * x * y
    assert LieBracket(d_dx, d_dy)(x * y) == algebra.zero()
    assert LieBracket(d_dx, euler)(x) == algebra.one()
    assert LieBracket(rotation, euler)(x) == algebra.zero()
    assert Derivations(algebra, values).rank() == dimension
    assert InteriorProduct(d_dx)(dx) == de_rham.one()
    assert InteriorProduct(rotation)(dx) == de_rham(-y)
    assert InteriorProduct(euler)(dx * dy) == de_rham(x) * dy - de_rham(y) * dx
    assert LieDerivative(euler)(dx) == dx
    assert LieDerivative(euler)(dx * dy) == 2 * dx * dy
    assert LieDerivative(rotation)(dx * dy) == de_rham.zero()
    one_form = de_rham(x) * dy
    for vector_field in (d_dx, euler, rotation):
        cartan = d(InteriorProduct(vector_field)(one_form)) + InteriorProduct(vector_field)(d(one_form))
        assert LieDerivative(vector_field)(one_form) == cartan

    # A connection on a line bundle and its curvature.
    line_bundle = FreeModule(algebra, 1)
    connections = Connections(line_bundle)
    target = connections.target_module()
    section = line_bundle.module_generator(0)
    flat = connections(lambda label: target.pure_tensor(section, omega.differential_generator("x")))
    curved = connections(lambda label: target.pure_tensor(section, omega.scalar_multiple(x, omega.differential_generator("y"))))
    rendered(flat)
    rendered(curved)
    assert flat.is_flat()
    assert not curved.is_flat()
    assert ModuleWithConnection(flat) in ModulesWithFlatConnection(algebra)
    assert ModuleWithConnection(curved) not in ModulesWithFlatConnection(algebra)

    # De Rham cohomology of affine space and of the punctured plane.
    for degree in range(dimension + 1):
        rendered(de_rham.cohomology(degree))
    assert de_rham.cohomology(0).rank() == 1
    if field.characteristic() == 0:
        for degree in range(1, dimension + 1):
            assert de_rham.cohomology(degree).cardinality() == 1
        punctured = DeRhamAlgebra(LaurentPolynomialRing(field, names))
        rendered(punctured)
        assert punctured.cohomology(0).rank() == 1
        assert punctured.cohomology(1).rank() == dimension
        assert punctured.cohomology(dimension).rank() == 1
    else:
        assert de_rham.cohomology(1).rank() >= 1
