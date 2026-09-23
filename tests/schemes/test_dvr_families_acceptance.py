from dzack_research.preamble.all import QQ


def _nodal_dvr_family():
    polynomial = QQ.polynomial_ring(("t",))
    t = polynomial.algebra_generator("t")
    local = polynomial.localize_at_prime(polynomial.ideal(t))

    def equation(relative):
        x = relative.algebra_generator("x")
        y = relative.algebra_generator("y")
        return (x * y - relative.base_ring().localization_map()(t),)

    return local.affine_equation_family(("x", "y"), equation)


def test_xy_equals_t_has_generic_special_and_completed_fibres_from_one_parameter_map() -> None:
    family = _nodal_dvr_family()
    generic = family.generic_fiber()
    special = family.special_fiber()
    completed = family.base_change_to_completion()

    assert generic.left_projection().codomain() is family
    assert special.left_projection().codomain() is family
    assert completed.left_projection().codomain() is family
    assert family.scheme_base_ring().adic_completion(family.scheme_base_ring().maximal_ideal()).completion_map().domain() is family.scheme_base_ring()
    assert family.scheme_base_ring().residue_map().domain() is family.scheme_base_ring()
    assert family.scheme_base_ring().fraction_field_map().domain() is family.scheme_base_ring()


def test_direct_and_completion_first_special_fibres_are_compared_by_actual_maps() -> None:
    family = _nodal_dvr_family()
    comparison = family.special_fiber_comparison()
    direct = comparison.codomain()
    completed = comparison.domain()

    assert comparison.forward().domain() is completed
    assert comparison.forward().codomain() is direct
    assert comparison.inverse().domain() is direct
    assert comparison.inverse().codomain() is completed
    assert comparison.forward() * comparison.inverse() == direct.categorical_identity_morphism()
    assert comparison.inverse() * comparison.forward() == completed.categorical_identity_morphism()


def test_completion_precision_does_not_enter_the_exact_special_parameter_map() -> None:
    family = _nodal_dvr_family()
    residue = family.scheme_base_ring().residue_map()
    completion = family.scheme_base_ring().adic_completion(family.scheme_base_ring().maximal_ideal())

    assert completion.source_residue_map() == residue
    assert completion.computation_precision() > 0


def test_scalar_killed_family_detects_nonflatness_over_the_same_dvr() -> None:
    polynomial = QQ.polynomial_ring(("t",))
    t = polynomial.algebra_generator("t")
    local = polynomial.localize_at_prime(polynomial.ideal(t))

    def killed_parameter(relative):
        return (relative.base_ring().localization_map()(t),)

    nonflat = local.affine_equation_family(("z",), killed_parameter)
    assert not nonflat.is_flat()
    assert nonflat.scheme_base_ring().residue_map().domain() is local
