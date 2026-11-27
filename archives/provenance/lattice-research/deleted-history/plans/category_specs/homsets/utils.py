r"""Shared helpers for homset construction specs."""

from __future__ import annotations

from sage.categories.category import Category
from sage.categories.homset import Homset as SageHomset
from sage.categories.morphism import Morphism as SageMorphism
from sage.sets.condition_set import ConditionSet as SageConditionSet

from ..utils import refine_category


def is_automorphism_morphism(morphism: SageMorphism) -> bool:
    r"""Return whether ``morphism`` represents an automorphism when computable."""
    if hasattr(morphism, "is_automorphism"):
        return morphism.is_automorphism()
    if hasattr(morphism, "is_invertible"):
        return morphism.is_invertible()
    if hasattr(morphism, "is_isomorphism"):
        return morphism.is_isomorphism()
    if hasattr(morphism, "is_bijective"):
        return morphism.is_bijective()
    return False


def refine_automorphism_set_from_endset(endset: SageHomset, category: Category) -> SageHomset:
    r"""Build ``Aut(X)`` as the invertible subobject of ``End(X)``."""
    return refine_category(SageConditionSet(endset, is_automorphism_morphism), category)
