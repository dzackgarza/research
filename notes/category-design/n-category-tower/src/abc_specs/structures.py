# Origin: gitclones/integral_lattice/cat/src/abc_specs/structures.py
# Copied 2026-08-20 by the integral_lattice enrichment migration
# (PLAN-corpora-audit-registry, sections R3/R4). Content below is unmodified.
#
# This is a DESIGN RECORD: it states an intended interface, not the built
# preamble. Divergences and recorded errors are listed in the INDEX.md of
# this corpus.

"""
Structure ABCs for categorical objects.

Per implementation_spec.md §Structures on Objects (lines 102-230).

These are pure ABCs. Implementations go in bases/structures.py.
"""

from __future__ import annotations

from src._types import CategoryABCs
from src.local_typing import *


# === Terminal/Initial/Zero ===


class _TerminalCategory_ABC(ABC):
    """
    An identification Z = *.
    Note that this is an additional STRUCTURE on a category, exhibiting a PROOF that it satisfies a terminal property in its AMBIENT category.
    This is NOT an interface specifically for THE terminal category * in Cat_w.
    """

    @final
    @abstractmethod
    def unique_morphism_from(self, x: CategoryABCs.Object) -> CategoryABCs.OneMorphism:
        """
        The unique morphism *_X: X → *.
        """
        ...


class _InitialCategory_ABC(ABC):
    """
    An identification Z = ∅.
    Note that this is an additional STRUCTURE on a category.
    This is NOT an interface specifically for the initial category ∅ in Catw.
    """

    @final
    @abstractmethod
    def unique_morphism_to(self, x: CategoryABCs.Object) -> CategoryABCs.OneMorphism:
        """The unique morphism ∅_X: ∅ → X."""
        ...


class _ZeroCategory_ABC(_TerminalCategory_ABC, _InitialCategory_ABC, ABC):
    """
    An identification Z = 0.

    Has both unique_morphism_to (0_X: 0 → X) and unique_morphism_from (X_0: X → 0).
    """

    pass


# === Slice/Coslice ===


class _SliceCategory_ABC(ABC):
    """
    A fixed lift of Z in C to (Z, π: Z → c) in C_{/c}.
    """

    @final
    @abstractmethod
    def structure_morphism(self) -> CategoryABCs.OneMorphism:
        """π: X → c."""
        ...

    @final
    @abstractmethod
    def base_object(self) -> CategoryABCs.Object:
        """c."""
        ...


class _CosliceCategory_ABC(ABC):
    """
    A fixed lift of Z in C to (Z, ι: c → Z) in C_{c/}.
    """

    @final
    @abstractmethod
    def structure_morphism(self) -> CategoryABCs.OneMorphism:
        """ι: c → X."""
        ...

    @final
    @abstractmethod
    def apex_object(self) -> CategoryABCs.Object:
        """c."""
        ...


# === Spans/Cospans ===


class _SpanObject_ABC(ABC):
    """
    A fixed lift of Z in C to (Z, f: Z → X, g: Z → Y) in C_{/X, /Y}.
    Write as X ← Z → Y.
    """

    @final
    @abstractmethod
    def left_morphism(self) -> CategoryABCs.OneMorphism:
        """f: Z → X."""
        ...

    @final
    @abstractmethod
    def right_morphism(self) -> CategoryABCs.OneMorphism:
        """g: Z → Y."""
        ...

    @final
    @abstractmethod
    def apex(self) -> CategoryABCs.Object:
        """Z."""
        ...


class _CospanCategory_ABC(ABC):
    """
    A fixed lift of Z in C to (Z, f: X → Z, g: Y → Z) in C_{X/, Y/}.
    Write as X → Z ← Y.
    """

    @final
    @abstractmethod
    def left_morphism(self) -> CategoryABCs.OneMorphism:
        """f: X → Z."""
        ...

    @final
    @abstractmethod
    def right_morphism(self) -> CategoryABCs.OneMorphism:
        """g: Y → Z."""
        ...

    @final
    @abstractmethod
    def nadir(self) -> CategoryABCs.Object:
        """Z."""
        ...


# === Pullback/Pushout ===


class _PullbackCategory_ABC(ABC):
    """
    A fixed identification A = X_1 ×_Z X_2.
    """

    @final
    @abstractmethod
    def cospan(self) -> CategoryABCs.Cospan:
        """The cospan X_1 → Z ← X_2."""
        ...

    @final
    @abstractmethod
    def projection_morphism(self, i: int) -> CategoryABCs.OneMorphism:
        """π_i: A = X_1 ×_Z X_2 → X_i."""
        ...

    @final
    @abstractmethod
    def lift_morphisms(
        self, f: CategoryABCs.OneMorphism, g: CategoryABCs.OneMorphism
    ) -> CategoryABCs.OneMorphism:
        """Given f: B → X_1, g: B → X_2 with f ∘ π_1 = g ∘ π_2, return h: B → A."""
        ...


