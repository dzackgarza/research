from dzack_research.preamble.all import QQ










def test_scalar_killed_family_detects_nonflatness_over_the_same_dvr() -> None:
    polynomial = QQ.polynomial_ring(("t",))
    t = polynomial.algebra_generator("t")
    local = polynomial.localize_at_prime(polynomial.ideal(t))

    def killed_parameter(relative):
        return (relative.base_ring().localization_map()(t),)

    nonflat = local.affine_equation_family(("z",), killed_parameter)
    assert not nonflat.is_flat()
    assert nonflat.scheme_base_ring().residue_map().domain() is local
