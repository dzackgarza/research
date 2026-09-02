from sage.all import exp, pi, sqrt
from sage.categories.map import Map
from sage.rings.infinity import Infinity


def _session():
    scope = {}
    exec("from dzack_research.preamble.all import *", scope)
    return scope


def test_lebesgue_spaces_form_a_graded_module_over_holder_degrees() -> None:
    session = _session()
    QQ = session["QQ"]
    RR = session["RR"]
    Lp = session["Lp"]
    Algebras = session["Algebras"]
    GradedModules = session["GradedModules"]
    GradedLebesgueModule = session["GradedLebesgueModule"]
    LebesgueGradedModules = session["LebesgueGradedModules"]
    NonNegativeReals = session["NonNegativeReals"]
    UnitInterval = session["UnitInterval"]

    holder = GradedLebesgueModule(NonNegativeReals)
    young = GradedLebesgueModule(UnitInterval)
    maps = session["C"](Infinity, RR)
    gaussian = Lp(2)(maps(exp(-(maps.indeterminate() ** 2))))

    assert holder in GradedModules(RR, NonNegativeReals)
    assert holder in LebesgueGradedModules(RR)
    assert young in GradedModules(RR, UnitInterval)
    assert holder.grading_monoid() is NonNegativeReals
    assert young.grading_monoid() is UnitInterval
    assert holder.graded_piece(NonNegativeReals.zero()) is Lp(Infinity)
    assert holder.graded_piece(~NonNegativeReals(2)) is Lp(2)
    assert holder.graded_piece(NonNegativeReals(2)) is Lp(QQ(1) / 2)
    assert young.graded_piece(UnitInterval.one()) is Lp(1)
    assert young.graded_piece(UnitInterval.zero()) is Lp(Infinity)
    assert young.graded_piece(UnitInterval(QQ(1) / 2)) is Lp(2)
    assert holder.graded_piece(NonNegativeReals(1)) is young.graded_piece(UnitInterval.one())
    assert holder not in Algebras(RR)
    try:
        holder(gaussian) * holder(gaussian)
    except TypeError:
        pass
    else:
        raise AssertionError("the graded module has no product")

    try:
        young(Lp(QQ(1) / 2).zero())
    except ValueError:
        pass
    else:
        raise AssertionError("expected L^{1/2} to be excluded from the Young-graded module")


def test_lebesgue_spaces_form_a_graded_algebra_under_pointwise_product() -> None:
    session = _session()
    C = session["C"]
    RR = session["RR"]
    Lp = session["Lp"]
    Algebras = session["Algebras"]
    AssociativeAlgebras = session["AssociativeAlgebras"]
    CommutativeAlgebras = session["CommutativeAlgebras"]
    GradedAlgebras = session["GradedAlgebras"]
    GradedModules = session["GradedModules"]
    GradedLebesgueAlgebra = session["GradedLebesgueAlgebra"]
    GradedLebesgueModule = session["GradedLebesgueModule"]
    GradedTensorProductModules = session["GradedTensorProductModules"]
    LebesgueGradedModules = session["LebesgueGradedModules"]
    NonNegativeReals = session["NonNegativeReals"]
    Pairings = session["Pairings"]
    AlgebrasWithChosenMultiplication = session["AlgebrasWithChosenMultiplication"]

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
    assert algebra in CommutativeAlgebras(RR)
    assert algebra in AlgebrasWithChosenMultiplication(RR)
    assert algebra in AssociativeAlgebras(RR)
    assert algebra in LebesgueGradedModules(RR)
    assert algebra.is_graded()
    assert algebra.grading_monoid() is NonNegativeReals
    assert algebra.graded_piece(algebra.grading_monoid().monoidal_unit()) is Lp(Infinity)
    assert algebra.graded_piece(half) is Lp(2)
    assert algebra.graded_piece(one) is Lp(1)
    assert algebra.one().homogeneous_component(algebra.grading_monoid().monoidal_unit()).parent() is Lp(
        Infinity
    )
    assert isinstance(multiplication, Map)
    assert multiplication.codomain() is algebra
    assert multiplication.domain() in GradedTensorProductModules(RR)
    assert multiplication.domain().tensor_factors() == (algebra, algebra)
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
    assert pairing.parent() is Pairings(algebra, algebra, RR)
    assert pairing(left, right) == Lp(2).b(gaussian, gaussian)
    assert epsilon(left) == RR.zero()
    assert epsilon(left) * epsilon(right) != epsilon(product)
    assert unit_projection.codomain() is Lp(Infinity)
    assert unit_projection(algebra.one()).expression() == Lp(Infinity).one().expression()
    constant_left = algebra(Lp(Infinity)(2))
    constant_right = algebra(Lp(Infinity)(3))
    assert unit_projection(constant_left * constant_right).expression() == Lp(Infinity)(6).expression()


