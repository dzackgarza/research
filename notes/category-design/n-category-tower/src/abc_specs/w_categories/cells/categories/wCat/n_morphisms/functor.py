# Origin: gitclones/integral_lattice/cat/src/abc_specs/w_categories/cells/categories/wCat/n_morphisms/functor.py
# Copied 2026-08-20 by the integral_lattice enrichment migration
# (PLAN-corpora-audit-registry, sections R3/R4). Content below is unmodified.
#
# This is a DESIGN RECORD: it states an intended interface, not the built
# preamble. Divergences and recorded errors are listed in the INDEX.md of
# this corpus.

"""
Functor ABC.

A functor can be viewed as:
- 0-arrow in Fun(C, D)
- 1-arrow in Cat_w
"""

from __future__ import annotations
from src.abc_specs.w_categories.cells.morphisms import Morphism
from src.local_typing import *
from src._types import BoolProof


class Functor:
    """Container for Functor as n-arrow types."""

    # (-1)-Morphisms
    mn1 = None

    # =========================================================================
    # 0-Morphisms: Functors as objects
    # =========================================================================

    class m0(Morphism.m0, ABC):
        """
        A functor viewed as a 0-arrow (object in Fun(C, D)).
        
        In this context, functor has object-level operations.
        """
        pass

    class m0_endo(m0, Morphism.m0_endo, ABC):
        """
        An endofunctor viewed as a 0-arrow (object in End(C)).
        """
        pass

    class m0_auto(m0_endo, Morphism.m0_auto, ABC):
        """
        An autofunctor viewed as a 0-arrow (object in Aut(C)).
        """
        pass

    # =========================================================================
    # 1-Morphisms: Functors as morphisms
    # =========================================================================

    class m1(Morphism.m1, ABC):
        """
        A functor viewed as a 1-arrow (morphism in Cat_w).
        
        In this context, functor has morphism-level operations.
        """

        def function_on_objects(self) -> Callable[[Morphism.m0], Morphism.m0]: ...
        def function_on_morphisms(self) -> Callable[[Morphism.m1], Morphism.m1]: ...

        @abstractmethod
        def is_faithful(self) -> BoolProof:
            """Check if this functor is faithful."""
            ...

        @abstractmethod
        def is_full(self) -> BoolProof:
            """Check if this functor is full."""
            ...

    class m1_endo(m1, Morphism.m1_endo, ABC):
        """
        An endofunctor viewed as a 1-arrow (morphism in Cat_w).
        """
        ...

    class m1_auto(m1_endo, Morphism.m1_auto, ABC):
        """
        An autofunctor viewed as a 1-arrow (morphism in Cat_w).
        """
        ...

    # =========================================================================
    # 2-Morphisms: Functors are not 2-morphisms
    # =========================================================================

    m2 = None
    m2_endo = None
    m2_auto = None