# Origin: gitclones/integral_lattice/cat/src/abc_specs/w_categories/cells/categories/wCat/hom_categories/_end_wcat_x.py
# Copied 2026-08-20 by the integral_lattice enrichment migration
# (PLAN-corpora-audit-registry, sections R3/R4). Content below is unmodified.
#
# This is a DESIGN RECORD: it states an intended interface, not the built
# preamble. Divergences and recorded errors are listed in the INDEX.md of
# this corpus.

"""
End_wCat(C) category ABC.

End_wCat(C) is a category whose 0-cells are endofunctors F: C -> C.
This is a subcategory of Hom_wCat(C, C).
"""

from __future__ import annotations
from src.local_typing import *
from src._types import *

from ..n_morphisms.category import Category, Morphism_Collection
from ..n_morphisms.functor import Functor
from ..n_morphisms.natural_transformation import NaturalTransformation
from .end_wcat import EndoFun


class End_wCat_x_Morphism_Collection(Morphism_Collection):
    # (-1)-Morphisms
    mn1 = None

    # 0-Morphisms: Endofunctors F: C -> C

    class m0(Functor.m0_endo, ABC):
        """
        0-morphism in End_wCat(C): an endofunctor F: C -> C.
        
        An endofunctor is registered here as a 0-cell, and is also
        interpretable as a 1-cell of wCat.
        """
        ...

    m0_endo = Functor.m0_endo
    m0_auto = Functor.m0_auto

    # 1-Morphisms: Natural transformations η: F -> G between endofunctors
    m1 = NaturalTransformation.m1_endo
    m1_endo = NaturalTransformation.m1_endo
    m1_auto = NaturalTransformation.m1_auto

    # 2-Morphisms: Modifications (trivial for now)
    m2 = None
    m2_endo = None
    m2_auto = None

    # Hom Categories of End_wCat_x
    # Hom_{End(C)}(F, G) where F, G are endofunctors
    hom_c = None        # TODO: Nat_{End(C)} category
    hom_c_xy = None     # TODO: Nat(F, G) for endofunctors

    # Endomorphism Categories
    end_c = None        # TODO: End_{End(C)}
    end_c_x = None      # TODO: End_{End(C)}(F)

    # Automorphism Categories
    aut_c = None        # TODO: Aut_{End(C)}
    aut_c_x = None      # TODO: Aut_{End(C)}(F)


class End_wCat_x(Category.m0):
    """
    The category End_wCat(C) for a fixed category C in wCat.
    
    Objects: Endofunctors F: C -> C.
    Morphisms: Natural transformations between endofunctors.
    """

    @override
    @abstractmethod
    def amb(self) -> EndoFun: ...

    @override
    @abstractmethod
    def _n_morphism_classes(self) -> type[End_wCat_x_Morphism_Collection]: ...