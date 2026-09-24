"""Lazy public aggregation for the owned group-theoretic vocabulary."""

from importlib import import_module as _import_module


_EXPORTS = {
    "EquivariantMorphism": ("dzack_research.preamble.categories.group.g_objects", "EquivariantMorphism"),
    "GObjectMor": ("dzack_research.preamble.categories.group.g_objects", "GObjectMor"),
    "GObjects": ("dzack_research.preamble.categories.group.g_objects", "GObjects"),
    "Grp": ("dzack_research.preamble.categories.group.g_objects", "Grp"),
    "InternalGroupActions": ("dzack_research.preamble.categories.group.g_objects", "InternalGroupActions"),
    "InternalGroupObjects": ("dzack_research.preamble.categories.group.g_objects", "InternalGroupObjects"),
    "FiniteGSets": ("dzack_research.preamble.categories.group.g_sets", "FiniteGSets"),
    "GSetMor": ("dzack_research.preamble.categories.group.g_sets", "GSetMor"),
    "GSetMorphism": ("dzack_research.preamble.categories.group.g_sets", "GSetMorphism"),
    "OrbitSets": ("dzack_research.preamble.categories.group.g_sets", "OrbitSets"),
    "Torsors": ("dzack_research.preamble.categories.group.g_sets", "Torsors"),
    "FiniteGroupClassFunction": (
        "dzack_research.preamble.categories.group.class_functions",
        "FiniteGroupClassFunction",
    ),
    "CyclicGroups": ("dzack_research.preamble.categories.group.cyclic_subgroups", "CyclicGroups"),
    "AbelianGroups": ("dzack_research.preamble.categories.group.groups", "AbelianGroups"),
    "FiniteAbelianGroups": ("dzack_research.preamble.categories.group.groups", "FiniteAbelianGroups"),
    "FiniteGroups": ("dzack_research.preamble.categories.group.groups", "FiniteGroups"),
    "FinitelyGeneratedGroups": ("dzack_research.preamble.categories.group.groups", "FinitelyGeneratedGroups"),
    "FinitelyPresentedGroups": ("dzack_research.preamble.categories.group.groups", "FinitelyPresentedGroups"),
    "GroupAutomorphism": ("dzack_research.preamble.categories.group.groups", "GroupAutomorphism"),
    "GroupAutomorphismGroup": ("dzack_research.preamble.categories.group.groups", "GroupAutomorphismGroup"),
    "GroupMorphism": ("dzack_research.preamble.categories.group.groups", "GroupMorphism"),
    "GroupMor": ("dzack_research.preamble.categories.group.groups", "GroupMor"),
    "Groups": ("dzack_research.preamble.categories.group.groups", "Groups"),
    "GroupsWithChosenFiniteGeneratingSet": (
        "dzack_research.preamble.categories.group.groups",
        "GroupsWithChosenFiniteGeneratingSet",
    ),
    "GroupsWithChosenFinitePresentation": (
        "dzack_research.preamble.categories.group.groups",
        "GroupsWithChosenFinitePresentation",
    ),
    "GroupsWithChosenFreeBasis": (
        "dzack_research.preamble.categories.group.groups",
        "GroupsWithChosenFreeBasis",
    ),
    "InfiniteGroups": ("dzack_research.preamble.categories.group.groups", "InfiniteGroups"),
    "IndexedFreeGroupMorphism": (
        "dzack_research.preamble.categories.group.groups",
        "IndexedFreeGroupMorphism",
    ),
    "IndexedFreeGroupMor": ("dzack_research.preamble.categories.group.groups", "IndexedFreeGroupMor"),
    "OwnedAbelianGroups": ("dzack_research.preamble.categories.group.groups", "OwnedAbelianGroups"),
    "OwnedFiniteAbelianGroups": (
        "dzack_research.preamble.categories.group.groups",
        "OwnedFiniteAbelianGroups",
    ),
    "OwnedFiniteGroups": ("dzack_research.preamble.categories.group.groups", "OwnedFiniteGroups"),
    "OwnedFinitelyGeneratedGroups": (
        "dzack_research.preamble.categories.group.groups",
        "OwnedFinitelyGeneratedGroups",
    ),
    "OwnedFinitelyPresentedGroups": (
        "dzack_research.preamble.categories.group.groups",
        "OwnedFinitelyPresentedGroups",
    ),
    "OwnedGroups": ("dzack_research.preamble.categories.group.groups", "OwnedGroups"),
    "OwnedInfiniteGroups": ("dzack_research.preamble.categories.group.groups", "OwnedInfiniteGroups"),
    "Subgroups": ("dzack_research.preamble.categories.group.groups", "Subgroups"),
    "groups": ("dzack_research.preamble.categories.group.groups", "groups"),
    "_own_group": ("dzack_research.preamble.categories.group.groups", "_own_group"),
    "AdditiveGroups": ("dzack_research.preamble.categories.group.magmas", "AdditiveGroups"),
    "PredicateSubgroups": (
        "dzack_research.preamble.categories.group.predicate_subgroups",
        "PredicateSubgroups",
    ),
    "AbsoluteDecompositionGroup": (
        "dzack_research.preamble.categories.group.profinite",
        "AbsoluteDecompositionGroup",
    ),
    "AbsoluteGaloisGroup": ("dzack_research.preamble.categories.group.profinite", "AbsoluteGaloisGroup"),
    "AbsoluteGaloisGroupElement": (
        "dzack_research.preamble.categories.group.profinite",
        "AbsoluteGaloisGroupElement",
    ),
    "AbsoluteGaloisGroups": ("dzack_research.preamble.categories.group.profinite", "AbsoluteGaloisGroups"),
    "AbsoluteGaloisGroupsOfFiniteFields": (
        "dzack_research.preamble.categories.group.profinite",
        "AbsoluteGaloisGroupsOfFiniteFields",
    ),
    "AbsoluteInertiaGroup": ("dzack_research.preamble.categories.group.profinite", "AbsoluteInertiaGroup"),
    "CyclotomicCharacter": ("dzack_research.preamble.categories.group.profinite", "CyclotomicCharacter"),
    "DecompositionGroupConjugacyClass": (
        "dzack_research.preamble.categories.group.profinite",
        "DecompositionGroupConjugacyClass",
    ),
    "ElementConjugacyClass": ("dzack_research.preamble.categories.group.profinite", "ElementConjugacyClass"),
    "FiniteElementConjugacyClass": (
        "dzack_research.preamble.categories.group.profinite",
        "FiniteElementConjugacyClass",
    ),
    "FiniteGaloisAutomorphism": (
        "dzack_research.preamble.categories.group.profinite",
        "FiniteGaloisAutomorphism",
    ),
    "FiniteGaloisExtension": ("dzack_research.preamble.categories.group.profinite", "FiniteGaloisExtension"),
    "FiniteGaloisQuotient": ("dzack_research.preamble.categories.group.profinite", "FiniteGaloisQuotient"),
    "FiniteGaloisSubgroup": ("dzack_research.preamble.categories.group.profinite", "FiniteGaloisSubgroup"),
    "FrobeniusConjugacyClass": (
        "dzack_research.preamble.categories.group.profinite",
        "FrobeniusConjugacyClass",
    ),
    "FrobeniusElement": ("dzack_research.preamble.categories.group.profinite", "FrobeniusElement"),
    "InertiaGroupConjugacyClass": (
        "dzack_research.preamble.categories.group.profinite",
        "InertiaGroupConjugacyClass",
    ),
    "LiftCoset": ("dzack_research.preamble.categories.group.profinite", "LiftCoset"),
    "OpenAbsoluteGaloisSubgroup": (
        "dzack_research.preamble.categories.group.profinite",
        "OpenAbsoluteGaloisSubgroup",
    ),
    "OpenAbsoluteGaloisSubgroups": (
        "dzack_research.preamble.categories.group.profinite",
        "OpenAbsoluteGaloisSubgroups",
    ),
    "OpenGaloisSubgroupConjugacyClass": (
        "dzack_research.preamble.categories.group.profinite",
        "OpenGaloisSubgroupConjugacyClass",
    ),
    "PrimeProlongation": ("dzack_research.preamble.categories.group.profinite", "PrimeProlongation"),
    "ProfiniteCharacter": ("dzack_research.preamble.categories.group.profinite", "ProfiniteCharacter"),
    "ProfiniteGroups": ("dzack_research.preamble.categories.group.profinite", "ProfiniteGroups"),
    "QuadraticCharacter": ("dzack_research.preamble.categories.group.profinite", "QuadraticCharacter"),
    "RestrictedProfiniteCharacter": (
        "dzack_research.preamble.categories.group.profinite",
        "RestrictedProfiniteCharacter",
    ),
}

