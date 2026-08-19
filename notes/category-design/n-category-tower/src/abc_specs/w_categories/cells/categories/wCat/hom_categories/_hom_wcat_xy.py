# Origin: gitclones/integral_lattice/cat/src/abc_specs/w_categories/cells/categories/wCat/hom_categories/_hom_wcat_xy.py
# Copied 2026-08-20 by the integral_lattice enrichment migration
# (PLAN-corpora-audit-registry, sections R3/R4). Content below is unmodified.
#
# This is a DESIGN RECORD: it states an intended interface, not the built
# preamble. Divergences and recorded errors are listed in the INDEX.md of
# this corpus.

"""
Hom_wCat(C, D) category ABC.

Hom_wCat(C, D) is a category whose 0-cells are functors F: C -> D.
This is the functor category Fun(C, D).
"""

from __future__ import annotations
from src.local_typing import *
from src._types import *

from ..n_morphisms.category import Category, Morphism_Collection
from ..n_morphisms.functor import Functor
from ..n_morphisms.natural_transformation import NaturalTransformation
from src.abc_specs.w_categories.cells.morphisms import Morphism
from .hom_wcat import Fun


class Hom_wCat_xy_Morphism_Collection(Morphism_Collection):
    # (-1)-Morphisms
    mn1 = None

    # 0-Morphisms: Functors F: C -> D

    class m0(Functor.m0, ABC):
        """
        0-morphism in Hom_wCat(C, D): a functor F: C -> D.
        
        A functor is registered here as a 0-cell, and is also
        interpretable as a 1-cell of wCat.
        """
        ...

    m0_endo = Functor.m0_endo
    m0_auto = Functor.m0_auto

    # 1-Morphisms: Natural transformations η: F -> G
    m1 = NaturalTransformation.m1
    m1_endo = NaturalTransformation.m1_endo
    m1_auto = NaturalTransformation.m1_auto

    # 2-Morphisms: Modifications (trivial for now)
    m2 = None
    m2_endo = None
    m2_auto = None

    # Hom Categories of Hom_wCat_xy
    # Hom_{Fun(C,D)}(F, G) where F, G are functors
    hom_c = None        # TODO: Nat(C, D) category
    hom_c_xy = None     # TODO: Nat(F, G) = natural transformations from F to G

    # Endomorphism Categories
    end_c = None        # TODO: End_{Fun(C,D)}
    end_c_x = None      # TODO: End_{Fun(C,D)}(F)

    # Automorphism Categories
    aut_c = None        # TODO: Aut_{Fun(C,D)}
    aut_c_x = None      # TODO: Aut_{Fun(C,D)}(F)


class Hom_wCat_xy(Category.m0):
    """
    The category Hom_wCat(C, D) for fixed categories C, D in wCat.
    
    Objects: Functors F: C -> D.
    Morphisms: Natural transformations between functors.
    """

    @override
    @abstractmethod
    def amb(self) -> Fun: ...

    @override
    @abstractmethod
    def _n_morphism_classes(self) -> type[Hom_wCat_xy_Morphism_Collection]: ...
