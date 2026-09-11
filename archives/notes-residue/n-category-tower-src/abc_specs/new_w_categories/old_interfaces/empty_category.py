# Origin: gitclones/integral_lattice/cat/src/abc_specs/new_w_categories/old_interfaces/empty_category.py
# Copied 2026-08-20 by the integral_lattice enrichment migration
# (PLAN-corpora-audit-registry, sections R3/R4). Content below is unmodified.
#
# This is a DESIGN RECORD: it states an intended interface, not the built
# preamble. Divergences and recorded errors are listed in the INDEX.md of
# this corpus.

from __future__ import annotations

from src._types import *
from src.local_typing import *

from .___cells import Cell
from .__arrows import Arrow
from .scaffolding import wCategory


@dataclass
class _EmptyObject(Arrow.m1):
    """The unique (-1)-arrow. Source/target of itself."""

    _underlying_data: Any
    _ambient_category: Any

    @override
    def source(self) -> Self:
        return self

    @override
    def target(self) -> Self:
        return self

    @override
    def suspend(self) -> Self:
        return self

    @override
    def desuspend(self) -> Self:
        return self

    @override
    def underlying_data(self) -> None:
        return self._underlying_data

    @override
    def as_cell(self) -> Cell.mn1:
        """Convert this arrow to a cell."""
        raise NotImplementedError

    @override
    def amb(self) -> None:
        """The ambient category containing this arrow."""
        return None


@dataclass
class _EmptyMorphism(_EmptyObject):
    ...


@dataclass
class _Empty_Hom_wCategory(wCategory):
    _base_category: wCategory

    @override
    def objects(self) -> type[_EmptyMorphism]: 
        return _EmptyMorphism

    @override
    def morphisms(self) -> type[_Empty_Hom_wCategory]: 
        return _Empty_Hom_wCategory

    @override
    def hom_category(self, x: Any, y: Any) -> _Empty_Hom_wCategory:
        return _Empty_Hom_wCategory(_base_category=self)

    @override
    def object_from(self, x: Any) -> Arrow.n0:
       return E_obj


class Empty_wCategory(wCategory):

    @override
    def objects(self) -> type[Arrow.m1]: 
        return _EmptyObject

    @override
    def morphisms(self) -> type[_Empty_Hom_wCategory]: 
        return _Empty_Hom_wCategory

    @override
    def hom_category(self, x: Any, y: Any) -> _Empty_Hom_wCategory:
        return _Empty_Hom_wCategory(_base_category=self)

    @override
    def object_from(self, x: Any) -> Arrow.n0:
        raise NotImplementedError  # Empty category has no objects

    def unique_object(self) -> _EmptyObject:
        return E_obj

    def unique_morphism(self) -> _EmptyMorphism:
        return E_mor


E = Empty_wCategory()
E_obj = _EmptyObject(_underlying_data= {}, _ambient_category=E)
E_mor = _EmptyMorphism(_underlying_data= {}, _ambient_category=E)