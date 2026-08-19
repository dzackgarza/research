# Origin: gitclones/integral_lattice/cat/src/abc_specs/w_categories/hom_categories/hom_c_xy.py
# Copied 2026-08-20 by the integral_lattice enrichment migration
# (PLAN-corpora-audit-registry, sections R3/R4). Content below is unmodified.
#
# This is a DESIGN RECORD: it states an intended interface, not the built
# preamble. Divergences and recorded errors are listed in the INDEX.md of
# this corpus.

"""
HomC_xy ABC: The hom-category Hom_C(X,Y) for specific objects X and Y.

Architecture:
- Hom_C(X,Y) is an object (0-cell) in HomC
- Objects of Hom_C(X,Y) = morphisms f: X → Y in base category C
- 1-cells of Hom_C(X,Y) = 2-cells between those morphisms
- 2-cells of Hom_C(X,Y) = 3-cells (modifications) between 2-cells
"""

from __future__ import annotations

from src.local_typing import *
from dataclasses import dataclass

from src._types import CategoryABCs
from .abstract_arrows import *
    

# =============================================================================
# 0-cells (objects in Hom_C(X,Y) = morphisms f: X → Y)
# =============================================================================


@dataclass
class _HomC_xy_0Cell_ABC(ABC):
    """
    0-cells in Hom_C(X,Y): morphisms f: X → Y in the base category C.

    These are the objects of Hom_C(X,Y).
    """

    def as_zero_cell(self) -> CategoryABCs.Cell:
        """Regard this morphism f: x->y as a 0-cell in Hom_C(x,y)"""
        ...

    def as_object(self) -> CategoryABCs.Object:
        """Regard this morphism f: x->y as a point in Hom_C(x,y)"""
        ...

    def as_one_cell(self) -> CategoryABCs.Cell:
        """Regard this morphism f: x->y as a 1-cell in C."""
        ...

    def as_arrow(self) -> OneArrow:
        """Regard this morphism f: x->y as an arrow in C."""
        ...

    def apply_to_element(self, x: Any) -> CategoryABCs.Element:
        ...

class _HomC_xy_Endo_0Cell_ABC(_HomC_xy_0Cell_ABC):

    @override
    def as_arrow(self) -> OneEndoArrow:
        """Regard this morphism f: x->y as an arrow in C."""
        ...

class _HomC_xy_Auto_0Cell_ABC(_HomC_xy_Endo_0Cell_ABC):

    @override
    def as_arrow(self) -> OneAutoArrow:
        """Regard this morphism f: x->y as an arrow in C."""
        ...
# =============================================================================
# 1-cells (2-morphisms in the base category)
# =============================================================================


@dataclass
class _HomC_xy_1Cell_ABC(ABC):
    """
    1-cells in Hom_C(X,Y): 2-cells α: f ⇒ g between morphisms.
    """

    """
    A 2-morphism in a category.
    """

    def as_zero_cell(self) -> CategoryABCs.Cell:
        """Regard this 2-morphism η: f -> g as a 0-cell in Hom_D(f, g) where D := Hom_C(x,y)."""
        ...
    
    def as_object(self) -> CategoryABCs.Object:
        """Regard this 2-morphism η: f -> g as an object in Hom_D(f, g) where D := Hom_C(x,y)."""
        ...

    def as_one_cell(self) -> CategoryABCs.Cell:
        """Regard this 2-morphism η: f -> g as a 1-cell in Arr_C."""
        ...

    def as_arrow(self) -> OneArrow:
        """Regard this 2-morphism η: f -> g as an arrow in Arr_C."""
        ...
    
    def as_two_cell(self) -> CategoryABCs.Cell:
        """Regard this 2-morphism η: f -> g as a 2-cell in C."""
        ...
    
    def as_two_arrow(self) -> TwoArrow:
        """Regard this 2-morphism η: f -> g as a 2-arrow in C."""
        ...


@dataclass
class _HomC_xy_Endo1Cell_ABC(_HomC_xy_1Cell_ABC, ABC):
    """
    Endo-1-cells in Hom_C(X,Y): endo-2-cells α: f ⇒ f.
    """

    @override
    def as_arrow(self) -> OneEndoArrow:
        """Regard this 2-morphism η: f -> f as an arrow in Arr_C."""
        ...

    @override
    def as_two_cell(self) -> CategoryABCs.Cell:
        """Regard this 2-morphism η: f -> f as a 2-cell in C."""
        ...



