from dzack_research.preamble.all import QQ
from dzack_research.preamble.categories.algebras.free_algebras import PolynomialRing
from dzack_research.preamble.categories.schemes.families import affine_equation_family


def _nodal_dvr_family():
    polynomial = PolynomialRing(QQ, ("t",))
    t = polynomial.algebra_generator("t")
    local = polynomial.localize_at_prime(polynomial.ideal(t))

    def equation(relative):
        x = relative.algebra_generator("x")
        y = relative.algebra_generator("y")
        return (x * y - relative.base_ring().localization_map()(t),)

    return affine_equation_family(local, ("x", "y"), equation).as_dvr_family()


def test_xy_equals_t_has_generic_special_and_completed_fibres_from_one_parameter_map() -> None:
    family = _nodal_dvr_family()
    generic = family.generic_fiber()
    special = family.special_fiber()
    completed = family.completed_total_space()

    assert generic.left_projection().codomain() is family.family().total_space()
    assert special.left_projection().codomain() is family.family().total_space()
    assert completed.left_projection().codomain() is family.family().total_space()
    assert family.completion_parameter_map().domain() is family.parameter_algebra()
    assert family.special_parameter_map().domain() is family.parameter_algebra()
    assert family.generic_parameter_map().domain() is family.parameter_algebra()


def test_direct_and_completion_first_special_fibres_are_compared_by_actual_maps() -> None:
    family = _nodal_dvr_family()
    comparison = family.special_fiber_comparison()
    direct = comparison.direct_special_fiber()
    completed = comparison.completed_special_fiber()

    assert comparison.forward().domain() is completed
    assert comparison.forward().codomain() is direct
    assert comparison.inverse().domain() is direct
    assert comparison.inverse().codomain() is completed
    assert comparison.forward() * comparison.inverse() == direct.categorical_identity_morphism()
    assert comparison.inverse() * comparison.forward() == completed.categorical_identity_morphism()


def test_completion_precision_does_not_enter_the_exact_special_parameter_map() -> None:
    family = _nodal_dvr_family()
    residue = family.special_parameter_map()
    completion = family.completion()

    assert completion.source_residue_map() == residue
    assert completion.computation_precision() > 0


def test_scalar_killed_family_detects_nonflatness_over_the_same_dvr() -> None:
    polynomial = PolynomialRing(QQ, ("t",))
    t = polynomial.algebra_generator("t")
    local = polynomial.localize_at_prime(polynomial.ideal(t))

    def killed_parameter(relative):
        return (relative.base_ring().localization_map()(t),)

    nonflat = affine_equation_family(local, ("z",), killed_parameter).as_dvr_family()
    assert not nonflat.family().is_flat()
    assert nonflat.special_parameter_map().domain() is local
