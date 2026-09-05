from dzack_research.preamble.all import QQ
from dzack_research.preamble.categories.algebras.algebras import (
    AlgebrasWithChosenFinitePresentation,
    CommutativeAlgebraPushouts,
    CommutativeAlgebras,
    commutative_algebra_pushout,
)
from dzack_research.preamble.categories.algebras.free_algebras import (
    FinitelyPresentedAlgebra,
    PolynomialRing,
)


def test_xy_equals_t_relative_presentation_and_special_fiber() -> None:
    parameter = PolynomialRing(QQ, "t")
    t = parameter.algebra_generator("t")
    presentation = PolynomialRing(parameter, ("x", "y"))
    x = presentation.algebra_generator("x")
    y = presentation.algebra_generator("y")
    family = FinitelyPresentedAlgebra(presentation, (x * y - t,))
    xbar = family.algebra_generator("x")
    ybar = family.algebra_generator("y")

    assert family.base_ring() is parameter
    assert family in CommutativeAlgebras(parameter)
    assert family in AlgebrasWithChosenFinitePresentation(parameter)
    structure = family.algebra_structure_morphism()
    assert structure.domain() is parameter
    assert family(structure(t)) == xbar * ybar
    assert (
        family.algebra_presentation_morphism()(family.relations().value(0))
        == family.zero()
    )
    assert family.lift_to_presentation(xbar) == x
    assert family.lift_to_presentation(family(t)) == presentation(t)

    residue = parameter.Mor(QQ)({"t": QQ.zero()})
    special_fiber = family.base_change(residue)
    assert special_fiber.base_ring() is QQ
    assert special_fiber in AlgebrasWithChosenFinitePresentation(QQ)
    assert (
        special_fiber.algebra_generator("x")
        * special_fiber.algebra_generator("y")
        == special_fiber.zero()
    )
    fiber_presentation = special_fiber.presentation_ring()
    assert tuple(special_fiber.relations()) == (
        fiber_presentation.algebra_generator("x")
        * fiber_presentation.algebra_generator("y"),
    )


def test_pushout_accepts_maps_from_a_presented_source() -> None:
    source_presentation = PolynomialRing(QQ, "t")
    t = source_presentation.algebra_generator("t")
    source = FinitelyPresentedAlgebra(source_presentation, (t**2,))
    tbar = source.algebra_generator("t")

    target_presentation = PolynomialRing(QQ, "x")
    x = target_presentation.algebra_generator("x")
    target = FinitelyPresentedAlgebra(target_presentation, (x**2,))
    xbar = target.algebra_generator("x")

    left = source.Mor(source).identity()
    right = source.Mor(target)({"t": xbar})
    assert left.parent() is source.Mor(source)
    assert right.parent() is source.Mor(target)

    pushout = commutative_algebra_pushout(left, right)
    assert pushout in CommutativeAlgebraPushouts(QQ)
    left_pushout, right_pushout = pushout.pushout_maps()
    assert left_pushout(left(tbar)) == right_pushout(right(tbar))


def test_number_field_algebra_uses_its_primitive_presentation_for_coproduct() -> None:
    from dzack_research.preamble.all import (
        FinitelyGeneratedFreeModules,
        IntegralDomains,
        QuadraticField,
    )
    from dzack_research.preamble.categories.algebras.algebras import (
        CommutativeAlgebraCoproducts,
        commutative_algebra_coproduct,
    )

    field = QuadraticField(-1, "i")
    gaussian = field.as_algebra()
    primitive = gaussian.algebra_generator("i")

    assert gaussian is not field
    assert gaussian.base_ring() is QQ
    assert gaussian in AlgebrasWithChosenFinitePresentation(QQ)
    assert gaussian in FinitelyGeneratedFreeModules(QQ)
    assert tuple(gaussian.module_generators()) == (gaussian.one(), primitive)
    assert gaussian.algebra_presentation_morphism()(gaussian.relations().value(0)) == 0
    assert gaussian.lift_to_presentation(primitive) == gaussian.presentation_ring().algebra_generator("i")

    split = commutative_algebra_coproduct(gaussian, gaussian)
    assert split in CommutativeAlgebraCoproducts(QQ)
    assert split not in IntegralDomains()


def test_relative_number_field_algebra_uses_an_absolute_primitive_presentation() -> None:
    from dzack_research.preamble.all import (
        FinitelyGeneratedFreeModules,
        NumberField,
        QuadraticField,
    )

    base = QuadraticField(2, "a")
    relative_polynomials = PolynomialRing(base, "u")
    u = relative_polynomials.algebra_generator("u")
    field = NumberField(u**2 - base.primitive_element(), "b")
    algebra = field.as_algebra()
    primitive = algebra.algebra_generator("absolute_generator")

    assert algebra.base_ring() is QQ
    assert algebra in AlgebrasWithChosenFinitePresentation(QQ)
    assert algebra in FinitelyGeneratedFreeModules(QQ)
    assert algebra.number_of_module_generators() == field.degree()
    assert algebra.algebra_presentation_morphism()(algebra.relations().value(0)) == 0
    assert (
        algebra.lift_to_presentation(primitive)
        == algebra.presentation_ring().algebra_generator("absolute_generator")
    )
