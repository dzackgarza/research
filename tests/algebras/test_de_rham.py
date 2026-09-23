from dzack_research.preamble.all import QQ, ZZ
from dzack_research.preamble.categories.algebras import (
    Algebras,
    DifferentialGradedAlgebras,
    GradedCommutativeAlgebras,
    StrictlyCommutativeDifferentialGradedAlgebras,
    StrictlyGradedCommutativeAlgebras,
)
from dzack_research.preamble.categories.algebras.algebras import Algebras
from dzack_research.preamble.categories.modules import (
    Modules,
    ModuleSubobjects,
)
from dzack_research.preamble.categories.sets import finite_ordered_set


def test_exterior_algebra_lands_in_strict_graded_commutative_algebras() -> None:
    module = ZZ.free_module(finite_ordered_set(("e", "f")))
    exterior = module.exterior_algebra()

    assert exterior in StrictlyGradedCommutativeAlgebras(ZZ)
    assert exterior in GradedCommutativeAlgebras(ZZ)
    e = exterior.algebra_generator("e")
    f = exterior.algebra_generator("f")
    assert e * e == exterior.zero()
    assert e * f == -(f * e)


def test_kahler_differentials_use_the_jacobian_relation_and_universal_property() -> None:
    polynomial = QQ.free_module(("x", "y")).symmetric_algebra()
    x = polynomial.algebra_generator("x")
    y = polynomial.algebra_generator("y")
    algebra = (polynomial).quotient_by_relations([x * y])
    xbar = algebra.algebra_generator("x")
    ybar = algebra.algebra_generator("y")

    omega = algebra.kahler_differentials()
    dx = omega.differential_generator("x")
    dy = omega.differential_generator("y")
    universal = omega.universal_derivation()

    assert ybar * dx + xbar * dy == omega.zero()
    assert universal(xbar * ybar) == omega.zero()

    values = algebra.regular_module()
    derivation = algebra.derivations(values)(
        {
            "x": values.scalar_multiple(xbar, values.module_generator(0)),
            "y": values.scalar_multiple(-ybar, values.module_generator(0)),
        }
    )
    classifier = omega.from_derivation(derivation)
    assert classifier(universal(xbar + ybar)) == derivation(xbar + ybar)

    derivations = derivation.parent()
    representing = omega.derivation_classifier_isomorphism(values)
    assert representing.domain() is omega.module_category().Mor(omega, values)
    assert representing.codomain() is derivations
    assert representing in Modules(algebra).Iso(representing.domain(), derivations)
    represented_derivation = representing(classifier)
    represented_classifier = representing.inverse()(derivation)
    assert represented_derivation(xbar + ybar) == derivation(xbar + ybar)
    assert represented_classifier(universal(xbar + ybar)) == derivation(xbar + ybar)

    module_morphisms = derivations.arrow_set()
    restricted_derivations = derivations.restricted_module()
    underlying = derivations.inclusion()(restricted_derivations(derivation))
    assert derivations in Modules(algebra)
    assert restricted_derivations in ModuleSubobjects(QQ)
    assert derivations.inclusion().domain() is restricted_derivations
    assert derivations.inclusion().codomain() is module_morphisms
    assert module_morphisms is Modules(QQ).Mor(
        algebra, derivations.restricted_target_module()
    )
    assert underlying.parent() is module_morphisms
    assert underlying(xbar).underlying_element() == derivation(xbar)
    action = derivations.algebra_action()
    assert action.domain() is algebra
    assert action.codomain() is Modules(algebra).End(derivations)
    assert action(xbar)(derivation)(xbar) == values.scalar_multiple(
        xbar,
        derivation(xbar),
    )


def test_relative_conormal_and_tangent_comparison_for_xy_equals_t() -> None:

    parameter = QQ.polynomial_ring("t")
    t = parameter.algebra_generator("t")
    presentation = parameter.polynomial_ring(("x", "y"))
    x = presentation.algebra_generator("x")
    y = presentation.algebra_generator("y")
    algebra = (presentation).quotient_by_relations((x * y - t,))
    xbar = algebra.algebra_generator("x")
    ybar = algebra.algebra_generator("y")

    omega = algebra.kahler_differentials()
    conormal = omega.conormal_module()
    conormal_map = omega.conormal_morphism()
    relation_label = next(iter(conormal.module_generating_set()))
    relation = conormal.module_generator(relation_label)

    assert conormal_map.domain() is conormal
    assert conormal_map.codomain() is omega.ambient_differentials()
    assert conormal_map(relation) == (
        ybar * omega.ambient_differentials().module_generator(("d", "x"))
        + xbar * omega.ambient_differentials().module_generator(("d", "y"))
    )
    assert omega.differential_projection()(conormal_map(relation)) == omega.zero()
    assert omega.fitting_ideal(1) == algebra.ideal(xbar, ybar)

    spectrum = algebra.spectrum()
    origin = spectrum(algebra.ideal(xbar, ybar))
    smooth_point = spectrum(algebra.ideal(xbar - algebra.one(), ybar))

    origin_cotangent = omega.cotangent_space(origin)
    smooth_cotangent = omega.cotangent_space(smooth_point)
    assert origin_cotangent.dimension() == 2
    assert smooth_cotangent.dimension() == 1
    assert omega.tangent_dimension(origin) == 2
    assert omega.tangent_dimension(smooth_point) == 1
    assert omega.tangent_space(origin).source_module() is origin_cotangent
    assert omega.tangent_space(smooth_point).source_module() is smooth_cotangent

    origin_conormal = omega.conormal_morphism_at(origin)
    smooth_conormal = omega.conormal_morphism_at(smooth_point)
    assert origin_conormal(origin_conormal.domain().module_generator(relation_label)).is_zero()
    assert not smooth_conormal(
        smooth_conormal.domain().module_generator(relation_label)
    ).is_zero()


