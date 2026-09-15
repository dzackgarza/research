from dzack_research.preamble.all import ZZ
from dzack_research.preamble.categories.forms.forms import BilinearForms


def _double_map(module):
    label = module.module_generating_set()[0]
    generator = module.module_generator(label)
    return module.module_category().Mor(module, module)({label: 2 * generator})


def test_bilinear_form_descends_through_mod_two_with_projected_values() -> None:
    integers = ZZ.regular_module()
    relation = _double_map(integers)
    value_projection = relation.cokernel_projection()
    form = BilinearForms(integers, integers)([[ZZ.one()]])

    assert form.descends_along(relation, value_projection)
    descended = form.descend_along(relation, value_projection)
    quotient = relation.cokernel()
    generator = quotient.module_generator(quotient.module_generating_set()[0])

    assert descended.module() is quotient
    assert descended.codomain() is value_projection.codomain()
    assert descended(generator, generator) == value_projection(
        integers.module_generator(integers.module_generating_set()[0])
    )


def test_bilinear_form_refuses_descent_when_a_relation_pairs_nontrivially() -> None:
    integers = ZZ.regular_module()
    relation = _double_map(integers)
    identity_values = integers.module_category().Mor(integers, integers).identity()
    form = BilinearForms(integers, integers)([[ZZ.one()]])

    assert not form.descends_along(relation, identity_values)
