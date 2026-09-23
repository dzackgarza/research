r"""Supported singularity equivalences and the regular/smooth boundary."""

from dzack_research.preamble.all import (
    Algebras,
    GF,
    QQ,
)
from dzack_research.preamble.categories.schemes.singularities import (
    IsolatedHypersurfaceSingularity,
)


def test_a_sheared_A2_is_classified_by_its_actual_coordinate_change() -> None:
    plane = QQ.polynomial_ring(("x", "y"))
    x, y = tuple(plane.algebra_generators())
    sheared = IsolatedHypersurfaceSingularity(
        plane,
        (x - y) ** 2 + y**3,
    )

    assert sheared.ade_normal_form_type() is None
    equivalence = sheared.ade_type_via_linear_right_equivalence(
        {"x": x + y, "y": y},
        {"x": x - y, "y": y},
    )

    assert equivalence is not None
    assert equivalence.parent() is Algebras(QQ).Associative().Unital().Core().Mor(plane, plane)
    assert equivalence.coordinate_change() is equivalence.forward()
    assert equivalence.ade_type() == ("A", 2)
    assert equivalence.forward()(sheared.equation()) == equivalence.target().equation()
    for generator in plane.algebra_generators():
        assert equivalence.inverse()(equivalence.forward()(generator)) == generator


def test_equal_milnor_and_tjurina_numbers_do_not_classify_plane_curve_germs() -> None:
    plane = QQ.polynomial_ring(("x", "y"))
    x, y = tuple(plane.algebra_generators())
    a4 = IsolatedHypersurfaceSingularity(plane, x**2 + y**5)
    triple = IsolatedHypersurfaceSingularity(plane, x * y * (x - y))

    assert a4.milnor_number() == triple.milnor_number() == 4
    assert a4.tjurina_number() == triple.tjurina_number() == 4
    assert a4.number_of_branches_at_origin() == 1
    assert triple.number_of_branches_at_origin() == 3


def test_regular_purely_inseparable_field_extension_is_not_smooth_over_its_base() -> None:
    prime_field = GF(2)
    parameters = prime_field.polynomial_ring(("a",))
    a = parameters.algebra_generator("a")
    base = parameters.fraction_field()
    a_in_base = parameters.fraction_field_map()(a)
    line = base.polynomial_ring(("x",))
    x = line.algebra_generator("x")
    extension = (line).quotient_by_relations((x**2 - a_in_base,))

    assert extension.is_field()
    scheme = (extension).affine_spectrum(base_ring=base)
    generic = scheme.underlying_space().generic_point()
    assert scheme.is_regular_at(generic)

    nonsmooth = scheme.singular_subscheme()
    assert nonsmooth.inclusion().codomain() is scheme
    assert nonsmooth.defining_ideal_owned() == extension.ideal(extension.zero())