def test_lebesgue_spaces_form_an_associative_algebra_under_convolution() -> None:
    session = _session()
    C = session["C"]
    QQ = session["QQ"]
    RR = session["RR"]
    Lp = session["Lp"]
    Algebras = session["Algebras"]
    AssociativeAlgebras = session["AssociativeAlgebras"]
    GradedAlgebras = session["GradedAlgebras"]
    GradedModules = session["GradedModules"]
    LebesgueConvolutionAlgebra = session["LebesgueConvolutionAlgebra"]
    GradedLebesgueModule = session["GradedLebesgueModule"]
    GradedTensorProductModules = session["GradedTensorProductModules"]
    LebesgueGradedModules = session["LebesgueGradedModules"]
    UnitInterval = session["UnitInterval"]
    AssociativeAlgebrasWithChosenMultiplication = session[
        "AssociativeAlgebrasWithChosenMultiplication"
    ]

    algebra = LebesgueConvolutionAlgebra
    maps = C(Infinity, RR)
    gaussian = Lp(2)(maps(exp(-(maps.indeterminate() ** 2))))
    left = algebra(gaussian)
    right = algebra(gaussian)
    product = left * right
    half = UnitInterval(QQ(1) / 2)
    multiplication = algebra.multiplication_morphism()
    epsilon = algebra.integral_form()
    pairing_morphism = algebra.integral_pairing_morphism()

    assert algebra is not GradedLebesgueModule(UnitInterval)
    assert algebra in AssociativeAlgebras(RR)
    assert algebra in AssociativeAlgebrasWithChosenMultiplication(RR)
    assert algebra in LebesgueGradedModules(RR)
    assert algebra not in Algebras(RR)
    assert algebra not in GradedAlgebras(RR, UnitInterval)
    assert algebra.is_graded()
    assert algebra.grading_monoid() is UnitInterval
    assert algebra.graded_piece(UnitInterval.one()) is Lp(1)
    assert algebra.graded_piece(UnitInterval.zero()) is Lp(Infinity)
    assert algebra.graded_piece(half) is Lp(2)
    assert algebra.combine_degrees(half, half) == UnitInterval.zero()
    assert algebra.combine_degrees(UnitInterval.one(), half) == half
    assert product.homogeneous_component(UnitInterval.zero()).parent() is Lp(Infinity)
    assert multiplication.domain() in GradedTensorProductModules(RR)
    assert product == multiplication(multiplication.domain().pure_tensor(left, right))
    assert pairing_morphism.domain() is multiplication.domain()
    assert pairing_morphism(
        multiplication.domain().pure_tensor(left, right)
    ) == epsilon(product)
    assert epsilon(product) == RR.zero()
    try:
        algebra.one()
    except AttributeError:
        pass
    else:
        raise AssertionError("convolution L^1(R) is non-unital")
    try:
        algebra.unit_piece_projection()
    except TypeError:
        pass
    else:
        raise AssertionError("convolution has no unit-piece augmentation")
