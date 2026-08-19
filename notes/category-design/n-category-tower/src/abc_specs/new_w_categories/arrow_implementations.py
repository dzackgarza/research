# Origin: gitclones/integral_lattice/cat/src/abc_specs/new_w_categories/arrow_implementations.py
# Copied 2026-08-20 by the integral_lattice enrichment migration
# (PLAN-corpora-audit-registry, sections R3/R4). Content below is unmodified.
#
# This is a DESIGN RECORD: it states an intended interface, not the built
# preamble. Divergences and recorded errors are listed in the INDEX.md of
# this corpus.

"""
Concrete implementations of the Arrow ABCs for ω-category scaffolding.

This module provides concrete implementations of:
- Elements ((-1)-arrows)
- Objects (0-arrows) in base categories
- Morphisms (1-arrows) in base categories
- 2-morphisms (2-arrows) in base categories
- Hom-category objects (0-arrows wrapping 1-arrows)
- Hom-category morphisms (1-arrows wrapping 2-arrows)
- Category and Hom-category structures
"""
from __future__ import annotations

from dataclasses import dataclass, field
from abc import ABCMeta
from src.local_typing import *
from ._arrow_abcs import Arrow, P2

# Type variables for generic Map
S = TypeVar("S")
T = TypeVar("T")
_C = TypeVar("_C", bound="Category")  # For type-preserving register


# =============================================================================
# Global Category Cache (wCat singleton)
# =============================================================================

class wCat:
    """Global singleton container caching all categories."""
    _category_cache: set[Category | HomCategory] = set()
    
    @classmethod
    def register(cls, category: _C) -> _C:
        """Register a category in the global cache. Returns cached instance if one exists."""
        if category in cls._category_cache:
            return cast(_C, next(x for x in cls._category_cache if x == category))
        cls._category_cache.add(category)
        return category
    
    @classmethod
    def get_hom_category(
        cls,
        base: Category,
        domain: Object,
        codomain: Object,
    ) -> HomCategory:
        """Get or create a hom-category for the given base category and objects."""
        hom = HomCategory(
            _domain=domain,
            _codomain=codomain,
            _base=base
        )
        if hom in cls._category_cache:
            x = next(x for x in cls._category_cache if x == hom)
            assert isinstance(x, HomCategory)
            return x
        cls._category_cache.add(hom)
        return hom
    
    @classmethod
    def clear(cls) -> None:
        """Clear all caches (useful for testing)."""
        cls._category_cache.clear()
    
    @classmethod
    def product(cls, categories: list[Category]) -> Category:
        """Compute the product of categories in wCat.
        
        For any categories C1, ..., Cn, returns C1 × ... × Cn.
        - Product of empty list is the terminal category 1.
        - Product of single category is itself.
        """
        raise NotImplementedError("wCat.product not yet implemented")
    
    @classmethod
    def coproduct(cls, categories: list[Category]) -> Category:
        """Compute the coproduct of categories in wCat.
        
        For any categories C1, ..., Cn, returns C1 ⊔ ... ⊔ Cn (disjoint union).
        - Coproduct of empty list is the initial category ∅.
        - Coproduct of single category is itself.
        """
        raise NotImplementedError("wCat.coproduct not yet implemented")


class CategoryMeta(ABCMeta):
    """Metaclass implementing singleton pattern for Category instances.
    
    Uses wCat as the backing store. Categories with the same field values
    (based on __eq__ and __hash__) return the same instance.
    
    Based on: https://stackoverflow.com/questions/6760685
    """
    
    def __call__(cls, *args: Any, **kwargs: Any) -> Any:
        # Create the instance
        instance = super().__call__(*args, **kwargs)
        # Register with wCat - returns cached instance if one exists
        return wCat.register(instance)


# =============================================================================
# Covariant Callable Implementation
# =============================================================================

@dataclass(frozen=True)
class Map(Arrow.Map[S, T], Generic[S, T]):
    """Concrete implementation of a covariant callable."""
    _underlying_data: Callable[[S], T]
    
    @final
    @override
    def __call__(self, x: S) -> T:
        return self._underlying_data(x)
    
    @final
    @override
    def source(self) -> S:
        return get_args(self.__orig_class__)[0]  # type: ignore[attr-defined]
    
    @final
    @override
    def target(self) -> T:
        return get_args(self.__orig_class__)[1]  # type: ignore[attr-defined]


# =============================================================================
# (-1)-Arrows: Elements
# =============================================================================

@dataclass(frozen=True)
class Element(Arrow.m1):
    """An element (point) in an object."""
    _data: Any
    _ambient: Object
    
    @final
    @override
    def underlying_data(self) -> Any:
        return self._data
    
    @final
    @override
    def ambient_object(self) -> Object:
        return self._ambient


