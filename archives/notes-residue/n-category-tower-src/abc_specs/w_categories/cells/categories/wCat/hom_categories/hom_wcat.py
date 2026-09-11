# Origin: gitclones/integral_lattice/cat/src/abc_specs/w_categories/cells/categories/wCat/hom_categories/hom_wcat.py
# Copied 2026-08-20 by the integral_lattice enrichment migration
# (PLAN-corpora-audit-registry, sections R3/R4). Content below is unmodified.
#
# This is a DESIGN RECORD: it states an intended interface, not the built
# preamble. Divergences and recorded errors are listed in the INDEX.md of
# this corpus.

"""
Hom_wCat category ABC.

Hom_wCat is a category whose 0-cells are Hom_wCat(C, D) categories.
"""

from __future__ import annotations
from src.local_typing import *
from src._types import *

from ..n_morphisms.category import Morphism_Collection, Category
from ..n_morphisms.functor import Functor
from ..n_morphisms.natural_transformation import NaturalTransformation


class Hom_wCat_Morphism_Collection(Morphism_Collection):
    from ._hom_wcat_xy import Hom_wCat_xy

    # (-1)-Morphisms
    mn1 = None

    # 0-Morphisms: Hom_wCat(C, D) categories

    class m0(Hom_wCat_xy):
        """0-morphism in Hom_wCat: a Hom_wCat(C, D) category."""
        @override
        def amb(self) -> Fun: ...

    m0_endo = None
    m0_auto = None

    # 1-Morphisms: Functors between Hom categories
    m1 = Functor.m1
    m1_endo = Functor.m1_endo
    m1_auto = Functor.m1_auto

    # 2-Morphisms: Natural transformations
    m2 = NaturalTransformation.m2
    m2_endo = NaturalTransformation.m2_endo
    m2_auto = NaturalTransformation.m2_auto

    # Hom Categories of Hom_wCat
    # Hom_{Hom_wCat}(F, G) where F, G are Fun(A,B), Fun(C,D) functor categories
    hom_c = None        # TODO; Hom_{Hom_{wCat}} = Hom_{Fun} := Nat
    hom_c_xy = None     # TODO; Hom_{Hom_{wCat}}(F, G) := Nat(F, G)

    # Endomorphism Categories
    end_c = None        # TODO: End_{Hom_{wCat}} := End_{Fun}
    end_c_x = None      # TODO: End_{Hom_{wCat}}(F) := End_{Fun}(F) := EndoNat(F)

    # Automorphism Categories
    aut_c = None        # TODO: Aut_{Hom_{wCat}} := Aut_{Fun}
    aut_c_x = None      # TODO: Aut_{Hom_{wCat}}(F) := Aut_{Fun}(F) := AutoNat(F)


class _Hom_wCat(Category.m0):
    """
    The category Hom_wCat.
    
    Objects: Hom_wCat(C, D) categories for categories C, D in wCat.
    Morphisms: Functors between Hom categories.
    """

    @override
    @abstractmethod
    def _n_morphism_classes(self) -> type[Hom_wCat_Morphism_Collection]: ...


Fun = _Hom_wCat
Fun_xy = Hom_wCat_Morphism_Collection.m0