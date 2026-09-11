# Origin: gitclones/integral_lattice/cat/src/abc_specs/w_categories/cells/categories/wCat/hom_categories/_aut_wcat_x.py
# Copied 2026-08-20 by the integral_lattice enrichment migration
# (PLAN-corpora-audit-registry, sections R3/R4). Content below is unmodified.
#
# This is a DESIGN RECORD: it states an intended interface, not the built
# preamble. Divergences and recorded errors are listed in the INDEX.md of
# this corpus.

"""
Aut_wCat(C) category ABC.

Aut_wCat(C) is a category whose 0-cells are autoequivalences F: C -> C.
This is a subcategory of End_wCat(C).
"""

from __future__ import annotations
from src.local_typing import *
from src._types import *

from ..n_morphisms.category import Category, Morphism_Collection
from ..n_morphisms.functor import Functor
from ..n_morphisms.natural_transformation import NaturalTransformation
from src.abc_specs.w_categories.cells.morphisms import Morphism
from .aut_wcat import AutoFun


class Aut_wCat_x_Morphism_Collection(Morphism_Collection):
    # (-1)-Morphisms
    mn1 = None

    # 0-Morphisms: Autoequivalences F: C -> C

    class m0(Functor.m0_auto, ABC):
        """
        0-morphism in Aut_wCat(C): an autoequivalence F: C -> C.
        
        An autoequivalence is registered here as a 0-cell, and is also
        interpretable as a 1-cell of wCat.
        """
        ...

    m0_endo = Functor.m0_auto  # In Aut, endo is also auto
    m0_auto = Functor.m0_auto

    # 1-Morphisms: Natural isomorphisms η: F -> G between autoequivalences
    m1 = NaturalTransformation.m1_auto
    m1_endo = NaturalTransformation.m1_auto
    m1_auto = NaturalTransformation.m1_auto

    # 2-Morphisms: Modifications (trivial for now)
    m2 = None
    m2_endo = None
    m2_auto = None

    # Hom Categories of Aut_wCat_x
    # Hom_{Aut(C)}(F, G) where F, G are autoequivalences
    hom_c = None        # TODO: NatIso_{Aut(C)} category
    hom_c_xy = None     # TODO: NatIso(F, G) for autoequivalences

    # Endomorphism Categories
    end_c = None        # TODO: End_{Aut(C)}
    end_c_x = None      # TODO: End_{Aut(C)}(F)

    # Automorphism Categories
    aut_c = None        # TODO: Aut_{Aut(C)}
    aut_c_x = None      # TODO: Aut_{Aut(C)}(F)


class Aut_wCat_x(Category.m0):
    """
    The category Aut_wCat(C) for a fixed category C in wCat.
    
    Objects: Autoequivalences F: C -> C.
    Morphisms: Natural isomorphisms between autoequivalences.
    """

    @override
    @abstractmethod
    def amb(self) -> AutoFun: ...

    @override
    @abstractmethod
    def _n_morphism_classes(self) -> type[Aut_wCat_x_Morphism_Collection]: ...
