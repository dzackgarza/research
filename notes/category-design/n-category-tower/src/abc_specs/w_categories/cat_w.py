# Origin: gitclones/integral_lattice/cat/src/abc_specs/w_categories/cat_w.py
# Copied 2026-08-20 by the integral_lattice enrichment migration
# (PLAN-corpora-audit-registry, sections R3/R4). Content below is unmodified.
#
# This is a DESIGN RECORD: it states an intended interface, not the built
# preamble. Divergences and recorded errors are listed in the INDEX.md of
# this corpus.

"""
wCat cell types: the category of (small) categories.

This is the primary container for all categorical structures. An object in
wCat is simply a category. We work with truncated objects:
- 0-cells: Categories (objects)
- 1-cells: Functors (morphisms between categories)
- 2-cells: Natural Transformations
- All n-cells for n ≥ 2 are assumed invertible (natural isomorphisms)

Category hierarchy (Cat levels):
    Cat_{-2} = ∅                (empty)
    Cat_{-1} = {∅, *}           (truth values)
    Cat_0 = Set                 (sets)
    Cat_1 = Cat                 (1-categories)
    Cat_∞ = wCat                (ω-categories)

This file uses cell terminology internally. Re-exported in _types.py as:
    Category = _wCat_0Cell_ABC
    Functor = _wCat_1Cell_ABC
    NaturalTransformation = _wCat_2Cell_ABC
"""

from __future__ import annotations

from src.local_typing import *
from src._types import BoolProof, CategoryABCs

# =============================================================================
# 0-cells
# =============================================================================

@dataclass
class _Minimal_Cat_W_Zero_Cell_ABC(CategoryABCs.Category, ABC):
    """
    0-cells C in wCat (categories), with possibly C = ∅ the initial category.
    Use this interface if and only if you expect the output of an operation
    to possibly be empty.
    """
    
# =============================================================================
# 0-cells with at least one object (nontrivial categories)
# =============================================================================


@dataclass
class Nontrivial_Cat_W_Zero_Cell_ABC(
    CategoryABCs.Nontrivial_TwoCategory,
    ABC,
):
    """
    0-cells in wCat with at least one object.

    Inherits from all mixin classes providing category operations.
    """

# =============================================================================
# 1-cells (functors: morphisms between categories)
#
# A 1-cell in Cat_w is a 0-cell in Fun(C, D) = Hom_{Cat_w}(C, D)
# =============================================================================


@dataclass
class _Cat_W_1Cell_ABC(
    CategoryABCs.Functor,    ABC,
):
    """
    1-cells in wCat (functors between categories).

    A functor F: C → D is a 0-cell in Fun(C, D) = Hom_{Cat_w}(C, D).
    """



@dataclass
class _Cat_W_Endo1Cell_ABC(
    _Cat_W_1Cell_ABC,
    CategoryABCs.EndoFunctor,
    ABC,
):
    """
    1-cell with source == target (endofunctor).

    Inherits order() and fixed_points() from _Endo_Morphism.
    """


@dataclass
class _Cat_W_Auto1Cell_ABC(
    _Cat_W_Endo1Cell_ABC,
    CategoryABCs.AutoFunctor,
    ABC,
):
    """
    Invertible 1-cell with source == target (autoequivalence).

    Inherits inverse() from _Auto_Morphism.
    Has group structure under composition.
    """


# =============================================================================
# 2-cells (natural transformations: morphisms between functors)
#
# A 2-cell in Cat_w is a 1-cell in Fun(C, D) = Hom_{Cat_w}(C, D)
# =============================================================================


@dataclass
class _Cat_W_2Cell_ABC(
    CategoryABCs.NaturalTransformation,
    ABC,
):
    """
    2-cells in wCat (natural transformations between 1-cells).

    A natural transformation η: F ⇒ G is a 1-cell in Fun(C, D).
    All 2-cells are assumed invertible (natural isomorphisms).
    """

    


@dataclass
class _Cat_W_Endo2Cell_ABC(
    _Cat_W_2Cell_ABC,
    CategoryABCs.EndoNaturalTransformation,
    ABC,
):
    """
    2-cell with source == target (endo-natural transformation).

    Inherits order() and fixed_points() from _Endo_TwoCell.
    """


@dataclass
class _Cat_W_Auto2Cell_ABC(
    _Cat_W_Endo2Cell_ABC,
    CategoryABCs.AutoNaturalTransformation,
    ABC,
):
    """
    Invertible 2-cell with source == target (auto-natural transformation).

    Inherits inverse() from _Auto_TwoCell.
    Has group structure under vertical composition.
    """



# =============================================================================
# wCat itself
# =============================================================================


