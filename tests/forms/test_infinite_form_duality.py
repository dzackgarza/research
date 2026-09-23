from dzack_research.preamble.all import NN, QQ, FormModules


def _countable_diagonal_form():
    module = QQ.free_module(NN)
    form = module.bilinear_forms(QQ)(
        lambda pair: QQ(
            1 if pair.component(0) == pair.component(1) else 0
        )
    )
    return FormModules(QQ)(form)


def test_countable_free_form_correlates_into_the_full_algebraic_dual() -> None:
    formed = _countable_diagonal_form()
    dual = formed.dual_module()
    correlation = formed.algebraic_correlation_morphism()
    e0 = formed.module_generator(0)
    e1 = formed.module_generator(1)

    assert dual is formed.module_category().Mor(formed, QQ.regular_module())
    assert correlation.domain() is formed
    assert correlation.codomain() is dual
    first_covector = correlation(e0)
    assert first_covector(e0) == 1
    assert first_covector(e1) == 0

    all_ones = dual(lambda _label: QQ.regular_module()(1))
    assert all_ones(e0) == all_ones(e1) == 1


def test_finite_perfect_form_retains_an_actual_correlation_inverse() -> None:
    module = QQ.free_module(2)
    formed = module.equip_bilinear_form(QQ, [[0, 1], [1, 0]])
    correlation = formed.correlation_isomorphism()

    for generator in formed.module_generators():
        assert correlation.inverse()(correlation.forward()(generator)) == generator
    for functional in correlation.forward().codomain().module_generators():
        assert correlation.forward()(correlation.inverse()(functional)) == functional
