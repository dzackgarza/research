r"""PAdicRings ring subcategory spec."""

from __future__ import annotations

from abc import abstractmethod
from collections.abc import Callable
from typing import TYPE_CHECKING, Any, final, override

from sage.rings.integer import Integer

from ...cat import Category, Category_singleton
from ._lazy_subcategories import (
    _CompleteRings,
    _ValuedRings,
)
from .approximate import ApproximateRingsCategory

if TYPE_CHECKING:
    from ...types import (
        CompleteRing,
        Field,
        Polynomial,
        RealNumber,
        Ring,
        RingElement,
        RingMorphism,
    )


class _PAdicRings(Category_singleton):
    r"""Common category for Sage p-adic rings and fields.

    Constructor target: p-adic constructors under ``Rings().Constructors()``
    refine through this valued approximate family.
    """

    @override
    @final
    def _repr_object_names(self) -> str:
        return "p-adic rings and fields"

    @override
    @final
    def super_categories(self) -> list[Category]:
        return [ApproximateRingsCategory(), _CompleteRings(), _ValuedRings()]

    @override
    @final
    def __contains__(self, R: Any) -> bool:
        from sage.rings.padics.generic_nodes import pAdicFieldGeneric, pAdicRingGeneric

        return isinstance(R, (pAdicFieldGeneric, pAdicRingGeneric))

    class ParentMethods:
        @abstractmethod
        def prime(self) -> Integer: ...

        @abstractmethod
        def precision_cap(self) -> Integer: ...

        @abstractmethod
        def teichmuller(
            self, x: RingElement | Integer, prec: Integer | None = None
        ) -> RingElement: ...

        @abstractmethod
        def teichmuller_system(self) -> list[RingElement]: ...

        @abstractmethod
        def inertia_subring(self) -> CompleteRing: ...

        @abstractmethod
        def residue_ring(self, n: Integer) -> Ring: ...

        @abstractmethod
        def residue_system(self) -> list[RingElement]: ...

        @abstractmethod
        def ground_ring(self) -> CompleteRing: ...

        @abstractmethod
        def ground_ring_of_tower(self) -> CompleteRing: ...

        @abstractmethod
        def ramification_index(self) -> Integer: ...

        @abstractmethod
        def e(self) -> Integer: ...

        @abstractmethod
        def inertia_degree(self) -> Integer: ...

        @abstractmethod
        def f(self) -> Integer: ...

        @abstractmethod
        def absolute_e(self) -> Integer: ...

        @abstractmethod
        def absolute_f(self) -> Integer: ...

        @abstractmethod
        def absolute_ramification_index(self) -> Integer: ...

        @abstractmethod
        def absolute_inertia_degree(self) -> Integer: ...

        @abstractmethod
        def relative_degree(self) -> Integer: ...

        @abstractmethod
        def relative_e(self) -> Integer: ...

        @abstractmethod
        def relative_f(self) -> Integer: ...

        @abstractmethod
        def relative_ramification_index(self) -> Integer: ...

        @abstractmethod
        def relative_inertia_degree(self) -> Integer: ...

        @abstractmethod
        def print_mode(self) -> str: ...

        @abstractmethod
        def change_precision(
            self, precision: Integer, precision_type: str | None = None
        ) -> CompleteRing: ...

        @abstractmethod
        def change_prime(self, p: Integer) -> CompleteRing: ...

        @abstractmethod
        def fraction_field(self) -> Field: ...

        @abstractmethod
        def _change_print_mode(self, print_mode: str) -> CompleteRing: ...

        @abstractmethod
        def ext(
            self,
            modulus: Polynomial,
            prec: Integer | None = None,
            names: str | None = None,
            print_mode: str | None = None,
            implementation: str = "FLINT",
        ) -> CompleteRing: ...

        @abstractmethod
        def frobenius_endomorphism(self, n: Integer = 1) -> RingMorphism: ...

        @abstractmethod
        def maximal_unramified_subextension(self) -> CompleteRing: ...

        @abstractmethod
        def defining_polynomial(
            self, var: str | None = None, exact: bool = False
        ) -> RingElement:
            ...

        @abstractmethod
        def integer_ring(self) -> CompleteRing: ...

        @abstractmethod
        def exact_ring(self) -> Ring: ...

        @abstractmethod
        def metric(self) -> Callable[[RingElement, RingElement], RealNumber]: ...

        @abstractmethod
        def metric_function(
            self,
        ) -> Callable[[RingElement, RingElement], RealNumber]: ...

        @abstractmethod
        def dist(self, x: RingElement, y: RingElement) -> RealNumber: ...

        @abstractmethod
        def is_capped_absolute(self) -> bool: ...

        @abstractmethod
        def is_capped_relative(self) -> bool: ...

        @abstractmethod
        def is_fixed_mod(self) -> bool: ...

        @abstractmethod
        def is_floating_point(self) -> bool: ...

        @abstractmethod
        def is_relaxed(self) -> bool: ...

        @abstractmethod
        def is_lattice_prec(self) -> bool: ...

        @abstractmethod
        def has_pth_root(self) -> bool: ...

        @abstractmethod
        def has_root_of_unity(self, n: Integer) -> bool: ...

    class ElementMethods: ...
