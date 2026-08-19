# Origin: gitclones/integral_lattice/cat/src/abc_specs/w_categories/hom_categories/fun_categories/hom_cat_w_xy.py
# Copied 2026-08-20 by the integral_lattice enrichment migration
# (PLAN-corpora-audit-registry, sections R3/R4). Content below is unmodified.
#
# This is a DESIGN RECORD: it states an intended interface, not the built
# preamble. Divergences and recorded errors are listed in the INDEX.md of
# this corpus.

"""
Fun_xy ABC: Fun(C, D) = Hom_{Cat_w}(C, D), the functor category from C to D.

Architecture:
- Fun(C, D) is an object (0-cell) in Fun
- Objects of Fun(C, D) = functors F: C → D
- 1-cells of Fun(C, D) = natural transformations between those functors
- 2-cells of Fun(C, D) = modifications between natural transformations
"""

from __future__ import annotations
from src.local_typing import *
from src._types import CategoryABCs


# =============================================================================
# 0-cells (objects in Fun(C, D) = functors F: C → D)
# =============================================================================



@dataclass
class _Fun_xy_0Cell_ABC(CategoryABCs.HomC_xy.ZeroCell, ABC):
    """
    0-cells in Fun(C, D): functors F: C → D.

    These are the objects of Fun(C, D).
    """

    @classmethod
    def from_object_and_morphism_functions(
        cls,
        F0: Callable[[CategoryABCs.Object], CategoryABCs.Object],
        F1: Callable[[CategoryABCs.OneMorphism], CategoryABCs.OneMorphism],
    ) -> CategoryABCs.Functor:
        """
        Construct a 1-cell from its action on 0-cells and 1-cells.

        Given two functions:
            F0: 0-cells(C) -> 0-cells(D)
            F1: 1-cells(C) -> 1-cells(D)
        return the 1-cell F: C -> D.
        """
        ...

    @final
    @abstractmethod
    def apply_to_object(self, x: CategoryABCs.Object) -> CategoryABCs.Object:
        """Apply to a 0-cell in domain."""
        ...

    @final
    @abstractmethod
    def apply_to_morphism(self, f: CategoryABCs.OneMorphism) -> CategoryABCs.OneMorphism:
        """Apply to a 1-cell in domain."""
        ...

    @final
    @abstractmethod
    def limit(self) -> CategoryABCs.Object:
        """Construct lim F as a 0-cell."""
        ...

    @final
    @abstractmethod
    def colimit(self) -> CategoryABCs.Object:
        """Construct colim F as a category."""
        ...

    @final
    @abstractmethod
    def is_free(self) -> BoolProof: ...

    @final
    @abstractmethod
    def is_forgetful(self) -> BoolProof: ...

    @final
    @abstractmethod
    def is_faithful(self) -> BoolProof: ...

    @final
    @abstractmethod
    def is_full(self) -> BoolProof: ...

    @final
    @abstractmethod
    def is_fully_faithful(self) -> BoolProof: ...

    @final
    @abstractmethod
    def is_essentially_surjective(self) -> BoolProof: ...

    @final
    @abstractmethod
    def is_continuous(self) -> BoolProof: ...

    @final
    @abstractmethod
    def is_cocontinuous(self) -> BoolProof: ...

    @final
    @abstractmethod
    def is_bicontinuous(self) -> BoolProof: ...

    @final
    @abstractmethod
    def is_representable(self) -> BoolProof: ...

    @final
    @abstractmethod
    def representing_object(self) -> CategoryABCs.Object:
        """If representable, return the representing 0-cell."""
        ...

    @final
    @abstractmethod
    def is_contravariant(self) -> bool:
        """True if contravariant (domain is an opposite category)."""
        ...

    @final
    @abstractmethod
    def is_covariant(self) -> bool:
        """True if covariant (not contravariant)."""
        ...


# =============================================================================
# 1-cells (natural transformations η: F ⇒ G)
# =============================================================================


