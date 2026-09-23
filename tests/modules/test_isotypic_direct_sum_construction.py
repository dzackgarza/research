
from dzack_research.preamble.all import Groups, Modules, QQ
from dzack_research.preamble.categories.sets import finite_ordered_set


def test_isotypic_decomposition_derives_its_direct_sum_family_from_components() -> None:
    group = Groups.C(2)
    module = QQ.free_module(finite_ordered_set(("plus", "minus")))
    plus = module.module_generator("plus")
    minus = module.module_generator("minus")
    involution = module.Mor(module)({"plus": plus, "minus": -minus})

    acted = Modules(QQ[group])(
        module,
        lambda element, vector: vector if element == group.one() else involution(vector),
    )
    decomposition = acted.isotypic_decomposition()

    assert decomposition.number_of_summands() == 2
    assert decomposition.summand_index_set() == decomposition.isotypic_characters()
    for character in decomposition.isotypic_characters():
        assert decomposition.summand(character) is decomposition.isotypic_component(character)


