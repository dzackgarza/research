r"""Any module morphism can factor through a represented module subobject."""


from dzack_research.preamble.all import ZZ
from dzack_research.preamble.categories.sets import finite_ordered_set


def test_general_module_map_factors_through_embedding_by_lifting_generator_images() -> None:
    line = ZZ.free_module(finite_ordered_set(("e",)))
    e = line.module_generator("e")
    doubled = line.Mono(line)({"e": 2 * e})
    assert doubled.parent() is line.Mono(line)
    sixfold = line.module_category().Mor(line, line)({"e": 6 * e})

    factor = sixfold.factor_through(doubled)

    assert factor.domain() is line
    assert factor.codomain() is line
    assert factor(e) == 3 * e
    assert doubled * factor == sixfold


