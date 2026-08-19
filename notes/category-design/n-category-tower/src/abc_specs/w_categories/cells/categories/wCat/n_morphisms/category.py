# Origin: gitclones/integral_lattice/cat/src/abc_specs/w_categories/cells/categories/wCat/n_morphisms/category.py
# Copied 2026-08-20 by the integral_lattice enrichment migration
# (PLAN-corpora-audit-registry, sections R3/R4). Content below is unmodified.
#
# This is a DESIGN RECORD: it states an intended interface, not the built
# preamble. Divergences and recorded errors are listed in the INDEX.md of
# this corpus.

"""
Category ABC.

A category is a 0-morphism that contains its own n-morphism types.
"""

from __future__ import annotations
from src.local_typing import *
from src.abc_specs.w_categories.cells.morphisms import Morphism


@dataclass
class Morphism_Collection:
    """Collection of n-morphisms in a category."""
    
    # (-1)-Morphisms
    mn1: type[Morphism.mn1] | None
    # 0-Morphisms
    m0: type[Morphism.m0 | Morphism.n] # Required
    m0_endo: type[Morphism.m0_endo] | None
    m0_auto: type[Morphism.m0_auto] | None
    # 1-Morphisms
    m1: type[Morphism.m1 | Morphism.n] # Required
    m1_endo: type[Morphism.m1_endo | Morphism.n] # Required
    m1_auto: type[Morphism.m1_auto | Morphism.n] # Required
    # 2-Morphisms
    m2: type[Morphism.m2] | None
    m2_endo: type[Morphism.m2_endo] | None
    m2_auto: type[Morphism.m2_auto] | None

    # Hom Categories
    hom_c: type[Category.m0] | None # Required: Hom_C should be an object in wCat.
    hom_c_xy: type[Category.m0] | None # Required: Hom_C(X, Y) should be an object in wCat.

    # Endomorphism Categories
    end_c: type[Category.m0] | None # Required: End_C should be an object in wCat.
    end_c_x: type[Category.m0] | None # Required: End_C(X) should be an object in wCat.

    # Automorphism Categories
    aut_c: type[Category.m0] | None # Required: Aut_C should be an object in wCat.
    aut_c_x: type[Category.m0] | None # Required: Aut_C(X) should be an object in wCat.


class Category:
    """Container for Category as n-arrow types."""

    # (-1)-Morphisms
    mn1 = None

    # =========================================================================
    # 0-Morphisms: Categories as objects
    # =========================================================================

    @dataclass
    class m0(Morphism.m0, ABC):
        """
        A category viewed as a 0-arrow.
        
        A category is a 0-morphism in Cat_w. It declares its own n-morphism types.
        """

        @abstractmethod
        def amb(self) -> Category.m0:
            """The ambient 2-category containing this category."""
            ...

        @abstractmethod
        def _n_morphism_classes(self) -> type[Morphism_Collection]:
            """
            Return the classes of n-morphisms (objects, morphisms, 2-morphisms) in this category,
            along with the classes of endo and auto n-morphisms.
            """
            ...

    m0_endo = None
    m0_auto = None

    # =========================================================================
    # 1-Morphisms: Categories are not 1-arrows
    # =========================================================================

    m1 = None
    m1_endo = None
    m1_auto = None

    # =========================================================================
    # 2-Morphisms: Categories are not 2-arrows
    # =========================================================================

    m2 = None
    m2_endo = None
    m2_auto = None