def test_de_rham_algebra_is_the_existing_exterior_algebra_with_differential_constants() -> None:
    algebra = QQ.free_module(("x", "y")).symmetric_algebra()
    x = algebra.algebra_generator("x")
    y = algebra.algebra_generator("y")
    de_rham = algebra.de_rham_algebra()

    assert de_rham in StrictlyCommutativeDifferentialGradedAlgebras(QQ)
    assert de_rham.degree_zero_algebra() is algebra
    assert de_rham.extension_algebra() is de_rham.kahler_differentials().exterior_algebra()
    assert de_rham.differential().graded_leibniz_decision() is True
    assert de_rham.differential().square_zero_decision() is True

    X = de_rham.from_degree_zero(x)
    Y = de_rham.from_degree_zero(y)
    dX = de_rham.d(X)

    assert de_rham.d(dX) == de_rham.zero()
    assert de_rham.d(X * Y) == dX * Y + X * de_rham.d(Y)
    assert dX * dX == de_rham.zero()

    degree_zero_d = de_rham.differential_component(0)
    degree_zero_component = X.homogeneous_component(0)
    assert degree_zero_d(degree_zero_component) == dX.homogeneous_component(1)


def test_de_rham_differential_descends_through_a_singular_quotient() -> None:
    polynomial = QQ.free_module(("x", "y")).symmetric_algebra()
    x = polynomial.algebra_generator("x")
    y = polynomial.algebra_generator("y")
    algebra = (polynomial).quotient_by_relations([x * y])
    de_rham = algebra.de_rham_algebra()
    X = de_rham.from_degree_zero(algebra.algebra_generator("x"))
    Y = de_rham.from_degree_zero(algebra.algebra_generator("y"))

    assert X * Y == de_rham.zero()
    assert de_rham.d(X * Y) == de_rham.zero()
    assert de_rham.d(X) * Y + X * de_rham.d(Y) == de_rham.zero()


def test_dual_numbers_use_generic_de_rham_cohomology() -> None:
    polynomial = QQ.free_module(("x",)).symmetric_algebra()
    x = polynomial.algebra_generator("x")
    algebra = (polynomial).quotient_by_relations([x**2])
    xbar = algebra.algebra_generator("x")

    omega = algebra.kahler_differentials()
    dx = omega.differential_generator("x")
    assert omega.scalar_multiple(2 * xbar, dx) == omega.zero()
    assert omega.universal_derivation()(xbar**2) == omega.zero()

    de_rham = algebra.de_rham_algebra()
    assert de_rham.cohomology(0).module_rank() == 1
    assert de_rham.cohomology(1).is_zero()


def test_kahler_differentials_and_universal_derivation_commute_with_localization() -> None:
    from dzack_research.preamble.categories.algebras import (
        KahlerDifferentialModules,
    )
    from dzack_research.preamble.categories.modules.localizations import (
        LocalizedModules,
    )

    polynomial = QQ.free_module(("x", "y")).symmetric_algebra()
    x = polynomial.algebra_generator("x")
    y = polynomial.algebra_generator("y")
    axes = (polynomial).quotient_by_relations([x * y])
    xbar = axes.algebra_generator("x")
    ybar = axes.algebra_generator("y")
    localized = axes.localization(xbar)

    omega = axes.kahler_differentials()
    localized_omega = localized.kahler_differentials()
    assert localized_omega in KahlerDifferentialModules(localized)
    assert localized_omega in LocalizedModules(localized)
    assert localized_omega.localization_source_module() is omega
    assert localized_omega.source_algebra() is localized

    universal = localized_omega.universal_derivation()
    assert universal.domain() is localized
    assert universal.codomain() is localized_omega

    dx = localized_omega.differential_generator("x")
    inverse_x = localized.fraction(axes.one(), xbar)
    assert universal(localized(ybar)) == localized_omega.zero()
    assert universal(inverse_x) == localized_omega.scalar_multiple(
        -(inverse_x * inverse_x),
        dx,
    )
    assert universal(localized(xbar) * inverse_x) == localized_omega.zero()

    # Fitting ideals use the same selected base-change model.  Since x is
    # invertible on D(x), Fitt_1(Omega)_x=(x,y)A_x is the unit ideal.
    localized_fitting = localized_omega.fitting_ideal(1)
    assert localized_fitting.contraction() == axes.ideal(axes.one())
    assert localized_fitting.contains_ambient_element(localized.one())


