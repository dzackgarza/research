r"""The global framing datum and the three structure-specific realizations agree."""

from sage.misc.unknown import Unknown

from dzack_research.preamble.all import (
    AlgebrasWithChosenFinitePresentation,
    Groups,
    GroupsWithChosenFinitePresentation,
    Modules,
    OwnedFinitelyPresentedGroups,
    OwnedGroups,
    QQ,
    ZZ,
)


def test_finite_presentability_does_not_select_a_group_presentation() -> None:
    group = Groups.S(3)

    assert group in OwnedFinitelyPresentedGroups()
    assert group not in GroupsWithChosenFinitePresentation()
    assert not hasattr(group, "presenting_free_group")

    presented = group.presentation()
    assert presented is group
    assert presented in GroupsWithChosenFinitePresentation()
    assert presented.presentation() is presented
    assert presented.presenting_free_group() is presented.selected_framing_source(
        OwnedGroups()
    )
    assert presented.group_generators() == presented.selected_framing_generators(
        OwnedGroups()
    )
    framing = presented.selected_framing_morphism(OwnedGroups())
    assert framing.domain() is presented.presenting_free_group()
    assert framing.codomain() is presented
    for label in presented.presenting_free_group().free_basis():
        assert framing(presented.presenting_free_group().free_generator(label)) == (
            presented.selected_framing_generator(OwnedGroups(), label)
        )


def test_selected_module_presentation_and_resolution_reuse_the_framing_maps() -> None:
    free = ZZ.free_module(("x",))
    relations = ZZ.free_module(("r",))
    relation_map = relations.module_category().Mor(relations, free)(
        {"r": ZZ(2) * free.module_generator("x")}
    )
    module = relation_map.cokernel()
    owner = Modules(ZZ)

    assert module.presentation().codomain() is module.selected_framing_source(owner)
    assert module.presentation_projection() is module.selected_framing_morphism(owner)

    resolution = module.free_resolution()
    assert resolution.differential(1) is module.presentation()
    assert resolution.augmentation() is module.presentation_projection()


def test_finite_framing_decides_map_equality_only_with_established_linearity() -> None:
    module = ZZ.free_module(("e",))
    mor = Modules(ZZ).Mor(module, module)
    identity = mor.identity()
    stated = mor({"e": module.module_generator("e")})
    opaque = mor.elementwise(lambda element: element)

    assert identity == stated
    assert opaque.linearity_decision() is Unknown
    assert (identity == opaque) is Unknown


def test_selected_algebra_presentation_extends_one_retained_algebra_framing() -> None:
    generating = ZZ.free_module(("x",))
    presentation = generating.symmetric_algebra()
    algebra = presentation.quotient_by_relations(("x^2",))
    owner = algebra.algebra_framing_owner()

    assert algebra in AlgebrasWithChosenFinitePresentation(ZZ)
    assert algebra.presentation_ring() is algebra.selected_framing_source(owner)
    framing = algebra.selected_framing_morphism(owner)
    assert framing is algebra.algebra_presentation_morphism()
    assert framing is algebra.algebra_presentation_morphism()
    assert algebra.generating_module() is generating
    assert algebra.algebra_generating_set() == generating.module_generating_set()
    assert algebra.relations().cardinality() == 1
    assert algebra.multiplication().codomain() is algebra


def test_derivation_presentation_uses_its_actual_selected_framing_source() -> None:
    polynomial = QQ.free_module(("x", "y")).symmetric_algebra()
    x = polynomial.algebra_generator("x")
    y = polynomial.algebra_generator("y")
    algebra = polynomial.quotient_by_relations((x * y,))
    derivations = algebra.derivations(algebra.regular_module())
    owner = Modules(algebra)

    assert derivations.presentation().codomain() is derivations.selected_framing_source(owner)