class _PushoutCategory_ABC(ABC):
    """
    A fixed identification A = X_1 +^Z X_2.
    """

    @final
    @abstractmethod
    def span(self) -> CategoryABCs.Span:
        """The span X_1 ← Z → X_2."""
        ...

    @final
    @abstractmethod
    def inclusion_morphism(self, i: int) -> CategoryABCs.OneMorphism:
        """ι_i: X_i → A = X_1 +^Z X_2."""
        ...

    @final
    @abstractmethod
    def lift_morphisms(
        self, f: CategoryABCs.OneMorphism, g: CategoryABCs.OneMorphism
    ) -> CategoryABCs.OneMorphism:
        """Given f: X_1 → B, g: X_2 → B with ι_1 ∘ f = ι_2 ∘ g, return h: A → B."""
        ...


# === Product/Coproduct ===


class _ProductCategory_ABC(CategoryABCs.Object, ABC):
    """
    A fixed decomposition X = ∏_i X_i.
    """

    @final
    @abstractmethod
    def objects(self) -> Sequence[Sequence[CategoryABCs.ZeroCell]]: # type: ignore[TODO]
        """
        Objects in in X are sequences [x_1, x_2, ...] of objects in X_i.
        """
        ...

    @final
    @abstractmethod
    def product_factors(self) -> Sequence[CategoryABCs.Object]:
        """The factor objects [X_1, X_2, ...]."""
        ...

    @final
    @abstractmethod
    def projection_morphism(self, i: int) -> CategoryABCs.OneMorphism:
        """π_i: X → X_i."""
        ...

    @final
    @abstractmethod
    def lift_morphisms(self, morphisms: Sequence[CategoryABCs.OneMorphism]) -> CategoryABCs.OneMorphism:
        """Given f_i: Y → X_i, return f: Y → ∏ X_i."""
        ...


class _CoproductCategory_ABC(ABC):
    """
    A fixed decomposition X = ∐_i X_i.
    """

    @final
    @abstractmethod
    def coproduct_factors(self) -> Sequence[CategoryABCs.Object]:
        """The factor objects [X_1, X_2, ...]."""
        ...

    @final
    @abstractmethod
    def inclusion_morphism(self, i: int) -> CategoryABCs.OneMorphism:
        """ι_i: X_i → X."""
        ...

    @final
    @abstractmethod
    def colift_morphisms(self, morphisms: Sequence[CategoryABCs.OneMorphism]) -> CategoryABCs.OneMorphism:
        """Given f_i: X_i → Y, return f: ∐ X_i → Y."""
        ...


# === Tensor/DirectSum ===


class _TensorProductCategory_ABC(ABC):
    """
    A fixed decomposition X = ⨂_i X_i.
    """

    @final
    @abstractmethod
    def tensor_factors(self) -> Sequence[CategoryABCs.Object]:
        """The factor objects [X_1, X_2, ...]."""
        ...

    @final
    @abstractmethod
    def lift_product_morphism(self, f: CategoryABCs.OneMorphism) -> CategoryABCs.OneMorphism:
        """Given bilinear f: X_1 × X_2 → Y, return f': X_1 ⊗ X_2 → Y."""
        ...


class _DirectSumCategory_ABC(ABC):
    """
    A fixed decomposition X = ⊕_i X_i.
    """

    @final
    @abstractmethod
    def factors(self) -> tuple[CategoryABCs.Object, ...]:
        """The factor objects [X_1, X_2, ...]."""
        ...

    @final
    @abstractmethod
    def lift_source_morphisms(
        self, morphisms: Sequence[CategoryABCs.OneMorphism]
    ) -> CategoryABCs.OneMorphism:
        """Given f_i: X_i → Y, return f: ⊕ X_i → Y."""
        ...

    @final
    @abstractmethod
    def lift_target_morphisms(
        self, morphisms: Sequence[CategoryABCs.OneMorphism]
    ) -> CategoryABCs.OneMorphism:
        """Given f_i: Y → X_i, return f: Y → ⊕ X_i."""
        ...

    @final
    @abstractmethod
    def morphism_from_matrix(
        self, matrix: Sequence[Sequence[CategoryABCs.OneMorphism]]
    ) -> CategoryABCs.OneMorphism:
        """Given f_{ij}: X_i → Y_j, return f: ⊕_i X_i → ⊕_j Y_j."""
        ...

_ = _ZeroCategory_ABC
_ = _SliceCategory_ABC
_ = _CosliceCategory_ABC
_ = _SpanObject_ABC
_ = _CospanCategory_ABC
_ = _PullbackCategory_ABC
_ = _PushoutCategory_ABC
_ = _ProductCategory_ABC
_ = _CoproductCategory_ABC
_ = _TensorProductCategory_ABC
_ = _DirectSumCategory_ABC
