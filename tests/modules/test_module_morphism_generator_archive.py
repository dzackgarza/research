r"""Archive reconciliation for module morphisms as generator-defined linear extensions."""

import pytest

from dzack_research.preamble.all import ZZ


def _zmod2():
    relations = ZZ.free_module(1)
    generators = ZZ.free_module(1)
    relation = relations.module_category().Mor(relations, generators)(
        {relations.module_generating_set()[0]: 2 * generators.module_generator(0)}
    )
    return relation.cokernel()


def test_generator_assignment_is_retained_as_the_defining_set_morphism() -> None:
    module = _zmod2()
    label = module.module_generating_set()[0]
    generator = module.module_generator(label)
    mor = module.module_category().Mor(module, module)
    morphism = mor({label: generator})
    defining = morphism.module_generator_morphism()

    assert module.module_category().Mor(module, module) is mor
    assert morphism.parent() is mor
    assert defining.domain() is module.module_generating_set()
    assert defining.codomain() is module
    assert defining(label) == generator
    assert morphism(generator) == generator
    assert morphism(2 * generator) == module.zero()


def test_generator_assignment_must_kill_every_presented_relation() -> None:
    source = _zmod2()
    target = ZZ.free_module(1)
    label = source.module_generating_set()[0]

    with pytest.raises(AssertionError, match="kill every relation"):
        source.module_category().Mor(source, target)(
            {label: target.module_generator(0)}
        )