class _Cat_W_ABC(CategoryABCs.Nontrivial_TwoCategory, ABC):
    """
    wCat, the category of categories.

    Provides operations for constructing and manipulating categories.
    """

    @final
    @abstractmethod
    def known_functors(self) -> Sequence[CategoryABCs.Functor]:
        """All known 1-cells involving this category."""
        ...

    @final
    @abstractmethod
    def functors_from(self, source: CategoryABCs.Nontrivial_TwoCategory) -> Sequence[CategoryABCs.Functor]:
        """All 1-cells from source to this category."""
        ...

    @final
    @abstractmethod
    def functors_to(self, target: CategoryABCs.Nontrivial_TwoCategory) -> Sequence[CategoryABCs.Functor]:
        """All 1-cells from this category to target."""
        ...

    @final
    @abstractmethod
    def op(self, C: CategoryABCs.Nontrivial_TwoCategory) -> CategoryABCs.Nontrivial_TwoCategory:
        """C^op, the opposite category."""
        ...

    @final
    @abstractmethod
    def functor_from(self, **data: Any) -> CategoryABCs.Functor:
        """Construct a 1-cell F: C -> D."""
        ...

    @final
    @abstractmethod
    def natural_transformation_from(self, **data: Any) -> CategoryABCs.NaturalTransformation:
        """Construct a 2-cell η: F => G."""
        ...

    @final
    @abstractmethod
    def yoneda_embedding(self, C: CategoryABCs.Nontrivial_TwoCategory) -> CategoryABCs.Functor:
        """Yoneda embedding Y: C → [C^op, Set]."""
        ...

    @final
    @abstractmethod
    def presheaf_category(self, C: CategoryABCs.Nontrivial_TwoCategory) -> CategoryABCs.Nontrivial_TwoCategory:
        """[C^op, Set], the presheaf category on C."""
        ...

    @final
    @abstractmethod
    def category_of_elements_F(self, F: CategoryABCs.Functor) -> CategoryABCs.Nontrivial_TwoCategory:
        """The category of elements: ∫_C F."""
        ...

    @final
    @abstractmethod
    def category_of_elements_U(self, C: CategoryABCs.Nontrivial_TwoCategory) -> CategoryABCs.Functor:
        """The forgetful functor U: C -> Set."""
        ...

    @final
    @abstractmethod
    def covariant_hom(self, x: CategoryABCs.Object) -> CategoryABCs.Functor:
        """Hom_C(x, -): C -> Set."""
        ...

    @final
    @abstractmethod
    def contravariant_hom(self, x: CategoryABCs.Object) -> CategoryABCs.Functor:
        """Hom_C(-, x): C^op -> Set."""
        ...

    # === Arrow-based predicates (queries about arrows in wCat) ===

    @final
    @abstractmethod
    def subobjects_of(self, x: CategoryABCs.Object) -> Sequence[CategoryABCs.Object]:
        """All subobjects of x in wCat (monomorphisms into x)."""
        ...

    @final
    @abstractmethod
    def quotients_of(self, x: CategoryABCs.Object) -> Sequence[CategoryABCs.Object]:
        """All quotients of x in wCat (epimorphisms out of x)."""
        ...

    @final
    @abstractmethod
    def superobjects_of(self, x: CategoryABCs.Object) -> Sequence[CategoryABCs.Object]:
        """All superobjects containing x in wCat."""
        ...

    @final
    @abstractmethod
    def subcategory_generated_by(self, xs: Sequence[CategoryABCs.Object]) -> CategoryABCs.Object:
        """The subcategory <x>_C generated by x in ambient C."""
        ...

    # === Slice/Coslice/Star Subcategory Formation ===

    @final
    @abstractmethod
    def slice_category_of(
        self, C: CategoryABCs.Category, x: CategoryABCs.Object
    ) -> CategoryABCs.Nontrivial_TwoCategory:
        """Form the slice category C/x."""
        ...

    @final
    @abstractmethod
    def coslice_category(
        self, C: CategoryABCs.Object, x: CategoryABCs.Object
    ) -> CategoryABCs.Nontrivial_TwoCategory:
        """Form the coslice category x/C."""
        ...

    @final
    @abstractmethod
    def star_subcategory(
        self, C: CategoryABCs.Object, x: CategoryABCs.Object
    ) -> CategoryABCs.Nontrivial_TwoCategory:
        """Form the star subcategory around x in C."""
        ...


# Semantic exports

# This category:
CategoryDefinition = _Cat_W_ABC

# Cells
ZeroCell = _Minimal_Cat_W_Zero_Cell_ABC
OneCell = _Cat_W_1Cell_ABC
EndoOneCell = _Cat_W_Endo1Cell_ABC
AutoOneCell = _Cat_W_Auto1Cell_ABC
TwoCell = _Cat_W_2Cell_ABC
EndoTwoCell = _Cat_W_Endo2Cell_ABC
AutoTwoCell = _Cat_W_Auto2Cell_ABC

# Misc Extra
PossiblyEmptyCategory = _Minimal_Cat_W_Zero_Cell_ABC
NontrivialCategory = Nontrivial_Cat_W_Zero_Cell_ABC
Category = PossiblyEmptyCategory
Cat_w = CategoryDefinition

