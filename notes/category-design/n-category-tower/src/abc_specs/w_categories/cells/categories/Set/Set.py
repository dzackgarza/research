# Origin: gitclones/integral_lattice/cat/src/abc_specs/w_categories/cells/categories/Set/Set.py
# Copied 2026-08-20 by the integral_lattice enrichment migration
# (PLAN-corpora-audit-registry, sections R3/R4). Content below is unmodified.
#
# This is a DESIGN RECORD: it states an intended interface, not the built
# preamble. Divergences and recorded errors are listed in the INDEX.md of
# this corpus.


from __future__ import annotations
from src.local_typing import *
from src._types import *
from src.abc_specs.w_categories.cells.morphisms import Morphism
from ..wCat.wCat import wCat_Morphism, wCat
from .n_morphisms import SetObject, SetMorphism

class _Set_Morphism_0_ABC(SetObject.m0, ABC):
    """0-morphism in Set: a set."""
    ...

class _Set_Morphism_1_ABC(SetMorphism.m1, ABC):
    """1-morphism in Set: a function."""
    ...

class _Set_Morphism_1_endo_ABC(SetMorphism.m1_endo, ABC):
    """1-morphism in Set: a function."""
    ...

class _Set_Morphism_1_auto_ABC(SetMorphism.m1_auto, ABC):
    """1-morphism in Set: a function."""
    ...

class _Set_Morphism_2_ABC(Morphism.n, ABC):
    """All 2-morphisms in Set are identities."""
    ...

class Set_Morphism:
    m0 = _Set_Morphism_0_ABC
    m1 = _Set_Morphism_1_ABC
    m2 = _Set_Morphism_2_ABC

class Set(wCat_Morphism.m0):

    @override
    @abstractmethod
    def amb(self) -> wCat: ...

    @override
    @abstractmethod
    def _n_morphism_classes(self) -> tuple[
        type[Set_Morphism.m0], 
        type[Set_Morphism.m1], 
        type[Set_Morphism.m2]
    ]: ...