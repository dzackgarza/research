from sage.all import exp, pi, sqrt
from sage.rings.infinity import Infinity


def _session():
    scope = {}
    exec("from dzack_research.preamble.all import *", scope)
    return scope




def test_lebesgue_spaces_form_a_graded_algebra_under_pointwise_product() -> None:
    session = _session()
    C = session["C"]
    RR = session["RR"]
    Lp = session["Lp"]
    Algebras = session["Algebras"]
    GradedAlgebras = session["GradedAlgebras"]
    GradedModules = session["GradedModules"]
    GradedLebesgueAlgebra = session["GradedLebesgueAlgebra"]
    GradedLebesgueModule = session["GradedLebesgueModule"]
    from dzack_research.preamble.categories.modules.pure.modules import TensorProductModules
    LebesgueGradedModules = session["LebesgueGradedModules"]
    NonNegativeReals = session["NonNegativeReals"]

    algebra = GradedLebesgueAlgebra
    module = GradedLebesgueModule(NonNegativeReals)
    half = ~NonNegativeReals(2)
    one = NonNegativeReals(1)
    maps = C(Infinity, RR)
    gaussian = Lp(2)(maps(exp(-(maps.indeterminate() ** 2))))
    left = algebra(gaussian)
    right = algebra(gaussian)
    product = left * right
    multiplication = algebra.multiplication_morphism()
    projection = algebra.degree_projection(one)
    integration = algebra.integration_of_degree_one()
    epsilon = algebra.integral_form()
    pairing_morphism = algebra.integral_pairing_morphism()
    pairing = algebra.integral_pairing()
    unit_projection = algebra.unit_piece_projection()

    assert GradedAlgebras(RR, NonNegativeReals).is_subcategory(
        GradedModules(RR, NonNegativeReals)
    )
    assert algebra is not module
    assert algebra in GradedAlgebras(RR, NonNegativeReals)
    assert algebra in Algebras(RR)
    assert algebra in Algebras(RR).Associative().Unital().Commutative()
    assert algebra.unformed_module() is module
    assert algebra in Algebras(RR).Associative()
    assert algebra in LebesgueGradedModules(RR)
    assert algebra.is_graded()
    assert algebra.grading_monoid() is NonNegativeReals
    assert algebra.graded_piece(algebra.grading_monoid().monoidal_unit()) is Lp(Infinity)
    assert algebra.graded_piece(half) is Lp(2)
    assert algebra.graded_piece(one) is Lp(1)
    assert algebra.one().homogeneous_component(algebra.grading_monoid().monoidal_unit()).parent() is Lp(
        Infinity
    )
    assert multiplication in multiplication.domain().Mor(algebra)
    assert multiplication.codomain() is algebra
    assert multiplication.domain() in TensorProductModules(RR)
    assert product.homogeneous_component(one).parent() is Lp(1)
    assert product == multiplication(multiplication.domain().pure_tensor(left, right))
    assert epsilon.domain() is algebra
    assert epsilon.codomain() is RR
    assert projection.codomain() is Lp(1)
    assert integration.domain() is Lp(1)
    assert pairing_morphism.domain() is multiplication.domain()
    assert pairing_morphism.codomain() is RR
    assert pairing_morphism(
        multiplication.domain().pure_tensor(left, right)
    ) == Lp(2).b(gaussian, gaussian)
    assert pairing_morphism(
        multiplication.domain().pure_tensor(left, right)
    ) == RR(sqrt(pi / 2))
    assert pairing.parent() is algebra.pairings_with(algebra, RR)
    assert pairing(left, right) == Lp(2).b(gaussian, gaussian)
    assert epsilon(left) == RR.zero()
    assert epsilon(left) * epsilon(right) != epsilon(product)
    assert unit_projection.codomain() is Lp(Infinity)
    assert unit_projection(algebra.one()).expression() == Lp(Infinity).one().expression()
    constant_left = algebra(Lp(Infinity)(2))
    constant_right = algebra(Lp(Infinity)(3))
    assert unit_projection(constant_left * constant_right).expression() == Lp(Infinity)(6).expression()


def test_full_young_family_retains_the_gaussian_convolution_on_its_quotient_sum() -> None:
    from dzack_research.preamble.all import (
        Algebras, Lp, RR, UnitInterval, LebesgueConvolutionModule, LebesgueConvolution,
    )

    module = LebesgueConvolutionModule
    x = Lp(2).indeterminate()
    gaussian = Lp(2)(exp(-x**2))
    left = module(gaussian)
    product = module.convolution(left, left)
    half = UnitInterval(RR(1) / 2)
    pair = UnitInterval.degree_pairs()(lambda _: half)
    pairing = LebesgueConvolution[pair]
    target = Lp(Infinity).quotient_by_null_functions()
    expected = target(Lp(Infinity)(sqrt(pi / 2) * exp(-x**2 / 2)))
    assert module not in Algebras(RR)
    assert module.grading_index_set() is UnitInterval
    assert module.graded_piece(half) is Lp(2).quotient_by_null_functions()
    assert pairing.codomain() is target
    assert product.homogeneous_component(UnitInterval.zero()) == expected
    assert pairing(Lp(2).quotient_by_null_functions()(gaussian), Lp(2).quotient_by_null_functions()(gaussian)) == expected
    assert module.integral_form()(product) == RR.zero()


def test_l1_convolution_is_the_total_algebra_specialization_with_the_actual_module() -> None:
    from dzack_research.preamble.all import Algebras, Lp, RR, LebesgueConvolutionAlgebra

    algebra = LebesgueConvolutionAlgebra
    module = Lp(1).quotient_by_null_functions()
    x = Lp(1).indeterminate()
    gaussian = Lp(1)(exp(-x**2))
    element = algebra(gaussian)
    assert algebra.unformed_module() is module
    assert algebra in Algebras(RR).Associative().Commutative()
    assert algebra not in Algebras(RR).Unital()
    assert algebra.multiplication().domain().tensor_factor(0) is module
    assert algebra.multiplication().domain().tensor_factor(1) is module
    assert algebra.multiplication().codomain() is module
    assert (element * element) * element == element * (element * element)
    integral = algebra.integration_morphism()
    assert integral(element * element) == integral(element) * integral(element)


