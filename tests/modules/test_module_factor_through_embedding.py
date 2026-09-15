r"""Any module morphism can factor through a represented module subobject."""

import pytest

from dzack_research.preamble.all import ZZ, BasedFreeModule, module_embedding, module_homset
from dzack_research.preamble.categories.sets import finite_ordered_set


def test_general_module_map_factors_through_embedding_by_lifting_generator_images() -> None:
    line = BasedFreeModule(ZZ, finite_ordered_set(("e",)))
    e = line.module_generator("e")
    doubled = module_embedding(line, line, {"e": 2 * e})
    sixfold = line.module_category().Mor(line, line)({"e": 6 * e})

    factor = sixfold.factor_through(doubled)

    assert factor.domain() is line
    assert factor.codomain() is line
    assert factor(e) == 3 * e
    assert doubled * factor == sixfold


def test_factorization_refuses_an_image_outside_the_target_subobject() -> None:
    line = BasedFreeModule(ZZ, finite_ordered_set(("e",)))
    e = line.module_generator("e")
    doubled = module_embedding(line, line, {"e": 2 * e})
    identity = line.module_category().Mor(line, line).identity()

    with pytest.raises(ValueError, match="not contained"):
        identity.factor_through(doubled)
