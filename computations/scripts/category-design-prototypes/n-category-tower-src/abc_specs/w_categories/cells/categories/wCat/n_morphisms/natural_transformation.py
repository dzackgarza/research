# Origin: gitclones/integral_lattice/cat/src/abc_specs/w_categories/cells/categories/wCat/n_morphisms/natural_transformation.py
# Copied 2026-08-20 by the integral_lattice enrichment migration
# (PLAN-corpora-audit-registry, sections R3/R4). Content below is unmodified.
#
# This is a DESIGN RECORD: it states an intended interface, not the built
# preamble. Divergences and recorded errors are listed in the INDEX.md of
# this corpus.

"""
Natural Transformation ABC.

A natural transformation can be viewed as:
- 0-arrow in a Hom category 
- 1-arrow in Fun(C, D)
- 2-arrow in Cat_w
"""

from __future__ import annotations
from src.local_typing import *
from src._types import BoolProof
from src.abc_specs.w_categories.cells.morphisms import Morphism


class NaturalTransformation:
    """Container for Natural Transformation as n-arrow types."""

    # (-1)-Morphisms
    mn1 = None

    # =========================================================================
    # 0-Morphisms: Natural transformations as objects
    # =========================================================================

    class m0(Morphism.m0, ABC):
        """
        A natural transformation viewed as a 0-arrow.
        
        In this context (as object in a Hom category), has object-level operations.
        """
        pass

    class m0_endo(Morphism.m0_endo, ABC):
        """
        An endo-natural transformation viewed as a 0-arrow.
        """
        pass

    class m0_auto(Morphism.m0_auto, ABC):
        """
        An auto-natural transformation viewed as a 0-arrow.
        """
        pass

    # =========================================================================
    # 1-Morphisms: Natural transformations as morphisms
    # =========================================================================

    class m1(Morphism.m1, ABC):
        """
        A natural transformation viewed as a 1-arrow.
        
        In this context (as morphism in Fun(C, D)), has morphism-level operations.
        """
        pass

    class m1_endo(Morphism.m1_endo, ABC):
        """
        An endo-natural transformation viewed as a 1-arrow.
        """
        pass

    class m1_auto(Morphism.m1_auto, ABC):
        """
        An auto-natural transformation viewed as a 1-arrow.
        """
        pass

    # =========================================================================
    # 2-Morphisms: Natural transformations as 2-arrows
    # =========================================================================

    class m2(Morphism.m2, ABC):
        """
        A natural transformation viewed as a 2-arrow (in Cat_w).
        
        In this context, has 2-morphism-level operations.
        """

        @abstractmethod
        def component_function(self) -> Callable[[Morphism.m0], Morphism.m1]:
            """
            Given η: F -> G for F, G: C -> D, return the function 
            X -> (η_X: F(X) -> G(X)).
            """

        @abstractmethod
        def is_natural_isomorphism(self) -> BoolProof:
            """Check if all components are isomorphisms."""
            ...

    class m2_endo(Morphism.m2_endo, ABC):
        """
        An endo-natural transformation viewed as a 2-arrow.
        """
        pass

    class m2_auto(Morphism.m2_auto, ABC):
        """
        An auto-natural transformation viewed as a 2-arrow.
        """
        pass