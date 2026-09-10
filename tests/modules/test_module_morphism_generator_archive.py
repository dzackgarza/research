r"""Archive reconciliation for module morphisms as generator-defined linear extensions."""

import pytest

from dzack_research.preamble.all import FinitelyPresentedModule, FreeModule, ZZ
from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
    module_homset,
)


def _zmod2():
    relations = FreeModule(ZZ, 1)
    generators = FreeModule(ZZ, 1)
    relation = module_homset(relations, generators)(
        {relations.module_generating_set()[0]: 2 * generators.module_generator(0)}
    )
    return FinitelyPresentedModule(relation)


def test_generator_assignment_is_retained_as_the_defining_set_morphism() -> None:
    module = _zmod2()
    label = module.module_generating_set()[0]
    generator = module.module_generator(label)
    homset = module_homset(module, module)
    morphism = homset({label: generator})
    defining = morphism.module_generator_morphism()

    assert module_homset(module, module) is homset
    assert morphism.parent() is homset
    assert defining.domain() is module.module_generating_set()
    assert defining.codomain() is module
    assert defining(label) == generator
    assert morphism(generator) == generator
    assert morphism(2 * generator) == module.zero()


def test_generator_assignment_must_kill_every_presented_relation() -> None:
    source = _zmod2()
    target = FreeModule(ZZ, 1)
    label = source.module_generating_set()[0]

    with pytest.raises(AssertionError, match="kill every relation"):
        module_homset(source, target)(
            {label: target.module_generator(0)}
        )
