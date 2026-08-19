# Origin: gitclones/integral_lattice/cat/src/abc_specs/new_w_categories/old_interfaces/__arrows.py
# Copied 2026-08-20 by the integral_lattice enrichment migration
# (PLAN-corpora-audit-registry, sections R3/R4). Content below is unmodified.
#
# This is a DESIGN RECORD: it states an intended interface, not the built
# preamble. Divergences and recorded errors are listed in the INDEX.md of
# this corpus.

"""
Arrow ABCs.

Arrows are primitive to C (not extending cells).
They provide dimension-specific operations.
n-Morphisms inherit from Arrows.
"""

from __future__ import annotations

from src._types import BoolProof
from src.local_typing import *

from .___cells import Cell
from .scaffolding import wCategory

# =============================================================================
# Arrow ABCs
# =============================================================================

# A category C is a collection of objects and an assignment of a category Hom_C(x,y) for each pair of objects x,y in C.
# An 0-arrow is an object in a category.
# A 1-arrow is a morphism between 0-arrows, say f: x->y where x,y in C and f in Hom_C(x,y).
# A 2-arrow is a morphism between 1-arrows, say η: f->g where f,g in Hom_C(x,y) and η in Hom_{Hom_C(x,y)}(f, g).
# ... (etc)
# Thus given a 2-arrow η, it can be regarded as:
# 1. A 2-arrow η: f->g in C,
# 2. A 1-arrow η: f->g in Hom_C(x,y),
# 3. A 0-arrow η: x->y in Hom_{Hom_C(x,y)}(f, g).
# Conversely, given a 0-arrow x, it can be regarded as:
# 1. A 0-arrow x in C,
# 2. A 1-arrow x in ΣC := {0 ->_y 1 | y in C}, the category with two objects 0 and 1 and morphisms 0 ->_y 1 for each y in C.
# 3. A 2-arrow x in ...

class _nArrow(ABC):
    """Arrow: primitive notion in C with dimension-specific operations."""

    @abstractmethod
    def source(self) -> _nArrow:
        ...

    @abstractmethod
    def target(self) -> _nArrow:
        ...

    @abstractmethod
    def underlying_data(self) -> Any:
        """Return the underlying data of this arrow."""
        ...

    @abstractmethod
    def as_cell(self) -> Cell.n:
        """Convert this arrow to a cell."""
        ...

    @abstractmethod
    def suspend(self) -> Arrow.n:
        """
        Any n-arrow f: x->y in C can be regarded as an (n+1)-arrow in ΣC.
        In particular, a 0-arrow in Hom_C(x,y) ≤ Arr(C) can be regarded as a 1-arrow in C.
        """
        ...

    @abstractmethod
    def desuspend(self) -> Arrow.n:
        """
        Any n-arrow f: x->y in C can be regarded as an (n-1) arrow in Arr(C).
        In particular, a 1-arrow in C is equivalent to a 0-arrow in Hom_C(x,y) for some x,y.
        """
        ... 

    @abstractmethod
    def amb(self) -> wCategory:
        """
        The ambient category containing this arrow, if n >= 0.
        If n = -1, return the ambient category of the parent object.
        """
        ...

class _NegativeOneArrow(_nArrow, ABC):
    """(-1)-arrow: the empty/terminal arrow. source = target = self."""
    _underlying_data: Any
    _parent_object: Arrow.n0

    def parent_object(self) -> Arrow.n0:
        return self._parent_object

    @override
    @final
    def source(self) -> Self:
        return self

    @override
    @final
    def target(self) -> Self:
        return self

    @override
    @final
    def suspend(self) -> Arrow.n0 | Self:
        # This object is always x in X, an object of C. Possibilities:
        # - X itself is a category; then re-interpret x as an object of X.
        # - x is the desuspension of some object y in C, in which case
        #   the underlying data of x is assumed to be y. Return y.
        # - Else: force X to be interpreted as a category with objects X.
        if isinstance(self._parent_object, wCategory):
            return self._parent_object.object_from(self.underlying_data())
        elif isinstance(self._underlying_data, Arrow.n0):
            return self._underlying_data
        else:
            X = wCategory.

    @override
    @final
    def desuspend(self) -> Self:
        return self

    @override
    @final
    def as_cell(self) -> Cell.mn1:
        return Cell.mn1() # type: ignore[TODO]