def test_de_rham_functor_sends_f_to_f_and_df_to_d_of_f() -> None:
    source = QQ.free_module(("x",)).symmetric_algebra()
    target = QQ.free_module(("t",)).symmetric_algebra()
    x = source.algebra_generator("x")
    t = target.algebra_generator("t")
    morphism = Algebras(source.base_ring()).Associative().Unital().Mor(source, target)({"x": t**2})

    functor = Algebras(QQ).Associative().Unital().Commutative().de_rham()
    source_dr = functor(source)
    target_dr = functor(target)
    mapped = functor(morphism)
    X = source_dr.from_degree_zero(x)
    T2 = target_dr.from_degree_zero(t**2)

    assert mapped(X) == T2
    assert mapped(source_dr.d(X)) == target_dr.d(T2)


def test_de_rham_degree_zero_adjunction_mor_bijection_and_triangles() -> None:
    source = QQ.free_module(("x",)).symmetric_algebra()
    degree_zero = QQ.free_module(("t",)).symmetric_algebra()
    x = source.algebra_generator("x")
    t = degree_zero.algebra_generator("t")
    adjunction = Algebras(QQ).Associative().Unital().Commutative().de_rham_adjunction()
    assert adjunction.left_adjoint() is Algebras(QQ).Associative().Unital().Commutative().de_rham()
    assert adjunction.right_adjoint() is DifferentialGradedAlgebras(QQ).degree_zero_algebra()
    target = adjunction.left_adjoint()(degree_zero)
    algebra_map = Algebras(source.base_ring()).Associative().Unital().Mor(source, degree_zero)({"x": t**2})

    transpose = adjunction.mor_set_isomorphism_inverse(
        algebra_map,
        codomain=target,
    )
    recovered = adjunction.mor_set_isomorphism_forward(transpose, source)
    source_dr = adjunction.left_adjoint()(source)

    assert recovered(x) == algebra_map(x)
    assert transpose(source_dr.d(source_dr.from_degree_zero(x))) == target.d(
        target.from_degree_zero(t**2)
    )

    unit = adjunction.unit(source)
    left_triangle = adjunction.counit(source_dr) * adjunction.left_adjoint()(unit)
    X = source_dr.from_degree_zero(x)
    assert left_triangle(X) == X
    assert left_triangle(source_dr.d(X)) == source_dr.d(X)

    right_triangle = (
        adjunction.right_adjoint()(adjunction.counit(target))
        * adjunction.unit(degree_zero)
    )
    assert right_triangle(t) == t


def test_de_rham_constructs_restricted_pieces_and_product_before_exposing_the_dga() -> None:
    algebra = QQ.polynomial_ring(("x", "y"))
    de_rham = algebra.de_rham_algebra()
    module = de_rham.unformed_module()
    exterior = de_rham.extension_algebra()
    assert module is not de_rham
    assert module not in Algebras(QQ)
    assert module.graded_piece(1).module_over_extension() is exterior.graded_piece(1)
    assert module.graded_piece(1) is de_rham.graded_piece(1)
    x = de_rham.from_degree_zero(algebra.algebra_generator("x"))
    dx = de_rham.d(x)
    multiplication = de_rham.multiplication()
    assert multiplication.codomain() is module
    assert multiplication.domain().tensor_factor(0) is module
    assert multiplication.domain().tensor_factor(1) is module
    assert de_rham(multiplication(module(x), module(dx))) == x * dx
    assert de_rham.one() * dx == dx
    assert de_rham.d(de_rham.d(x)) == de_rham.zero()
    assert module.projection(1)(module(dx)) == dx.homogeneous_component(1)


def test_restriction_does_not_invent_exterior_identities_on_a_tensor_algebra() -> None:
    from dzack_research.preamble.all import GradedAlgebras, OwnedRings

    source = QQ.free_module(finite_ordered_set(("x", "y"))).tensor_algebra()
    restricted = source.restrict_scalars(OwnedRings().Mor(QQ, QQ).identity())
    x = restricted.from_realization(source.algebra_generator("x"))
    y = restricted.from_realization(source.algebra_generator("y"))
    assert restricted.realize(x * y) == source.algebra_generator("x") * source.algebra_generator("y")
    assert restricted.realize(x * x) != source.zero()
    assert restricted not in GradedAlgebras(QQ).Supercommutative().Alternating()
    assert restricted.unformed_module() is not restricted