__all__ = [
    "AbsoluteDecompositionGroup",
    "AbsoluteGaloisGroup",
    "AbsoluteGaloisGroupElement",
    "AbsoluteGaloisGroups",
    "AbsoluteGaloisGroupsOfFiniteFields",
    "AbsoluteInertiaGroup",
    "AbelianGroups",
    "AdditiveGroups",
    "CyclicGroups",
    "CyclotomicCharacter",
    "DecompositionGroupConjugacyClass",
    "ElementConjugacyClass",
    "EquivariantMorphism",
    "FiniteAbelianGroups",
    "FiniteElementConjugacyClass",
    "FiniteGSets",
    "FiniteGaloisAutomorphism",
    "FiniteGaloisExtension",
    "FiniteGaloisQuotient",
    "FiniteGaloisSubgroup",
    "FiniteGroups",
    "FiniteGroupClassFunction",
    "FinitelyGeneratedGroups",
    "FinitelyPresentedGroups",
    "FrobeniusConjugacyClass",
    "FrobeniusElement",
    "GObjectMor",
    "GObjects",
    "Grp",
    "GSetMor",
    "GSetMorphism",
    "GroupAutomorphism",
    "GroupAutomorphismGroup",
    "GroupMorphism",
    "GroupMor",
    "IndexedFreeGroupMorphism",
    "IndexedFreeGroupMor",
    "InertiaGroupConjugacyClass",
    "InternalGroupActions",
    "InternalGroupObjects",
    "LiftCoset",
    "OpenAbsoluteGaloisSubgroup",
    "OpenAbsoluteGaloisSubgroups",
    "OpenGaloisSubgroupConjugacyClass",
    "Groups",
    "GroupsWithChosenFiniteGeneratingSet",
    "GroupsWithChosenFinitePresentation",
    "GroupsWithChosenFreeBasis",
    "InfiniteGroups",
    "OwnedAbelianGroups",
    "OwnedFiniteAbelianGroups",
    "OwnedFiniteGroups",
    "OwnedFinitelyGeneratedGroups",
    "OwnedFinitelyPresentedGroups",
    "OwnedGroups",
    "OwnedInfiniteGroups",
    "Subgroups",
    "OrbitSets",
    "PredicateSubgroups",
    "PrimeProlongation",
    "ProfiniteCharacter",
    "ProfiniteGroups",
    "QuadraticCharacter",
    "RestrictedProfiniteCharacter",
    "Torsors",
    "groups",
]


def __getattr__(name):
    if name not in _EXPORTS:
        raise AttributeError(name)
    module_name, attribute = _EXPORTS[name]
    value = getattr(_import_module(module_name), attribute)
    globals()[name] = value
    return value


def __dir__():
    return sorted((*globals(), *__all__))