class _ZeroArrow(_nArrow, ABC):
    """0-arrow: object operations."""

    @override
    @abstractmethod
    def source(self) -> Arrow.m1:
        ...

    @override
    @abstractmethod
    def target(self) -> Arrow.m1:
        ...

    @override
    @abstractmethod
    def as_cell(self) -> Cell.m0:
        """Convert this arrow to a cell."""
        ...

    @override
    @abstractmethod
    def suspend(self) -> Arrow.n1: ...

    @override
    @abstractmethod
    def desuspend(self) -> Arrow.m1: ...

    @abstractmethod
    def identity_arrow(self) -> Arrow.n1:
        """Return the identity arrow on this object."""
        ...

    @abstractmethod
    def some_elements(self) -> Iterable[Arrow.m1]:
        """Return some elements of this object."""
        ...

class _OneArrow(_nArrow, ABC):
    """1-arrow: morphism operations."""

    @override
    @abstractmethod
    def source(self) -> Arrow.n0:
        ...

    @override
    @abstractmethod
    def target(self) -> Arrow.n0:
        ...

    @override
    @abstractmethod
    def as_cell(self) -> Cell.m1:
        """Convert this arrow to a cell."""
        ...

    @override
    @abstractmethod
    def suspend(self) -> Arrow.n2: ...

    @override
    @abstractmethod
    def desuspend(self) -> Arrow.n0: ...

    @abstractmethod
    def compose(self, other: Annotated[Any, lambda self: isinstance(self, Arrow.n1)]) -> Self:
        """Compose this morphism with another."""
        ...
    
    @abstractmethod
    def apply(self, x: Annotated[Any, lambda self: isinstance(self, Arrow.m1)]) -> Arrow.m1:
        """Apply this morphism to an element/object."""
        ...

    @abstractmethod
    def is_surjective(self) -> BoolProof:
        """Check if this morphism is surjective."""
        ...

    @abstractmethod
    def is_injective(self) -> BoolProof:
        """Check if this morphism is injective."""
        ...


class _Endomorphism_Mixin(ABC):
    @abstractmethod
    def is_unipotent(self) -> BoolProof: ...

class _Automorphism_Mixin(ABC):
    @abstractmethod
    def inverse(self) -> Self: ...


class _Endo_OneArrow(_OneArrow, _Endomorphism_Mixin, ABC):
    """
    1-arrow f: x -> x in C.
    """
    ...

class _Auto_OneArrow(_Endo_OneArrow, _Automorphism_Mixin, ABC):
    """Invertible 1-arrow f: x -> x in C."""
    ...


class _TwoArrow(_nArrow, ABC):
    """2-arrow: 2-morphism operations."""

    @override
    @abstractmethod
    def source(self) -> Arrow.n1:
        ...

    @override
    @abstractmethod
    def target(self) -> Arrow.n1:
        ...
    
    @override
    @abstractmethod
    def as_cell(self) -> Cell.m2:
        """Convert this arrow to a cell."""
        ...

    @override
    @abstractmethod
    def suspend(self) -> Arrow.m1: ...

    @override
    @abstractmethod
    def desuspend(self) -> Arrow.n1: ...

    @abstractmethod
    def vertically_compose(self, other: Self) -> Self:
        """Vertical composition of 2-morphisms."""
        ...

    @abstractmethod
    def horizontally_compose(self, other: Self) -> Self:
        """Horizontal composition of 2-morphisms."""
        ...

class _Endo_TwoArrow(_TwoArrow, _Endomorphism_Mixin, ABC):
    """
    2-arrow η: f -> f in C.
    """
    ...

class _Auto_TwoArrow(_Endo_TwoArrow, _Automorphism_Mixin, ABC):
    """Invertible 2-arrow η: f -> f in C."""
    ...

# =============================================================================
# Friendly Exports
# =============================================================================


class Arrow:
    """Container for n-arrow types."""
    m1 = _NegativeOneArrow

    # 0-arrows
    n0 = _ZeroArrow
    
    # 1-Arrows
    n1 = _OneArrow
    n1_endo = _Endo_OneArrow
    n1_auto = _Auto_OneArrow

    # 2-Arrows
    n2 = _TwoArrow
    n2_endo = _Endo_TwoArrow
    n2_auto = _Auto_TwoArrow
    
    # n-Arrows
    n = _nArrow
