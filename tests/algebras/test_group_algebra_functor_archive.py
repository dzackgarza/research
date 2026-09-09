r"""Archive reconciliation for the group-ring and underlying-module functors."""

from dzack_research.preamble.all import Groups, ZZ, group_homset
from dzack_research.preamble.categories.algebras.group_algebras import (
    FreeModuleOnGroupFunctor,
    GroupAlgebraFunctor,
    GroupAlgebraUnderlyingModuleFunctor,
)


def test_underlying_module_of_group_algebra_is_the_literal_functor_composite() -> None:
    group = Groups.C(4)
    algebra_functor = GroupAlgebraFunctor(ZZ)
    module_functor = GroupAlgebraUnderlyingModuleFunctor(ZZ)

    algebra = algebra_functor(group)
    underlying = module_functor(group)

    assert underlying is module_functor.underlying_module_functor()(algebra)
    assert FreeModuleOnGroupFunctor is GroupAlgebraUnderlyingModuleFunctor
    assert underlying.base_ring() is ZZ
    assert underlying.module_generating_set() is algebra.module_generating_set()


def test_nonidentity_group_map_moves_the_group_basis_through_the_same_composite() -> None:
    source = Groups.C(2)
    target = Groups.C(4)
    source_generator = source.group_generators()[0]
    target_generator = target.group_generators()[0]
    inclusion = group_homset(source, target)(
        {source_generator: target_generator**2}
    )
    functor = GroupAlgebraUnderlyingModuleFunctor(ZZ)

    induced = functor(inclusion)
    source_module = functor(source)
    target_module = functor(target)

    assert induced.domain() is source_module
    assert induced.codomain() is target_module
    assert induced(source_module.module_generator(source_generator)) == (
        target_module.module_generator(target_generator**2)
    )
    assert induced(source_module.module_generator(source.one())) == (
        target_module.module_generator(target.one())
    )
