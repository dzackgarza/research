from dzack_research.preamble.all import QQ
from dzack_research.preamble.categories.algebras.algebras import (
    AlgebrasWithChosenFinitePresentation,
    Algebras,
)


def test_xy_equals_t_relative_presentation_and_special_fiber() -> None:
    parameter = QQ.polynomial_ring("t")
    t = parameter.algebra_generator("t")
    presentation = parameter.polynomial_ring(("x", "y"))
    x = presentation.algebra_generator("x")
    y = presentation.algebra_generator("y")
    family = (presentation).quotient_by_relations((x * y - t,))
    xbar = family.algebra_generator("x")
    ybar = family.algebra_generator("y")

    assert family.base_ring() is parameter
    assert family in Algebras(parameter).Associative().Unital().Commutative()
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






def test_number_field_algebra_uses_its_primitive_presentation_for_coproduct() -> None:
    from dzack_research.preamble.all import (
        FinitelyGeneratedFreeModules,
        IntegralDomains,
        QuadraticField,
    )
    from dzack_research.preamble.categories.algebras.algebras import (
        CommutativeAlgebraCoproducts,
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

    split = Algebras(QQ).Associative().Unital().Commutative().coproduct((gaussian, gaussian))
    assert split in CommutativeAlgebraCoproducts(QQ)
    assert split not in IntegralDomains()