@dataclass
class _Fun_xy_1Cell_ABC(CategoryABCs.HomC_xy, ABC):
    """
    1-cells in Fun(C, D): natural transformations η: F ⇒ G.
    """

    @final
    @abstractmethod
    def component(self, x: CategoryABCs.Object) -> CategoryABCs.OneMorphism:
        """The component at 0-cell x."""
        ...


@dataclass
class _Fun_xy_Endo1Cell_ABC(_Fun_xy_1Cell_ABC, CategoryABCs.EndoNaturalTransformation, ABC):
    """
    Endo-1-cells in Fun(C, D): endo-natural transformations η: F ⇒ F.
    """


@dataclass
class _Fun_xy_Auto1Cell_ABC(_Fun_xy_Endo1Cell_ABC, CategoryABCs.AutoNaturalTransformation, ABC):
    """
    Auto-1-cells in Fun(C, D): natural isomorphisms.
    """


# =============================================================================
# 2-cells (modifications between natural transformations)
# =============================================================================


@dataclass
class _Fun_xy_2Cell_ABC(ABC):
    """
    2-cells in Fun(C, D): modifications between natural transformations.
    """


@dataclass
class _Fun_xy_Endo2Cell_ABC(_Fun_xy_2Cell_ABC, ABC):
    """
    Endo-2-cells in Fun(C, D).
    """


@dataclass
class _Fun_xy_Auto2Cell_ABC(_Fun_xy_Endo2Cell_ABC, ABC):
    """
    Auto-2-cells in Fun(C, D).
    """


# =============================================================================
# Fun(C, D) itself
# =============================================================================


@dataclass
class _Fun_xy_ABC(CategoryABCs.HomC_xy, ABC):
    """
    Fun(C, D) = Hom_{Cat_w}(C, D): The category of functors from C to D.

    This is an object in Fun. Its structure:
    - Domain: category C
    - Codomain: category D
    - Objects (0-cells): functors F: C → D
    - Morphisms (1-cells): natural transformations η: F ⇒ G
    """

    @final
    @abstractmethod
    @override
    def domain(self) -> CategoryABCs.Nontrivial_TwoCategory:
        """The source category C."""
        ...

    @final
    @abstractmethod
    @override
    def codomain(self) -> CategoryABCs.Nontrivial_TwoCategory:
        """The target category D."""
        ...

    @final
    @abstractmethod
    @override
    def objects(self) -> Sequence[_Fun_xy_0Cell_ABC]:
        """All functors F: C → D."""
        ...

    @final
    @abstractmethod
    def morphisms(self) -> Sequence[_Fun_xy_1Cell_ABC]:
        """All natural transformations between functors."""
        ...

    @final
    @abstractmethod
    @override
    def amb(self) -> CategoryABCs.Fun:
        """Return Fun, the ambient category."""
        ...

    @final
    @abstractmethod
    @override
    def object_from_callable(self, f: Any) -> _Fun_xy_0Cell_ABC:
        """Construct a functor from callable."""
        ...


# Semantic exports

# This category:
CategoryDefinition = _Fun_xy_ABC

# Cells
## Objects
ZeroCell = _Fun_xy_0Cell_ABC
## 1-Morphisms
OneCell = _Fun_xy_1Cell_ABC
EndoOneCell = _Fun_xy_Endo1Cell_ABC
AutoOneCell = _Fun_xy_Auto1Cell_ABC
## 2-Morphisms
TwoCell = _Fun_xy_2Cell_ABC
EndoTwoCell = _Fun_xy_Endo2Cell_ABC
AutoTwoCell = _Fun_xy_Auto2Cell_ABC

# Misc Extra
Functor = _Fun_xy_0Cell_ABC
EndoFunctor = _Fun_xy_Endo1Cell_ABC
AutoFunctor = _Fun_xy_Auto1Cell_ABC
NaturalTransformation = _Fun_xy_1Cell_ABC
EndoNaturalTransformation = _Fun_xy_Endo1Cell_ABC
AutoNaturalTransformation = _Fun_xy_Auto1Cell_ABC
Modification = _Fun_xy_2Cell_ABC
EndoModification = _Fun_xy_Endo2Cell_ABC
AutoModification = _Fun_xy_Auto2Cell_ABC

