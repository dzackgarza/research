# Origin: gitclones/integral_lattice/cat/src/abc_specs/w_categories/cells/categories/wCat/hom_categories/end_wcat.py
# Copied 2026-08-20 by the integral_lattice enrichment migration
# (PLAN-corpora-audit-registry, sections R3/R4). Content below is unmodified.
#
# This is a DESIGN RECORD: it states an intended interface, not the built
# preamble. Divergences and recorded errors are listed in the INDEX.md of
# this corpus.

"""
End_wCat category ABC.

End_wCat is a category whose 0-cells are End_wCat(C) categories.
"""

from __future__ import annotations
from src.local_typing import *
from src._types import *

from ..n_morphisms.category import Category, Morphism_Collection
from ..n_morphisms.functor import Functor
from ..n_morphisms.natural_transformation import NaturalTransformation


class End_wCat_Morphism_Collection(Morphism_Collection):
    from ._end_wcat_x import End_wCat_x

    # (-1)-Morphisms
    mn1 = None

    # 0-Morphisms: End_wCat(C) categories

    class m0(End_wCat_x):
        """0-morphism in End_wCat: an End_wCat(C) category."""
        @override
        def amb(self) -> EndoFun: ...

    m0_endo = None
    m0_auto = None

    # 1-Morphisms: Functors between End categories
    m1 = Functor.m1
    m1_endo = Functor.m1_endo
    m1_auto = Functor.m1_auto

    # 2-Morphisms: Natural transformations
    m2 = NaturalTransformation.m2
    m2_endo = NaturalTransformation.m2_endo
    m2_auto = NaturalTransformation.m2_auto

    # Hom Categories of End_wCat
    # Hom_{End_wCat}(F, G) where F, G are End(A), End(B) endofunctor categories
    hom_c = None        # TODO: Hom_{End_{wCat}}
    hom_c_xy = None     # TODO: Hom_{End_{wCat}}(F, G)

    # Endomorphism Categories
    end_c = None        # TODO: End_{End_{wCat}}
    end_c_x = None      # TODO: End_{End_{wCat}}(F)

    # Automorphism Categories
    aut_c = None        # TODO: Aut_{End_{wCat}}
    aut_c_x = None      # TODO: Aut_{End_{wCat}}(F)


class _End_wCat(Category.m0):
    """
    The category End_wCat.
    
    Objects: End_wCat(C) categories for categories C in wCat.
    Morphisms: Functors between endofunctor categories.
    """

    @override
    @abstractmethod
    def _n_morphism_classes(self) -> type[End_wCat_Morphism_Collection]: ...


EndoFun = _End_wCat
EndoFun_x = End_wCat_Morphism_Collection.m0
