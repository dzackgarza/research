# Origin: gitclones/integral_lattice/cat/src/abc_specs/w_categories/two_category_interface/minimal_two_category.py
# Copied 2026-08-20 by the integral_lattice enrichment migration
# (PLAN-corpora-audit-registry, sections R3/R4). Content below is unmodified.
#
# This is a DESIGN RECORD: it states an intended interface, not the built
# preamble. Divergences and recorded errors are listed in the INDEX.md of
# this corpus.

from __future__ import annotations
from src.local_typing import *
from src._types import CategoryABCs
from .two_category_mixins import *

class _Minimal_Two_Category_ABC(
    Required_Sage_Methods,
    Basic_Metadata, # E.g. str(self), self == other.
    Object_And_Morphism_Classes, # E.g. self.object_class() must be defined for objects in C.
    Predicates_On_This_Category, # E.g. self.is_groupoid()
    Ambient_Category_Interactions, # E.g. self.product(D) := C x D
    Self_With_Other_Operators, # E.g. self * D := C x D in Cat_w
    Equivalence_Of_Self_With_Other_Checks, # E.g. self.is_equal_to(D) := (self == D)
    ABC):

    @final
    @abstractmethod
    def __post_init__(self) -> None:
        """Validate class-level invariants at construction time."""
        ...

    @final
    @abstractmethod
    def cells(self) -> CategoryABCs.CellContainer:
        """All cells in this category, organized by dimension."""
        ...

    @abstractmethod
    def amb(self) -> CategoryABCs.Category:
        """The ambient category this object lives in."""
        ...

    @final
    @abstractmethod
    def level(self) -> int:
        """The level of this category."""
        ...

    @final
    @abstractmethod
    def category_name(self) -> str:
        """Human-readable name of this category."""
        ...

    # === Objects and Morphisms ===

    @final
    @abstractmethod
    def underlying_object(self) -> Any:
        """Concrete Python/Sage data underlying this category."""
        ...

    # === Dual ===

    @final
    @abstractmethod
    def dual(self, additive: bool = False) -> CategoryABCs.Category:
        """The dual of this category."""
        ...

    @final
    @abstractmethod
    def mor_n(self, n: int) -> CategoryABCs.Category:
        """The category whose objects are n-morphisms in C."""
        ...

    # === Identity and Structure Classes ===

    @final
    @abstractmethod
    def identity_endomorphism_on_self(self) -> CategoryABCs.OneMorphism:
        """Return id_C in End_A(C) where A = self.amb()."""
        ...

    @final
    @abstractmethod
    def generators(self) -> Sequence[CategoryABCs.Object]:
        """Generators of this category."""
        ...


MinimalCategory = _Minimal_Two_Category_ABC
Category = _Minimal_Two_Category_ABC