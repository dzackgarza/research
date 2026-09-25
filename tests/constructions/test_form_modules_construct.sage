r"""Form modules retain their underlying modules, value module, and form morphism.

The hyperbolic plane gives a unimodular scalar-valued bilinear form with
isotropic basis vectors.  Its identity map is both a fixed-fibre formed morphism
and a fibrewise formed morphism over the identity of ``ZZ``.
"""

from dzack_research.preamble.all import *  # noqa: F401,F403


def _hyperbolic_form():
    return ZZ.free_module(2).equip_bilinear_form(ZZ, [[0, 1], [1, 0]])


def test_form_module_retains_unformed_left_right_and_value_modules() -> None:
    form = _hyperbolic_form()
    module = form.unformed_module()

    assert form in FormModules(ZZ)
    assert form.left_module() is module
    assert form.right_module() is module
    assert form.value_module() == ZZ.regular_module()
    assert form.form().codomain() == form.value_module()
    assert isinstance(form.module_generator(0), form.ElementType)


def test_form_pairing_norm_gram_and_element_predicates_have_hyperbolic_values() -> None:
    form = _hyperbolic_form()
    e, f = form.module_generator(0), form.module_generator(1)

    assert form.b(e, f) == form.pairing(e, f) == ZZ.one()
    assert form.norm(e) == form.q(e) == ZZ.zero()
    assert e.b(f) == ZZ.one()
    assert e.q() == ZZ.zero()
    assert e.is_isotropic()
    assert e.is_orthogonal_to(e)
    assert not e.is_orthogonal_to(f)
    assert e.represents(ZZ.zero())
    assert form.gram_tensor() == tensor(ZZ, (), (2, 2), [[0, 1], [1, 0]])


def test_form_index_raising_lowering_twist_and_fraction_field_raise() -> None:
    form = _hyperbolic_form()
    vector = tensor.vector(ZZ, [3, 7])
    covector = tensor.covector(ZZ, [3, 7])
    twisted = form.twist(3)
    rational = form.raise_index_over_fraction_field(covector)

    assert form.lower_index(vector) == tensor.covector(ZZ, [7, 3])
    assert form.raise_index(covector) == tensor.vector(ZZ, [7, 3])
    assert rational == tensor.vector(QQ, [QQ(7), QQ(3)])
    assert twisted.b(twisted.module_generator(0), twisted.module_generator(1)) == 3


def test_form_base_change_keeps_the_pairing_over_the_rationals() -> None:
    form = _hyperbolic_form()
    inclusion = ZZ.Mor(QQ)(lambda integer: QQ(integer))
    changed = form.base_change(inclusion)

    assert changed in FormModules(QQ)
    assert changed.b(changed.module_generator(0), changed.module_generator(1)) == QQ.one()


def test_fixed_and_fibered_formed_identity_morphisms_preserve_the_form() -> None:
    form = _hyperbolic_form()
    module = form.unformed_module()
    values = form.value_module()
    module_identity = Modules(ZZ).Mor(module, module).identity()
    value_identity = values.Mor(values).identity()
    fixed = form.formed_mor(module_identity, value_identity)
    fibered = form.fibered_formed_mor(
        form,
        ZZ.Mor(ZZ).identity(),
        module_identity,
        value_identity,
    )

    assert fixed in form.Mor(form)
    assert fibered.domain() is form
    assert fibered.codomain() is form
    assert fixed.preserves_form_exactly()
    assert fibered.preserves_form_exactly()
    assert form.Mono(form).identity().preserves_form_exactly()
