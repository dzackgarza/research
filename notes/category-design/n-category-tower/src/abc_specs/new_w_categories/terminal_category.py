# Origin: gitclones/integral_lattice/cat/src/abc_specs/new_w_categories/terminal_category.py
# Copied 2026-08-20 by the integral_lattice enrichment migration
# (PLAN-corpora-audit-registry, sections R3/R4). Content below is unmodified.
#
# This is a DESIGN RECORD: it states an intended interface, not the built
# preamble. Divergences and recorded errors are listed in the INDEX.md of
# this corpus.

"""
Terminal category 1: the category with exactly one object and one morphism.

Mathematically, 1 is terminal in Cat: for any category C, there is a unique functor C → 1.

The terminal category is defined up to equivalence - the single object can be any object.
This implementation takes the underlying object data as a parameter.
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


class TerminalCategory(Category):
    """The terminal category 1, parameterized by the underlying object data."""
    
    # Non-hom arrows (base category)
    @dataclass(eq=False, unsafe_hash=True, frozen=True)
    class TerminalObject(Object_non_hom):
        """The unique object * in 1."""
        pass
    
    @dataclass(frozen=True)
    class TerminalMorphism(Morphism_non_hom):
        """The unique morphism id_* in 1 (identity on the terminal object)."""
        pass
    
    @dataclass(frozen=True)
    class TerminalTwoMorphism(TwoMorphism_non_hom):
        """The unique 2-morphism in 1 (identity 2-cell on the identity morphism)."""
        pass
    
    # Hom-category arrows (unique terminal versions)
    @dataclass(eq=False, unsafe_hash=True, frozen=True)
    class TerminalObject_hom(Object_hom):
        """The unique 0-arrow in Hom_1 (terminal morphism viewed as object)."""
        pass
    
    @dataclass(frozen=True)
    class TerminalMorphism_hom(Morphism_hom):
        """The unique 1-arrow in Hom_1 (terminal 2-morphism viewed as 1-arrow)."""
        pass
    
    @dataclass(frozen=True)
    class TerminalTwoMorphism_hom(TwoMorphism_hom):
        """The unique 2-arrow in Hom_1."""
        pass
    
    def __init__(self, terminal_object_data: Any = frozenset()) -> None:
        self._terminal_object_data = terminal_object_data
        super().__init__(
            _name=f"1 (Terminal Category on {terminal_object_data})",
            _element_type=EmptyElement,
            _object_type=TerminalCategory.TerminalObject,
            _morphism_type=TerminalCategory.TerminalMorphism,
            _two_morphism_type=TerminalCategory.TerminalTwoMorphism,
            _hom_type=TerminalHomCategory,  # External class
        )
        self.__post_init__()

    def __post_init__(self) -> None:
        # Create the unique terminal object
        terminal_obj = TerminalCategory.TerminalObject(
            _data=self._terminal_object_data,
            _category=self
        )
        self._obj_cache: set[TerminalCategory.TerminalObject] = set([terminal_obj])
        
        # Create the unique terminal morphism (identity on the terminal object)
        terminal_morph = TerminalCategory.TerminalMorphism(
            _source=terminal_obj,
            _target=terminal_obj,
            _func=lambda x: x
        )
        self._morph_cache: set[TerminalCategory.TerminalMorphism] = set([terminal_morph])
        
        # Create the unique terminal 2-morphism (identity 2-cell)
        terminal_two_morph = TerminalCategory.TerminalTwoMorphism(
            _source=terminal_morph,
            _target=terminal_morph,
            _data=None
        )
        self._two_morph_cache: set[TerminalCategory.TerminalTwoMorphism] = set([terminal_two_morph])
    
    @override
    def make_object(self, *data: Any) -> TerminalObject:
        # Terminal category has exactly one object
        return list(self._obj_cache)[0]
    
    @override
    def make_morphism(self, *data: Any) -> TerminalMorphism:
        # Terminal category has exactly one morphism (identity)
        return list(self._morph_cache)[0]
    
    @override
    def make_two_morphism(self, *data: Any) -> TerminalTwoMorphism:
        # Terminal category has exactly one 2-morphism (identity 2-cell)
        return list(self._two_morph_cache)[0]
    
    @property
    def terminal_object(self) -> TerminalObject:
        """The unique object in this terminal category."""
        return self.make_object()
    
    @property
    def identity_morphism(self) -> TerminalMorphism:
        """The unique morphism in this terminal category (identity on the terminal object)."""
        return self.make_morphism()


class TerminalHomCategory(HomCategory):
    """Hom_1(*, *) - a hom-category in the terminal category.
    
    This is EQUIVALENT to 1 (both are terminal categories) but NOT EQUAL:
    - 1 is a base category
    - Hom_1(*, *) is a hom-category
    
    They are equivalent because both have exactly one object, one morphism, etc.
    The unique morphism * -> * in 1 (which is id_*) becomes the unique object in Hom_1(*, *).
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
        # Explicitly use unique terminal hom types
        Category.__init__(
            self,
            _name=f"Hom_1({_domain}, {_codomain})",
            _element_type=None,
            _object_type=TerminalCategory.TerminalObject_hom,
            _morphism_type=TerminalCategory.TerminalMorphism_hom,
            _two_morphism_type=TerminalCategory.TerminalTwoMorphism_hom,
            _hom_type=TerminalHomCategory,
        )


# Default terminal category with frozenset() as the underlying object
TERMINAL: TerminalCategory = TerminalCategory()

