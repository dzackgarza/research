r"""Archive reconciliation for the group-ring and underlying-module functors."""

from dzack_research.preamble.all import GF, ZZ, Groups, PolynomialRing, group_homset
from dzack_research.preamble.categories.algebras import (
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


def test_group_algebra_of_an_infinite_free_group_has_the_group_as_its_lazy_basis() -> None:
    group = Groups.Free(1, names="t")
    generator = group.group_generators()[0]
    algebra = GroupAlgebraFunctor(ZZ)(group)
    module = algebra.underlying_module()

    assert algebra.group() is group
    assert module.module_generating_set() is group
    assert not module.module_generating_set().cardinality().is_finite()
    assert (
        algebra.module_generator(generator)
        * algebra.module_generator(generator.inverse())
        == algebra.one()
    )
    assert (
        algebra.module_generator(generator**2)
        * algebra.module_generator(generator**-3)
        == algebra.module_generator(generator**-1)
    )


def test_group_algebra_functor_carries_a_nonidentity_map_between_infinite_free_groups() -> None:
    source = Groups.Free(1, names="s")
    target = Groups.Free(2, names=("x", "y"))
    source_generator = source.group_generators()[0]
    target_generators = tuple(target.group_generators())
    morphism = group_homset(source, target)(
        {source_generator: target_generators[0] * target_generators[1]}
    )
    functor = GroupAlgebraUnderlyingModuleFunctor(ZZ)
    induced = functor(morphism)

    assert induced.domain() is functor(source)
    assert induced.codomain() is functor(target)
    assert induced(
        induced.domain().module_generator(source_generator**2)
    ) == induced.codomain().module_generator(
        (target_generators[0] * target_generators[1]) ** 2
    )


def test_group_algebra_keeps_nontrivial_coefficient_rings() -> None:
    cyclic = Groups.C(3)
    finite_field = GF(5)
    polynomial_ring = PolynomialRing(ZZ, "u")

    for ring in (finite_field, polynomial_ring):
        algebra = GroupAlgebraFunctor(ring)(cyclic)
        generator = cyclic.group_generators()[0]
        assert algebra.base_ring() is ring
        assert algebra.module_generating_set() is cyclic
        assert (
            algebra.module_generator(generator)
            * algebra.module_generator(generator**2)
            == algebra.one()
        )


def test_group_algebra_multiplication_remembers_whether_the_group_commutes() -> None:
    cyclic = Groups.C(3)
    cyclic_generator = cyclic.group_generators()[0]
    cyclic_algebra = GroupAlgebraFunctor(ZZ)(cyclic)
    assert (
        cyclic_algebra.module_generator(cyclic_generator)
        * cyclic_algebra.module_generator(cyclic_generator**2)
        == cyclic_algebra.module_generator(cyclic_generator**2)
        * cyclic_algebra.module_generator(cyclic_generator)
    )

    symmetric = Groups.S(3)
    left, right = tuple(symmetric.group_generators())[:2]
    assert left * right != right * left
    symmetric_algebra = GroupAlgebraFunctor(ZZ)(symmetric)
    assert (
        symmetric_algebra.module_generator(left)
        * symmetric_algebra.module_generator(right)
        != symmetric_algebra.module_generator(right)
        * symmetric_algebra.module_generator(left)
    )
