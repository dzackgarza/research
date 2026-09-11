# Origin: gitclones/integral_lattice/cat/src/abc_specs/w_categories/2_category.py
# Copied 2026-08-20 by the integral_lattice enrichment migration
# (PLAN-corpora-audit-registry, sections R3/R4). Content below is unmodified.
#
# This is a DESIGN RECORD: it states an intended interface, not the built
# preamble. Divergences and recorded errors are listed in the INDEX.md of
# this corpus.


from __future__ import annotations
from src.local_typing import *
from src._types import CategoryABCs


class Possibly_Empty_Two_Category_ABC(ABC):

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
    def as_cell(self) -> CategoryABCs.Cell:
        """View this category as a cell in its ambient category."""
        ...

    @final
    @abstractmethod
    def category_name(self) -> str:
        """Human-readable name of this category."""
        ...

    # === Objects and Morphisms ===

    @abstractmethod
    def objects(self) -> Sequence[CategoryABCs.Object]:
        """All 0-cells (objects) in this category."""
        ...

    @abstractmethod
    def morphisms(self) -> Sequence[CategoryABCs.OneMorphism]:
        """All 1-cells (morphisms) in this category."""
        ...

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


class Nontrivial_Two_Category_ABC(Possibly_Empty_Two_Category_ABC):
    
    # === Methods specific to nontrivial categories ===

    @final
    @abstractmethod
    def forgetful_functor_to_set(self) -> CategoryABCs.Functor:
        """The forgetful functor U: C -> Set."""
        ...

    # === Cell Construction (requires nontrivial category) ===

    @final
    @abstractmethod
    def object_C_from(self, **cell_data: Any) -> CategoryABCs.Object:
        """Construct an object in C from given data."""
        ...

    @final
    @abstractmethod
    def morphism_C_from(self, **cell_data: Any) -> CategoryABCs.Cell:
        """Construct a morphism f: X -> Y in C from given data."""
        ...

    # === Selectors requiring at least one element ===

    @final
    @abstractmethod
    def an_object(self) -> CategoryABCs.Object:
        """Return an arbitrary object in C."""
        ...

    @final
    @abstractmethod
    def a_morphism(self) -> CategoryABCs.OneMorphism:
        """Return an arbitrary morphism in C."""
        ...

    @final
    @abstractmethod
    def random_object(self) -> CategoryABCs.Object:
        """Return a random object in C."""
        ...

    @final
    @abstractmethod
    def random_morphism(self) -> CategoryABCs.OneMorphism:
        """Return a random morphism in C."""
        ...