class EmptyElement(Element):
    """The empty element of an object - serves as source/target of the object itself."""
    
    def __init__(self, _ambient: Object) -> None:
        super().__init__(_data=None, _ambient=_ambient)


# =============================================================================
# 0-Arrows (Non-Hom): Objects
# =============================================================================

@dataclass(eq=False, unsafe_hash=True, frozen=True)
class Object_non_hom(Arrow.n0_non_hom):
    """A 0-arrow (object) in a base category."""
    _data: Any
    _category: Category
    
    @final
    @override
    def underlying_data(self) -> Any:
        return self._data
    
    @final
    @override
    def ambient_category(self) -> Category:
        return self._category
    
    @final
    @cached_property
    def empty_element(self) -> EmptyElement:
        return EmptyElement(_ambient=self)
    
    @final
    @override
    def source(self) -> EmptyElement:
        return self.empty_element
    
    @final
    @override
    def target(self) -> EmptyElement:
        return self.empty_element

@dataclass(eq=False, unsafe_hash=True, frozen=True)
class Object_hom(Arrow.n0_hom, Object_non_hom):
    """A 0-arrow (object) in a hom-category."""
    _wrapped_arrow: Morphism
    _data: Any
    _category: HomCategory
    
    @final
    @override
    def wrapped_arrow(self) -> Morphism_non_hom:
        return self._wrapped_arrow
    
    @final
    @override
    def fully_unwrap(self) -> Morphism_non_hom:
        c: Arrow.n_non_hom | Arrow.n_hom = self.wrapped_arrow()
        while Arrow.n.is_hom_arrow(c):
            c = c.wrapped_arrow()
        assert isinstance(c, Morphism_non_hom)
        return c

Object = Object_hom | Object_non_hom

# =============================================================================
# 1-Arrows (Non-Hom): Morphisms
# =============================================================================

@dataclass(frozen=True)
class Morphism_non_hom(Arrow.n1_non_hom):
    """A 1-arrow (morphism) between objects in a base category."""
    _source: Object_non_hom
    _target: Object_non_hom
    _func: Callable[[Element], Element] | None
    
    @final
    @override
    def underlying_data(self) -> Map[Element, Element]:
        assert self._func is not None
        return Map[Element, Element](_underlying_data=self._func)
    
    @override
    def source(self) -> Object_non_hom:
        return self._source
    
    @override
    def target(self) -> Object_non_hom:
        return self._target
    
    @final
    @override
    def ambient_category(self) -> Category:
        return self._source.ambient_category()
    
    def __call__(self, x: Element) -> Element:
        assert self._func is not None, "Morphisms between morphisms are not callable."
        if isinstance(self, Morphism_hom):
            raise ValueError("1-arrows in Hom_C(x,y) cannot be called.")
        return self._func(x)


@dataclass(frozen=True)
class Morphism_hom(Arrow.n1_hom, Morphism_non_hom):
    """A 1-arrow (morphism) between objects in a hom-category."""
    _source: Object_hom
    _target: Object_hom
    _wrapped_arrow: TwoMorphism
    _func: None
    
    @final
    @override
    def source(self) -> Object_hom: 
        return self._source

    @final
    @override
    def target(self) -> Object_hom:
        return self._target

    @final
    @override
    def wrapped_arrow(self) -> TwoMorphism:
        return self._wrapped_arrow
    
    @final
    @override
    def fully_unwrap(self) -> TwoMorphism_non_hom:
        c: Arrow.n_non_hom | Arrow.n_hom = self.wrapped_arrow()
        while Arrow.n.is_hom_arrow(c):
            c = c.wrapped_arrow()
        assert isinstance(c, TwoMorphism_non_hom)
        return c

Morphism = Morphism_hom | Morphism_non_hom

# =============================================================================
# 2-Arrows (Non-Hom): 2-Morphisms
# =============================================================================

@dataclass(frozen=True)
class TwoMorphism_non_hom(Arrow.n2_non_hom):
    """A 2-arrow (2-morphism) between morphisms in a base category."""
    _source: Morphism_non_hom
    _target: Morphism_non_hom
    _data: Any # Structural content
    
    @override
    def underlying_data(self) -> Any:
        return self._data
    
    @override
    def source(self) -> Morphism_non_hom:
        return self._source
    
    @override
    def target(self) -> Morphism_non_hom:
        return self._target
    
    @final
    @override
    def ambient_category(self) -> Category:
        return self._source.ambient_category()



