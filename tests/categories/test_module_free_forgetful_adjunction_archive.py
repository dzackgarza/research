"""Archive reconciliation for the free-module/underlying-set adjunction.

``free_forgetful_adjunction.sage`` stated the unit, counit, Hom-set bijection,
and two triangle identities explicitly.  The live implementation factors those
responsibilities between ``FreeForgetfulAdjunction`` and the common
``Adjunction`` owner; these specimens identify that semantic replacement.
"""

from dzack_research.preamble.all import Modules, ZZ
from dzack_research.preamble.categories.sets import finite_ordered_set
from dzack_research.preamble.categories.sets.set_categories import Sets

ARCHIVE_RECONCILIATIONS = (
    {
        "archive_module": "preamble/tests/test_functor_codomains.sage",
        "live_owner": "tests/categories/test_module_free_forgetful_adjunction_archive.py",
        "owner_overrides": {
            "test_underlying_set_of_group_functor_lands_in_sets": "tests/groups/test_functors_out_of_groups.py",
            "test_group_ring_module_functor_lands_in_modules": "tests/algebras/test_group_algebra_functor_archive.py",
            "test_group_ring_over_many_base_rings": "tests/algebras/test_group_algebra_functor_archive.py",
            "test_group_ring_is_noncommutative_exactly_when_the_group_is": "tests/algebras/test_group_algebra_functor_archive.py",
        },
        "disposition": "reconciled-live-owner",
    },
    {
        "archive_module": "preamble/categories/functors/free_forgetful_adjunction.sage",
        "live_owner": "src/dzack_research/preamble/categories/functors/free_forgetful.py",
        "owner_overrides": {
            "ModuleAlgebraFunctor": "src/dzack_research/preamble/categories/functors/free_algebras.py",
            "FreeAlgebraFunctor": "src/dzack_research/preamble/categories/functors/free_algebras.py",
            "FreeAlgebraFunctor.unit": "src/dzack_research/preamble/categories/functors/free_algebras.py",
            "TensorAlgebraFunctor": "src/dzack_research/preamble/categories/functors/free_algebras.py",
            "SymmetricAlgebraFunctor": "src/dzack_research/preamble/categories/functors/free_algebras.py",
            "AlternatingAlgebraFunctor": "src/dzack_research/preamble/categories/functors/free_algebras.py",
            "DividedPowerAlgebraFunctor": "src/dzack_research/preamble/categories/functors/free_algebras.py",
            "UnderlyingSetOfGroupFunctor": "src/dzack_research/preamble/categories/functors/free_groups.py",
            "GroupRingFunctor": "src/dzack_research/preamble/categories/algebras/group_algebras.py",
            "GroupRingFunctor.base_ring": "src/dzack_research/preamble/categories/algebras/group_algebras.py",
            "FreeModuleOnGroupFunctor": "src/dzack_research/preamble/categories/algebras/group_algebras.py",
            "FreeModuleOnGroupFunctor.base_ring": "src/dzack_research/preamble/categories/algebras/group_algebras.py",
            "Adjunction": "src/dzack_research/preamble/categories/functors/core.py",
            "Adjunction.left_adjoint": "src/dzack_research/preamble/categories/functors/core.py",
            "Adjunction.right_adjoint": "src/dzack_research/preamble/categories/functors/core.py",
            "Adjunction.unit": "src/dzack_research/preamble/categories/functors/core.py",
            "Adjunction.counit": "src/dzack_research/preamble/categories/functors/core.py",
            "Adjunction.hom_set_isomorphism_forward": "src/dzack_research/preamble/categories/functors/core.py",
            "Adjunction.hom_set_isomorphism_inverse": "src/dzack_research/preamble/categories/functors/core.py",
        },
        "disposition": "reconciled-live-owner",
    },
)


def test_archived_hom_bijection_is_the_live_adjunction_transpose() -> None:
    adjunction = Sets().free_module_adjunction(ZZ)
    labels = finite_ordered_set(("x", "y"))
    module = ZZ.free_module(finite_ordered_set(("a", "b")))
    free = adjunction.left_adjoint()(labels)
    morphism = free.module_category().Mor(free, module)(
        {
            "x": module.module_generator("a") + module.module_generator("b"),
            "y": 3 * module.module_generator("a"),
        }
    )

    # The free-module adjunction reads its source from the constructor-owned
    # framing, not from a reverse functor-provenance cache.
    transpose = adjunction.hom_set_isomorphism_forward(morphism, labels)
    recovered = adjunction.hom_set_isomorphism_inverse(transpose, module)

    assert transpose(labels("x")) == morphism(free.module_generator("x"))
    assert transpose(labels("y")) == morphism(free.module_generator("y"))
    assert recovered == morphism


def test_archived_triangle_identities_are_the_live_unit_and_counit() -> None:
    adjunction = Sets().free_module_adjunction(ZZ)
    free = adjunction.left_adjoint()
    underlying = adjunction.right_adjoint()
    labels = finite_ordered_set(("u", "v"))
    module = ZZ.free_module(finite_ordered_set(("p", "q")))

    first_triangle = underlying(adjunction.counit(module)) * adjunction.unit(
        underlying(module)
    )
    for generator in module.module_generators():
        assert first_triangle(generator) == generator

    free_labels = free(labels)
    second_triangle = adjunction.counit(free_labels) * free(adjunction.unit(labels))
    for generator in free_labels.module_generators():
        assert second_triangle(generator) == generator


def test_free_and_underlying_functors_land_in_declared_codomains_on_a_nonidentity_map() -> None:
    source = finite_ordered_set(("x", "y"))
    target = finite_ordered_set(("a", "b", "c"))
    set_map = Sets().Mor(source, target)(
        lambda label: target("b") if label == source("x") else target("c")
    )
    free = Sets().free_module(ZZ)
    underlying = Modules(ZZ).underlying_set()

    source_module = free(source)
    target_module = free(target)
    induced = free(set_map)

    assert source_module in free.codomain()
    assert target_module in free.codomain()
    assert induced.domain() is source_module
    assert induced.codomain() is target_module
    assert induced(source_module.module_generator("x")) == target_module.module_generator("b")
    assert induced(source_module.module_generator("y")) == target_module.module_generator("c")

    forgotten = underlying(induced)
    assert underlying(source_module) in underlying.codomain()
    assert forgotten.domain() is source_module
    assert forgotten.codomain() is target_module
    assert forgotten(source_module.module_generator("x")) == target_module.module_generator("b")


def test_archived_unit_is_natural_on_a_nonidentity_set_map() -> None:
    adjunction = Sets().free_module_adjunction(ZZ)
    source = finite_ordered_set(("x", "y"))
    target = finite_ordered_set(("a", "b", "c"))
    morphism = Sets().Mor(source, target)(
        lambda label: target("b") if label == source("x") else target("c")
    )
    free = adjunction.left_adjoint()
    underlying = adjunction.right_adjoint()

    left = underlying(free(morphism)) * adjunction.unit(source)
    right = adjunction.unit(target) * morphism

    assert left == right
    assert left(source("x")) == free(target).module_generator("b")
    assert left(source("y")) == free(target).module_generator("c")
