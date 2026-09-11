# Origin: gitclones/integral_lattice/cat/src/abc_specs/new_w_categories/initial_category.py
# Copied 2026-08-20 by the integral_lattice enrichment migration
# (PLAN-corpora-audit-registry, sections R3/R4). Content below is unmodified.
#
# This is a DESIGN RECORD: it states an intended interface, not the built
# preamble. Divergences and recorded errors are listed in the INDEX.md of
# this corpus.

"""
Initial category ∅: the empty category.

Mathematically, ∅ is initial in Cat: for any category C, there is a unique functor ∅ → C.

Defines specialized types for each level as nested classes within InitialCategory.
"""
from __future__ import annotations

from dataclasses import dataclass, field

from src.local_typing import *
from ._arrow_abcs import Arrow
from .arrow_implementations import (
    Map, Element, EmptyElement, 
    Object_non_hom, Object_hom, Morphism_non_hom, Morphism_hom,
    TwoMorphism_non_hom, TwoMorphism_hom,
    Category, HomCategory
)

class InitialCategory(Category):
    """The initial category ∅."""
    
    # Non-hom arrows (base category)
    @dataclass(eq=False, unsafe_hash=True, frozen=True)
    class EmptyObject(Object_non_hom):
        """The unique object in ∅."""
        pass
    
    @dataclass(frozen=True)
    class EmptyMorphism(Morphism_non_hom):
        """The unique morphism in ∅ (identity on EmptyObject)."""
        pass
    
    @dataclass(frozen=True)
    class EmptyTwoMorphism(TwoMorphism_non_hom):
        """The unique 2-morphism in ∅."""
        pass
    
    # Hom-category arrows (unique empty versions)
    @dataclass(eq=False, unsafe_hash=True, frozen=True)
    class EmptyObject_hom(Object_hom):
        """The unique 0-arrow in Hom_∅ (empty morphism viewed as object)."""
        pass
    
    @dataclass(frozen=True)
    class EmptyMorphism_hom(Morphism_hom):
        """The unique 1-arrow in Hom_∅ (empty 2-morphism viewed as 1-arrow)."""
        pass
    
    @dataclass(frozen=True)
    class EmptyTwoMorphism_hom(TwoMorphism_hom):
        """The unique 2-arrow in Hom_∅."""
        pass
    
    def __init__(self) -> None:
        # Import here to avoid forward reference issues
        super().__init__(
            _name="∅ (Initial Category)",
            _element_type=EmptyElement,
            _object_type=InitialCategory.EmptyObject,
            _morphism_type=InitialCategory.EmptyMorphism,
            _two_morphism_type=InitialCategory.EmptyTwoMorphism,
            _hom_type=EmptyHomCategory,  # External class
        )
        self.__post_init__()

    def __post_init__(self) -> None:
        # Create singleton instances with explicit self reference (avoids recursion)
        empty_obj = InitialCategory.EmptyObject(_data=None, _category=self)
        empty_morph = InitialCategory.EmptyMorphism(_source=empty_obj, _target=empty_obj, _func=None)
        empty_two_morph = InitialCategory.EmptyTwoMorphism(_source=empty_morph, _target=empty_morph, _data=None)
        
        self._obj_cache: set[InitialCategory.EmptyObject] = set([empty_obj])
        self._morph_cache: set[InitialCategory.EmptyMorphism] = set([empty_morph])
        self._two_morph_cache: set[InitialCategory.EmptyTwoMorphism] = set([empty_two_morph])
    
    @override
    def make_object(self, *data: None) -> EmptyObject:
        return list(self._obj_cache)[0]
    
    @override
    def make_morphism(self, *data: None) -> EmptyMorphism:  
        return list(self._morph_cache)[0]
    
    @override
    def make_two_morphism(self, *data: None) -> EmptyTwoMorphism:  
        return list(self._two_morph_cache)[0]
    
    @property
    def empty_object(self) -> EmptyObject:
        """The unique object in the empty category."""
        return self.make_object()
    
    @property
    def empty_morphism(self) -> EmptyMorphism:
        """The unique morphism in the empty category."""
        return self.make_morphism()
    
    @property
    def empty_two_morphism(self) -> EmptyTwoMorphism:
        """The unique 2-morphism in the empty category."""
        return self.make_two_morphism()


class EmptyHomCategory(HomCategory):
    """Hom_∅(x, y) - a hom-category in the empty category.
    
    This is EQUIVALENT to ∅ (both are initial categories) but NOT EQUAL:
    - ∅ is a base category
    - Hom_∅(x, y) is a hom-category
    
    They are equivalent because both have exactly one object, one morphism, etc.
    """
    
    def __init__(
        self,
        _domain: Object_non_hom,
        _codomain: Object_non_hom,
        _base: Category,
    ) -> None:
        self._domain = _domain
        self._codomain = _codomain
        self._base = _base
        # Explicitly use unique empty hom types
        Category.__init__(
            self,
            _name=f"Hom_∅({_domain}, {_codomain})",
            _element_type=None,
            _object_type=InitialCategory.EmptyObject_hom,
            _morphism_type=InitialCategory.EmptyMorphism_hom,
            _two_morphism_type=InitialCategory.EmptyTwoMorphism_hom,
            _hom_type=EmptyHomCategory,
        )