class TwoMorphism_hom(Arrow.n2_hom, TwoMorphism_non_hom):
    """A 2-arrow (2-morphism) between morphisms in a hom-category."""
    _source: Morphism_hom
    _target: Morphism_hom
    _wrapped_arrow: ThreePlusMorphism_non_hom
    _data: Any

    def __init__(
        self,
        _source: Morphism_hom,
        _target: Morphism_hom,
        _wrapped_arrow: ThreePlusMorphism_non_hom,
    ):
        self._wrapped_arrow = _wrapped_arrow
        TwoMorphism_non_hom.__init__(
            self,
            _source=_source,
            _target=_target,
            _data=None
        )
    
    @final
    @override
    def source(self) -> Morphism_hom:
        return self._source
    
    @final
    @override
    def target(self) -> Morphism_hom:
        return self._target
    
    @final
    @override
    def wrapped_arrow(self) -> ThreePlusMorphism_non_hom:
        return self._wrapped_arrow
    
    @final
    @override
    def fully_unwrap(self) -> ThreePlusMorphism_non_hom:
        c: Arrow.n_non_hom | Arrow.n_hom = self.wrapped_arrow()
        while Arrow.n.is_hom_arrow(c):
            c = c.wrapped_arrow()
        assert isinstance(c, ThreePlusMorphism_non_hom)
        return c


TwoMorphism = TwoMorphism_hom | TwoMorphism_non_hom


# =============================================================================
# 3+ Arrows (Non-Hom): Trivial higher morphisms
# =============================================================================

@dataclass(frozen=True)
class ThreePlusMorphism_non_hom(Arrow.n_geq_3_non_hom):
    """A 3+ arrow (trivial/invertible) between 2-morphisms in a base category."""
    _source: TwoMorphism_non_hom
    _target: TwoMorphism_non_hom
    
    @override
    def underlying_data(self) -> None:
        return None
    
    @override
    def source(self) -> TwoMorphism_non_hom:
        return self._source
    
    @override
    def target(self) -> TwoMorphism_non_hom:
        return self._target
    
    @final
    @override
    def ambient_category(self) -> Category:
        return self._source.ambient_category()


@dataclass(frozen=True)
class ThreePlusMorphism_hom(Arrow.n_geq_3_hom, ThreePlusMorphism_non_hom):
    """A 3+ arrow in a hom-category."""
    _source: TwoMorphism_hom
    _target: TwoMorphism_hom
    _wrapped_arrow: ThreePlusMorphism_non_hom
    
    @final
    @override
    def source(self) -> TwoMorphism_hom:
        return self._source
    
    @final
    @override
    def target(self) -> TwoMorphism_hom:
        return self._target
    
    @final
    @override
    def wrapped_arrow(self) -> ThreePlusMorphism_non_hom:
        return self._wrapped_arrow
    
    @final
    @override
    def fully_unwrap(self) -> ThreePlusMorphism_non_hom:
        c: Arrow.n_non_hom | Arrow.n_hom = self.wrapped_arrow()
        while Arrow.n.is_hom_arrow(c):
            c = c.wrapped_arrow()
        assert isinstance(c, ThreePlusMorphism_non_hom)
        return c


ThreePlusMorphism = ThreePlusMorphism_hom | ThreePlusMorphism_non_hom


# =============================================================================
# Base Category
# =============================================================================

@dataclass(unsafe_hash=True)
class Category(Arrow.wCategory, metaclass=CategoryMeta):
    """A concrete ω-category implementation."""
    _name: str
    _element_type: type[Element] | None
    _object_type: type[Object]
    _morphism_type: type[Morphism]
    _two_morphism_type: type[TwoMorphism]
    _hom_type: type[HomCategory]
    
    # Exclude from hash/eq/init - these are per-instance mutable state
    _obj_cache: set[Any] = field(default_factory=set, init=False, repr=False, compare=False, hash=False)
    _morph_cache: set[Any] = field(default_factory=set, init=False, repr=False, compare=False, hash=False)
    _two_morph_cache: set[Any] = field(default_factory=set, init=False, repr=False, compare=False, hash=False)

    @final
    @override
    def category_name(self) -> str:
        return self._name
    
    @final
    @override
    def elements(self) -> type[Element] | None:
        return self._element_type
    
    @override
    def objects(self) -> type[Object]:
        return self._object_type
    
    @override
    def morphisms(self) -> type[Morphism]:
        return self._morphism_type
    
    @override
    def two_morphisms(self) -> type[TwoMorphism]:
        return self._two_morphism_type
    
    @override
    def hom(self) -> Arrow.Map[P2[Object], HomCategory]:
        def get_or_create(pair: P2[Object]) -> HomCategory:
            return wCat.get_hom_category(self, pair[0], pair[1])
        
        return Map[
            P2[self._object_type], self._hom_type](
                _underlying_data=get_or_create
            )

    @final
    @override
    def hom_categories(self) -> type[HomCategory]:
        return self._hom_type
    
    
    def make_object(self, *data: Any) -> Object_non_hom:
        obj = self._object_type(*data)
        if obj in self._obj_cache:
            # Return the existing object from cache
            return next(x for x in self._obj_cache if x == obj)
        self._obj_cache.add(obj)
        return obj
    
    def make_morphism(
        self, *data: Any
    ) -> Morphism_non_hom:
        mor = self._morphism_type(*data)
        if mor in self._morph_cache:
            return next(x for x in self._morph_cache if x == mor)
        self._morph_cache.add(mor)
        return mor
    
    def make_two_morphism(
        self,
        *data: Any
    ) -> TwoMorphism_non_hom:
        two_mor = self._two_morphism_type(*data)
        if two_mor in self._two_morph_cache:
            return next(x for x in self._two_morph_cache if x == two_mor)
        self._two_morph_cache.add(two_mor)
        return two_mor