@dataclass
class _HomC_xy_Auto1Cell_ABC(_HomC_xy_Endo1Cell_ABC, ABC):
    """
    Auto-1-cells in Hom_C(X,Y): invertible 2-cells.
    """

    @override
    def as_arrow(self) -> OneAutoArrow:
        """Regard this 2-morphism η: f -> f as an arrow in Arr_C."""
        ...

    @override
    def as_two_cell(self) -> CategoryABCs.Cell:
        """Regard this 2-morphism η: f -> f as a 2-cell in C."""
        ...



# =============================================================================
# 2-cells (3-morphisms / modifications)
# =============================================================================


@dataclass
class _HomC_xy_2Cell_ABC(ABC):
    """
    2-cells in Hom_C(X,Y): modifications between 2-cells.
    """
    ...


@dataclass
class _HomC_xy_Endo2Cell_ABC(_HomC_xy_2Cell_ABC, ABC):
    """
    Endo-2-cells in Hom_C(X,Y).
    """
    ...


@dataclass
class _HomC_xy_Auto2Cell_ABC(_HomC_xy_Endo2Cell_ABC, ABC):
    """
    Auto-2-cells in Hom_C(X,Y).
    """
    ...


# =============================================================================
# Hom_C(X,Y) itself
# =============================================================================


@dataclass
class _HomC_xy_ABC(CategoryABCs.Nontrivial_TwoCategory, ABC):
    """
    Hom_C(X,Y): The category of morphisms from X to Y.

    This is an object (0-cell) in HomC. Its structure:
    - Domain: object X in base category C
    - Codomain: object Y in base category C
    - Objects (0-cells): morphisms f: X → Y in C
    - Morphisms (1-cells): 2-cells between those morphisms
    """

    @abstractmethod
    def domain(self) -> CategoryABCs.Object:
        """The source object X in the base category."""
        ...

    @abstractmethod
    def codomain(self) -> CategoryABCs.Object:
        """The target object Y in the base category."""
        ...

    @abstractmethod
    def objects(self) -> Sequence[_HomC_xy_0Cell_ABC]:
        """All morphisms f: X → Y in C."""
        ...

    @abstractmethod
    def amb(self) -> CategoryABCs.HomC:
        """Return HomC, the ambient category this Hom_C(X,Y) lives in."""
        ...

    @abstractmethod
    def object_from_callable(self, f: Callable[[Any], Any]) -> _HomC_xy_0Cell_ABC:
        """Construct a morphism X → Y from callable."""
        ...


# Semantic exports

# This category:
CategoryDefinition = _HomC_xy_ABC

# Cells
## Objects
PlainZeroCell = _HomC_xy_0Cell_ABC
EndoZeroCell = _HomC_xy_Endo_0Cell_ABC
AutoZeroCell = _HomC_xy_Auto_0Cell_ABC
ZeroCell = PlainZeroCell | EndoZeroCell | AutoZeroCell
## 1-Morphisms
PlainOneCell = _HomC_xy_1Cell_ABC
EndoOneCell = _HomC_xy_Endo1Cell_ABC
AutoOneCell = _HomC_xy_Auto1Cell_ABC
OneCell = PlainOneCell | EndoOneCell | AutoOneCell
## 2-Morphisms
PlainTwoCell = _HomC_xy_2Cell_ABC
EndoTwoCell = _HomC_xy_Endo2Cell_ABC
AutoTwoCell = _HomC_xy_Auto2Cell_ABC
TwoCell = PlainTwoCell | EndoTwoCell | AutoTwoCell

# Misc Extra
PlainOneMorphism = PlainZeroCell
EndoOneMorphism = EndoZeroCell
AutoOneMorphism = AutoZeroCell
OneMorphism = PlainOneMorphism | EndoOneMorphism | AutoOneMorphism

PlainTwoMorphism = PlainOneCell
EndoTwoMorphism = EndoOneCell
AutoTwoMorphism = AutoOneCell
TwoMorphism = PlainTwoMorphism | EndoTwoMorphism | AutoTwoMorphism