# =============================================================================
# Hom-Category
# =============================================================================

@dataclass(eq=False)
class HomCategory(Arrow.Hom_wCategory, Category):
    """Hom-category Hom_C(x, y) for objects x, y in base category C."""
    _domain: Object_non_hom
    _codomain: Object_non_hom
    _base: Category
    # _obj_cache: dict[Morphism_non_hom, Object_hom]

    def __init__(
        self,
        _domain: Object,
        _codomain: Object,
        _base: Category,
    ) -> None:
        self._domain = _domain
        self._codomain = _codomain
        self._base = _base
        Category.__init__(
            self,
            _name=f"Hom_C(x, y) where C = {self._base.category_name()}, x = {self._domain}, y = {self._codomain}",
            _element_type=None,
            _object_type=Object_hom,
            _morphism_type=Morphism_hom,
            _two_morphism_type=TwoMorphism_hom,
            _hom_type=HomCategory,
        )
        # Override with correctly typed cache for HomCategory
        self._obj_cache: set[Object | Object_hom] = set()
    
    @final
    @override
    def base_category(self) -> Category:
        return self._base
    
    @final
    @override
    def root_base_category(self) -> Category:
        c = self
        while Arrow.Hom_wCategory.is_hom_category(c):
            c = c.base_category()
        return c
    
    @final
    @override
    def domain(self) -> Object_non_hom:
        return self._domain
    
    @final
    @override
    def codomain(self) -> Object_non_hom:
        return self._codomain
    
    @final
    @override
    def objects(self) -> type[Object_hom]:
        obj_hom = self._object_type
        assert issubclass(obj_hom, Object_hom)
        return obj_hom
    
    @final
    @override
    def morphisms(self) -> type[Morphism_hom]:
        morph_hom = self._morphism_type
        assert issubclass(morph_hom, Morphism_hom)
        return morph_hom
    
    @final
    @override
    def two_morphisms(self) -> type[TwoMorphism_hom]:
        two_morph_hom = self._two_morphism_type
        assert issubclass(two_morph_hom, TwoMorphism_hom)
        return two_morph_hom
    
    @final
    @override
    def hom(self) -> Arrow.Map[P2[Object_hom], HomCategory]:
        def get_or_create(pair: P2[Object_hom]) -> HomCategory:
            return wCat.get_hom_category(self, pair[0], pair[1])
        
        return Map[P2[Object_hom], HomCategory](_underlying_data=get_or_create)
    
    @final
    def morphism_to_object(self, f: Morphism_non_hom) -> Object_hom:
        """Wrap a morphism as an object in this hom-category."""
        obj = Object_hom(_wrapped_arrow=f, _data=f, _category=self)
        if obj in self._obj_cache:
            x = next(x for x in self._obj_cache if x == obj)
            assert isinstance(x, Object_hom)
            return x
        self._obj_cache.add(obj)
        return obj
    
    @final
    def object_to_morphism(self, obj: Object_hom) -> Morphism_non_hom:
        """Unwrap an object in this hom-category to a morphism."""
        return obj.wrapped_arrow()
    
    @final
    def make_hom_morphism(
        self,
        source: Object_hom,
        target: Object_hom,
        two_morph: TwoMorphism_non_hom
    ) -> Morphism_hom:
        """Create a morphism in this hom-category from a 2-morphism."""
        return Morphism_hom(_source=source, _target=target, _wrapped_arrow=two_morph, _func=None)